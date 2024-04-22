
def main():
    print("Welcome to the pizzeria time of arival calculator!")
    distance = float(input("Enter the distance from the pizzeria to your location: "))
    speed = float(input("Enter the speed of your delivery driver in miles per hour: "))
    calculated_time = 60 * (distance / speed)
    print(f"Estimated time until delivery (minutes): {calculated_time}")
    print(f"Calculation: 60 * ({distance}/{speed}) = {calculated_time}")
    
main()