from product.models import Customer

class CustomerRepository:

    @staticmethod
    def create(
        name:str,
        email:str,
        phone: str,
    ) -> Customer: 
        return Customer.objects.create(
            name=name,
            email=email,
            phone=phone,
        )
    
    @staticmethod
    def update(customer: Customer, email: str, phone: str) -> Customer:
        customer.email = email
        customer.phone = phone
        customer.save()

        return customer
    
    @staticmethod
    def delete(customer: Customer) -> bool: 
        try:
            Customer.delete()
        except Customer.DoesNotExist:
            raise ValueError("el cliente no existe")
    
    @staticmethod
    def get_all() -> list[Customer]: 
        return Customer.objects.all()
    
    @staticmethod
    def get_by_id(customer_id: int) -> Customer: #obtiene el id del cliente
        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return None
    
    @staticmethod
    def search_by_name(name: str) -> list[Customer]: #obtiene los clientes que tengan el nombre ingresado
        return Customer.objects.filter(name__icontains=name)
    
    