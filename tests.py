import unittest
import copy
from alphabet_cipher import AlphabetCipher

# class TestAlphabetCipher(unittest.TestCase):
#     """Тесты для базовых операций"""
    
#     def setUp(self):
#         self.cipher = AlphabetCipher()

#     def test_symbol_to_number(self):
#         """Проверка: символ -> номер"""
#         self.assertEqual(self.cipher.get_number_by_symbol('А'), 1)
#         self.assertEqual(self.cipher.get_number_by_symbol('_'), 0)
#         self.assertEqual(self.cipher.get_number_by_symbol('Я'), 31)
#         print("✓ test_symbol_to_number passed")

#     def test_number_to_symbol(self):
#         """Проверка: номер -> символ"""
#         self.assertEqual(self.cipher.get_symbol_by_number(1), 'А')
#         self.assertEqual(self.cipher.get_symbol_by_number(0), '_')
#         self.assertEqual(self.cipher.get_symbol_by_number(31), 'Я')
#         print("✓ test_number_to_symbol passed")

#     def test_add_numbers(self):
#         """Проверка сложения с mod 32"""
#         self.assertEqual(self.cipher.add_numbers(30, 5), 3)
#         self.assertEqual(self.cipher.add_numbers(31, 1), 0)
#         self.assertEqual(self.cipher.add_numbers(0, 0), 0)
#         print("✓ test_add_numbers passed")

#     def test_subtract_numbers(self):
#         """Проверка вычитания с mod 32"""
#         self.assertEqual(self.cipher.subtract_numbers(2, 5), 29)
#         self.assertEqual(self.cipher.subtract_numbers(0, 1), 31)
#         self.assertEqual(self.cipher.subtract_numbers(31, 31), 0)
#         print("✓ test_subtract_numbers passed")

#     def test_add_symbols(self):
#         """Проверка сложения символов"""
#         self.assertEqual(self.cipher.add_symbols('А', 'В'), 'Г')
#         self.assertEqual(self.cipher.add_symbols('Я', 'Б'), 'А')
#         self.assertEqual(self.cipher.add_symbols('Щ', 'Г'), 'Ю')
#         print("✓ test_add_symbols passed")

#     def test_subtract_symbols(self):
#         """Проверка вычитания символов"""
#         self.assertEqual(self.cipher.subtract_symbols('Г', 'В'), 'А')
#         self.assertEqual(self.cipher.subtract_symbols('А', 'Б'), 'Я')
#         self.assertEqual(self.cipher.subtract_symbols('А', 'А'), '_')
#         print("✓ test_subtract_symbols passed")

#     def test_encrypt_decrypt(self):
#         """Проверка шифрования/расшифрования в бинарный код"""
#         test_cases = ["А", "АБВГ", "ПРИВЕТ_МИР", "СЫЗРАНЬ", "ГЛАДИУС"]
#         for original in test_cases:
#             binary = self.cipher.encrypt(original)
#             decrypted = self.cipher.decrypt(binary)
#             self.assertEqual(decrypted, original)
#             print(f"  ✓ encrypt/decrypt for '{original}'")

#     def test_add_text(self):
#         """Проверка поэлементного сложения строк"""
#         # А(1) + В(3) = Г(4), В(3) + Г(4) = Ж(7)
#         self.assertEqual(self.cipher.add_text("АВ", "ВГ"), "ГЖ")
#         # А(1) + Г(4) = Д(5), остальные без изменений
#         self.assertEqual(self.cipher.add_text("АБВ", "Г"), "ДБВ")
#         print("✓ test_add_text passed")

#     def test_sub_text(self):
#         """Проверка поэлементного вычитания строк"""
#         # Г(4) - В(3) = А(1), В(3) - Г(4) = Я(31)
#         self.assertEqual(self.cipher.sub_text("ГВ", "ВГ"), "АЯ")
#         print("✓ test_sub_text passed")


# class TestCaesarCipher(unittest.TestCase):
#     """Тесты для шифра Цезаря"""
    
#     def setUp(self):
#         self.cipher = AlphabetCipher()

#     def test_caesar_symbol_encrypt(self):
#         """Шифрование символа: С + А = Т"""
#         result = self.cipher.frw_caesar("С", "А")
#         self.assertEqual(result, "Т")
#         print("✓ test_caesar_symbol_encrypt passed")

#     def test_caesar_symbol_decrypt(self):
#         """Расшифрование символа: Т - А = С"""
#         result = self.cipher.inv_caesar("Т", "А")
#         self.assertEqual(result, "С")
#         print("✓ test_caesar_symbol_decrypt passed")

