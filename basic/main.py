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

