def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

def main():
    time = input("What time is it? ").strip()
    time_float = convert(time)

    if 7 <= time_float <= 8 :
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()
