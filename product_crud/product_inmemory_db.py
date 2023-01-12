class ProductOnMemory():

    _product_list = []

    # def __int__(self, data:dict):
    #     self._data = data

    @classmethod
    def add(cls,obj) -> int:
        try:
            ProductOnMemory._product_list.append(obj.dict)
            return True
        except:
            return False

#read_by_id
    def read(self, id:int) -> dict:
        for item in self._product_list:
            if item['id'] == id:
                return item
        return False

    def read_by_title(self, title:str) -> dict:
        for item in self._product_list:
            if item['title'] == title:
                return item
        return False

    def read_all(self):
        for item in  ProductOnMemory._product_list:
            return item

    def update(self, id:int, updated_values:dict):
        for item in self._product_list:
            if item['id'] == id:
                item.update(updated_values)
                return self._product_list
        return False


    def delete(self, id:int):
        for item in self._product_list:
            if item['id'] == id:
                self._product_list.remove(item)
                return self._product_list
        return False

    def list_all(self) -> list:
        return self._product_list