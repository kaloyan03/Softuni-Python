def stock_availability(inventory, action, *args):
    if action == 'delivery':
        for el in args:
            inventory.append(el)

        return inventory


    elif action == 'sell':
        if not args:
            del inventory[0]
            return inventory
        else:
            if type(args[0]) == int:
                for i in range(args[0]):
                    del inventory[0]
                return inventory

            else:
                for el in args:
                    if el in inventory:
                        while el in inventory:
                            inventory.remove(el)

                return inventory





print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
