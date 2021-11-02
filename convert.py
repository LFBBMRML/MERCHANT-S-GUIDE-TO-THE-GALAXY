
from functools import reduce
from numpy.core.fromnumeric import product


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

metal_value = {
    "silver" : 17,
    "iron" : 195.5,
    "gold" : 14450
}

forbidden_order = ["IIII", "XXXX", "CCCC", "MMMM", "DD", "LL", "VV"]
forbidden_sub = ["IL", "IC", "ID", "IM", "VL", "VC", "VD", "VM", "XD", "XM", "LD", "LM", "DM"]


def galaxy_in_list(galaxy_string):
    galaxy_list = galaxy_string.split(" ")
    return galaxy_list


def split_the_list(galaxy_list):
    liste_galaxy_currency = []
    liste_metal = []
    for i in galaxy_list:
        if i in metal_value:
            liste_metal.append(i)
        elif i in galaxy_currency:
            liste_galaxy_currency.append(i)
    return liste_galaxy_currency, liste_metal


def metal_in_value(metals_list):
    metal_list = []
    if not metals_list:
        metal_list.append(1)
    else:
        for i in metals_list:
            metal_list.append(metal_value.get(i))
    return metal_list


def galaxy_in_roman(galaxy_list):
    roman_list = []
    for i in galaxy_list:
        roman_list.append(galaxy_currency.get(i))
    return roman_list


def check_order(roman_string):
    roman_numerals_as_a_list = "".join(roman_string)
    if any(i in roman_numerals_as_a_list for i in forbidden_order):
        return "invalid Value!"
    elif any(i in roman_numerals_as_a_list for i in forbidden_sub):
        return "invalid Value!"
    else:
        return roman_string


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


def sum_arabic_value(arabic_list):
    value_sum = sum(arabic_list)
    return value_sum


def product_arabic_value(metal_list):
    product = reduce((lambda x, y: x*y), metal_list)
    return product


def arabic_value_total(value_sum, metal_product):
    value = value_sum * metal_product
    return value


def convert_currency(galaxy_string):
    galaxy_list = galaxy_in_list(galaxy_string)
    galaxy_currency_list, metal_list = split_the_list(galaxy_list)
    metal_value = metal_in_value(metal_list)
    roman_list = galaxy_in_roman(galaxy_currency_list)   
    roman_list = check_order(roman_list)
    if roman_list == "invalid Value!":
        return "invalid Value!"
    else:
        arabic_list = roman_in_arabic(roman_list)
        subtract_arabic_list, indices = subtract(arabic_list)
        new_arabic_list = list_to_sum_up(subtract_arabic_list, indices)
        value_sum = sum_arabic_value(new_arabic_list)
        product = product_arabic_value(metal_value)
        value = arabic_value_total(value_sum, product)
        return value


if __name__ == "__main__":
    print("Please run GUI.py")