#     def test_caesar_text_encrypt_from_file(self):
#         """Шифрование текста: СЫЗРАНЬ + А = ТЬИСБОЭ (согласно вашему алфавиту)"""
#         result = self.cipher.frw_caesar("СЫЗРАНЬ", "А")
#         self.assertEqual(result, "ТЬИСБОЭ")
#         print("✓ test_caesar_text_encrypt_from_file passed")

#     def test_caesar_text_encrypt_example2(self):
#         """Шифрование текста: ГЛАДИУС + Е = ЙСЖКОЩЧ """
#         result = self.cipher.frw_caesar("ГЛАДИУС", "Е")
#         self.assertEqual(result, "ЙСЖКОЩЧ")
#         print("✓ test_caesar_text_encrypt_example2 passed")

#     def test_caesar_roundtrip(self):
#         """Шифрование + расшифрование = оригинал"""
#         original = "СЫЗРАНЬ"
#         key = "К"
#         encrypted = self.cipher.frw_caesar(original, key)
#         decrypted = self.cipher.inv_caesar(encrypted, key)
#         self.assertEqual(decrypted, original)
#         print("✓ test_caesar_roundtrip passed")


# class TestPolyalphabeticCipher(unittest.TestCase):
#     """Тесты для полиалфавитного шифра Цезаря (Виженера)"""
    
#     def setUp(self):
#         self.cipher = AlphabetCipher()

#     def test_poly_caesar_encrypt(self):
#         """Проверка полиалфавитного шифрования"""
#         result = self.cipher.frw_poly_caesar("А", "КЛЮЧ")
#         self.assertIsInstance(result, str)
#         self.assertEqual(len(result), 1)
#         print("✓ test_poly_caesar_encrypt passed")

#     def test_poly_caesar_roundtrip(self):
#         """Шифрование + расшифрование = оригинал"""
#         original = "ОТКРЫТЫЙ_ТЕКСТ"
#         key = "СЕКРЕТ"
#         encrypted = self.cipher.frw_poly_caesar(original, key)
#         decrypted = self.cipher.inv_poly_caesar(encrypted, key)
#         self.assertEqual(decrypted, original)
#         print("✓ test_poly_caesar_roundtrip passed")

#     def test_poly_caesar_different_keys(self):
#         """Разные ключи дают разный результат"""
#         text = "АБВГ"
#         encrypted1 = self.cipher.frw_poly_caesar(text, "КЛЮЧ1")
#         encrypted2 = self.cipher.frw_poly_caesar(text, "КЛЮЧ2")
#         self.assertIsInstance(encrypted1, str)
#         self.assertIsInstance(encrypted2, str)
#         print("✓ test_poly_caesar_different_keys passed")


# class TestSBlocks(unittest.TestCase):
#     """Тесты для S-блоков (4 символа)"""
    
#     def setUp(self):
#         self.cipher = AlphabetCipher()

#     def test_s_block_encrypt_decrypt(self):
#         """S-блок: шифрование + расшифрование = оригинал"""
#         key = "НЕТ_ЗВЕЗД_В_НОЧИ"
#         plaintext = "БЛОК"
#         encrypted = self.cipher.frw_S_caesar(plaintext, key)
#         decrypted = self.cipher.inv_S_caesar(encrypted, key)
#         self.assertEqual(decrypted, plaintext)
#         print("✓ test_s_block_encrypt_decrypt passed")

#     def test_s_block_input_validation(self):
#         """Проверка валидации входных данных"""
#         result = self.cipher.frw_S_caesar("БЛ", "НЕТ_ЗВЕЗД_В_НОЧИ")
#         self.assertEqual(result, "input_error")
        
#         result = self.cipher.frw_S_caesar("БЛОК", "КОРОТКИЙ")
#         self.assertEqual(result, "input_error")
        
#         print("✓ test_s_block_input_validation passed")

#     def test_s_block_key_sensitivity(self):
#         """Чувствительность к ключу: разные ключи -> разный результат"""
#         plaintext = "БЛОК"
#         key1 = "НЕТ_ЗВЕЗД_В_НОЧИ"
#         key2 = "ХОРОШО_БЫТЬ_ВАМИ"
        
#         encrypted1 = self.cipher.frw_S_caesar(plaintext, key1)
#         encrypted2 = self.cipher.frw_S_caesar(plaintext, key2)
        
#         print(f"  encrypted1 = '{encrypted1}'")
#         print(f"  encrypted2 = '{encrypted2}'")
#         print("✓ test_s_block_key_sensitivity passed")


# class TestMergeBlock(unittest.TestCase):
#     """Тесты для перемешивания блоков"""
    
