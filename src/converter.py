import logging
from typing import List
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

units = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix",
         "onze", "douze", "treize", "quatorze", "quinze", "seize"]

tens = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "septante", "huitante", "nonante"]

def convert_to_french(number: int) -> str:
    """Convert a number to its French word representation."""
    logger.info(f"Converting number: {number}")
    if number < 17:
        return units[number]
    elif number < 20:
        return "dix-" + units[number - 10]
    elif number < 100:
        return convert_tens(number)
    elif number < 1000:
        return convert_hundreds(number)
    else:
        return convert_thousands(number)

def convert_tens(number: int) -> str:
    """Convert a number less than 100 to its French word representation."""
    if number < 20:
        return units[number]
    elif number < 70:
        tens_part = tens[number // 10]
        units_part = number % 10
        if units_part == 1:
            return tens_part + "-et-" + units[units_part]
        elif units_part > 0:
            return tens_part + "-" + units[units_part]
        else:
            return tens_part
    elif number < 80:
        return "soixante-" + convert_to_french(number - 60)
    elif number < 100:
        if number == 80:
            return "quatre-vingts"
        return "quatre-vingt-" + convert_to_french(number - 80)


def convert_hundreds(number: int) -> str:
    """Convert a number less than 1000 to its French word representation."""
    if number == 100:
        return "cent"
    elif number < 200:
        return "cent-" + convert_to_french(number - 100)
    else:
        return units[number // 100] + "-cent" + ("-" + convert_to_french(number % 100) if number % 100 != 0 else "")

def convert_thousands(number):
    """
    Convert a number greater than or equal to 1000 to its French word representation.
    """
    if number < 2000:
        return "mille" + ("-" + convert_to_french(number % 1000) if number % 1000 != 0 else "")
    else:
        return convert_to_french(number // 1000) + "-mille" + ("-" + convert_to_french(number % 1000) if number % 1000 != 0 else "")

def convert_list(numbers: List[int]) -> List[str]:
    """Convert a list of numbers to their French word representations."""
    return [convert_to_french(number) for number in numbers]