print("\tArithmetic Operations")

#def calculator():
while True:
      """ Calculator is the main function
      while add, sub, multiply and division are
      sub-functions which perform mathematical operations """
      print("Enter your choice as yes or no")
      choice_run = input()
      choice_run = choice_run.lower()
      if choice_run == "no":
        print("Thank you for using calculator")
        break  # Properly indented to be inside the while loop
      print("Enter First Number: ")
      num1 = int(input())
      print("Enter Second Number: ")
      num2 = int(input())
      print("Enter Your Choice as +, -, * or / ")
      choice = input()
      if choice == '+':
       def add(num1, num2):
          return num1 + num2
       sum = add(num1, num2)
       print("Sum: ", sum)
      elif choice == "-":
       def sub(num1, num2):
        return num1 - num2
       difference = sub(num1, num2)
       print("Difference: ", difference)
      elif choice == "*":
        def multiply(num1, num2):
         return num1 * num2
        product = multiply(num1, num2)
        print("Product: ", product)
      elif choice == "/":
          if num2 == 0:
           print("Cannot divide by zero")
          else:
           def divide(num1, num2):
            return num1 / num2
          quotient = divide(num1, num2)
          print("Quotient: ", quotient)
      else:
        print("Invalid Choice")

#calculator()