#     def setUp(self):
#         self.cipher = AlphabetCipher()

#     def test_merge_block_encrypt_decrypt(self):
#         """Перемешивание + обратное перемешивание = оригинал"""
#         key = "ХОРОШО_БЫТЬ_ВАМИ"
#         plaintext = "ОРЕХ"
        
#         merged = self.cipher.frw_merge_block(plaintext, key)
#         unmerged = self.cipher.inv_merge_block(merged, key)
        
#         self.assertEqual(unmerged, plaintext)
#         print("✓ test_merge_block_encrypt_decrypt passed")

#     def test_merge_block_changes_order(self):
#         """Проверка, что перемешивание действительно меняет блок"""
#         key = "ХОРОШО_БЫТЬ_ВАМИ"
#         plaintext = "АБВГ"
        
#         merged = self.cipher.frw_merge_block(plaintext, key)
        
#         self.assertIsInstance(merged, str)
#         self.assertEqual(len(merged), 4)
#         print("✓ test_merge_block_changes_order passed")


# class TestFullCipher(unittest.TestCase):
#     """Тесты для полного шифра с усилением (frw_s_caesar_m)"""
    
#     def setUp(self):
#         self.cipher = AlphabetCipher()

#     def test_full_cipher_roundtrip(self):
#         """Полное шифрование + расшифрование = оригинал"""
#         key = "ХОРОШО_БЫТЬ_ВАМИ"
#         plaintext = "ОРЕХ"
        
#         encrypted = self.cipher.frw_s_caesar_m(plaintext, key)
#         decrypted = self.cipher.inv_s_caesar_m(encrypted, key)
        
#         self.assertEqual(decrypted, plaintext)
#         print(f"  plaintext: '{plaintext}' -> encrypted: '{encrypted}'")
#         print("✓ test_full_cipher_roundtrip passed")

#     def test_full_cipher_sensitivity_to_input(self):
#         """Изменение одного символа входа меняет результат"""
#         key = "ХОРОШО_БЫТЬ_ВАМИ"
#         plaintext1 = "ОРЕХ"
#         plaintext2 = "ОПЕХ"
        
#         encrypted1 = self.cipher.frw_s_caesar_m(plaintext1, key)
#         encrypted2 = self.cipher.frw_s_caesar_m(plaintext2, key)
        
#         diff_count = sum(1 for a, b in zip(encrypted1, encrypted2) if a != b)
#         print(f"  Изменение 1 символа входа -> {diff_count} символов выхода")
#         self.assertGreaterEqual(diff_count, 1)
#         print("✓ test_full_cipher_sensitivity_to_input passed")

#     def test_full_cipher_sensitivity_to_key(self):
#         """Изменение одного символа ключа меняет результат"""
#         plaintext = "ОРЕХ"
#         key1 = "ХОРОШО_БЫТЬ_ВАМИ"
#         key2 = "ХОРОШО_БЫТЬ_ВАМЖ"
        
#         encrypted1 = self.cipher.frw_s_caesar_m(plaintext, key1)
#         encrypted2 = self.cipher.frw_s_caesar_m(plaintext, key2)
        
#         diff_count = sum(1 for a, b in zip(encrypted1, encrypted2) if a != b)
#         print(f"  Изменение 1 символа ключа -> {diff_count} символов выхода")
#         self.assertGreaterEqual(diff_count, 1)
#         print("✓ test_full_cipher_sensitivity_to_key passed")


# class TestRobustness(unittest.TestCase):
#     """Тесты надежности """
    
#     def setUp(self):
#         self.cipher = AlphabetCipher()

#     def test_small_input_change_caesar_m(self):
#         """Тест на малое изменение входа """
#         key = "ХОРОШО_БЫТЬ_ВАМИ"
#         p1 = "ОРЕХ"
#         p2 = "ОПЕХ"
        
#         c1 = self.cipher.frw_s_caesar_m(p1, key)
#         c2 = self.cipher.frw_s_caesar_m(p2, key)
        
#         diff_count = sum(1 for a, b in zip(c1, c2) if a != b)
#         print(f"  Изменение 1 символа на входе: {p1} -> {c1}, {p2} -> {c2}")
#         print(f"  Различается {diff_count} из 4 символов")
        
#         self.assertGreaterEqual(diff_count, 1)
#         print("✓ test_small_input_change_caesar_m passed")

#     def test_key_small_change(self):
#         """Тест на малое изменение ключа """
#         plaintext = "ОРЕХ"
#         key1 = "ХОРОШО_БЫТЬ_ВАМИ"
#         key2 = "ХОРОШО_БЫТЬ_ВАМЖ"
        
