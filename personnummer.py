
def stripCentury(number):
    """Strips the number of the century

    Sometimes, personnummer is written including century.
    This is not included in the algorithm for calculating the
    final digit, and thus is removed by this function."""

    if len(number) < 11:
        return number
    else:
        return number[2:]


def fixFormat(original_number):
    """Format the number in a predictable way.

    Fixes the problem with different ways of formatting the number.
    The resulting format is always yymmddnnn or yymmddnnnn depending on the
    input."""

    dashless_number = original_number.replace("-", "")
    century_stripped_number = stripCentury(dashless_number)
    return century_stripped_number


def doubleAndSum(number):
    """Doubles a number and adds the digits in it

    Takes an intiger and doubles it, and then adds the numbers together. Will not work for numbers larger than 49"""

    number *= 2
    if number >= 10:
        number = number // 10 + number % 10
    return number


def calculateControlDigit(number):
    """Calculate the control digit for a personnummer

    The control digit is calculated by multiplying every other number by two,
    (Starting with the first) then adding the separate digits. The control digit is then the difference
    between that sum and the closest higher multiple of ten. E.g. if the sum is 44, the control digit will be 50-44=6"""

    # Make it easier to handle individual digits
    number_as_string = str(number)

    cumulative_sum = 0

    # Enumerate makes a tuple of index and element
    for index, digit in enumerate(number_as_string):

        # HACK: Added this to make sure it only takes the first 9 numbers in personnummer.
        if index >= 9:
            break

        # Make calculations possible
        current_number = int(digit)

        if index % 2 == 0:
            current_number = doubleAndSum(current_number)

        # HACK: Made it so cumulative_sum also adds itself to the new variable
        cumulative_sum = current_number + cumulative_sum

    # This is equivalent to taking the following multiple of ten minus the number
    control_digit = (10 - (cumulative_sum % 10)) % 10

    return control_digit


def printControlDigitMatch(personnummer, control_digit):
    last_digit = int(personnummer) % 10
    if last_digit == control_digit:
        print("Personnumrets kontrollsiffra stämmer!")
    else:
        print(f"Personnumrets kontrollsiffra stämmer INTE!\nDen ska vara {control_digit}, men är {last_digit}")

# This statement means that the code below will not run if imported.
# This is good when running automated tests, which we will cover later


if __name__ == "__main__":

    personnummer = input("Skriv in ett personnummer du vill testa eller ett ofullständigt som du vill generera: ")
    personnummer = fixFormat(personnummer)
    control_digit = calculateControlDigit(personnummer)

    if len(personnummer) == 10:
        printControlDigitMatch(control_digit=control_digit,
                               personnummer=personnummer)
    else:
        print(f"Det fullständiga personnumret är: {personnummer}{control_digit}")
