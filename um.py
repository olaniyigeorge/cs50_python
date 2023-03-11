import re


def main():
    print(count(input("Type in the text: ").strip()))


def count(text):
    count=0
    
    t=[]
    for x in text.split(" "):
        t.append(x)
    
    for word in t:
        if re.search(r"^um(,|\.|\?)?$", word, re.IGNORECASE):
            count += 1
        
    return count


if __name__ == "__main__":
    main()