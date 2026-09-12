LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*"
def generate_password(length, use_uppercase=True,use_digits=True, use_special=False):
    alphabet = LOWERCASE
    if use_uppercase:
        alphabet += UPPERCASE
    if use_digits:
        alphabet += DIGITS
    if use_special:
        alphabet += SPECIAL
    alphabet_length = len(alphabet)
    result = ""
    for i in range(length):
        index = i % alphabet_length
        result = result + alphabet[index]
    return result