class invoice:
    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total = 0
        for k, v in products.items():
            total += float(v['unit_price'] * int(v['qnt']))
        total = round(total,2)
        return total

    def totalDiscount(self,products):
        total = 0

        for k, v in products.items():
            total += float(v['unit_price'])*int(v['qnt'])*float(v['discount']) /100
        total = round(total, 2)
        self . total_discount = total
        return total

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput