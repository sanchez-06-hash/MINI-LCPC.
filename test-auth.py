
from auth import hash_password, verify_password

password = "TestPassword123"

hashed_password = hash_password(password)

print("Password hashed:", hashed_password != password)
print("Correct password:", verify_password(password, hashed_password))
print("Wrong password:", verify_password("WrongPassword", hashed_password))