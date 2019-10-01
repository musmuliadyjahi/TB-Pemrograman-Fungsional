# Lambda dan Map

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print("1. ", list(result))

# First Class Object
def square(x):
    return x*x

f = square
print("2. ", f(5))

#High Order Function
def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total

print("3. ", sum(3, square))

#Filter
randomList = [1, 'a', 0, False, True, '0', ""]

filteredList = filter(None, randomList)
print("4. ", list(filteredList))

#Closure
def print_msg(msg):
    # This is the outer enclosing function
    def printer():
# This is the nested function
        print(msg)
    return printer
another = print_msg("Hello")
another()