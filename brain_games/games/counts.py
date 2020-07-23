def check(result, answer):
    """checks whether answer is the same as the correct result"""
    if result == answer:
        return True
    else:
        return False


def check_even(number):
    """Checks whether number is even"""
    if number % 2 == 0:
        return "yes"
    else:
        return "no"
