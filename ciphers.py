import numpy as np
import validator
def caesar_cipher(text, key, alphabet, encrypt=True):
    """Функция шифрования/расшифрования шифром Цезаря"""
    result = []
    if key not in alphabet:
        raise ValueError(f"Некорректный символ '{key}' в ключе для шифра Цезаря.")
    key=alphabet.index(key)
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            shift = key if encrypt else -key
            new_index = (index + shift) % len(alphabet)
            result.append(alphabet[new_index])
        else:
            result.append(char)
    return ''.join(result)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Находим мультипликативную обратную для a по модулю m"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Обратного для {a} по модулю {m} не существует.")

def affine_cipher(text,key, alphabet, encrypt=True):
    """Функция шифрования/расшифрования аффинным шифром"""
    M = len(alphabet)
    
    # Валидация ключа
    k1_index, k2_index = validator.validate_affine_key(key, alphabet)
    result = []
    for char in text:
        if char in alphabet:
            x = alphabet.index(char)
            if encrypt:
                new_char = (k1_index * x + k2_index) % M
            else:
                k1_inv = mod_inverse(k1_index, M)
                if k1_inv is None:
                    raise ValueError(f"Не существует обратного для k1={k1_index} по модулю {M}")
                new_char = (k1_inv * (x - k2_index)) % M
            
            result.append(alphabet[new_char])
        else:
            result.append(char)  # Оставляем символ без изменений, если он не в алфавите
    
    return ''.join(result)

def substitution_cipher(text, key, alphabet, encrypt=True):
    "Функция шифрования/расшифрования шифром простой замены"
    if len(key) != len(alphabet):
        raise ValueError("Ключ должен быть той же длины, что и алфавит")
    substitution_dict = {alphabet[i]: key[i] for i in range(len(alphabet))}
    reverse_substitution_dict = {key[i]: alphabet[i] for i in range(len(alphabet))}
    result = []
    for char in text:
        if char in alphabet:
            if encrypt:
                result.append(substitution_dict[char])
            else:
                result.append(reverse_substitution_dict[char])
        else:
            result.append(char)

    return ''.join(result)

def permutation_cipher(text, key, alphabet, encrypt=True):
    """Функция шифрования/расшифрования шифром перестановки"""
    m = len(alphabet)
    key_length = len(key)
    
    if len(set(key)) != key_length:
        raise ValueError("Ключ должен состоять из попарно различных символов алфавита.")
    
    key_order = sorted(range(key_length), key=lambda x: alphabet.index(key[x]))
    
    original_length = len(text)
    if len(text) % key_length != 0:
        padding_length = key_length - (len(text) % key_length)
        text += alphabet[len(alphabet)-1] * padding_length

    result = []
    for i in range(0, len(text), key_length):
        block = text[i:i+key_length]
        
        if encrypt:
            result_block = ''.join([block[key_order[j]] for j in range(key_length)])
        else:
            result_block = [''] * key_length
            for j in range(key_length):
                result_block[key_order[j]] = block[j]
            result_block = ''.join(result_block)
        
        result.append(result_block)
    decrypted_text = ''.join(result)
    if not encrypt:
        decrypted_text = decrypted_text[:original_length]

    return decrypted_text
def vigenere_cipher(text, key, alphabet, encrypt=True):
    """"Функция шифрования/расшифрования шифром Виженера"""
    result = []
    key=validator.validate_key_vigenere(key, alphabet)
    key_length = len(key)
    key_indices = [alphabet.index(k) for k in key]
    alphabet_len = len(alphabet)
    key_index = 0
    for char in text:
        if char in alphabet:
            text_index = alphabet.index(char)
            shift = key_indices[key_index % key_length]
            if encrypt:
                new_index = (text_index + shift) % alphabet_len
            else:
                new_index = (text_index - shift) % alphabet_len
            result.append(alphabet[new_index])
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)
def hill_encrypt(text, key, alphabet):
    """Шифрование шифром Хилла"""
    if len(text) % 2 != 0:
        text += alphabet[0]
    k11 = alphabet.index(key[0])
    k12 = alphabet.index(key[1])
    k21 = alphabet.index(key[2])
    k22 = alphabet.index(key[3])
    result = ""
    for i in range(0, len(text), 2):
        x1 = alphabet.index(text[i])
        x2 = alphabet.index(text[i + 1])
        y1 = (k11 * x1 + k21 * x2) % len(alphabet)
        y2 = (k12 * x1 + k22 * x2) % len(alphabet)

        result += alphabet[y1]
        result += alphabet[y2]

    return result
def hill_decrypt(text, key, alphabet):
    """Расшифрование шифром Хилла"""
    k11 = alphabet.index(key[0])
    k12 = alphabet.index(key[1])
    k21 = alphabet.index(key[2])
    k22 = alphabet.index(key[3])
    det = (k11 * k22 - k12 * k21) % len(alphabet)
    if det == 0:
        raise ValueError("Матрица необратима, дешифрование невозможно.")
    det_inv = mod_inverse(det, len(alphabet))
    inv_k11 = (det_inv * k22) % len(alphabet)
    inv_k12 = (-det_inv * k12) % len(alphabet)
    inv_k21 = (-det_inv * k21) % len(alphabet)
    inv_k22 = (det_inv * k11) % len(alphabet)
    result = ""
    for i in range(0, len(text), 2):
        y1 = alphabet.index(text[i])
        y2 = alphabet.index(text[i + 1])
        x1 = (inv_k11 * y1 + inv_k21 * y2) % len(alphabet)
        x2 = (inv_k12 * y1 + inv_k22 * y2) % len(alphabet)
        result += alphabet[x1]
        result += alphabet[x2]

    return result
