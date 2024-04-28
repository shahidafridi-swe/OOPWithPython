import math

def timer(func):
    def inner(*args):
        print('Time started')
        func(*args)
        print("Time ended")

    return inner

# timer()()
@timer
def get_factorial(n):
    print("Factorial Starting")
    result = math.factorial(n)
    print(f"Factorial of {n} is: {result}")


get_factorial(5)