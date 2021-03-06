class Product:
    def __init__(self, code, name, price, qty):
        self.code = code
        self.name = name
        self.price = price
        self.qty = qty

class VendingMachine:
      def __init__(self, products):
            self.products = products
            self.inserted_money = 0

      def insert_money(self, money):
            self.inserted_money = money

      def buy(self, raw_product_code):
            if len(raw_product_code) == " ":
                print("Product code is empty!")
                return
            product_code = int(raw_product_code)
            change = self.inserted_money
            for i, product in enumerate(self.products):
                if product.code == product_code and change >= product.price:
                    if product.qty == 0:
                        print("No stock available for the product.")
                        return
                    self.products[i].qty -= 1
                    change = change - product.price
                    print("You successfully ordered product code: {}".format(product_code))
                    print("Your change is: P{}".format(change))
                    print('-'*50)
                    break
            if change == self.inserted_money:
                print("Product not found!")
            elif change < product.price:
                print("Insufficient balance!")

      def list_products(self):
            print("AVAILABLE PRODUCTS: ")
            for i, product in enumerate(self.products):
                print("({}) {} - P{}".format(i + 1, product.name, product.price))

products = [
        Product(1, 'Cloud 9 Bar', 7, 10), 
        Product(2, 'Growers Peanuts', 15, 10),
        Product(3, 'Clover Chips (Small)', 20, 10), 
        Product(4, 'Coke in Can', 35, 10),
        Product(5, 'Nescafe Coffee in Can', 35, 10)
    ]
vending_machine = VendingMachine(products)

def main():
    running = True
    while running:
        print('-'*50)
        print("VEND-O-MATIC")
        print('-'*50)
        money = float(input("Insert money: "))
        vending_machine.insert_money(money)
        if money == 0:
            print("Insufficient balance!")
            break
        print('-'*50)
        vending_machine.list_products()
        print('(0) Cancel and return money')
        print('-'*50)
        code = input("Enter the product code: ")
        print('-'*50)
        if code == '0':
            print('-'*50)
            print("Closing Vend-O-Matic...")
            running = False
        else:
            vending_machine.buy(code)
main()