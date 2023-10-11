import random

def flip_coin():

        # heads is zero　
        number = random.randint(0,1)
        if number == 0:
            return "HEAD"
        return "TAIL"

def print_report(heads, tails, visual):
    print("Flip Coin Final Report")
    print(f"Flip history is: {visual}")
    print(f"Number of Heads = {heads}. Number of Tails = {tails}")


def game():
    heads = 0
    tails = 0
    visual = ""
    i = 0 # initial value of loop variable
    while i < TIMES: # iniial value to know when to stop
        answer = flip_coin()
        if i == 10:
            i = i + 1
            continue
        if i == 15:
            break
        visual = visual + answer + " "
        if answer == "HEAD":
            heads = heads + 1
        else:
            tails = tails +1 
            
        i += 1 #same as i = i + 1

    print_report(heads, tails, visual)
        
def main():
    game()
