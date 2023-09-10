import os
import pytest
import shutil

# Функция для создания папки
def create_folder(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    try:
        os.mkdir(folder_path)
        return f'Папка "{folder_name}" создана успешно.'
    except FileExistsError:
        return f'Папка "{folder_name}" уже существует.'

# Функция для удаления файла или папки
def delete_item(target_name):
    target_path = os.path.join(os.getcwd(), target_name)
    try:
        if os.path.isdir(target_path):
            shutil.rmtree(target_path)
            return f'Папка "{target_name}" удалена успешно.'
        elif os.path.isfile(target_path):
            os.remove(target_path)
            return f'Файл "{target_name}" удален успешно.'
        else:
            return f'"{target_name}" не существует.'
    except Exception as e:
        return str(e)

# Тесты для функций
def test_create_folder():
    assert create_folder("test_folder") == 'Папка "test_folder" создана успешно.'

def test_create_existing_folder():
    create_folder("test_folder")
    assert create_folder("test_folder") == 'Папка "test_folder" уже существует.'

def test_delete_existing_folder():
    create_folder("test_folder")
    assert delete_item("test_folder") == 'Папка "test_folder" удалена успешно.'

def test_delete_nonexistent_item():
    assert delete_item("nonexistent_item") == '"nonexistent_item" не существует.'

if __name__ == '__main__':
    pytest.main()