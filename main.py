from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Union
from config.db import SessionLocal
from models.orders import Order
from models.post import Post
from models.post_meta import PostMeta
from models.jawaban import Jawaban
from models.kuesioner import Kuesioner
from models.user import Users
from datetime import date

app=FastAPI()


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/api/v1/reports/orders")
async def reportOrders(
    db: Session = Depends(get_database_session), field: Union[str, None] = None, to: Union[str, None] = None, date_from: Union[str, None] = None
):
    if field == None:
        return JSONResponse(content={
            'success' : False,
            'message' : 'Failed missing field value parameter query'
        }, status_code=400)
    
    if date_from != None and to != None:
        results = db.query(Order).filter(Order.created_at.between(date_from, to))
    elif date_from != None:
        today = date.today()
        results = db.query(Order).filter(Order.created_at.between(date_from, today))
    else:
        results = db.query(Order).all()
    
    data= []
    for result in results:
        if field == 'post_date':
            result_data = {'created_at': result.created_at}
            data.append(result_data)
        elif field == 'order_id':
            result_data = {'id': result.id}
            data.append(result_data)
        elif field == 'product_id':
            result_data = {'product_id': result.product_id}
            data.append(result_data)
        elif field == 'product_name':
            result_post = db.query(Post).filter(Post.ID == result.product_id).one()
            result_data = {'product_name': result_post.post_title}
            data.append(result_data)
        elif field == 'harga':
            result_post = db.query(PostMeta).filter(PostMeta.post_id == result.product_id).filter(PostMeta.meta_key == '_price').one()
            result_data = {'harga': result_post.meta_value}
            data.append(result_data)
        elif field == 'coupon':
            result_data = {'coupon': result.code_coupon}
            data.append(result_data)
        elif field == 'discount':
            result_data = {'discount': result.coupon_price}
            data.append(result_data)
        elif field == 'total_order':
            result_data = {'order_total': result.order_total}
            data.append(result_data)
        elif field == 'unique_fee':
            if result.diskon_price == 0 :
                unique_fee = 0
            else :
                unique_fee = '-'+str(result.diskon_price)
            result_data = {'unique_fee': str(unique_fee)}
            data.append(result_data)
        elif field == 'payment_method':
            result_data = {'payment_method': result.payment_method}
            data.append(result_data)
        elif field == 'first_name':
            result_data = {'first_name': result.billing_first_name}
            data.append(result_data)
        elif field == 'email':
            result_data = {'email': result.billing_email}
            data.append(result_data)
        elif field == 'phone':
            result_data = {'phone': result.billing_phone}
            data.append(result_data)
        elif field == 'user_id':
            result_data = {'user_id': result.user_id}
            data.append(result_data)
        elif field == 'sale_price':
            result_data = {'sale_price': result.sale_price}
            data.append(result_data)
        elif field == 'regular_price':
            result_data = {'regular_price': result.reguler_price}
            data.append(result_data)
        else : 
            break
    
    return data


@app.get("/api/v1/reports/courses/JRC")
async def reportOrders(
    db: Session = Depends(get_database_session), to: Union[str, None] = None, date_from: Union[str, None] = None
):
    if to == None or date_from ==None:
         return JSONResponse(content={
            'success' : False,
            'message' : 'Failed missing query parameter to or date_from'
        }, status_code=400)
    
    results = db.query(Jawaban).filter(Jawaban.created_at.between(date_from, to))
    data = []
    for result in results:
        result_kues = db.query(Kuesioner).filter(Kuesioner.id == result.pertanyaan_id).one()
        result_post = db.query(Post).filter(Post.ID == result.course_id).one()
        result_users = db.query(Users).filter(Users.ID == result.user_id).one()
        result_data = {
            'id': result.id,
            'course_id': result.course_id,
            'user_id': result.user_id,
            'display_name': result_users.display_name,
            'post_title': result_post.post_title,
            'type': result_kues.type,
            'pertanyaan': result_kues.pertanyaan,
            'jawaban': result.jawaban
            }
        data.append(result_data)
    return data