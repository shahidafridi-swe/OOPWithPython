try:
    num1= int(input())
    num2= int(input())
    print(num1/num2)
except ZeroDivisionError:
    print("Division by 0 is not possible")
except ValueError:
    print("Invalid Value")

finally:
    print("Kaj ses ja akhon muri kha")
