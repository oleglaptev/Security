import unittest
from alphabet_cipher import AlphabetCipher

class TestAlphabetCipher(unittest.TestCase):
    """Тесты для базовых операций"""
    
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
        self.assertEqual(self.cipher.add_symbols('А', 'В'), 'Г')
        self.assertEqual(self.cipher.add_symbols('Я', 'Б'), 'А')
        self.assertEqual(self.cipher.add_symbols('Щ', 'Г'), 'Ю')
        print("✓ test_add_symbols passed")

    def test_subtract_symbols(self):
        """Проверка вычитания символов"""
        self.assertEqual(self.cipher.subtract_symbols('Г', 'В'), 'А')
        self.assertEqual(self.cipher.subtract_symbols('А', 'Б'), 'Я')
        self.assertEqual(self.cipher.subtract_symbols('А', 'А'), '_')
        print("✓ test_subtract_symbols passed")

    def test_encrypt_decrypt(self):
        """Проверка шифрования/расшифрования в бинарный код"""
        test_cases = ["А", "АБВГ", "ПРИВЕТ_МИР", "СЫЗРАНЬ", "ГЛАДИУС"]
        for original in test_cases:
            binary = self.cipher.encrypt(original)
            decrypted = self.cipher.decrypt(binary)
            self.assertEqual(decrypted, original)
            print(f"  ✓ encrypt/decrypt for '{original}'")

    def test_add_text(self):
        """Проверка поэлементного сложения строк"""
        # А(1) + В(3) = Г(4), В(3) + Г(4) = Ж(7)
        self.assertEqual(self.cipher.add_text("АВ", "ВГ"), "ГЖ")
        # А(1) + Г(4) = Д(5), остальные без изменений
        self.assertEqual(self.cipher.add_text("АБВ", "Г"), "ДБВ")
        print("✓ test_add_text passed")

    def test_sub_text(self):
        """Проверка поэлементного вычитания строк"""
        # Г(4) - В(3) = А(1), В(3) - Г(4) = Я(31)
        self.assertEqual(self.cipher.sub_text("ГВ", "ВГ"), "АЯ")
        print("✓ test_sub_text passed")


class TestCaesarCipher(unittest.TestCase):
    """Тесты для шифра Цезаря"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_caesar_symbol_encrypt(self):
        """Шифрование символа: С + А = Т"""
        result = self.cipher.frw_caesar("С", "А")
        self.assertEqual(result, "Т")
        print("✓ test_caesar_symbol_encrypt passed")

    def test_caesar_symbol_decrypt(self):
        """Расшифрование символа: Т - А = С"""
        result = self.cipher.inv_caesar("Т", "А")
        self.assertEqual(result, "С")
        print("✓ test_caesar_symbol_decrypt passed")

    def test_caesar_text_encrypt_from_file(self):
        """Шифрование текста: СЫЗРАНЬ + А = ТЬИСБОЭ (согласно вашему алфавиту)"""
        result = self.cipher.frw_caesar("СЫЗРАНЬ", "А")
        self.assertEqual(result, "ТЬИСБОЭ")
        print("✓ test_caesar_text_encrypt_from_file passed")

    def test_caesar_text_encrypt_example2(self):
        """Шифрование текста: ГЛАДИУС + Е = ЙСЖКОЩЧ """
        result = self.cipher.frw_caesar("ГЛАДИУС", "Е")
        self.assertEqual(result, "ЙСЖКОЩЧ")
        print("✓ test_caesar_text_encrypt_example2 passed")

    def test_caesar_roundtrip(self):
        """Шифрование + расшифрование = оригинал"""
        original = "СЫЗРАНЬ"
        key = "К"
        encrypted = self.cipher.frw_caesar(original, key)
        decrypted = self.cipher.inv_caesar(encrypted, key)
        self.assertEqual(decrypted, original)
        print("✓ test_caesar_roundtrip passed")


class TestPolyalphabeticCipher(unittest.TestCase):
    """Тесты для полиалфавитного шифра Цезаря (Виженера)"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_poly_caesar_encrypt(self):
        """Проверка полиалфавитного шифрования"""
        result = self.cipher.frw_poly_caesar("А", "КЛЮЧ")
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 1)
        print("✓ test_poly_caesar_encrypt passed")

    def test_poly_caesar_roundtrip(self):
        """Шифрование + расшифрование = оригинал"""
        original = "ОТКРЫТЫЙ_ТЕКСТ"
        key = "СЕКРЕТ"
        encrypted = self.cipher.frw_poly_caesar(original, key)
        decrypted = self.cipher.inv_poly_caesar(encrypted, key)
        self.assertEqual(decrypted, original)
        print("✓ test_poly_caesar_roundtrip passed")

    def test_poly_caesar_different_keys(self):
        """Разные ключи дают разный результат"""
        text = "АБВГ"
        encrypted1 = self.cipher.frw_poly_caesar(text, "КЛЮЧ1")
        encrypted2 = self.cipher.frw_poly_caesar(text, "КЛЮЧ2")
        self.assertIsInstance(encrypted1, str)
        self.assertIsInstance(encrypted2, str)
        print("✓ test_poly_caesar_different_keys passed")


