# src/utils/file_manager.py

import os
from src.utils.shared import get_user_language
from src.utils.lang import translate

def save_file(content, directory, filename, user_id):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'wb') as file:
        file.write(content)

    user_language = get_user_language(user_id)
    return translate("file_saved", user_language, file_path=file_path)

def read_file(file_path, user_id):
    if not os.path.exists(file_path):
        user_language = get_user_language(user_id)
        return translate("file_not_found", user_language, file_path=file_path), None
    with open(file_path, 'rb') as file:
        content = file.read()
    user_language = get_user_language(user_id)
    return translate("file_retrieved", user_language, file_path=file_path), content

def delete_file(file_path, user_id):
    if not os.path.exists(file_path):
        user_language = get_user_language(user_id)
        return translate("file_not_found", user_language, file_path=file_path)
    os.remove(file_path)
    user_language = get_user_language(user_id)
    return translate("file_deleted", user_language)
