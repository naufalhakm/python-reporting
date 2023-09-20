from typing import List, Optional

from fastapi import Depends
from models.Orders import Order
from models.Post import Post

from repository.OrderRepository import OrderRepository
from repository.PostRepository import PostRepository
from repository.PostMetaRepository import PostMetaRepository


class ReportService:
    orderRepository: OrderRepository
    postRepository: PostRepository

    def __init__(
        self, 
        orderRepository: OrderRepository = Depends(),
        postRepository: PostRepository = Depends(),
        postMetaRepository: PostMetaRepository = Depends(),
    ) -> None:
        self.orderRepository = orderRepository
        self.postRepository = postRepository
        self.postMetaRepository = postMetaRepository

    def report(self, field: str , date_from: str, to: str):
        if field == None:
            return None
        results = self.orderRepository.list(date_from, to)
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
                result_post = self.postRepository.getById(result.product_id)
                result_data = {'product_name': result_post.post_title}
                data.append(result_data)
            elif field == 'harga':
                result_post = self.postMetaRepository.getMetaValue(result.product_id, "_price")
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
            
