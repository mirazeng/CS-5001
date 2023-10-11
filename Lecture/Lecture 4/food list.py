def main():
    food = ["grapes", "apples", "snickers"]

    user_food = []

    item = input("what food item do you want (stop to end)?")
    while item.upper() != "stop":
        user_food += [item]
        item = input("next food item (stop to end)?")

    print(user_food)

    i = 0
    while i < len(user_food):
        if user_food[i].lower() in food:
            print(f"I am shopping for {user_food[i]} too!")
        # how much are you counting by
        i = i + 1


if __name__ == '__main__':
    main()
