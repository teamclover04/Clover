def convert_temperature(value, unit):

    # I first wrote: if unit == "C":
    # But then lowercase 'c' was not accepted.
    # So I changed the condition to accept both uppercase and lowercase.

    if unit == "C" or unit == "c":
        # Earlier I wrote wrong formula: (value * 5/9) + 32
        # That gave incorrect output.
        # Then I checked formula and corrected it to (value * 9/5) + 32.
        result = (value * (9/5)) + 32
    
    elif unit == "F" or unit == "f":
        # Initially I forgot brackets and wrote value - 32 * 5/9
        # That followed wrong operator precedence and gave wrong answer.
        # So I corrected it using brackets.
        result = (value - 32) * (5/9)
    
    else:
        # Earlier I did not handle invalid unit.
        # Program returned nothing (None).
        # So I added this return message.
        return "Invalid unit. Use C or F"
    
    # At first I returned result directly.
    # But assignment requires rounding to 1 decimal place.
    return round(result, 1)


val = float(input("Enter temperature value: "))
u = input("Enter unit (C or F): ")

# Before this check, when I entered "CF" or "Celsius",
# the function behaved incorrectly.
# So I added length validation.
if len(u) > 1:
    print("Only Single charecter is Accepted...use C or F")
else:    
    print("Converted temperature:", convert_temperature(val, u))
