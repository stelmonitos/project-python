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


# Przykład szyfrowania i deszyfrowania tekstu
name_to_encrypt = "Witaj w świecie kryptografii!"
key = 3

encrypted = cezar_code(name_to_encrypt, key)
print("Zaszyfrowany tekst:", encrypted)

decrypted = cezara_decrypt(encrypted, key)
print("Odszyfrowany tekst:", decrypted)


# Funkcja zapisu danych do zewnętrznego pliku
def save_to_file(folders, encrypted, decrypted):
    # Zapisanie listy folderów
    with open("folders_list.txt", "w", encoding="utf-8") as folder_file:
        folder_file.write("Lista folderów:\n")
        for folder in folders:
            folder_file.write(f"{folder}\n")

    # Zapisanie wyników szyfrowania i deszyfrowania
    with open("encryption_results.txt", "w", encoding="utf-8") as result_file:
        result_file.write("Wyniki szyfrowania i deszyfrowania:\n")
        result_file.write(f"Zaszyfrowany tekst: {encrypted}\n")
        result_file.write(f"Odszyfrowany tekst: {decrypted}\n")

    print("Dane zostały zapisane do plików 'folders_list.txt' i 'encryption_results.txt'.")


# Wywołanie funkcji zapisu danych do pliku
save_to_file(a, encrypted, decrypted)
