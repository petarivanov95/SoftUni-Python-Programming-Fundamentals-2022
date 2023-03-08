class Catalogue:
    def __init__(self, name: str) -> None:
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        first_letter_list = [x for x in self.products if x[0] == first_letter]
        return first_letter_list

    def __repr__(self):
        items_sorted = sorted(self.products)
        items_str = "\n".join(str(item) for item in items_sorted)
        return f"Items in the {self.name} catalogue:\n{items_str}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
