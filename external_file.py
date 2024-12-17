from pathlib import Path


# Skanowanie folderu i analiza plików
def analyze_and_save_data():
    # 1. Wprowadzenie ścieżki
    path = Path(input("Wprowadź ścieżkę folderu do analizy: "))

    # Sprawdzenie, czy podana ścieżka jest folderem
    if not path.is_dir():
        print("Podana ścieżka nie jest folderem.")
        return

    # 2. Zbieranie danych o plikach
    analysis_data = []

    # Iterowanie przez pliki w folderze
    for file in path.iterdir():
        if file.is_file():
            file_name = file.name
            word_count = len(file_name.split())  # Liczenie słów w nazwie pliku
            char_count = len(file_name)  # Liczenie znaków w nazwie pliku
            analysis_data.append((file_name, word_count, char_count))

    # 3. Zapis danych do pliku
    output_file = "file_analysis.txt"

    # Zapis danych do pliku
    with open(output_file, "w", encoding="utf-8") as f:
        for file_name, word_count, char_count in analysis_data:
            f.write(f"Plik: {file_name}, Słowa: {word_count}, Znaki: {char_count}\n")

    # Potwierdzenie zapisania danych
    print(f"Dane zostały zapisane do pliku {output_file}")


# Uruchomienie funkcji
analyze_and_save_data()
