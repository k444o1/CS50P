amount = 0
due = 50 - amount
while amount < 50:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5: #reprompts user if coin is not 25/10/5
        amount += coin
        due = 50 - amount
        if due <= 0: #due is either negative (meaning there's change owed) or 0(no change owed)
            change = -1 * due
            print(f"Change Owed: {change}") 
