#calculadora de duas parcelas
expression = input("Expression: ")

x_str, operator, z_str = expression.split()
x = int(x_str)
z = int(z_str)

if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "/":
    result = x / z
elif operator == "*":
    result = x * z
else:
    raise ValueError("Invalid operator")

print(f"{result:.1f}")