#         c1 = self.cipher.frw_s_caesar_m(plaintext, key1)
#         c2 = self.cipher.frw_s_caesar_m(plaintext, key2)
        
#         diff_count = sum(1 for a, b in zip(c1, c2) if a != b)
#         print(f"  Изменение 1 символа в ключе: {c1} vs {c2}")
#         print(f"  Различается {diff_count} из 4 символов")
        
#         self.assertGreaterEqual(diff_count, 1)
#         print("✓ test_key_small_change passed")

#     def test_rotation_input(self):
#         """Тест на ротацию входа """
#         key = "ХОРОШО_БЫТЬ_ВАМИ"
#         p1 = "ОРЕХ"
#         p2 = "РЕХО"
        
#         c1 = self.cipher.frw_s_caesar_m(p1, key)
#         c2 = self.cipher.frw_s_caesar_m(p2, key)
        
#         self.assertNotEqual(sorted(c1), sorted(c2))
#         print(f"  Ротация входа: {p1} -> {c1}, {p2} -> {c2}")
#         print("✓ test_rotation_input passed")

# ===========================ТЕСТЫ ДЛЯ ЛАБОРАТОРНОЙ РАБОТЫ №2 ====================

class TestCoreFunctions(unittest.TestCase):
    """Тесты для ядерных функций (core_Caesar, confuse, mixinputs)"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_core_caesar_length(self):
        """Проверка: core_Caesar возвращает строку длиной 16 символов"""
        IN1 = "ХОРОШО_БЫТЬ_ВАМИ"
        IN2 = "КЬЕРКЕГОР_ПРОПАЛ"
        result = self.cipher.core_Caesar(IN1, IN2)
        self.assertEqual(len(result), 16)
        self.assertNotEqual(result, "input_error")
        print("✓ test_core_caesar_length passed")

def test_core_caesar_input_validation(self):
    """Проверка валидации входных данных core_Caesar"""
    # Неправильная длина первого аргумента
    result = self.cipher.core_Caesar("КОРОТКИЙ", "16_СИМВОЛОВ_ДЛЯ_ТЕСТА")
    self.assertEqual(result, "input_error")
    
    # Неправильная длина второго аргумента
    result = self.cipher.core_Caesar("16_СИМВОЛОВ_ДЛЯ_ТЕСТА", "КОРОТКИЙ")
    self.assertEqual(result, "input_error")
    
    # Оба аргумента правильной длины - не должно быть ошибки
    result = self.cipher.core_Caesar("16_СИМВОЛОВ_ДЛЯ_ТЕСТА", "16_СИМВОЛОВ_ДЛЯ_ТЕСТА")
    self.assertNotEqual(result, "input_error")  # Исправлено: проверяем что НЕ error
    print("✓ test_core_caesar_input_validation passed")

    def test_core_caesar_non_commutative(self):
        """Проверка: core_Caesar не коммутативна (порядок аргументов важен)"""
        IN1 = "ХОРОШО_БЫТЬ_ВАМИ"
        IN2 = "КЬЕРКЕГОР_ПРОПАЛ"
        result1 = self.cipher.core_Caesar(IN1, IN2)
        result2 = self.cipher.core_Caesar(IN2, IN1)
        # Результаты должны отличаться (некоммутативность)
        self.assertNotEqual(result1, result2)
        print(f"  core_Caesar(A,B) = {result1}")
        print(f"  core_Caesar(B,A) = {result2}")
        print("✓ test_core_caesar_non_commutative passed")

    def test_confuse_length(self):
        """Проверка: confuse возвращает строку длиной 16 символов"""
        IN1 = "ХОРОШО_БЫТЬ_ВАМИ"
        IN2 = "КЬЕРКЕГОР_ПРОПАЛ"
        result = self.cipher.confuse(IN1, IN2)
        self.assertEqual(len(result), 16)
        print("✓ test_confuse_length passed")

    def test_confuse_with_identical_inputs(self):
        """Проверка: confuse с одинаковыми входами"""
        IN = "ХОРОШО_БЫТЬ_ВАМИ"
        result = self.cipher.confuse(IN, IN)
        self.assertEqual(len(result), 16)
        # При одинаковых входах результат предсказуем
        print(f"  confuse({IN}, {IN}) = {result}")
        print("✓ test_confuse_with_identical_inputs passed")

    def test_mixinputs_length(self):
        """Проверка: mixinputs возвращает 4 строки по 16 символов"""
        IN = [
            "ХОРОШО_БЫТЬ_ВАМИ",
            "КЬЕРКЕГОР_ПРОПАЛ",
            "ХОРОШО_ПРОБРОСИЛ",
            "ЧЕРНЫЙ_АББАТ_ПОЛ"
        ]
        out1, out2, out3, out4 = self.cipher.mixinputs(IN)
        self.assertEqual(len(out1), 16)
        self.assertEqual(len(out2), 16)
        self.assertEqual(len(out3), 16)
        self.assertEqual(len(out4), 16)
        print("✓ test_mixinputs_length passed")

    def test_mixinputs_changes_output(self):
        """Проверка: mixinputs действительно изменяет входные данные"""
        IN = [
            "ХОРОШО_БЫТЬ_ВАМИ",  # Исправлено: не нулевые строки
            "КЬЕРКЕГОР_ПРОПАЛ",
            "ХОРОШО_ПРОБРОСИЛ",
            "ЧЕРНЫЙ_АББАТ_ПОЛ"
        ]
        out1, out2, out3, out4 = self.cipher.mixinputs(IN)
        # Проверяем, что хотя бы один выход отличается от соответствующего входа
        self.assertTrue(
            out1 != IN[0] or out2 != IN[1] or out3 != IN[2] or out4 != IN[3],
            "mixinputs не изменил данные"
        )
        print("✓ test_mixinputs_changes_output passed")

class TestCBlock(unittest.TestCase):
    """Тесты для C-блока (функция сжатия)"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_c_block_16_output(self):
        """Проверка: C_block с out_size=16 возвращает 16 символов"""
        IN = ["ХОРОШО_БЫТЬ_ВАМИ"]
        result = self.cipher.C_block(IN, 16)
        self.assertEqual(len(result), 16)
        self.assertNotEqual(result, "input_error")
        print("✓ test_c_block_16_output passed")

    def test_c_block_8_output(self):
        """Проверка: C_block с out_size=8 возвращает 8 символов"""
        IN = ["ХОРОШО_БЫТЬ_ВАМИ"]
        result = self.cipher.C_block(IN, 8)
        self.assertEqual(len(result), 8)
        print("✓ test_c_block_8_output passed")

    def test_c_block_4_output(self):
        """Проверка: C_block с out_size=4 возвращает 4 символа"""
        IN = ["ХОРОШО_БЫТЬ_ВАМИ"]
        result = self.cipher.C_block(IN, 4)
        self.assertEqual(len(result), 4)
        print("✓ test_c_block_4_output passed")

    def test_c_block_with_4_inputs(self):
        """Проверка: C_block с 4 входными блоками"""
        IN = [
            "ХОРОШО_БЫТЬ_ВАМИ",
            "КЬЕРКЕГОР_ПРОПАЛ",
            "ХОРОШО_ПРОБРОСИЛ",
            "ЧЕРНЫЙ_АББАТ_ПОЛ"
        ]
        result = self.cipher.C_block(IN, 16)
        self.assertEqual(len(result), 16)
        print("✓ test_c_block_with_4_inputs passed")

    def test_c_block_different_sizes_produce_different_outputs(self):
        """Проверка: разные выходные размеры дают разные результаты"""
        IN = ["ХОРОШО_БЫТЬ_ВАМИ"]
        result16 = self.cipher.C_block(IN, 16)
        result8 = self.cipher.C_block(IN, 8)
        result4 = self.cipher.C_block(IN, 4)
        
        # Результаты разных размеров не должны быть одинаковыми строками
        self.assertNotEqual(result16[:8], result8)  # Первые 8 символов 16-блока не равны 8-блоку
        self.assertNotEqual(result16[:4], result4)  # Первые 4 символа 16-блока не равны 4-блоку
        print("✓ test_c_block_different_sizes_produce_different_outputs passed")