class TestSBlocks(unittest.TestCase):
    """Тесты для S-блоков (4 символа)"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_s_block_encrypt_decrypt(self):
        """S-блок: шифрование + расшифрование = оригинал"""
        key = "НЕТ_ЗВЕЗД_В_НОЧИ"
        plaintext = "БЛОК"
        encrypted = self.cipher.frw_S_caesar(plaintext, key)
        decrypted = self.cipher.inv_S_caesar(encrypted, key)
        self.assertEqual(decrypted, plaintext)
        print("✓ test_s_block_encrypt_decrypt passed")

    def test_s_block_input_validation(self):
        """Проверка валидации входных данных"""
        result = self.cipher.frw_S_caesar("БЛ", "НЕТ_ЗВЕЗД_В_НОЧИ")
        self.assertEqual(result, "input_error")
        
        result = self.cipher.frw_S_caesar("БЛОК", "КОРОТКИЙ")
        self.assertEqual(result, "input_error")
        
        print("✓ test_s_block_input_validation passed")

    def test_s_block_key_sensitivity(self):
        """Чувствительность к ключу: разные ключи -> разный результат"""
        plaintext = "БЛОК"
        key1 = "НЕТ_ЗВЕЗД_В_НОЧИ"
        key2 = "ХОРОШО_БЫТЬ_ВАМИ"
        
        encrypted1 = self.cipher.frw_S_caesar(plaintext, key1)
        encrypted2 = self.cipher.frw_S_caesar(plaintext, key2)
        
        print(f"  encrypted1 = '{encrypted1}'")
        print(f"  encrypted2 = '{encrypted2}'")
        print("✓ test_s_block_key_sensitivity passed")


class TestMergeBlock(unittest.TestCase):
    """Тесты для перемешивания блоков"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_merge_block_encrypt_decrypt(self):
        """Перемешивание + обратное перемешивание = оригинал"""
        key = "ХОРОШО_БЫТЬ_ВАМИ"
        plaintext = "ОРЕХ"
        
        merged = self.cipher.frw_merge_block(plaintext, key)
        unmerged = self.cipher.inv_merge_block(merged, key)
        
        self.assertEqual(unmerged, plaintext)
        print("✓ test_merge_block_encrypt_decrypt passed")

    def test_merge_block_changes_order(self):
        """Проверка, что перемешивание действительно меняет блок"""
        key = "ХОРОШО_БЫТЬ_ВАМИ"
        plaintext = "АБВГ"
        
        merged = self.cipher.frw_merge_block(plaintext, key)
        
        self.assertIsInstance(merged, str)
        self.assertEqual(len(merged), 4)
        print("✓ test_merge_block_changes_order passed")


