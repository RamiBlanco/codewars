# Given two integers a and b, which can be positive or negative, find the sum of all the 
# integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

def get_sum(a,b):
    res = 0
    if a > b:
        min = b
        max = a
    elif a < b:
        min = a
        max = b
    else:
        return a

    for x in range(min, max+1):
        res = res + x
    return res
    
def get_sum_best_practice(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum(1,2))