from password_generator import generate_password

print(generate_password(5))
print(generate_password(30))
print(generate_password(length=30, use_uppercase=False, use_digits=False))
print(generate_password(length=70, use_special=True))