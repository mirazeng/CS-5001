
def main():

# user_input_1 = input("Do you like ice-cream?")

# if user_input_1 == "yes":
    # print("Yay! So do I!")

    ice_cream = input("Do you like ice-cream (y/n)?")
    if ice_cream.lower() == "y":
        print("Yay! So do I!")


    broccoli = input("Do you like broccoli (y/n)?")
    if broccoli == "Y" or broccoli == "y":
        print("I like it with cheese")
    else:
        print("But it is healthy!")

    if ice_cream.lower() == 'y' and broccoli.lower() == "y":
        print("Time for a healthy broccoli ice cream sundae. Yum!")
    

if __name__ == "__main__":
    main()
