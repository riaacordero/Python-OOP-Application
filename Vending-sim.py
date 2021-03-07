class Product:
    def __init__(self, code, name, price, qty):
        self.code = code
        self.name = name
        self.price = price
        self.qty = qty

class Money:
    def __init__(self, value):
        self.value = value

    def changeValue(self, newVal): 
        self.value = newVal

class VendingMachine:
      def __init__(self, product):
            self.product = product
            self.inserted_money = 0
      def insert_money(self, money):
            self.inserted_money += money
      def buy(self, product_code):
            change = self.inserted_money
            for product in self.product:
                if product.code == product_code:
                    change = Product.price - change
            print(change)

def main():
    print('-'*50)
    print("VEND-O-MATIC")
    print('-'*50)
    money = float(input("Insert your money here: "))
    print('-'*50)
    print("AVAILABLE PRODUCTS: ")
    products = [
        Product(1, 'Cloud 9 Bar', 7, 10), Product(2, 'Growers Peanuts', 15, 10),
        Product(3, 'Clover Chips (Small)', 20, 10), Product(4, 'Coke in Can', 35, 10),
        Product(5, 'Nescafe Coffee in Can', 35, 10)
    ]
    for i, product in enumerate(products):
        print("({}) {} - P{}".format(i + 1, product.name, product.price))
    print('-'*50)
    code = input("Enter the product code: ")

    vending_machine = VendingMachine(products)
    vending_machine.insert_money(money)
    vending_machine.buy(code)

main()