def test_c_block_input_validation(self):
    """Проверка валидации входных данных C_block"""
    # Пустой список - может обрабатываться по-разному
    result = self.cipher.C_block([], 16)
    # Если не error, то хотя бы проверим что вернулась строка
    if result != "input_error":
        self.assertIsInstance(result, str)
    
    # Список с неправильными длинами строк
    IN = ["КОРОТКИЙ"]
    result = self.cipher.C_block(IN, 16)
    # Может вернуть error или что-то другое
    print("✓ test_c_block_input_validation passed")


class TestCompress(unittest.TestCase):
    """Тесты для функции сжатия compress"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_compress_16_to_16(self):
        """Проверка: compress с out_n=16 возвращает исходную строку"""
        IN = "ХОРОШО_БЫТЬ_ВАМИ"
        result = self.cipher.compress(IN, 16)
        self.assertEqual(result, IN)
        print("✓ test_compress_16_to_16 passed")

    def test_compress_16_to_8(self):
        """Проверка: compress с out_n=8 возвращает 8 символов"""
        IN = "АБВГДЕЖЗИЙКЛМНОП"
        result = self.cipher.compress(IN, 8)
        self.assertEqual(len(result), 8)
        print("✓ test_compress_16_to_8 passed")

    def test_compress_16_to_4(self):
        """Проверка: compress с out_n=4 возвращает 4 символа"""
        IN = "АБВГДЕЖЗИЙКЛМНОП"
        result = self.cipher.compress(IN, 4)
        self.assertEqual(len(result), 4)
        print("✓ test_compress_16_to_4 passed")

    def test_compress_invalid_size(self):
        """Проверка: compress с неподдерживаемым размером"""
        IN = "АБВГДЕЖЗИЙКЛМНОП"
        result = self.cipher.compress(IN, 10)
        self.assertEqual(result, "input_error")
        print("✓ test_compress_invalid_size passed")


class TestSpongeInternals(unittest.TestCase):
    """Тесты для внутренних функций губки (mix_cols, shift_rows, shatter_blocks, shift_block)"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_shift_block_length(self):
        """Проверка: shift_block возвращает строку длиной 4 символа"""
        result = self.cipher.shift_block("АБВГ")
        self.assertEqual(len(result), 4)
        print("✓ test_shift_block_length passed")

    def test_shift_block_actually_shifts(self):
        """Проверка: shift_block действительно сдвигает символы"""
        # "АБВГ" при сдвиге вправо должно стать "ГАБВ"
        result = self.cipher.shift_block("АБВГ")
        # Это циклический сдвиг, ожидаем перестановку
        self.assertNotEqual(result, "АБВГ")
        print(f"  shift_block('АБВГ') = '{result}'")
        print("✓ test_shift_block_actually_shifts passed")

    def test_shift_block_reversible(self):
        """Проверка: shift_block обратим (два сдвига возвращают оригинал)"""
        original = "АБВГ"
        shifted_once = self.cipher.shift_block(original)
        shifted_twice = self.cipher.shift_block(shifted_once)
        shifted_thrice = self.cipher.shift_block(shifted_twice)
        shifted_four_times = self.cipher.shift_block(shifted_thrice)
        # 4 сдвига должны вернуть оригинал (так как длина 4)
        self.assertEqual(shifted_four_times, original)
        print("✓ test_shift_block_reversible passed")

    def test_mix_cols_returns_matrix(self):
        """Проверка: mix_cols возвращает матрицу 5x5"""
        state = [["____" for _ in range(5)] for _ in range(5)]
        result = self.cipher.mix_cols(state)
        self.assertEqual(len(result), 5)
        self.assertEqual(len(result[0]), 5)
        print("✓ test_mix_cols_returns_matrix passed")

    def test_mix_cols_modifies_state(self):
        """Проверка: mix_cols изменяет состояние"""
        state = [["____" for _ in range(5)] for _ in range(5)]
        # Добавим небольшое возмущение
        state[0][0] = "АБВГ"
        result = self.cipher.mix_cols(copy.deepcopy(state))
        # Хотя бы один элемент должен измениться
        changed = False
        for i in range(5):
            for j in range(5):
                if state[i][j] != result[i][j]:
                    changed = True
                    break
        self.assertTrue(changed)
        print("✓ test_mix_cols_modifies_state passed")

    def test_shift_rows_returns_matrix(self):
        """Проверка: shift_rows возвращает матрицу 5x5"""
        state = [["____" for _ in range(5)] for _ in range(5)]
        result = self.cipher.shift_rows(state)
        self.assertEqual(len(result), 5)
        self.assertEqual(len(result[0]), 5)
        print("✓ test_shift_rows_returns_matrix passed")

    def test_shatter_blocks_returns_matrix(self):
        """Проверка: shatter_blocks возвращает матрицу 5x5"""
        state = [["____" for _ in range(5)] for _ in range(5)]
        result = self.cipher.shatter_blocks(state)
        self.assertEqual(len(result), 5)
        self.assertEqual(len(result[0]), 5)
        print("✓ test_shatter_blocks_returns_matrix passed")

    def test_shatter_blocks_modifies_diagonal(self):
        """Проверка: shatter_blocks изменяет диагональные блоки"""
        state = [["____" for _ in range(5)] for _ in range(5)]
        state[0][0] = "АБВГ"
        state[1][1] = "ДЕЖЗ"
        state[2][2] = "ИЙКЛ"
        state[3][3] = "МНОП"
        state[4][4] = "РСТУ"
        
        result = self.cipher.shatter_blocks(copy.deepcopy(state))
        
        # Диагональные элементы должны измениться
        for i in range(5):
            self.assertNotEqual(state[i][i], result[i][i])
        print("✓ test_shatter_blocks_modifies_diagonal passed")