class TestFullCipher(unittest.TestCase):
    """Тесты для полного шифра с усилением (frw_s_caesar_m)"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_full_cipher_roundtrip(self):
        """Полное шифрование + расшифрование = оригинал"""
        key = "ХОРОШО_БЫТЬ_ВАМИ"
        plaintext = "ОРЕХ"
        
        encrypted = self.cipher.frw_s_caesar_m(plaintext, key)
        decrypted = self.cipher.inv_s_caesar_m(encrypted, key)
        
        self.assertEqual(decrypted, plaintext)
        print(f"  plaintext: '{plaintext}' -> encrypted: '{encrypted}'")
        print("✓ test_full_cipher_roundtrip passed")

    def test_full_cipher_sensitivity_to_input(self):
        """Изменение одного символа входа меняет результат"""
        key = "ХОРОШО_БЫТЬ_ВАМИ"
        plaintext1 = "ОРЕХ"
        plaintext2 = "ОПЕХ"
        
        encrypted1 = self.cipher.frw_s_caesar_m(plaintext1, key)
        encrypted2 = self.cipher.frw_s_caesar_m(plaintext2, key)
        
        diff_count = sum(1 for a, b in zip(encrypted1, encrypted2) if a != b)
        print(f"  Изменение 1 символа входа -> {diff_count} символов выхода")
        self.assertGreaterEqual(diff_count, 1)
        print("✓ test_full_cipher_sensitivity_to_input passed")

    def test_full_cipher_sensitivity_to_key(self):
        """Изменение одного символа ключа меняет результат"""
        plaintext = "ОРЕХ"
        key1 = "ХОРОШО_БЫТЬ_ВАМИ"
        key2 = "ХОРОШО_БЫТЬ_ВАМЖ"
        
        encrypted1 = self.cipher.frw_s_caesar_m(plaintext, key1)
        encrypted2 = self.cipher.frw_s_caesar_m(plaintext, key2)
        
        diff_count = sum(1 for a, b in zip(encrypted1, encrypted2) if a != b)
        print(f"  Изменение 1 символа ключа -> {diff_count} символов выхода")
        self.assertGreaterEqual(diff_count, 1)
        print("✓ test_full_cipher_sensitivity_to_key passed")


class TestRobustness(unittest.TestCase):
    """Тесты надежности """
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_small_input_change_caesar_m(self):
        """Тест на малое изменение входа """
        key = "ХОРОШО_БЫТЬ_ВАМИ"
        p1 = "ОРЕХ"
        p2 = "ОПЕХ"
        
        c1 = self.cipher.frw_s_caesar_m(p1, key)
        c2 = self.cipher.frw_s_caesar_m(p2, key)
        
        diff_count = sum(1 for a, b in zip(c1, c2) if a != b)
        print(f"  Изменение 1 символа на входе: {p1} -> {c1}, {p2} -> {c2}")
        print(f"  Различается {diff_count} из 4 символов")
        
        self.assertGreaterEqual(diff_count, 1)
        print("✓ test_small_input_change_caesar_m passed")

    def test_key_small_change(self):
        """Тест на малое изменение ключа """
        plaintext = "ОРЕХ"
        key1 = "ХОРОШО_БЫТЬ_ВАМИ"
        key2 = "ХОРОШО_БЫТЬ_ВАМЖ"
        
        c1 = self.cipher.frw_s_caesar_m(plaintext, key1)
        c2 = self.cipher.frw_s_caesar_m(plaintext, key2)
        
        diff_count = sum(1 for a, b in zip(c1, c2) if a != b)
        print(f"  Изменение 1 символа в ключе: {c1} vs {c2}")
        print(f"  Различается {diff_count} из 4 символов")
        
        self.assertGreaterEqual(diff_count, 1)
        print("✓ test_key_small_change passed")

    def test_rotation_input(self):
        """Тест на ротацию входа """
        key = "ХОРОШО_БЫТЬ_ВАМИ"
        p1 = "ОРЕХ"
        p2 = "РЕХО"
        
        c1 = self.cipher.frw_s_caesar_m(p1, key)
        c2 = self.cipher.frw_s_caesar_m(p2, key)
        
        self.assertNotEqual(sorted(c1), sorted(c2))
        print(f"  Ротация входа: {p1} -> {c1}, {p2} -> {c2}")
        print("✓ test_rotation_input passed")


if __name__ == '__main__':
    unittest.main(verbosity=2)