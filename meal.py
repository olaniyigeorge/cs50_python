def main():
    strtime= input("Type in the time: ")

    if 7.0 <= convert(strtime) <= 8.0:
        print("Breakfast time")
    elif 12.0 <= convert(strtime) <= 13.0:
        print("Lunch time")
    elif 18.0 <= convert(strtime) <= 19.0:
        print("Dinner time")


def convert(time):
    hours_and_mins= time.split(":")

    in_hours= float(hours_and_mins[0]) + (float(hours_and_mins[1]) / 60)
    return round(in_hours, 2)
    

if __name__ == "__main__":
    main()