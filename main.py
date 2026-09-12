from password_generator import generate_password
from password_generator import check_password

print(generate_password(length=8, seed=1))
print(generate_password(length=12, seed=123))
print(generate_password(length=12, seed=123, use_special=True))
print(generate_password(length=8, seed=1, use_uppercase=False, use_digits=False))
print(generate_password(length=-3, seed=42))

print(check_password("abc"))
print(check_password("abcdefgh"))
print(check_password("abcdef1234"))
print(check_password("Abcdef1234"))
print(check_password("Abcdef123!"))