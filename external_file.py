from pathlib import Path

def folders_list():
    path = Path(input("Enter the path that you want to scan: "))
    folders = []
    for i, element in enumerate(path.iterdir()):
        if element.is_dir():
            print(i + 1, element.name)
            folders.append(element.name)
    return folders

def analyze_file_names(folders):
    word_count = [len(folder.split()) for folder in folders]
    char_count = [len(folder) for folder in folders]
    return word_count, char_count

# Wywołanie funkcji z możliwością wyboru ścieżki
a = folders_list()
word_count, char_count = analyze_file_names(a)

for index, (folder, words, chars) in enumerate(zip(a, word_count, char_count)):
    print(f"{index + 1}. {folder} - Words: {words}, Characters: {chars}")
    
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

print("Odszyfrowany tekst:", decrypted)
