import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many arguments")

    muppet = sys.argv[1].lower()
    result = sys.argv[2].lower()

    safety(muppet, result)

    muppetimage = Image.open(muppet)
    shirtimage = Image.open("shirt.png")

    m = ImageOps.fit(muppetimage, muppetimage.size, bleed=0.1, centering=(0.5, 0.5))
    s = ImageOps.fit(shirtimage, muppetimage.size, bleed=0.0, centering=(0.5, 0.5))

    m.paste(s, box=None, mask=s)

    m.save(result)






def safety(muppet, result):

    if muppet[-4:] and result[-4:] not in [".jpg", ".png"]:
        if muppet[-5:] and result[-5:] not in [".jpeg", ".png"]:
            sys.exit("Invalid file format")
        sys.exit("Invalid file format")

    if muppet[-3:] != result[-3:]:
        sys.exit("Files extensions mismatch")

    try:
        Image.open(muppet)
    except:
        sys.exit("File not found")

        
    pass





if __name__ == "__main__":
    main()
