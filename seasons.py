import re
from datetime import datetime
import sys
from num2words import num2words


def main():
    birthday = get_date()

    t = datetime.today() 
    
    today = get_date(str(t.date()))

    days = (today - birthday).days
    print(days)

    #Convert number of days to words
    nw = num2words(days)
    words = re.sub(r" and ", " ", nw, re.IGNORECASE)
    print(words.title())


def get_date(d= input("Type in the date(YYYY-MM-DD): ").strip()):
    """
    Takes a string in the format (YYYY-MM-DD) as an argument and returns
    a datetime object of the corresponding date with time as 00:00:00
    :param: str(YYYY-MM-DD)
    :return: datetime object
    """

    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})", d, re.IGNORECASE):
        return datetime(
            int(matches.group(1)), int(matches.group(2)), int(matches.group(3))
        )
    else:
        sys.exit("Date Invalid")


if __name__ == "__main__":
    main()
