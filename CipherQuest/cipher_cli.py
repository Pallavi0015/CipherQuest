def main():
    print("🎮 Welcome to Secret Message Encoder!")
    print("1. Encrypt Message\n2. Decrypt Message\n3. Cipher Challenge\n4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        msg = input("Enter your message: ")
        shift = int(input("Enter shift value (1-25): "))
        print("Encrypted:", encrypt_caesar(msg, shift))
    elif choice == "2":
        cipher = input("Enter the encrypted message: ")
        shift = int(input("Enter the shift used: "))
        print("Decrypted:", decrypt_caesar(cipher, shift))
    elif choice == "3":
        play_challenge()
    else:
        print("Goodbye!")

def encrypt_caesar(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt_caesar(cipher, shift):
    return encrypt_caesar(cipher, -shift)

def play_challenge():
    print("\n🕵️ Cipher Challenge Mode!")
    secret = "python is fun"
    shift = 4
    encrypted = encrypt_caesar(secret, shift)
    print("Encrypted message:", encrypted)
    guess = input("Decrypt it and enter your guess: ").strip().lower()
    if guess == secret:
        print("🎉 Correct! You're a codebreaker!")
    else:
        print("❌ Nope! Try again later.")

main()