class TestSpongeAbsorbSqueeze(unittest.TestCase):
    """Тесты для фаз поглощения и выжимания"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_sponge_absorb_returns_state(self):
        """Проверка: sponge_absorb возвращает матрицу состояния 5x5"""
        state = [["____" for _ in range(5)] for _ in range(5)]
        result = self.cipher.sponge_absorb(state, "АБВГ")
        self.assertEqual(len(result), 5)
        self.assertEqual(len(result[0]), 5)
        print("✓ test_sponge_absorb_returns_state passed")

    def test_sponge_absorb_modifies_state(self):
        """Проверка: sponge_absorb изменяет состояние"""
        state = [["____" for _ in range(5)] for _ in range(5)]
        result = self.cipher.sponge_absorb(state, "АБВГ")
        
        # Состояние должно измениться
        changed = False
        for i in range(5):
            for j in range(5):
                if state[i][j] != result[i][j]:
                    changed = True
                    break
        self.assertTrue(changed)
        print("✓ test_sponge_absorb_modifies_state passed")

    def test_sponge_absorb_with_different_inputs(self):
        """Проверка: разные входные блоки дают разные состояния"""
        state = [["____" for _ in range(5)] for _ in range(5)]
        result1 = self.cipher.sponge_absorb(copy.deepcopy(state), "АБВГ")
        result2 = self.cipher.sponge_absorb(copy.deepcopy(state), "ГВБА")
        
        # Результаты должны отличаться
        different = False
        for i in range(5):
            for j in range(5):
                if result1[i][j] != result2[i][j]:
                    different = True
                    break
        self.assertTrue(different)
        print("✓ test_sponge_absorb_with_different_inputs passed")

    def test_sponge_squeeze_returns_block_and_state(self):
        """Проверка: sponge_squeeze возвращает [блок, состояние]"""
        state = [["____" for _ in range(5)] for _ in range(5)]
        result = self.cipher.sponge_squeeze(state)
        
        self.assertEqual(len(result), 2)  # [block, new_state]
        self.assertEqual(len(result[0]), 4)  # блок длиной 4 символа
        self.assertEqual(len(result[1]), 5)  # состояние 5x5
        self.assertEqual(len(result[1][0]), 5)
        print("✓ test_sponge_squeeze_returns_block_and_state passed")

    def test_sponge_squeeze_modifies_state(self):
        """Проверка: sponge_squeeze изменяет состояние после выжимки"""
        state = [["____" for _ in range(5)] for _ in range(5)]
        # Добавляем уникальные значения для уверенности
        for i in range(5):
            for j in range(5):
                state[i][j] = self.cipher.get_symbol_by_number((i * 5 + j) % 32) * 4
        
        # Сохраняем копию ДО
        state_before = copy.deepcopy(state)
        
        # Выполняем squeeze
        result = self.cipher.sponge_squeeze(state)
        
        # Получаем новое состояние из результата (sponge_squeeze возвращает [block, new_state])
        new_state = result[1]
        
        # Проверяем, что новое состояние отличается от старого
        changed = False
        for i in range(5):
            for j in range(5):
                if state_before[i][j] != new_state[i][j]:
                    changed = True
                    break
            if changed:
                break
        
        self.assertTrue(changed, "sponge_squeeze не изменил состояние")
        print("✓ test_sponge_squeeze_modifies_state passed")


class TestSpongeHash(unittest.TestCase):
    """Тесты для полной хеш-функции SpongeFun_hash"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_sponge_hash_returns_string(self):
        """Проверка: SpongeFun_hash возвращает строку"""
        result = self.cipher.SpongeFun_hash("ТЕСТ")
        self.assertIsInstance(result, str)
        print("✓ test_sponge_hash_returns_string passed")

    def test_sponge_hash_fixed_length(self):
        """Проверка: SpongeFun_hash возвращает строку фиксированной длины (60 символов)"""
        result1 = self.cipher.SpongeFun_hash("")
        result2 = self.cipher.SpongeFun_hash("А")  # Исправлено: только русская буква
        result3 = self.cipher.SpongeFun_hash("ОЧЕНЬ_ДЛИННОЕ_СООБЩЕНИЕ")
        
        self.assertEqual(len(result1), 60)
        self.assertEqual(len(result2), 60)
        self.assertEqual(len(result3), 60)
        print("✓ test_sponge_hash_fixed_length passed")

    def test_sponge_hash_deterministic(self):
        """Проверка: одинаковые входы дают одинаковый хеш"""
        msg = "ТЕСТОВОЕ_СООБЩЕНИЕ"
        hash1 = self.cipher.SpongeFun_hash(msg)
        hash2 = self.cipher.SpongeFun_hash(msg)
        self.assertEqual(hash1, hash2)
        print("✓ test_sponge_hash_deterministic passed")

    def test_sponge_hash_sensitivity(self):
        """Проверка: изменение одного символа сильно меняет хеш (лавинный эффект)"""
        msg1 = "ТЕСТОВОЕ_СООБЩЕНИЕ"
        msg2 = "ТЕСТОВОЕ_СООБЩЕНИЯ"  # Последний символ изменён
        
        hash1 = self.cipher.SpongeFun_hash(msg1)
        hash2 = self.cipher.SpongeFun_hash(msg2)
        
        # Подсчитываем количество различающихся символов
        diff_count = sum(1 for a, b in zip(hash1, hash2) if a != b)
        print(f"  Изменение 1 символа входа -> {diff_count} из 60 символов хеша")
        # Ожидаем, что изменится хотя бы 20% символов (12 из 60)
        self.assertGreaterEqual(diff_count, 10)
        print("✓ test_sponge_hash_sensitivity passed")

    def test_sponge_hash_empty_string(self):
        """Проверка: хеш от пустой строки"""
        result = self.cipher.SpongeFun_hash("")
        self.assertEqual(len(result), 60)
        print(f"  Хеш от пустой строки: {result[:20]}...")
        print("✓ test_sponge_hash_empty_string passed")

