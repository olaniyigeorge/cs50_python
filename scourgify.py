import csv
import sys


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    
    before = sys.argv[1]
    after = sys.argv[2]
    
    try:
        open(before)
    except:
        sys.exit("File not found")

    

    old= get_file(before)

    make_file(old, after)



def get_file(before):
    #Returns the file as a list of dictionaries
    old_rows = []
    with open(before) as old_file:
        reader = csv.DictReader(old_file)

        for row in reader:
            old_rows.append({"names": row["name"], "house": row["house"]})
    return old_rows


        
def make_file(old_rows, after):
    new_rows = []
    with open(after, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["firstname", "lastname", "house"])
    for person in old_rows:
        # print(person)

        f, l = person["names"].split(", ")
        # print(f)
        with open(after, "a") as file:
            writer = csv.writer(file)
            writer.writerow([f, l, person["house"]])
    return after



if __name__ == "__main__":
    main()
