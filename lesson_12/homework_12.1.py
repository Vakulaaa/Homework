import re


def clean_html_file(input_filename, output_filename="cleaned.txt"):

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()

        cleaned_content = re.sub(r'<[^>]*>', '', content)

        lines = cleaned_content.splitlines()
        cleaned_lines = [line.strip() for line in lines if line.strip()]

        final_content = "\n".join(cleaned_lines)

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(final_content)

        print(f"Файл сохранен в {output_filename}")

    except FileNotFoundError:
        print(f"Файл {input_filename} не найден.")
    except Exception as e:
        print(f"Ошибка {e}")
