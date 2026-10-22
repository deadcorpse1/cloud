import Pyro4
uri = input("Enter the server URI: ")
calculator = Pyro4.Proxy(uri)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
addition = calculator.add(a, b)
multiplication = calculator.multiply(a, b)
print("Addition =", addition)
print("Multiplication =", multiplication)