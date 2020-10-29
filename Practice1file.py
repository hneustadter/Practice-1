import math

def my_square_root(val):
    if val < 0:
        return -1
    else:
        return math.sqrt(val)

if __name__ == '__main__':
    a= ('red', 'blue', 'green', 'yellow')
    b= 'blue'

    if b in a:
        print("That is correct")
    else:
        print("That is incorrect")