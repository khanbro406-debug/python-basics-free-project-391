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
def check_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    has_lower = False
    for char in password:
        if char in LOWERCASE:
            has_lower = True
            break
    if has_lower:
        score += 1
    has_upper = False
    for char in password:
        if char in UPPERCASE:
            has_upper = True
        break
    if has_upper:
        score += 1
    has_digit = False
    for char in password:
        if char in DIGITS:
            has_digit = True
            break
    if has_digit: 
        score += 1
    has_special = False
    for char in password:
        if char in SPECIAL:
            has_special = True
            break
    if has_special:
        score += 1
    if score <= 2:
            verdict = "Слабый"
    elif score == 3:
        verdict = "Средний"
    elif score == 4:
        verdict = "Надёжный"
    else:
        verdict = "Очень надёжный"
    return f"{verdict} пароль (оценка {score} из 5)"
    
