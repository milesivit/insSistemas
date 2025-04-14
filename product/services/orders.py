from product.repositories.orders import OrderRepository

class OrderService:
        
    @staticmethod
    def get_all():
        return OrderRepository.get_all()