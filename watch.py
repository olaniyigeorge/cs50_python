import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(url):
    match_link_code = re.search(
        r"src=\"https?://(?:www.)?youtube.com/embed/(\w+)\"(?: .+)?", url, re.IGNORECASE
    )

    if match_link_code:
        return f"https://youtu.be/{match_link_code.group(1)}"


if __name__ == "__main__":
    main()
