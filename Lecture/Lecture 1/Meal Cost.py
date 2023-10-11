# grand total for a meal

def main():

    tax_rate = 0.08
    tip_rate = 0.18

    #get the cost of the mean from the uesr
    cost = float(input("Enter the amount of your meal："))

    #compute the each amount
    tax = cost * tax_rate
    tip = cost * tip_rate
    total = cost + tax + tip

    #output
    print(f"The tax is${tax:.2f}. The tip is ${tip:.2f}")
    print(f"The total cost is ${total:.2f}")

if __name__ == "__main__":
    main()
