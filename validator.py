import numpy as np
import ciphers
import os

def check_file_exists(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл '{filename}' не найден.")
    return True
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().strip()

def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)
def validate_alphabet(alphabet):
    """
    Проверяет корректность алфавита:
    - Алфавит не должен быть пустым.
    - Алфавит должен содержать уникальные символы.
    """
    if not alphabet:
        raise ValueError("Алфавит не может быть пустым.")
    
    if len(set(alphabet)) != len(alphabet):
        raise ValueError("Алфавит содержит повторяющиеся символы.")
    
    return True

def validate_key_caesar(key,alphabet):
    if key not in alphabet:
        raise ValueError(f"Некорректный символ '{key}' в ключе для шифра Цезаря.")
    return alphabet.index(key)
    

def validate_key_vigenere(key, alphabet)->str:
    for char in key:
        if char not in alphabet:
            raise ValueError(f"Некорректный символ '{char}' в ключе для шифра Виженера.")
    return key
        

def validate_affine_key(key, alphabet):
    if len(key) != 2:
        raise ValueError("Ключ для аффинного шифра должен состоять из двух символов.")
    M = len(alphabet)
    k1_index = alphabet.index(key[0])
    k2_index = alphabet.index(key[1])
    if ciphers.gcd(k1_index, M) != 1:
        raise ValueError("k1 и длина алфавита должны быть взаимно просты.")
    return k1_index, k2_index
    

def validate_key_hill(key, alphabet):
    if len(key) != 4:
        raise ValueError("Для шифра Хилла ключ должен состоять из четырёх символов.")
    k11 = alphabet.index(key[0])
    k12 = alphabet.index(key[1])
    k21 = alphabet.index(key[2])
    k22 = alphabet.index(key[3])
    m = len(alphabet)
    det = (k11 * k22 - k12 * k21) % m
    if det == 0 or np.gcd(det, m) != 1:
        raise ValueError("Матрица ключа не является обратимой по модулю длины алфавита.")

def validate_key_permutation(key, alphabet):
    if len(set(key)) != len(key):
        raise ValueError("Ключ для шифра перестановки должен содержать уникальные символы.")
    for char in key:
        if char not in alphabet:
            raise ValueError(f"Некорректный символ '{char}' в ключе для шифра перестановки.")


def validate_key_substitution(key, alphabet):
    """
    Проверяет корректность ключа для шифра простой замены:
    - Длина ключа должна быть равна длине алфавита.
    - Ключ должен состоять из уникальных символов.
    - Все символы ключа должны присутствовать в алфавите.
    
    :param key: Строка ключа для шифра замены.
    :param alphabet: Алфавит для проверки символов ключа.
    :raises ValueError: Если длина ключа не совпадает с длиной алфавита, если есть повторяющиеся символы
                       или если ключ содержит символы, не принадлежащие алфавиту.
    """
    # Проверка длины ключа
    if len(key) != len(alphabet):
        raise ValueError("Ключ для шифра простой замены должен содержать столько же символов, сколько и алфавит.")
    
    # Проверка уникальности символов ключа
    if len(set(key)) != len(alphabet):
        raise ValueError("Ключ для шифра простой замены должен состоять из уникальных символов алфавита.")
    
    # Проверка, что все символы ключа принадлежат алфавиту
    for char in key:
        if char not in alphabet:
            raise ValueError(f"Ключ для шифра простой замены содержит символ '{char}', который отсутствует в алфавите.")



def validate_text(text, alphabet):
    for char in text:
        if char not in alphabet:
            raise ValueError(f"Некорректный символ '{char}' в тексте.")

def validate_incorrect_symbols(text, alphabet, replace_with=None):
    """
    Обрабатывает некорректные символы в тексте:
    - Если replace_with не None, заменяет некорректные символы.
    - Если replace_with None, пропускает некорректные символы.
    """
    processed_text = []
    for char in text:
        if char not in alphabet:
            if replace_with is not None:
                print(f"Символ '{char}' заменен на '{replace_with}'.")
                processed_text.append(replace_with)
            else:
                print(f"Символ '{char}' пропущен.")
        else:
            processed_text.append(char)
    
    return ''.join(processed_text)

def validate_hill_key(key, alphabet):
    """Валидация ключа для шифра Хилла"""
    if len(key) != 4:
        raise ValueError("Ключ должен состоять из 4 символов.")
    k11 = alphabet.index(key[0])
    k12 = alphabet.index(key[1])
    k21 = alphabet.index(key[2])
    k22 = alphabet.index(key[3])
    det = (k11 * k22 - k12 * k21) % len(alphabet)
    if det == 0:
        raise ValueError("Определитель матрицы равен 0, матрица необратима.")
    if ciphers.gcd(det, len(alphabet)) != 1:
        raise ValueError("Определитель и длина алфавита не взаимно просты.")
    return True