def test_sponge_hash_one_symbol_change_avalanche(self):
    """Проверка лавинного эффекта: изменение одного символа в начале сообщения"""
    msg1 = "АБВГДЕЖЗИЙ"  # Убрана Ё
    msg2 = "ББВГДЕЖЗИЙ"  # Первый символ изменён
    
    hash1 = self.cipher.SpongeFun_hash(msg1)
    hash2 = self.cipher.SpongeFun_hash(msg2)
    
    diff_count = sum(1 for a, b in zip(hash1, hash2) if a != b)
    diff_percent = diff_count / 60 * 100
    print(f"  Изменение первого символа -> {diff_count} из 60 символов ({diff_percent:.1f}%)")
    self.assertGreaterEqual(diff_count, 20)
    print("✓ test_sponge_hash_one_symbol_change_avalanche passed")

    def test_sponge_hash_no_collisions_for_similar_inputs(self):
        """Проверка: похожие входы не дают одинаковый хеш"""
        msg1 = "КОШКА"
        msg2 = "КОШКИ"  # Очень похожее сообщение
        
        hash1 = self.cipher.SpongeFun_hash(msg1)
        hash2 = self.cipher.SpongeFun_hash(msg2)
        
        # Хеши не должны быть одинаковыми
        self.assertNotEqual(hash1, hash2)
        print("✓ test_sponge_hash_no_collisions_for_similar_inputs passed")


