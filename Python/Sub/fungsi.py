def increment(number, by=1):  # by optional paramater
    return number + by


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def save_user(**user):
    print(user)
