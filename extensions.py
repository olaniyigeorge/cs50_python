filename= input("Type in the filename: ")

extension= filename.split('.')[-1]

if extension in ['gif','jpg','jpeg', 'png']:
    print(f"image/{extension}")
elif extension == 'txt':
    print(f"text/plain")
elif extension in ['pdf','zip']:
    print(f"application/{extension}")
else:
    print("application/octet-stream")
