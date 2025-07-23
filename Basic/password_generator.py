import random
import string

ask1 = input(int("What length password you need?: "))

all_characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(all_characters) for _ in range(ask1))
print("Generated password:", password)


