import unittest
from alphabet_cipher import AlphabetCipher

class TestAlphabetCipher(unittest.TestCase):
    """Тесты для готовой части"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_symbol_to_number(self):
        """Проверка: символ -> номер"""
        self.assertEqual(self.cipher.get_number_by_symbol('А'), 1)
        self.assertEqual(self.cipher.get_number_by_symbol('_'), 0)
        self.assertEqual(self.cipher.get_number_by_symbol('Я'), 31)
        print("✓ test_symbol_to_number passed")

    def test_number_to_symbol(self):
        """Проверка: номер -> символ"""
        self.assertEqual(self.cipher.get_symbol_by_number(1), 'А')
        self.assertEqual(self.cipher.get_symbol_by_number(0), '_')
        self.assertEqual(self.cipher.get_symbol_by_number(31), 'Я')
        print("✓ test_number_to_symbol passed")

    def test_add_numbers(self):
        """Проверка сложения с mod 32"""
        self.assertEqual(self.cipher.add_numbers(30, 5), 3)
        self.assertEqual(self.cipher.add_numbers(31, 1), 0)
        self.assertEqual(self.cipher.add_numbers(0, 0), 0)
        print("✓ test_add_numbers passed")

    def test_subtract_numbers(self):
        """Проверка вычитания с mod 32"""
        self.assertEqual(self.cipher.subtract_numbers(2, 5), 29)
        self.assertEqual(self.cipher.subtract_numbers(0, 1), 31)
        self.assertEqual(self.cipher.subtract_numbers(31, 31), 0)
        print("✓ test_subtract_numbers passed")

    def test_add_symbols(self):
        """Проверка сложения символов"""
        # А(1) + В(3) = 4 -> Г
        self.assertEqual(self.cipher.add_symbols('А', 'В'), 'Г')
        
        # Я(31) + Б(2) = 33 mod32 = 1 -> А
        self.assertEqual(self.cipher.add_symbols('Я', 'Б'), 'А')
        
        # Щ(26) + Г(4) = 30 -> Ю
        self.assertEqual(self.cipher.add_symbols('Щ', 'Г'), 'Ю')
        
        # Проверка из файла: А + "3" не проверяем, т.к. цифр нет в алфавите
        print("✓ test_add_symbols passed")

    def test_subtract_symbols(self):
        """Проверка вычитания символов"""
        # Г(4) - В(3) = 1 -> А
        self.assertEqual(self.cipher.subtract_symbols('Г', 'В'), 'А')
        
        # А(1) - Б(2) = -1 mod32 = 31 -> Я
        self.assertEqual(self.cipher.subtract_symbols('А', 'Б'), 'Я')
        
        # А(1) - А(1) = 0 -> _
        self.assertEqual(self.cipher.subtract_symbols('А', 'А'), '_')
        
        # Щ(26) - В(3) = 23 -> Ц
        self.assertEqual(self.cipher.subtract_symbols('Щ', 'В'), 'Ц')
        print("✓ test_subtract_symbols passed")

    def test_encrypt_decrypt(self):
        """Проверка шифрования/расшифрования в бинарный код"""
        test_cases = [
            "А",
            "АБВГ",
            "ПРИВЕТ_МИР",
            "СЫЗРАНЬ",
            "ГЛАДИУС"
        ]
        for original in test_cases:
            binary = self.cipher.encrypt(original)
            decrypted = self.cipher.decrypt(binary)
            self.assertEqual(decrypted, original)
            print(f"  ✓ encrypt/decrypt for '{original}'")

    def test_encrypt_output_format(self):
        """Проверка, что encrypt возвращает строку из 0 и 1"""
        binary = self.cipher.encrypt("АБВ")
        
        # Отладочный вывод
        print(f"\n  Debug: binary = '{binary}'")
        print(f"  Debug: length = {len(binary)}")
        print(f"  Debug: unique chars = {set(binary)}")
        
        # Проверяем длину: 3 символа * 5 бит = 15
        self.assertEqual(len(binary), 15, f"Длина должна быть 15, а не {len(binary)}")
        
        # Проверяем, что все символы - '0' или '1'
        for i, c in enumerate(binary):
            self.assertIn(c, '01', f"Символ '{c}' (код {ord(c)}) на позиции {i} не является 0 или 1")
        
        print("✓ test_encrypt_output_format passed")


class TestCaesarCipher(unittest.TestCase):
    """Заготовки для шифра Цезаря (пока пропускаются)"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_caesar_symbol_encrypt(self):
        self.skipTest("Функция encrypt_caesar_symbol ещё не реализована")

    def test_caesar_symbol_decrypt(self):
        self.skipTest("Функция decrypt_caesar_symbol ещё не реализована")

    def test_caesar_text_encrypt(self):
        self.skipTest("Функция encrypt_caesar_text ещё не реализована")

    def test_caesar_text_encrypt_example_from_file(self):
        self.skipTest("Функция encrypt_caesar_text ещё не реализована")

    def test_caesar_roundtrip(self):
        self.skipTest("Функции шифрования/расшифрования не реализованы")


class TestPolyalphabeticCipher(unittest.TestCase):
    """Заготовки для полиалфавитных шифров"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_vigenere_encrypt(self):
        self.skipTest("Функция encrypt_vigenere ещё не реализована")

    def test_vigenere_decrypt(self):
        self.skipTest("Функция decrypt_vigenere ещё не реализована")


class TestSBlocks(unittest.TestCase):
    """Заготовки для S-блоков"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_s_block_4_symbols(self):
        self.skipTest("S-блоки не реализованы")

    def test_s_block_with_key(self):
        self.skipTest("S-блоки не реализованы")


if __name__ == '__main__':
    unittest.main(verbosity=2)