from itertools import count

def is_even(number:int) -> bool:
    """ Return True if number is even and False if it is odd.

    :param number: The integer to check.
    :return: True if even, anything else False.
    """
    return number % 2 == 0


def count_vowels(text:str) -> int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: The string to check.
    :return: The number of vowels in the string.
    """
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius: Temperature in Celsius.
    :return: Temperature in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def reverse_text(text: str) -> str:
    """Return the characters in reverse order.

    :param text: The string to reverse.
    :return: The reversed string.
    """
    return text[::-1]

def larger_number(a: int, b: int) -> int:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a: The first integer.
    :param b: The second integer.
    :return: The larger integer.
    """
    if a >= b:
        return a
    return b

def average_two(a: int, b: int) -> float:
    """Calculate and return the average of two integers.

    :param a: The first integer.
    :param b: The second integer.
    :return: The average.
    """
    return (a + b) / 2

def can_afford(balance: float, cost: float) -> bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance: The available money.
    :param cost: The purchase cost.
    :return: True if the balance covers the cost.
    """
    return balance >= cost

def repeat_text(text: str, times: int) -> str:
    """Return one string containing text repeated the given
    number of times.

    :param text: The string to repeat.
    :param times: The number of repetitions.
    :return: The repeated string.
    """
    return text * times


def contains_word(sentence: str, word: str) -> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence: The sentence to search.
    :param word: The word to find.
    :return: True if found, otherwise False.
    """
    return word in sentence

def calculate_tip(cost: float, percent: float) -> float:
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost: The original cost.
    :param percent: The tip percentage.
    :return: The tip amount.
    """
    return cost * percent / 100


def make_initials(first_name: str, last_name: str) -> str:
    """Return the uppercase first letters of the two names.

    :param first_name: The first name.
    :param last_name: The last name.
    :return: The two uppercase initials.
    """
    return first_name[0].upper() + last_name[0].upper()

def percent_score(points: float, possible: float) -> float | None:
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: The points earned.
    :param possible: The total possible points.
    :return: The percentage, or None if possible is less than 1.
    """
    if possible < 1:
        return None
    return points / possible * 100

