# Demo List

phones = ["Iphone", "SamSung", "Nokia", "Xiaomi"]

phones[3] = "Oppo"

phones.append("xxxx")

phones.sort()

print(phones)

tuple_phones = ("Iphone", "SamSung", "Nokia", "Xiaomi")

print(tuple_phones)

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'


def print_in_color(text, color):
    print(color + text + RESET)


# Example usage
print_in_color("This is red text", RED)
print_in_color("This is green text", GREEN)
print_in_color("This is yellow text", YELLOW)
print_in_color("This is blue text", BLUE)
print_in_color("This is magenta text", MAGENTA)
print_in_color("This is cyan text", CYAN)
print_in_color("This is white text", WHITE)
