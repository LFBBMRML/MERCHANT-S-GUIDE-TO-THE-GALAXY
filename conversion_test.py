import convert

def test_check_order():
    assert convert.check_order("MMVVI") == "invalid Value!"
    assert convert.check_order("MCMXVLIV") == "invalid Value!"
    assert convert.check_order("MCMXLIV") == "MCMXLIV"

def test_galaxy_in_list():
    assert convert.galaxy_in_list("glob glob") == ["glob", "glob"]

def test_galaxy_in_roman():
    assert convert.galaxy_in_roman(["glob", "glob"]) == ["I", "I"]
    assert convert.galaxy_in_roman(["pish", "prok"]) == ["X", "V"]
    assert convert.galaxy_in_roman(["prok", "tegj"]) == ["V", "L"]
    assert convert.galaxy_in_roman(["pish", "glob"]) == ["X", "I"]

def test_roman_in_arabic():
    assert convert.roman_in_arabic(["I", "I"]) == [1, 1]
    assert convert.roman_in_arabic(["X", "V"]) == [10, 5]
    assert convert.roman_in_arabic(["V", "L"]) == [5, 50]
    assert convert.roman_in_arabic(["X", "I"]) == [10, 1]
    assert convert.roman_in_arabic(["M", "D", "C", "L", "X", "V", "I"]) == [1000, 500, 100, 50, 10, 5, 1]

def test_subtract():
    assert convert.subtract([1000, 100, 1000, 10, 50, 1, 5]) == ([1000, 900, 1000, 40, 50, 4, 5], [2, 4, 6])

def test_list_to_sum_up():
    assert convert.list_to_sum_up([1000, 900, 1000, 40, 50, 4, 5], [2, 4, 6]) == [1000, 900, 0, 40, 0, 4, 0]

def test_arabic_value():
    assert convert.arabic_value([1000, 900, 0, 40, 0, 4, 0]) == 1944