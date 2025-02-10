# Boot.dev exercises that im doing

"""
We need to display the current time to our players. 
The problem is that the time is stored as a number of hours, but we want to display it as a number of seconds. 
There are 60 seconds in a minute, but how many are in an hour?
"""

def hours_to_seconds(hours):
    return hours * 3600

def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)


# Multiple return variables
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # return two values

dmg, mana = cast_iceblast(5, 100)
print(f"Damage: {dmg}, Remaining Mana: {mana}")
# Damage: 10, Remaining Mana: 90


"""
Complete the become_warrior function. It accepts 2 inputs: the full_name string, and the power integer. 
It should return 2 values: a "title" string and a "new power" integer.

Create the new_power value that is equal to the input power plus one.
Return both title and new_power
"""

def become_warrior(full_name, power):
    title = f"{full_name} the warrior"
    new_power = power + 1
    return title, new_power


def main():
    test("DiMagia", 5)
    test("Zenless Zen", 10)
    test("NaisuNaisu", 9000)


def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main()