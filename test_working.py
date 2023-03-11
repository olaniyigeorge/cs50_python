from working import convert, convert_hour_to_24hrs, convert_min_to_24hrs


def test_convert_hour_to_24hrs():
    assert convert_hour_to_24hrs(["3", "25", "AM"], ["5", "33", "PM"]) == (
        ["3", "25"],
        ["17", "33"],
    )
    assert convert_hour_to_24hrs(["1", "11", "AM"], ["12", "40", "PM"]) == (
        ["1", "11"],
        ["12", "40"],
    )
    assert convert_hour_to_24hrs(["5", "56", "PM"], ["1", "00", "PM"]) == (
        ["17", "56"],
        ["13", "00"],
    )
    assert convert_hour_to_24hrs(["8", "02", "AM"], ["3", "00", "AM"]) == (
        ["8", "02"],
        ["3", "00"],
    )
    assert convert_hour_to_24hrs(["11", "05", "AM"], ["10", "29", "PM"]) == (
        ["11", "05"],
        ["22", "29"],
    )
    assert convert_hour_to_24hrs(["9", "47", "PM"], ["12", "24", "AM"]) == (
        ["21", "47"],
        ["00", "24"],
    )


def test_convert_min_to_24hrs():
    assert convert_min_to_24hrs(["3", "25", "AM"], ["5", None, "PM"]) == (
        ["3", "25"],
        ["5", "00"],
    )
    assert convert_min_to_24hrs(["1", None, "AM"], ["12", "40", "PM"]) == (
        ["1", "00"],
        ["12", "40"],
    )
    assert convert_min_to_24hrs(["5", "56", "PM"], ["1", None, "PM"]) == (
        ["5", "56"],
        ["1", "00"],
    )

    assert convert_min_to_24hrs(["5", None, "PM"], ["1", "00", "PM"]) == (
        ["5", "00"],
        ["1", "00"],
    )


def test_convert():
    assert convert(f"3:25 AM to 5:33 PM") == f"3:25 to 17:33"
    assert convert(f"1:11 AM to 12:40 PM") == f"1:11 to 12:40"
    assert convert(f"5:56 PM to 1:00 PM") == f"17:56 to 13:00"
    assert convert(f"8:02 AM to 3:00 AM") == f"8:02 to 3:00"
    assert convert(f"11:05 AM to 10:29 PM") == f"11:05 to 22:29"
    assert convert(f"9:47 PM to 7:24 PM") == f"21:47 to 19:24"
    assert convert(f"7:00 AM to 8:12 PM") == f"7:00 to 20:12"
    assert convert(f"4:55 PM to 12:34 AM") == f"16:55 to 00:34"
    assert convert(f"12:06 AM to 11:06 PM") == f"00:06 to 23:06"
