def main():
    text = input()
    print(convert(text))

def convert(text):
    converted_text = text.replace(":)","🙂").replace(":(","🙁")
    return converted_text

main()

