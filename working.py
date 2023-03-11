import re

def main():
    print(convert(input("Hours: ").strip()))


def convert(time):
    # try to catch the error elegantly without the cryptic error message
    try:
        # Raise ValueError if re.search returns None
        if matches := re.search(
            r"^([0-9]|[0-1][0-2]):?([0-5][0-9])?( AM| PM) to ([0-9]|[0-1][0-2]):?([0-5][0-9])?( AM| PM)$",
            time,
            re.IGNORECASE,
        ):
            # Separate the matches into the working time beginning and end
            start_time = list(matches.groups()[0:3])
            end_time = list(matches.groups()[3:7])

            start_time, end_time = convert_hour_to_24hrs(start_time, end_time)
            start_time, end_time = convert_min_to_24hrs(start_time, end_time)

            return f"{start_time[0]}:{start_time[1]} to {end_time[0]}:{end_time[1]}"
        else:
            raise ValueError("ValueError")
    except ValueError:
        return "ValueError"



def convert_hour_to_24hrs(start_time, end_time):
    # Add extra 12 hours to the hour if the time is in PM
    for _ in (start_time, end_time):
        if _[-1].strip() == "PM":
            if _[0] == "12":
                _[0] = _[0]
            else:
                _[0] = f"{int(_[0]) + 12}"

        elif _[-1].strip() == "AM":
            if _[0] == "12":
                _[0] = "00"
            else:
                continue

    return (start_time[0:2], end_time[0:2])


def convert_min_to_24hrs(start_time, end_time):
    # Mark the min as 00 if the min wasnt specified
    """
    This function is only called on the lists after the convert_hour_to-24hrs function
    has been called on those list to ensure having correct values for the hours
    """
    for _ in (start_time, end_time):
        if _[-2] == None:
            _[-2] = "00"
    return (start_time[0:2], end_time[0:2])


if __name__ == "__main__":
    main()
