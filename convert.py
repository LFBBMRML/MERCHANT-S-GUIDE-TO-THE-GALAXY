roman_numerals = {
    "M" : 1000,
    "D" : 500,
    "C" : 100,
    "L" : 50,
    "X" : 10,
    "V" : 5,
    "I" : 1
}

galaxy_currency = {
    "glob" : "I",
    "prok" : "V",
    "pish" : "X",
    "tegj" : "L"
}

forbidden_order = ["IIII", "XXXX", "CCCC", "MMMM", "DD", "LL", "VV"]
forbidden_sub = ["IL", "IC", "ID", "IM", "VL", "VC", "VD", "VM", "XD", "XM", "LD", "LM", "DM"]


def check_order(roman_string):
    if any(i in roman_string for i in forbidden_order):
        info = "invalid Value!"
        return info
    elif any(i in roman_string for i in forbidden_sub):
        info = "invalid Value!"
        return info
    else:
        return roman_string


def galaxy_in_list(galaxy_string):
    galaxy_list = galaxy_string.split(" ")
    return galaxy_list


def galaxy_in_roman(galaxy_list):
    roman_list = []
    for i in galaxy_list:
        roman_list.append(galaxy_currency.get(i))
    return roman_list


def roman_in_arabic(roman_numeral):
    arabic_list = []
    for i in roman_numeral:
        arabic_list.append(roman_numerals.get(i))
    return arabic_list


def subtract(arabic_list):
    indices = []
    for i in range(len(arabic_list)-1):
        if arabic_list[i] < arabic_list[i+1]:
            arabic_list[i] = abs(arabic_list[i] - arabic_list[i+1])
            a = i+1
            indices.append(a)        
    return arabic_list, indices


def list_to_sum_up(arabic_list, indices):
    for i in indices:
        arabic_list[i] = 0
    return arabic_list


def arabic_value(arabic_list):
    value = sum(arabic_list)
    return value