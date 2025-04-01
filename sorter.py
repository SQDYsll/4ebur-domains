# Открываем исходный файл для чтения и создаем новый файл для записи
input_file = "input.txt"  # замените на имя вашего исходного файла
output_file = "output.txt"  # замените на имя вашего файла вывода

# Укажите символы для добавления
start_symbol = "domain("
end_symbol = ")->proxy"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        # Убираем лишние пробелы или переносы строк
        modified_line = f"{start_symbol}{line.strip()}{end_symbol}\n"
        outfile.write(modified_line)

print("Файл успешно обработан!")