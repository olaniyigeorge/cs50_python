import validator_collection
import sys

def main():
    check_mail(input("Type in the mail: ").strip())


def check_mail(mail):    
    try:
        validator_collection.email(mail)
    except validator_collection.errors.InvalidEmailError:
        sys.exit("Invalid")
    sys.exit("Valid")

if __name__ == "__main__":
    main()