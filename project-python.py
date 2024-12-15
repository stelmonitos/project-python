from pathlib import Path

#SKANOWANIE WYBRANEJ SCIEZKI
def folders_list():
    path = Path(input("Enter the path that you wanna scan: "))
    folders = []
    for i, element in enumerate(path.iterdir()):
        if element.is_dir():
            print(i + 1, element.name)
            folders.append(element.name)
    return folders


a = folders_list()
print(a[0])

# SZYFROWANIE
def cezar_code(name_to_encrypt, key):
    output = ""
    for char in name_to_encrypt:
        if char.isalpha():
            digit_move = 65 if char.isupper() else 97
            output += chr((ord(char) - digit_move + key) % 26 + digit_move)
        else:
            output += char
    return output


def cezara_decrypt(name_to_encrypt, key):
    return cezar_code(name_to_encrypt, -key)


name_to_encrypt = "Witaj w świecie kryptografii!"
key = 3

encrypted = cezar_code(name_to_encrypt, key)
print("Zaszyfrowany tekst:", encrypted)

decrypted = cezara_decrypt(encrypted, key)
print("Odszyfrowany tekst:", decrypted)