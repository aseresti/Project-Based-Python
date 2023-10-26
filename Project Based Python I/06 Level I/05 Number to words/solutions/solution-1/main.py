# Importing required constants
from constants import UNDER_20, ABOVE_100, TENS

def num_to_word(num: int) -> str:
    """
    Function converts an integer into words.

    :param int num: The number to be converted to words.
    :return: The word representation of the number.
    :rtype: str

    """
    # If the number is less than 20, use direct mapping.
    if num < 20:
        return UNDER_20[num]

    # If the number is less than 100, calculate tens and ones separately.
    if num < 100:
        return TENS[num // 10 - 2] + ("" if num % 10 == 0 else " " + UNDER_20[num % 10])

    # For numbers 100 and above, calculate words recursively.
    pivot = max([key for key in ABOVE_100.keys() if key <= num])

    return (
        num_to_word(num // pivot)
        + " "
        + ABOVE_100[pivot]
        + ("" if num % pivot == 0 else " " + num_to_word(num % pivot))
    )

def main() -> None:
    """
    Function accepts a number from the user and prints its word representation.

    :return: None
    """

    # Get number from user.
    num = int(input("Enter a Number: "))
    # Check if number is in acceptable range.
    if num >= 0 and num <= 999999999999:
        # Print number in words.
        print(num_to_word(num))
    else:
        print("Number out of range")

if __name__ == "__main__":
    main()

