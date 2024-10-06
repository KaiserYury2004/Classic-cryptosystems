import numpy as np
import validator,ciphers
'''В данном файле проводится тестировка валидаторов'''
def test_validate_key_caesar():
    try:
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ '
        assert validator.validate_key_caesar('А', alphabet) == 0
        assert validator.validate_key_caesar('Я', alphabet) == alphabet.index('Я')
        try:
            validator.validate_key_caesar('1', alphabet)
        except ValueError as e:
            assert str(e) == "Некорректный символ '1' в ключе для шифра Цезаря."
        print("Тест `validate_key_caesar` пройден.")
    except AssertionError as e:
        print(f"Тест `validate_key_caesar` провален: {e}")


def test_validate_key_vigenere():
    try:
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ '
        assert validator.validate_key_vigenere('АБВ', alphabet) == 'АБВ'
        try:
            validator.validate_key_vigenere('123', alphabet)
        except ValueError as e:
            assert str(e) == "Некорректный символ '1' в ключе для шифра Виженера."
        print("Тест `validate_key_vigenere` пройден.")
    except AssertionError as e:
        print(f"Тест `validate_key_vigenere` провален: {e}")


def test_validate_affine_key():
    try:
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ '

        key = 'БВ'  # Ожидаем k1_index=1, k2_index=2
        k1_index, k2_index = validator.validate_affine_key(key, alphabet)
        assert k1_index == 1 and k2_index == 2, "Ошибка в индексации ключа 'БВ'"
        
        # Тест 2: Некорректный ключ (k1 и длина алфавита не взаимно просты)
        try:
            validator.validate_affine_key('АБ', alphabet)  # 'А' имеет индекс 0, что не взаимно просто с длиной алфавита
            print("Ошибка: Ожидалась ошибка для некорректного ключа 'АБ'")
        except ValueError as e:
            assert str(e) == "k1 и длина алфавита должны быть взаимно просты", "Неправильное сообщение об ошибке для ключа 'АБ'"

        # Тест 3: Некорректная длина ключа
        try:
            validator.validate_affine_key('А', alphabet)  # Ключ должен состоять из двух символов
            print("Ошибка: Ожидалась ошибка для ключа с некорректной длиной 'А'")
        except ValueError as e:
            assert str(e) == "Ключ для аффинного шифра должен состоять из двух символов.", "Неправильное сообщение об ошибке для ключа с длиной 1"
        print("Тест `validate_affine_key` пройден.")
    except AssertionError as e:
        print(f"Тест `validate_affine_key` провален: {e}")


def test_validate_key_hill():
    try:
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ '
        try:
            validator.validate_key_hill('АБВ', alphabet)
        except ValueError as e:
            assert str(e) == "Для шифра Хилла ключ должен состоять из четырёх символов."
        try:
            validator.validate_key_hill('АБВГ', alphabet)
        except ValueError as e:
            assert str(e) == "Матрица ключа не является обратимой по модулю длины алфавита."
        print("Тест `validate_key_hill` пройден.")
    except AssertionError as e:
        print(f"Тест `validate_key_hill` провален: {e}")


def test_validate_key_permutation():
    try:
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ '
        try:
            validator.validate_key_permutation('АБВБ', alphabet)
        except ValueError as e:
            assert str(e) == "Ключ для шифра перестановки должен содержать уникальные символы."
        try:
            validator.validate_key_permutation('1234', alphabet)
        except ValueError as e:
            assert str(e) == "Некорректный символ '1' в ключе для шифра перестановки."
        print("Тест `validate_key_permutation` пройден.")
    except AssertionError as e:
        print(f"Тест `validate_key_permutation` провален: {e}")


def test_validate_key_substitution():
    """
    Тест для функции validate_key_substitution, проверяющий корректность ключа для шифра замены.
    """
    try:
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ '
        correct_key = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ '
        validator.validate_key_substitution(correct_key, alphabet)
        try:
            validator.validate_key_substitution('АБВ', alphabet)
            print("Ошибка: Ожидалась ошибка для ключа некорректной длины.")
        except ValueError as e:
            assert str(e) == "Ключ для шифра простой замены должен содержать столько же символов, сколько и алфавит.", "Неправильное сообщение об ошибке для некорректной длины ключа."
        
        try:
            validator.validate_key_substitution(alphabet + 'А', alphabet)
            print("Ошибка: Ожидалась ошибка для ключа с повторяющимися символами.")
        except ValueError as e:
            assert str(e) == "Ключ для шифра простой замены должен состоять из уникальных символов алфавита.", "Неправильное сообщение об ошибке для ключа с повторяющимися символами."
        try:
            validator.validate_key_substitution('ABCDEFGHIJKLMNOPQRSTUVWXYZ', alphabet)
            print("Ошибка: Ожидалась ошибка для ключа с символами, отсутствующими в алфавите.")
        except ValueError as e:
            assert str(e) == "Ключ для шифра простой замены содержит символ 'A', который отсутствует в алфавите.", "Неправильное сообщение об ошибке для символов, отсутствующих в алфавите."
        
        print("Тест `validate_key_substitution` пройден.")
    
    except AssertionError as e:
        print(f"Тест `validate_key_substitution` провален: {e}")
test_validate_key_substitution()



def test_validate_text():
    try:
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ '
        text = 'КАРЛ'
        validator.validate_text(text, alphabet)
        try:
            validator.validate_text('КАРЛ123', alphabet)
        except ValueError as e:
            assert str(e) == "Некорректный символ '1' в тексте."
        print("Тест `validate_text` пройден.")
    except AssertionError as e:
        print(f"Тест `validate_text` провален: {e}")

def test_gcd():
    print("Тестирование функции gcd:")
    try:
        assert ciphers.gcd(48, 18) == 6, "Ошибка в gcd(48, 18)"
        assert ciphers.gcd(101, 103) == 1, "Ошибка в gcd(101, 103)"
        assert ciphers.gcd(0, 5) == 5, "Ошибка в gcd(0, 5)"
        assert ciphers.gcd(10, 0) == 10, "Ошибка в gcd(10, 0)"
        assert ciphers.gcd(13, 17) == 1, "Ошибка в gcd(13, 17)"
        print("Все тесты для gcd пройдены.")
    except AssertionError as e:
        print(e)


def test_mod_inverse():
    print("Тестирование функции mod_inverse:")
    try:
        assert ciphers.mod_inverse(3, 11) == 4, "Ошибка в mod_inverse(3, 11)"
        assert ciphers.mod_inverse(2, 5) == 3, "Ошибка в mod_inverse(2, 5)"
        try:
            ciphers.mod_inverse(6, 12)
            print("Ошибка: mod_inverse(6, 12) не должно иметь обратного.")
        except ValueError as e:
            assert str(e) == "Обратного для 6 по модулю 12 не существует.", "Неправильное сообщение об ошибке для mod_inverse(6, 12)"
        
        print("Все тесты для mod_inverse пройдены.")
    except AssertionError as e:
        print(e)

def run_all_tests():
    test_validate_key_caesar()
    test_validate_key_vigenere()
    test_validate_affine_key()
    test_validate_key_hill()
    test_validate_key_permutation()
    test_validate_key_substitution()
    test_validate_text()
    test_gcd()
    test_mod_inverse()
    print("Все тесты завершены.")
if __name__ == "__main__":
    run_all_tests()
