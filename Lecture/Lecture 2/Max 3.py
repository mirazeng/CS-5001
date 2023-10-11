def max3(one, two, three):
    '''compare 3 ints, return the largest of the three'''
    return max(max(one, two), three)

def test_max3(one, two, three, expected):
    actual = max3(one, two, three)
    print(f"Inputs were {one}, {two}, {three}")
    print(f"Expected:{expected}  Actual Result:{actual}")

def main():
        print(max3(3,5, 6))
       

if __name__ == "__main__":
        main()
    
