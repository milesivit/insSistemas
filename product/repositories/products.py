from product.models import Product

class ProductRepository:
    #se encarga de conectarse con la db para manipular productos

    @staticmethod
    def create(
        name:str,
        price:float,
        description: str,
        stock: int
    ) -> Product: #crea product
        return Product.objects.create(
            name=name,
            price=price,
            description=description,
            stock=stock
        )
    
    @staticmethod
    def delete(product: Product) -> bool: #obtiene todos los objetos de product
        try:
            Product.delete()
        except Product.DoesNotExist:
            raise ValueError("el producto no existe")
    
    @staticmethod
    def update(product: Product, price: float, stock: int) -> Product:
        product.price = price
        product.stock = stock
        product.save()

        return product
    
    @staticmethod
    def get_all() -> list[Product]: #obtiene todos los objetos de product
        return Product.objects.all()

    @staticmethod
    def get_by_id(product_id: int) -> Product: #obtiene el id del producto
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None
    
    @staticmethod
    def search_by_name(name: str) -> list[Product]: #obtiene los productos que tengan el nombre ingresado
        return Product.objects.filter(name__icontains=name)
    ##################################atributo__quecontenga__cadena-q-le-paso

    @staticmethod
    def filter_by_price_range(min_price: float, max_price: float) -> list[Product]: #obtiene un rango de precio mayor, menor
        return Product.objects.filter(price__range=(min_price, max_price))
        #podemos utilizar cualquiera de los dos
        return Product.objects.filter(price__gte=min_price, price__lte=max_price)
