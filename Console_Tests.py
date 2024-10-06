import ciphers
import validator
try:
    validator.check_file_exists('in.txt')
    validator.check_file_exists('alphabet.txt')
    validator.check_file_exists('key.txt')
    print("Все необходимые файлы найдены.")
except FileNotFoundError as e:
        raise ValueError(e)
alphabet=validator.read_file('alphabet.txt')
if(validator.validate_alphabet(alphabet) is False):
    raise ValueError("Алфавит некорректен!")
cipher_system=input('Выберите шифр,который хотите использовать(Caesar,Vigenere,Affine,Hill,Permutation,Substitution):')
operation_choise=input('Какую операцию вы хотите выполнить(шифрование или расшифрование):encryption or decryption?')
if(operation_choise=='encryption'):
    encryption=True
elif(operation_choise=='decryption'):
    encryption=False
else:
    print('Неверный выбор!')
    SystemExit(0)
text=validator.validate_incorrect_symbols(validator.read_file('in.txt'), alphabet,' ')
key = validator.read_file('key.txt')
if cipher_system=='Caesar':
    validator.validate_key_caesar(key, alphabet)
    result=ciphers.caesar_cipher(text,key, alphabet, encrypt=encryption)
elif cipher_system == 'Vigenere':
    key=validator.validate_key_vigenere(key, alphabet)
    result = ciphers.vigenere_cipher(text,key,alphabet, encrypt=encryption)
elif cipher_system == 'Affine':
    validator.validate_affine_key(key,alphabet)
    result = ciphers.affine_cipher(text, key, alphabet, encrypt =encryption)
elif cipher_system == 'Hill':
    validator.validate_key_hill(key, alphabet)
    if(encryption):
        result=ciphers.hill_encrypt(text,key,alphabet)
    else:
        result=ciphers.hill_decrypt(text,key,alphabet)
elif cipher_system == 'Permutation':
    validator.validate_key_permutation(key, alphabet)
    result = ciphers.permutation_cipher(text, key, alphabet, encrypt =encryption)
elif cipher_system == 'Substitution':
    result = ciphers.substitution_cipher(text, key, alphabet, encrypt =encryption)
else:
    raise ValueError("Неверно введено название шифра")
if(encryption):
        print("Задача выполнена,проверьте файл encrypt.txt!")
        validator.write_file('encrypt.txt',result)
else:
        print("Задача выполнена,проверьте файл decrypt.txt!")
        validator.write_file('decrypt.txt',result)
