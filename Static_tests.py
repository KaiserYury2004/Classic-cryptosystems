import ciphers
import numpy as np
"""В данном файле все тесты заданы с корректными данными."""
alphabet = 'АБВГДЕЙЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
plaintext = 'ПРИВЕТ МИР'

"""Также здесь будут использованы тесты из задания "Самый быстрый шифровальщик"""

alphabet_practice='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key='Д'
print('\nШИФР ЦЕЗАРЯ')
encrypted_text = ciphers.caesar_cipher(plaintext, key, alphabet, encrypt=True)
print(f"Зашифрованный текст: {encrypted_text}")
decrypted_text = ciphers.caesar_cipher(encrypted_text,key, alphabet, encrypt=False)
print(f"Расшифрованный текст: {decrypted_text}")
practice_result=ciphers.caesar_cipher('ЁПАШВЧ',alphabet_practice[24], alphabet_practice, encrypt=False)
print(f"Задание с практики:{practice_result}")

print("\nАФФИННЫЙ ШИФР")
k1, k2 = 'Е', 'З'
encrypted_text = ciphers.affine_cipher(plaintext,'ЕЗ',alphabet, encrypt=True)
print(f"Зашифрованный текст: {encrypted_text}")
decrypted_text = ciphers.affine_cipher(encrypted_text,'ЕЗ', alphabet, encrypt=False)
print(f"Расшифрованный текст: {decrypted_text}")
k1, k2 = alphabet_practice[19],alphabet_practice[9]
practice_result=ciphers.affine_cipher('ИАЕКЖИ',str(k1+k2), alphabet_practice, encrypt=False)
print(f"Задание с практики:{practice_result}")

print("\nШИФР ПРОСТОЙ ЗАМЕНЫ")
encrypted_text = ciphers.substitution_cipher(plaintext,'ЙЦУКЕНГШЩЗХЪФЫВАРПОЛДЖЭЯЧСМИТЬБЮЁ ', alphabet, encrypt=True)
print(f"Зашифрованный текст: {encrypted_text}")
decrypted_text = ciphers.substitution_cipher(encrypted_text, 'ЙЦУКЕНГШЩЗХЪФЫВАРПОЛДЖЭЯЧСМИТЬБЮЁ ', alphabet, encrypt=False)
print(f"Расшифрованный текст: {decrypted_text}")
practice_result=ciphers.substitution_cipher('ЦАЦРАДЕЙУЙ','ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ', alphabet_practice, encrypt=False)
print(f"Задание с практики:{practice_result}")

print("\nШИФР ВИЖИНЕРА")
encrypted_text = ciphers.vigenere_cipher("ПРИВЕТ МИР", 'КЛЮЧ', alphabet, encrypt=True)
print(f"Зашифрованный текст: {encrypted_text}")
decrypted_text = ciphers.vigenere_cipher(encrypted_text, "КЛЮЧ", alphabet, encrypt=False)
print(f"Расшифрованный текст: {decrypted_text}")
practice_result=ciphers.vigenere_cipher('ЕТЦЙСПЧЕЭЕ','СЕНТЯБРЬ', alphabet_practice, encrypt=False)
print(f"Задание с практики:{practice_result}")

print('\nШИФР ПЕРЕСТАНОВКИ')
key='МЕ'
encrypted_text = ciphers.permutation_cipher("НЕ ДОВЕРЯЙ ВИКТОРУ",key, alphabet, encrypt=True)
print(f"Зашифрованный текст: {encrypted_text}")
decrypted_text = ciphers.permutation_cipher(encrypted_text,key, alphabet, encrypt=False)
print(f"Расшифрованный текст: {decrypted_text}")
practice_result=ciphers.permutation_cipher('НАЕВЖНИВЪСКОРТ','СТРЕЛОК', alphabet_practice, encrypt=False)
print(f"Задание с практики:{practice_result}")


print("\nШИФР ХИЛА")
plaintext = 'ПРИВЕТ'
key = 'ДОРН'
encrypted_text = ciphers.hill_encrypt(plaintext, key, alphabet)
print(f"Зашифрованный текст: {encrypted_text}")
decrypted_text = ciphers.hill_decrypt(encrypted_text, key, alphabet)
print(f"Расшифрованный текст: {decrypted_text}")
practice_result=ciphers.hill_decrypt('ЗЕРЭУБЭХГЗГЧ','МАСВ', alphabet_practice)
print(f"Задание с практики:{practice_result}")

a=('С','Т','Р','Е','Л','О','К')
print(sorted(a))