from product.repositories.customers import CustomerRepository

class CustomerService:
        
    @staticmethod
    def get_all():
        return CustomerRepository.get_all()