answer = int and str(input("What is the Great Question of Life, the Universe and Everything? ")).strip().lower()

match answer:
   case "42" | "forty-two" | "forty two":
     print("Yes")
   case _:
     print("No")
