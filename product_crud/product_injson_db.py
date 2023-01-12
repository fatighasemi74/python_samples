import json

class ProductInJson:

    # _product_json = []

    def add(self, data:dict) -> None:
        _product_json = self.list_all()
        _product_json.append(data)
        with open('examples.json', 'w') as f:
            json.dump(_product_json, f)

    def read(self, id:int) -> dict:
        with open('examples.json', 'r') as f:
            data = json.load(f)
            for item in data:
                if item["id"] == id:
                    return item

    def update(self, id:int, data:dict) -> None:
        with open('examples.json', 'r') as f:
            data = json.load(f)
            for item in data:
                if item["id"] == id:
                    data.remove(item)
                    data.append(data)
        with open('examples.json', 'w') as f:
            json.dump(data, f)

    def delete(self, id: int) -> None:
        with open('examples.json', 'r') as f:
            data = json.load(f)
            for item in data:
                if item["id"] == id:
                    data.remove(item)
        with open('examples.json', 'w') as f:
            json.dump(data, f)

    def list_all(self) -> dict:
        with open('data_file.json', 'r') as f:
            data = json.load(f)
            return data
