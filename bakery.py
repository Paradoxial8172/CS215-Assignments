
def bread_sales(loafs):
    global bread_price, days, n
    bread_price = 2.50
    days = 7
    for n in range(1, loafs+1):
        n *= bread_price * days
    return n

def main():
    print("Welcome to Tamer's Bakery! This week's sales are found below:")
    print(f"This week, you have made ${bread_sales(100)} from {n/7/2.50} loafs of bread from ${bread_price} per loaf of bread!")
    print("This program was made by Tamer Alssaleh!")
    
main()

        

