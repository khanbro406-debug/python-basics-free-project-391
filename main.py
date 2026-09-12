from password_generator import generate_password

print(generate_password(length=8, seed=1))
print(generate_password(length=12, seed=123))
print(generate_password(length=12, seed=123, use_special=True))
print(generate_password(length=8, seed=1, use_uppercase=False, use_digits=False))
print(generate_password(length=-3, seed=42))