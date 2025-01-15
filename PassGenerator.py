import secrets
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                      use_numbers=True, use_special=True, exclude_similar=False):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = "!@#$%^&*()-_=+[]{};:,.<>?/"
    similar_chars = "Il1O0"

    char_pool = ""
    if use_lowercase:
        char_pool += lowercase
    if use_uppercase:
        char_pool += uppercase
    if use_numbers:
        char_pool += numbers
    if use_special:
        char_pool += special
    if exclude_similar:
        char_pool = ''.join(ch for ch in char_pool if ch not in similar_chars)

    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    return password

if __name__ == "__main__":
    print(f"-# Welcome to the Password Generator! #-\n########################################\n\t-  #Made by Mick19j#  -\n########################################\n")
    try:
        length = int(input("Enter password length! - (default = 12): ") or 12)
        use_uppercase = input("Include uppercase letters? - (y/n, default = y): ").lower() != "n"
        use_lowercase = input("Include lowercase letters? - (y/n, default = y): ").lower() != "n"
        use_numbers = input("Include numbers? - (y/n, default = y): ").lower() != "n"
        use_special = input("Include special characters? - (y/n, default = y): ").lower() != "n"
        exclude_similar = input("Exclude similar-looking characters? - (y/n, default = n): ").lower() == "y"
        
        password = generate_password(length, use_uppercase, use_lowercase,
                                     use_numbers, use_special, exclude_similar)
        print(f"\nGenerated Password:\n(Double Click to copy!)\n\n-\n{password}\n-\n\n########################################\n     -# Thank you for using me! #-\n########################################")
    except ValueError as e:
        print(f"Error: {e}")
