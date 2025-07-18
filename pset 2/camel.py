#conversor de camelCase para snake_case
def camel_to_snake(text):
    result = []
    for char in text:
        if char.isupper():
            result.append("_")
            result.append(char.lower())
        else:
            result.append(char)

    return "".join(result)

text = str(input("camelCase: "))

print("snake_case: " + camel_to_snake(text))

