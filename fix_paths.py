# Укажи имя проекта, которое должно быть везде (замени на правильное)
correct_project_name = 'pythonProject1Modeldz'

# Список файлов, где нужно искать и исправлять ошибки
files_to_check = [
    'manage.py',
    f'{correct_project_name}/wsgi.py',
    f'{correct_project_name}/asgi.py',
    f'{correct_project_name}/settings.py',
    f'{correct_project_name}/urls.py'
]


def replace_in_file(file_path, wrong_value, correct_value):
    """Заменяет все вхождения wrong_value на correct_value в указанном файле."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Проверка, есть ли что-то для замены
        if wrong_value in content:
            content = content.replace(wrong_value, correct_value)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Исправлено в файле: {file_path}')
        else:
            print(f'Ничего не найдено для исправления в файле: {file_path}')

    except FileNotFoundError:
        print(f'Файл не найден: {file_path}')


def main():
    wrong_value = 'c'  # Ошибочное имя модуля, которое нужно заменить
    correct_value = correct_project_name  # Правильное имя проекта

    # Проверяем каждый файл и заменяем ошибочные вхождения
    for file in files_to_check:
        replace_in_file(file, wrong_value, correct_value)


if __name__ == '__main__':
    main()
