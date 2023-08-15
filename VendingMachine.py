class VendingMachine:
    def __init__(self, num_items, items_price):
        self.num_items = num_items
        self.items_price = items_price

    def buy(self, req_items, money_put):
        if self.num_items >= req_items and req_items * self.items_price <= money_put:
            self.num_items -= req_items
            return money_put - (req_items * self.items_price)
        else:
            if self.num_items < req_items:
                return "Not enough items in the machine"
            else:
                return "Not enough coins"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")

    fptr.close()