def is_between(
    number: float, minimum: float, maximum: float
) -> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number: The number to check.
    :param minimum: The minimum value.
    :param maximum: The maximum value.
    :return: True if within the range.
    """
    return minimum <= number <= maximum

def all_different(a: str, b: str, c: str) -> bool:
    """Check whether all three strings are different.

    :param a: The first string.
    :param b: The second string.
    :param c: The third string.
    :return: True if all three are different.
    """
    return a != b and a != c and b != c


def average_three(a: int, b: int, c: int) -> float:
    """Calculate and return the average of three integers.
    :param a: The first integer.
    :param b: The second integer.
    :param c: The third integer.
    :return: The average.
    """
    return (a + b + c) / 3

def describe_temperature(
    temperature: float,
    cold_limit: float,
    hot_limit: float
) -> str:
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature: The temperature to describe.
    :param cold_limit: The temperature below which it is cold.
    :param hot_limit: The temperature above which it is hot.
    :return: "cold", "hot", or "comfortable".
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"

if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    pass

# Advanced Functions

def temperature_in_safe_range(
    celsius: float,
    minimum_f: float,
    maximum_f: float
) -> bool:
    """Check whether a Celsius temperature is in a safe Fahrenheit range.

    :param celsius: The temperature in Celsius.
    :param minimum_f: The minimum safe Fahrenheit temperature.
    :param maximum_f: The maximum safe Fahrenheit temperature.
    :return: True if the converted temperature is within the range.
    """
    fahrenheit = celsius_to_fahrenheit(celsius)
    return minimum_f <= fahrenheit <= maximum_f


def can_afford_with_tip(
    balance: float,
    cost: float,
    tip_percent: float
) -> bool:
    """Check whether the balance covers the cost and tip.

    :param balance: The available money.
    :param cost: The original purchase cost.
    :param tip_percent: The tip percentage.
    :return: True if the balance covers the total.
    """
    tip = calculate_tip(cost, tip_percent)
    total = cost + tip
    return balance >= total


def meets_average(
    score1: float,
    score2: float,
    score3: float,
    required_average: float
) -> bool:
    """Check whether three scores meet the required average.

    :param score1: The first score.
    :param score2: The second score.
    :param score3: The third score.
    :param required_average: The minimum required average.
    :return: True if the average meets or exceeds the requirement.
    """
    average = average_three(score1, score2, score3)
    return average >= required_average


def initials_match(
    first_name: str,
    last_name: str,
    expected_initials: str
) -> bool:
    """Check whether initials match, ignoring capitalization.

    :param first_name: The person's first name.
    :param last_name: The person's last name.
    :param expected_initials: The initials to compare against.
    :return: True if the initials match, otherwise False.
    """
    initials = make_initials(first_name, last_name)
    return initials.lower() == expected_initials.strip().lower()


# ---------------------------------------
# TEST CALLS
# ---------------------------------------

if __name__ == "__main__":

    # Basic function tests
    print("BASIC FUNCTION TESTS")

    print(is_even(8))
    print(is_even(7))

    print(count_vowels("Arshia"))
    print(count_vowels("AEIOU"))

    print(celsius_to_fahrenheit(0))
    print(celsius_to_fahrenheit(25))

    print(reverse_text("Bob The robot"))
    print(reverse_text("Lakkaraju"))

    print(larger_number(10, 20))
    print(larger_number(5, 5))

    print(average_two(10, 20))
    print(average_two(5, 8))

    print(can_afford(50, 30))
    print(can_afford(10, 20))

    print(repeat_text("Hello", 3))
    print(repeat_text("Cool", 2))

    print(contains_word("Python is okay", "Python"))
    print(contains_word("Python is okay", "Java"))

    print(calculate_tip(20.0, 15))
    print(calculate_tip(50.0, 10))

    print(make_initials("Arshia", "Lakkaraju"))
    print(make_initials("Charmika", "Yellapu"))

    print(percent_score(18, 20))
    print(percent_score(10, 0))

    print(is_between(5, 1, 10))
    print(is_between(15, 1, 10))

    print(all_different("cat", "dog", "bird"))
    print(all_different("cat", "dog", "cat"))

    print(average_three(80, 90, 100))
    print(average_three(60, 70, 80))

    print(describe_temperature(10, 15, 25))
    print(describe_temperature(20, 15, 25))
    print(describe_temperature(30, 15, 25))

    # Advanced function tests
    print("ADVANCED FUNCTION TESTS")

    # Temperature challenge
    print(temperature_in_safe_range(20, 60, 80))
    print(temperature_in_safe_range(0, 60, 80))

    # Purchase challenge
    print(can_afford_with_tip(50, 40, 15))
    print(can_afford_with_tip(40, 40, 15))

    # Average challenge
    print(meets_average(80, 90, 100, 90))
    print(meets_average(60, 70, 80, 90))

    # Initials challenge
    print(initials_match("Arshia", "Lakkaraju", "AL"))
    print(initials_match("Charmika", "Yellapu", "CY"))
    print(initials_match("Nathan", "Forsyth", "NF"))


    # Optional interactive input validation example
    print("TEMPERATURE INPUT TEST")

    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            minimum_f = float(input("Enter minimum Fahrenheit: "))
            maximum_f = float(input("Enter maximum Fahrenheit: "))

            if minimum_f > maximum_f:
                print("Minimum cannot be greater than maximum.")
                continue

            result = temperature_in_safe_range(
                celsius, minimum_f, maximum_f
            )
            print("Within safe range:", result)
            break

        except ValueError:
            print("Invalid input. Please enter numbers only.")
