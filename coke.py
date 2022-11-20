total_deposit= 0 

while total_deposit < 50:
    deposit= input("Insert your coin: ")
    if int(deposit) not in [25, 10, 5]:
        continue
    else:
        total_deposit= total_deposit + int(deposit)
    if total_deposit < 50:
        print(f"Amount Due: {50 - total_deposit}")

#print("Enjoy this bottle of coke")

print(f"Your change is {total_deposit- 50}")

