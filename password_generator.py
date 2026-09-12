LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*"
def next_random(number):
    return (16807 * number) % 2147483647

def generate_password(length, seed, use_uppercase=True,use_digits=True, use_special=False):
    alphabet = LOWERCASE
    if use_uppercase:
        alphabet += UPPERCASE
    if use_digits:
        alphabet += DIGITS
    if use_special:
        alphabet += SPECIAL
    alphabet_length = len(alphabet)
    result = ""
    current = seed
    for i in range(length):
        current = next_random(current)
        index = current % alphabet_length
        result = result + alphabet[index]
    return result