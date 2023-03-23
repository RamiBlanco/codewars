# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.
# Happy Coding!

def square_digits(num):
    try:
        num_list = [int(x) for x in str(num)]
        squares_int_list = map(lambda x: x * x ,num_list)
        squares_str_list = [str(x) for x in squares_int_list]
        squares_str = ''.join(squares_str_list)
        return int(squares_str)          
    except ValueError:
        print("This is not an integer")
  
print(square_digits(9119))