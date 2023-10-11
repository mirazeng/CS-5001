'''
test code for max3

'''

import evening_max3

def test_max3(one, two, three, expected):
    ''' test foucntion for max3'''
    actual = evening_max3.max3(one, two, three)
    print(f"Inputs were {one}, {two}, {three}")
    print(f"Expected:{expected}  Actual Result:{actual}")

def main():
    
        test_max3(2, 10, 5, 10)
        test_max3(7, 6, 5, 7)

if __name__ == "__main__":
        main()
    