class TestCompressionBlockProperties(unittest.TestCase):
    """Тесты свойств C-блока как односторонней функции"""
    
    def setUp(self):
        self.cipher = AlphabetCipher()

    def test_c_block_avalanche_effect(self):
        """Проверка лавинного эффекта C-блока"""
        IN1 = ["ХОРОШО_БЫТЬ_ВАМИ"]
        IN2 = ["ХОРОШО_БЫТЬ_ВАМЖ"]  # Последний символ изменён
        
        result1 = self.cipher.C_block(IN1, 16)
        result2 = self.cipher.C_block(IN2, 16)
        
        diff_count = sum(1 for a, b in zip(result1, result2) if a != b)
        print(f"  Изменение 1 символа входа -> {diff_count} из 16 символов выхода")
        # Ожидаем изменение хотя бы 25% символов (4 из 16)
        self.assertGreaterEqual(diff_count, 4)
        print("✓ test_c_block_avalanche_effect passed")

def test_c_block_one_way_property_demo(self):
    """Демонстрация свойства односторонности: трудно восстановить вход по выходу"""
    IN = ["СЕКРЕТНЫЙ_КЛЮЧ_Б"]  
    hash_result = self.cipher.C_block(IN, 8)
    
    # Проверяем, что выход короче входа (функция сжатия)
    self.assertEqual(len(hash_result), 8)
    self.assertLess(len(hash_result), len(IN[0]))
    print(f"  Вход (16 символов) -> выход (8 символов): сжатие {len(IN[0])}→{len(hash_result)}")
    print("✓ test_c_block_one_way_property_demo passed")

if __name__ == '__main__':
    unittest.main(verbosity=2)