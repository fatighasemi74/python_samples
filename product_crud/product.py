from datetime import datetime

class Product():

    _product_list = {}

    def __init__(self, title:str, short_description:str , description:str  , slug:str, permalink:str, sku:str, price:float, regular_price:float,
                 sale_price:float, manage_stock:bool, stock_quantity:int, date_created_gmt :int, date_modified_gmt:int,category_id:int = 0, 
                 is_visible = True, is_available:bool = False):

        assert price >= 0 , f"price {price} is not greater than or equal to 0"

        self.id = None
        self.category_id = category_id
        self.title = title
        self.short_description =  short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.is_available = is_available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visible = is_visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt
       

    def create(self):
        self._product_list[self] = self.id
        # self._product_list.append(self)

        return self.__repr__()

    #this method shall be able read a product via id/uuid or ... from the the product datastructure (dictionary,list or maybe database)
    def read(self, id):
        for value, key in self._product_list.items():
            if value == id:
                return key
        # return self._product_list[id]

    #this method shall be able to update product and amend the data structure for related product
    def update(self, updated_item):
        pass


    #this method shall be able to remove the product
    def delete(self, id):
        for value, key in self._product_list.items():
            if value == id:
                self._product_list.remove(key)
                return 'deleted'

    #shall I get all products with staticmethod ? any better solution ? what about a class method ?
    # what is the diffrence ?
    # shall I seprate the datastructe from the class ? why? who? any better solution?
    @staticmethod
    def list_all():
        return tuple(Product._product_list.keys())
        # return tuple(Product._product_list)


    def __repr__(self) -> str:
        return f"the product with \n\
        Product Id: N/A \n\
        Title: {self.title} \n\
        Short description: {self.short_description} \n\
        Description: {self.description} \n\
        Slug: {self.slug} \n\
        Permanent link: {self.permalink} \n\
        availablity: {self.is_available} \n\
        Stock keeping Unit: {self.sku} \n\
        Price: {self.price} \n\
        Reqular Price: ${self.regular_price} \n\
        Sale Price: ${self.sale_price} \n\
        Manage Stock {self.manage_stock} \n\
        Stock Quantity: {self.stock_quantity} \n\
        Visible: {self.is_visible} \n\
        Date Created: {datetime.utcfromtimestamp(self.date_created_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        Date Modified: {datetime.utcfromtimestamp(self.date_modified_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        "
       