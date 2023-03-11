import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    for _ in ip.split("."):
        try:
            int(_)
        except:
            return False
    


    for _ in ip.split("."):
        if int(_) not in range(0,256):
            return False
            #sys.exit("Numbers not in range 0-255")


    if re.search(r"^\d(\d)?(\d)?\.\d(\d)?(\d)?\.\d(\d)?(\d)?\.\d(\d)?(\d)?$", ip, re.IGNORECASE):
        return True
    else:
        return False




if __name__ == "__main__":
    main()