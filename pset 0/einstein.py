def energy_calculator(m):
    energy = m * 300000000 ** 2
    return energy

def main():
    user_input = int(input("What is m? "))
    result = energy_calculator(user_input)
    print(f"{result} Joules")

main()



