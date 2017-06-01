def int_to_word(x):
    def less_than_100_to_word(x):
        return tens_place_to_word(x // 10) + int_to_word(int(str(x)[1:]))
    if x < 20:
        return less_than_twenty_to_word(x)
    elif x < 100:
        return less_than_100_to_word(x)
    elif x < 1000:
        hundreds = less_than_twenty_to_word(x // 100) + "hundred"
        rest = int_to_word(int(str(x)[1:]))
        if rest:
            return hundreds + "and" + rest
        else:
            return hundreds
    elif x == 1000:
        return "onethousand"
    else:
        raise ValueError("Only implemented for numbers under 1000")


def less_than_twenty_to_word(x):
    if x > 0:
        return ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
                "twenty"][x - 1]
    else:
        return ""

def tens_place_to_word(x):
    if x > 0:
        return ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][x - 1]
    else:
        return ""

assert less_than_twenty_to_word(5) == "five"
assert less_than_twenty_to_word(13) == "thirteen"

assert tens_place_to_word(5) == "fifty"

assert int_to_word(1) == "one"
assert int_to_word(80) == "eighty"
assert int_to_word(81) == "eightyone"
assert int_to_word(19) == "nineteen"
assert int_to_word(37) == "thirtyseven"
print(int_to_word(111))
assert int_to_word(111) == "onehundredandeleven"
assert int_to_word(342) == "threehundredandfortytwo"
print(int_to_word(200))
assert int_to_word(200) == "twohundred"
assert int_to_word(999) == "ninehundredandninetynine"
assert int_to_word(1000) == "onethousand"

#print([int_to_word(x) for x in range(1, 1001)])
print(sum([len(int_to_word(x)) for x in range(1, 1001)]))