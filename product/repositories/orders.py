from product.models import Order, Customer

class OrderRepository:
    # Se encarga de conectarse con la db para manipular órdenes

    @staticmethod
    def create(customer: Customer) -> Order:
        return Order.objects.create(customer=customer)

    @staticmethod
    def delete(order: Order) -> bool:
        try:
            order.delete()
            return True
        except Order.DoesNotExist:
            raise ValueError("La orden no existe")

    @staticmethod
    def update_customer(order: Order, new_customer: Customer) -> Order:
        order.customer = new_customer
        order.save()
        return order

    @staticmethod
    def get_all() -> list[Order]:
        return Order.objects.all()

