import math
from functools import cached_property


class AlphabetCipher:
    def __init__(self):
        """
        Инициализация шифра алфавита.
        Создаёт и заполняет четыре вспомогательных словаря для быстрого
        преобразования между символами, бинарными кодами и числовыми индексами (0-31).
        """
        # Основная таблица кодирования: Символ -> 5-битный бинарный код
        self.symbol_to_code = {
            '_': '00000', 'А': '00001', 'Б': '00010', 'В': '00011',
            'Г': '00100', 'Д': '00101', 'Е': '00110', 'Ж': '00111',
            'З': '01000', 'И': '01001', 'Й': '01010', 'К': '01011',
            'Л': '01100', 'М': '01101', 'Н': '01110', 'О': '01111',
            'П': '10000', 'Р': '10001', 'С': '10010', 'Т': '10011',
            'У': '10100', 'Ф': '10101', 'Х': '10110', 'Ц': '10111',
            'Ч': '11000', 'Ш': '11001', 'Щ': '11010', 'Ы': '11011',
            'Ь': '11100', 'Э': '11101', 'Ю': '11110', 'Я': '11111'
        }

        # Обратное отображение: 5-битный код -> Символ (для быстрого декодирования)
        self.code_to_symbol = {code: symbol for symbol, code in self.symbol_to_code.items()}

        # Числовые индексы (0-31), полученные из десятичного значения бинарных кодов
        self.number_to_symbol = {}
        self.symbol_to_number = {}

        for symbol, code in self.symbol_to_code.items():
            number = int(code, 2)
            self.number_to_symbol[number] = symbol
            self.symbol_to_number[symbol] = number

    def get_symbol_by_number(self, number):
        """
        Возвращает символ алфавита по его числовому индексу.

        Args:
            number: Целое число от 0 до 31.

        Returns:
            Символ алфавита (str).

        Raises:
            ValueError: Если число выходит за пределы диапазона [0, 31].
        """
        if 0 <= number <= 31:
            return self.number_to_symbol[number]
        raise ValueError("Номер должен быть в диапазоне от 0 до 31")

    def get_number_by_symbol(self, symbol):
        """
        Возвращает числовой индекс указанного символа.

        Args:
            symbol: Один символ из поддерживаемого алфавита (в верхнем регистре или '_').

        Returns:
            Индекс символа (int) от 0 до 31.

        Raises:
            ValueError: Если символ отсутствует в алфавите шифра.
        """
        if symbol in self.symbol_to_number:
            return self.symbol_to_number[symbol]
        raise ValueError(f"Символ '{symbol}' отсутствует в алфавите")

    def encrypt(self, text_input: str):
        """
        Кодирует текстовую строку в список 5-битных бинарных кодов.

        Args:
            text_input: Исходная строка для шифрования. Автоматически приводится к верхнему регистру.

        Returns:
            Список строк, где каждый элемент — 5-битный бинарный код соответствующего символа.

        Raises:
            KeyError: Если в тексте встречается неподдерживаемый символ.
        """
        res = []
        for char in text_input.upper():
            res.append(self.symbol_to_code[char])
        return res

    def decrypt(self, list_codes: list[str]):
        """
        Декодирует список 5-битных бинарных строк обратно в текстовую строку.

        Args:
            list_codes: Список бинарных строк длины 5.

        Returns:
            Расшифрованная строка. Неизвестные или повреждённые коды заменяются на '?'.
        """
        symbols = []
        for code in list_codes:
            symbols.append(self.code_to_symbol.get(code, '?'))
        return "".join(symbols)

    def text2array(self, text: str):
        """
        Преобразует текстовую строку в массив числовых индексов.

        Args:
            text: Входная строка

        Returns:
            list[int]: Массив индексов (0-31) для каждого символа
        """
        return [self.get_number_by_symbol(c) for c in text]

    def array2text(self, arr: list[int]):
        """
        Преобразует массив числовых индексов в текстовую строку.

        Args:
            arr: Массив индексов (0-31)

        Returns:
            str: Текстовая строка
        """
        return "".join([self.get_symbol_by_number(n) for n in arr])

    def add_numbers(self, num1, num2):
        """
        Выполняет циклическое сложение двух чисел по модулю 32.

        Args:
            num1: Первое слагаемое.
            num2: Второе слагаемое.

        Returns:
            Результат сложения (num1 + num2) % 32.
        """
        return (num1 + num2) % 32

    def subtract_numbers(self, num1, num2):
        """
        Выполняет циклическое вычитание двух чисел по модулю 32.

        Args:
            num1: Уменьшаемое.
            num2: Вычитаемое.

        Returns:
            Результат вычитания (num1 - num2) % 32.
        """
        return (num1 - num2) % 32

    def add_symbols(self, symbol1, symbol2):
        """
        Складывает два символа алфавита, интерпретируя их как числа по модулю 32.

        Args:
            symbol1: Первый символ.
            symbol2: Второй символ.

        Returns:
            Символ, являющийся результатом циклического сложения.
        """
        num1 = self.symbol_to_number[symbol1]
        num2 = self.symbol_to_number[symbol2]
        result_num = self.add_numbers(num1, num2)
        return self.number_to_symbol[result_num]

    def subtract_symbols(self, symbol1, symbol2):
        """
        Вычитает один символ из другого по модулю 32.

        Args:
            symbol1: Уменьшаемый символ.
            symbol2: Вычитаемый символ.

        Returns:
            Символ, являющийся результатом циклического вычитания.
        """
        num1 = self.symbol_to_number[symbol1]
        num2 = self.symbol_to_number[symbol2]
        result_num = self.subtract_numbers(num1, num2)
        return self.number_to_symbol[result_num]

    def add_text(self, text1: str, text2: str):
        """
        Выполняет поэлементное (посимвольное) сложение двух строк по модулю 32.

        Если длины строк различаются, символы более длинной строки,
        не нашедшие пары, добавляются в результат без изменений.

        Args:
            text1: Первая строка.
            text2: Вторая строка.

        Returns:
            Результирующая строка после поэлементного сложения.
        """
        result = ""
        maxstring = max(text1, text2, key=len)
        len_match = min(len(text1), len(text2))
        for i in range(len_match):
            result += self.add_symbols(text1[i], text2[i])
        result += maxstring[len_match:]
        return result

    def sub_text(self, text1: str, text2: str):
        """
        Выполняет поэлементное (посимвольное) вычитание второй строки из первой по модулю 32.

        При разной длине строк:
        - Если `text1` длиннее, "хвост" `text1` остаётся без изменений (вычитание '_' -> +0).
        - Если `text2` длиннее, "хвост" обрабатывается как операция 0 - символ.

        Args:
            text1: Уменьшаемая строка.
            text2: Вычитаемая строка.

        Returns:
            Результирующая строка после поэлементного вычитания.
        """
        result = ""
        len_match = min(len(text1), len(text2))
        if len(text1) > len(text2):
            longer_str = text1
            flag = 0
        else:
            longer_str = text2
            flag = 1
        for i in range(len_match):
            result += self.subtract_symbols(text1[i], text2[i])
        if len(longer_str) > len_match:
            for i in range(len_match, len(longer_str)):
                t = longer_str[i]
                if flag == 1:
                    result += self.subtract_symbols("_", t)
                else:
                    result += self.subtract_symbols(t, "_")
        return result

    def frw_caesar(self, text_input, key_input):
        """
        Шифрует текст с использованием шифра Цезаря с заданным ключом-символом.

        Алгоритм:
        1. Берет первый символ из ключа
        2. Для каждого символа входного текста складывает его с ключом
           по модулю 32 (используя add_symbols)
        3. Возвращает зашифрованный текст

        Args:
            text_input: Исходный текст для шифрования
            key_input: Ключ - символ для сдвига (используется первый символ)

        Returns:
            Зашифрованный текст (str)
        """
        out = ""
        key_1 = key_input[0]
        for i in range(len(text_input)):
            out += self.add_symbols(text_input[i], key_1)
        return out

    def inv_caesar(self, text_input, key_input):
        """
        Расшифровывает текст, зашифрованный шифром Цезаря, с использованием заданного ключа-символа.

        Алгоритм:
        1. Берет первый символ из ключа
        2. Для каждого символа входного текста вычитает ключ из символа
           по модулю 32 (используя subtract_symbols)
        3. Возвращает расшифрованный текст

        Args:
            text_input: Зашифрованный текст для расшифровки
            key_input: Ключ - символ, использованный при шифровании (используется первый символ)

        Returns:
            Расшифрованный текст (str)
        """
        out = ""
        key_1 = key_input[0]
        for i in range(len(text_input)):
            out += self.subtract_symbols(text_input[i], key_1)
        return out

    def frw_poly_caesar(self, text_input, key_input):
        """
        Шифрует текст с использованием полиалфавитного шифра Цезаря.

        Алгоритм:
        1. Для каждого символа текста вычисляется позиция в ключе (по модулю длины ключа)
        2. Накопительным итогом складываются символы ключа
        3. Каждый символ текста складывается с текущим значением накопленной суммы ключа

        Args:
            text_input: Исходный текст для шифрования
            key_input: Ключ - строка символов

        Returns:
            Зашифрованный текст (str)
        """
        out = ""
        t_k = "_"
        key_len = len(key_input)
        for i in range(len(text_input)):
            t_k = self.add_symbols(t_k, key_input[i % key_len])
            out += self.add_symbols(text_input[i], t_k)
        return out

    def inv_poly_caesar(self, text_input, key_input):
        """
        Расшифровывает текст, зашифрованный полиалфавитным шифром Цезаря.

        Алгоритм:
        1. Инициализирует накопитель t_k значением '_' (0).
        2. Проходит по зашифрованному тексту.
        3. На каждом шаге обновляет t_k, добавляя к нему символ ключа (циклически).
        4. Расшифровывает символ: вычитает текущее t_k из символа шифротекста.

        Args:
            text_input: Зашифрованный текст.
            key_input: Ключ, использованный при шифровании.

        Returns:
            Расшифрованный исходный текст (str).
        """
        out = ""
        t_k = "_"
        key_len = len(key_input)

        for i in range(len(text_input)):
            t_k = self.add_symbols(t_k, key_input[i % key_len])
            out += self.subtract_symbols(text_input[i], t_k)

        return out

    def _generate_s_key(self, key_input):
        """
        Генерирует производный ключ для S-блока на основе входного ключа.

        Алгоритм генерации:
        1. Создаёт расширенный ключ путём конкатенации входного ключа с самим собой
        2. Инициализирует производный ключ четырьмя символами '_' (нулевое значение)
        3. Выполняет 8 итераций:
           a. Извлекает подстроку длиной 4 символа из расширенного ключа со сдвигом
           b. Преобразует подстроку в массив числовых индексов (0-31)
           c. Для каждого из 4-х символов применяет нелинейное преобразование
              с использованием вектора коэффициентов
           d. Преобразует результат обратно в строку символов
           e. Добавляет полученную строку к производному ключу по модулю 32
        4. Возвращает итоговый производный ключ длиной 4 символа

        Args:
            key_input: Входной ключ длиной ровно 16 символов.

        Returns:
            derived_key: Сгенерированный ключ длиной 4 символа для использования
                        в полиалфавитном шифре Цезаря.

        Note:
            Вектор коэффициентов используется для нелинейного преобразования
            символов ключа, что повышает криптостойкость алгоритма.
        """
        transform_coefficients = [1, -1, 1, 2, -2, 1, 1, 3, -1, 2]
        derived_key = "____"
        extended_key = key_input + key_input
        for i in range(8):
            start_position = i * 2
            key_substring = extended_key[start_position: start_position + 4]
            substring_indices = [self.get_number_by_symbol(char) for char in key_substring]
            transformed_indices = []
            for k in range(4):
                coeff_index = (2 * i + k) % 10
                coefficient = transform_coefficients[coeff_index]
                symbol_index = substring_indices[k]
                transformed_index = (64 + k + coefficient * symbol_index) % 32
                transformed_indices.append(transformed_index)
            transformed_chunk = "".join([self.get_symbol_by_number(n) for n in transformed_indices])
            derived_key = self.add_text(derived_key, transformed_chunk)
        return derived_key

    def frw_S_caesar(self, text_input, key_input):
        """
        Выполняет прямое шифрование S-блока (подстановочного блока).

        S-блок представляет собой унифицированный интерфейс к шифру замены,
        который комбинирует нелинейное преобразование ключа с полиалфавитным
        шифром Цезаря.

        Алгоритм работы:
        1. Проверяет корректность входных данных:
           - text_input должен содержать ровно 4 символа (открытый текст)
           - key_input должен содержать ровно 16 символов (основной ключ)
        2. Генерирует производный ключ KEY_TMP длиной 4 символа из key_input
           с использованием нелинейных преобразований (см. _generate_s_key)
        3. Применяет полиалфавитный шифр Цезаря к text_input с производным ключом
           (накопительное сложение символов текста с символами ключа по модулю 32)
        4. Возвращает зашифрованный блок длиной 4 символа

        Args:
            text_input: Блок открытого текста длиной ровно 4 символа.
                     Каждый символ должен принадлежать алфавиту (0-31).
            key_input: Основной ключ длиной ровно 16 символов.
                   Используется для генерации рабочего ключа.

        Returns:
            str: Зашифрованный блок (шифротекст) длиной 4 символа,
                 либо строка "input_error" при неверных размерах входных данных.
        """
        if len(text_input) != 4 or len(key_input) != 16:
            return "input_error"
        ciphertext_block = text_input
        working_key = self._generate_s_key(key_input)
        ciphertext_block = self.frw_poly_caesar(ciphertext_block, working_key)
        return ciphertext_block

    def inv_S_caesar(self, text_input, key_input):
        """
        Выполняет обратное шифрование (расшифрование) S-блока.

        Является обратной операцией к frw_S_caesar. Восстанавливает исходный
        открытый текст из зашифрованного блока при условии использования
        того же самого ключа key_input.

        Алгоритм работы:
        1. Проверяет корректность входных данных:
           - text_input должен содержать ровно 4 символа (шифротекст)
           - key_input должен содержать ровно 16 символов (основной ключ)
        2. Генерирует тот же самый производный ключ из key_input
           (гарантируется детерминированность: тот же входной ключ → тот же производный ключ)
        3. Применяет обратный полиалфавитный шифр Цезаря к text_input с производным ключом
           (накопительное вычитание символов ключа из символов шифротекста по модулю 32)
        4. Возвращает расшифрованный блок (исходный открытый текст)

        Args:
            text_input: Блок шифротекста длиной ровно 4 символа.
                     Каждый символ должен принадлежать алфавиту (0-31).
            key_input: Основной ключ длиной ровно 16 символов.
                   Должен совпадать с ключом, использованным при шифровании.

        Returns:
            str: Расшифрованный блок (открытый текст) длиной 4 символа,
                 либо строка "input_error" при неверных размерах входных данных.

        Note:
            Для корректной расшифровки необходимо использовать тот же самый
            ключ key_input, что и при шифровании. Генерация производного ключа полностью
            детерминирована, поэтому при одинаковых key_input получится
            одинаковый производный ключ.
        """
        if len(text_input) != 4 or len(key_input) != 16:
            return "input_error"
        plaintext_block = text_input
        working_key = self._generate_s_key(key_input)
        plaintext_block = self.inv_poly_caesar(plaintext_block, working_key)
        return plaintext_block

    def frw_merge_block(self, text_input, key_input):
        """
        Прямое перемешивание блока (Forward Merge Block).
        
        Реализует алгоритм диффузии на основе ключа:
        1. Преобразует ключ в массив числовых индексов
        2. Вычисляет контрольную сумму (permutation seed) со знакопеременным сложением
        3. На основе seed генерирует перестановку индексов [0,1,2,3]
        4. Преобразует входной блок в массив индексов
        5. Выполняет циклическое сложение символов блока в порядке перестановки
        6. Преобразует результат обратно в текст
        
        Args:
            text_input: Блок текста длиной 4 символа.
            key_input: Ключ длиной 16 символов для генерации перестановки.
            
        Returns:
            str: Перемешанный блок длиной 4 символа или "input_error".
        """
        if len(text_input) != 4 or len(key_input) != 16:
            return "input_error"
        key_indices = [self.get_number_by_symbol(c) for c in key_input]
        permutation_seed = 0
        for i in range(16):
            coefficient_sign = 1 if i % 2 == 0 else -1
            permutation_seed = (48 + permutation_seed + coefficient_sign * key_indices[i]) % 24
        shuffle_indices = [0, 1, 2, 3]
        for k in range(3):
            swap_offset = permutation_seed % (4 - k)
            permutation_seed = (permutation_seed - swap_offset) // (4 - k)
            shuffle_indices[k], shuffle_indices[k + swap_offset] = shuffle_indices[k + swap_offset], shuffle_indices[k]
        block_indices = [self.get_number_by_symbol(symbol) for symbol in text_input]
        for j in range(4):
            source_idx = shuffle_indices[(1 + j) % 4]
            target_idx = shuffle_indices[j % 4]
            block_indices[source_idx] = (block_indices[source_idx] + block_indices[target_idx]) % 32
        return "".join([self.get_symbol_by_number(n) for n in block_indices])

    def inv_merge_block(self, text_input, key_input):
        """
        Обратное перемешивание блока (Inverse Merge Block).

        Восстанавливает исходный блок из перемешанного:
        1. Преобразует ключ в массив числовых индексов
        2. Вычисляет ту же контрольную сумму (permutation seed)
        3. Генерирует ту же перестановку индексов
        4. Преобразует входной блок в массив индексов
        5. Выполняет ОБРАТНЫЕ операции вычитания в ОБРАТНОМ порядке
        6. Преобразует результат обратно в текст

        Args:
            text_input: Перемешанный блок длиной 4 символа.
            key_input: Ключ длиной 16 символов (тот же, что при шифровании).

        Returns:
            str: Восстановленный блок длиной 4 символа или "input_error".
        """
        if len(text_input) != 4 or len(key_input) != 16:
            return "input_error"
        key_indices = [self.get_number_by_symbol(c) for c in key_input]
        permutation_seed = 0
        for i in range(16):
            coefficient_sign = 1 if i % 2 == 0 else -1
            permutation_seed = (48 + permutation_seed + coefficient_sign * key_indices[i]) % 24
        shuffle_indices = [0, 1, 2, 3]
        for k in range(3):
            swap_offset = permutation_seed % (4 - k)
            permutation_seed = (permutation_seed - swap_offset) // (4 - k)
            shuffle_indices[k], shuffle_indices[k + swap_offset] = shuffle_indices[k + swap_offset], shuffle_indices[k]
        block_indices = [self.get_number_by_symbol(c) for c in text_input]
        for j in range(3, -1, -1):
            source_idx = shuffle_indices[(1 + j) % 4]
            target_idx = shuffle_indices[j % 4]
            block_indices[source_idx] = (32 + block_indices[source_idx] - block_indices[target_idx]) % 32
        return "".join([self.get_symbol_by_number(n) for n in block_indices])

    def frw_s_caesar_m(self, text_input, key_input):
        """
                Прямое шифрование с использованием комбинированного S-блока и перемешивания.

                Алгоритм выполняет три этапа шифрования:
                1. Первичное перемешивание блока (диффузия)
                2. Нелинейная подстановка через S-блок (конфузия)
                3. Вторичное перемешивание блока (диффузия)

                Такая структура (перемешивание-подстановка-перемешивание) обеспечивает
                хорошее распределение влияния каждого бита ключа и открытого текста
                на зашифрованный результат.

                Args:
                    text_input: Блок открытого текста длиной 4 символа.
                    key_input: Ключ шифрования длиной 16 символов.

                Returns:
                    str: Зашифрованный блок длиной 4 символа.
                """
        temp_block = self.frw_merge_block(text_input, key_input)
        temp_block = self.frw_S_caesar(temp_block, key_input)
        ciphertext_block = self.frw_merge_block(temp_block, key_input)
        return ciphertext_block

    def inv_s_caesar_m(self, text_input, key_input):
        """
        Обратное шифрование (расшифрование) с использованием комбинированного
        S-блока и перемешивания.

        Алгоритм выполняет три этапа расшифрования в порядке,
        обратном прямому шифрованию:
        1. Обратное вторичному перемешиванию
        2. Обратная нелинейная подстановка через S-блок
        3. Обратное первичному перемешиванию

        Args:
            text_input: Блок шифротекста длиной 4 символа.
            key_input: Ключ шифрования длиной 16 символов (тот же, что при шифровании).

        Returns:
            str: Расшифрованный блок (открытый текст) длиной 4 символа.
        """
        temp_block = self.inv_merge_block(text_input, key_input)
        temp_block = self.inv_S_caesar(temp_block, key_input)
        plaintext_block = self.inv_merge_block(temp_block, key_input)
        return plaintext_block

    def core_Caesar(self, IN_prime: str, IN_aux: str):
        """
        Выполняет ядровое преобразование на основе модифицированного шифра Цезаря
        с нелинейным смешиванием двух 16-символьных блоков.

        Алгоритм работы:
        1. Проверяет, что оба входных блока имеют длину ровно 16 символов.
        2. Инициализирует вектора коэффициентов C1 (длина 7) и C2 (длина 5)
           для знакопеременного взвешивания при смешивании.
        3. Преобразует входные строки в массивы числовых индексов (0-31).
        4. Первый проход (16 итераций):
           - Накопительное суммирование символов IN_aux для вычисления c1 (mod 7)
           - Использование c1 для индексации IN_prime и вычисления c2 (mod 5)
           - Комбинированное вычисление c3 на основе c1, c2 и значений IN_prime (mod 16)
           - Финальные значения c1, c2, c3 используются как смещения во втором проходе.
        5. Второй проход (16 итераций):
           - Вычисление динамических индексов q, j, p, l на основе c1, c2, c3 и номера итерации
           - Нелинейное преобразование: (64 + prime[p] + C1[q]*C2[j]*aux[l]) % 32
           - Накопительное формирование выходного массива с сохранением истории в tmp
        6. Преобразует результирующий массив индексов обратно в строку символов.

        Args:
            IN_prime (str): Основной 16-символьный блок данных (ключ или текст).
            IN_aux (str): Вспомогательный 16-символьный блок для смешивания.

        Returns:
            str: Зашифрованный/преобразованный блок длиной 16 символов,
                 либо строка "input_error" при несоответствии длин входных данных.

        Note:
            Функция использует детерминированные псевдослучайные смещения,
            зависящие от содержимого обоих входов, что обеспечивает диффузию.
        """
        out = "input_error"
        if len(IN_prime) == 16 and len(IN_aux) == 16:
            C1 = [1, -1, 1, -1, 1, -1, 1]
            C2 = [1, -1, 1, -1, 1]
            aux = [self.get_number_by_symbol(c) for c in IN_aux]
            prime = [self.get_number_by_symbol(c) for c in IN_prime]
            tmp = 0
            t1 = 0
            c1 = 0
            c2 = 0
            c3 = 0
            for i in range(16):
                t1 = t1 + aux[i]
                c1 = t1 % 7
                c2 = prime[2 * c1 + 1] % 5
                c3 = (prime[2 * c2] + prime[2 * c1]) % 16
            arr = [0] * 16
            for i in range(16):
                q = (c1 + i) % 7
                j = (c2 + i) % 5
                p = (c3 + i) % 16
                l = i % 16
                tmp = (tmp + 64 + prime[p] + C1[q] * C2[j] * aux[l]) % 32
                arr[i] = tmp
            out = "".join([self.get_symbol_by_number(n) for n in arr])
        return out

    def confuse(self, IN1: str, IN2: str):
        """
        Выполняет операцию конфузии (перемешивания) двух 16-символьных блоков
        на основе поэлементного сравнения и условного преобразования.

        Алгоритм работы:
        1. Преобразует обе входные строки в массивы числовых индексов (0-31).
        2. Для каждой позиции i (0..15) выполняет условное преобразование:
           - Если arr1[i] > arr2[i]: arr1[i] = (arr1[i] + i) % 32
           - Иначе: arr1[i] = (arr2[i] + i) % 32
           (добавление индекса позиции усиливает зависимость результата от порядка)
        3. Преобразует модифицированный массив обратно в строку.
        4. Применяет дополнительное смешивание: к результату последовательно
           добавляются (по модулю 32) исходные строки IN1 и IN2 через add_text.

        Args:
            IN1 (str): Первый 16-символьный блок.
            IN2 (str): Второй 16-символьный блок.

        Returns:
            str: Результат конфузии — строка длиной 16 символов, полученная
                 после условного преобразования и дополнительного смешивания.

        Note:
            Функция реализует нелинейное преобразование, где выбор операнда
            зависит от сравнения значений, что затрудняет криптоанализ.
        """
        arr1 = self.text2array(IN1)
        arr2 = self.text2array(IN2)
        for i in range(16):
            if arr1[i] > arr2[i]:
                arr1[i] = (arr1[i] + i) % 32
            else:
                arr1[i] = (arr2[i] + i) % 32
        tmp = self.array2text(arr1)
        out = self.add_text(self.add_text(tmp, IN1), IN2)

        return out

    def mixinputs(self, IN: list[str]):
        """
        Выполняет комбинированное смешивание четырёх 16-символьных блоков
        с использованием операций сложения и вычитания по модулю 32.

        Алгоритм работы:
        1. Извлекает четыре входных блока из списка: in1, in2, in3, in4.
        2. Вычисляет четыре выходных блока:
           - out1 = in1 ⊕ in2 (поэлементное сложение)
           - out2 = in1 ⊖ in2 (поэлементное вычитание)
           - out3 = out2 ⊕ (in3 ⊕ in4) (комбинация вычитания и сложения)
           - out4 = out1 ⊕ (in3 ⊖ in4) (комбинация сложения и вычитания)
        3. Возвращает кортеж из четырёх смешанных блоков.

        Args:
            IN (list[str]): Список из четырёх строк длиной 16 символов каждая.

        Returns:
            tuple[str, str, str, str]: Кортеж из четырёх 16-символьных строк,
                                       полученных в результате смешивания.

        Note:
            Функция обеспечивает диффузию: изменение любого входного блока
            влияет на несколько выходных блоков одновременно.
        """
        in1 = IN[0]
        in2 = IN[1]
        in3 = IN[2]
        in4 = IN[3]
        out1 = self.add_text(in1, in2)
        out2 = self.sub_text(in1, in2)
        out3 = self.add_text(out2, self.add_text(in3, in4))
        out4 = self.add_text(out1, self.sub_text(in3, in4))
        return out1, out2, out3, out4

    def compress(self, IN_16: str, out_n: int):
        """
        Выполняет сжатие 16-символьного блока до заданного размера (16, 8 или 4 символа)
        путём разбиения на четверти и их комбинирования.

        Алгоритм работы:
        1. Если out_n == 16: возвращает входную строку без изменений.
        2. Если out_n == 8 или 4 и длина входа равна 16:
           - Разбивает IN_16 на четыре подблока по 4 символа: a1, a2, a3, a4
           - Для out_n == 8:
             * Объединяет a1+a3 и a2+a4 (конкатенация)
             * Применяет поэлементное сложение: (a1||a3) ⊕ (a2||a4)
           - Для out_n == 4:
             * Вычисляет a1⊖a3 и a2⊖a4 (поэлементное вычитание)
             * Применяет поэлементное сложение результатов
        3. При несоответствии параметров возвращает "input_error".

        Args:
            IN_16 (str): Входной блок длиной 16 символов.
            out_n (int): Желаемая длина выходного блока (16, 8 или 4).

        Returns:
            str: Сжатый блок длиной out_n символов, либо "input_error"
                 при неверных входных параметрах.

        Note:
            Операции сложения/вычитания выполняются по модулю 32 над числовыми
            индексами символов, что обеспечивает обратимость при расшифровании.
        """
        out = "input_error"
        out_n_str = str(out_n)
        if out_n_str != "16":
            if len(IN_16) == 16:
                a1 = IN_16[0:4]
                a2 = IN_16[4:8]
                a3 = IN_16[8:12]
                a4 = IN_16[12:16]
                if out_n_str == "8":
                    a13 = a1 + a3
                    a24 = a2 + a4
                    out = self.add_text(a13, a24)
                elif out_n_str == "4":
                    a13 = self.sub_text(a1, a3)
                    a24 = self.sub_text(a2, a4)
                    out = self.add_text(a13, a24)
                else:
                    out = "input_error"
            else:
                out = "input_error"
        else:
            out = IN_16
        return out

    def C_block(self, IN_ARR: list[str], out_size):
        """
        Комплексное преобразование блока (Compression block).

        Алгоритм:
        1. Инициализирует 4 константных 16-символьных вектора.
        2. Поэлементно складывает каждый входной блок с соответствующей константой.
        3. Применяет каскад: mixinputs → core_Caesar ×2 → confuse → core_Caesar.
        4. Сжимает результат до out_size через compress().

        Args:
            IN_ARR (list[str]): 4 строки по 16 символов.
            out_size (int): Желаемый размер выхода (16, 8 или 4).

        Returns:
            str: Преобразованный блок или "input_error".

        Note:
            Использует каскадное нелинейное преобразование для обеспечения диффузии.
        """
        out = "input_error"
        r = len(IN_ARR)
        C = [
            "________________",
            "ПРОЖЕКТОР_ЧЕПУХИ",
            "КОЛЫХАТЬ_ПАРОДИЮ",
            "КАРМАННЫЙ_АТАМАН"
        ]
        flag = 1
        for i in range(r):
            if len(IN_ARR[i]) == 16:
                C[i] = self.add_text(C[i], IN_ARR[i])
            else:
                flag = 0
        if flag == 1:
            C = self.mixinputs(C)
            TMP1 = self.core_Caesar(C[0], C[2])
            TMP2 = self.core_Caesar(C[3], C[1])
            TMP3 = self.confuse(TMP1, TMP2)
            out = self.core_Caesar(TMP3, TMP1)
            out = self.compress(out, out_size)
        return out

    def shift_block(self, INS: str):
        """
        Сдвигает символы в 4-символьном блоке на одну позицию вправо (циклически).

        Алгоритм:
        1. Преобразует текст в массив числовых индексов
        2. Для каждой позиции i (0..3) перемещает значение в позицию q = (i+1) mod 4
        3. Преобразует массив обратно в текст

        Args:
            INS: Входная строка длиной 4 символа

        Returns:
            str: Строка со сдвинутыми символами
        """
        arr = self.text2array(INS)
        tmp = [0] * 4
        for i in range(4):
            q = (i + 1) % 4
            tmp[q] = arr[i]
        out = self.array2text(tmp)
        return out

    def shift_rows(self, STATE: list):
        """
        Выполняет циклический сдвиг строк в матрице состояния 5x5.

        Алгоритм:
        Для каждой строки i и столбца j:
        - Вычисляет q = (j+i) mod 5
        - out[j,i] = a[q,i] (сдвигает элементы внутри столбца вниз на i позиций)

        Args:
            STATE: Матрица состояния 5x5 (список списков строк)

        Returns:
            list: Модифицированная матрица состояния 5x5
        """
        a = STATE
        out = [["" for _ in range(5)] for _ in range(5)]

        for i in range(5):
            for j in range(5):
                q = (j + i) % 5
                out[j][i] = a[q][i]

        return out

    def shatter_blocks(self, STATE: list):
        """
        Переставляет символы внутри блоков на главной диагонали матрицы.

        Алгоритм:
        Для каждого элемента диагонали a[i,i] (i=0..4):
        - Применяет shift_block к a[i,i]

        Args:
            STATE: Матрица состояния 5x5

        Returns:
            list: Матрица с переставленными диагональными блоками
        """
        a = STATE
        for i in range(5):
            a[i][i] = self.shift_block(a[i][i])
        return a

    def mix_cols(self, STATE: list):
        """
        Перемешивает столбцы матрицы состояния с использованием операций
        сложения и вычитания.

        Алгоритм:
        Для каждого столбца i (0..4):
        1. Инициализирует X_i как "____" (4 символа подчеркивания)
        2. Для каждого j (0..4): X_i = add_text(X_i, a[j,i])
        3. Вычисляет q = (i+1) mod 5
        4. Для каждого j (0..4):
           - tmp = add_text(X_i, a[j,q])
           - a[j,q] = sub_text(tmp, a[j,i])

        Args:
            STATE: Матрица состояния 5×5, где каждый элемент — строка из 4 символов.

        Returns:
            list: Модифицированная матрица состояния 5×5.
        """
        a = STATE
        for i in range(5):
            X_i = "____"
            for j in range(5):
                X_i = self.add_text(X_i, a[j][i])
            q = (i + 1) % 5

            for j in range(5):
                tmp = self.add_text(X_i, a[j][q])
                a[j][q] = self.sub_text(tmp, a[j][i])

        return a

    def sponge_absorb(self, state, b_in):
        """
        Фаза поглощения (Absorb) губчатой конструкции (Sponge Construction).

        Алгоритм работы:
        1. Формирует строку str1 = b_in + state[0][0] + b_in + state[0][0] (16 символов).
        2. Вычисляет вектор строк x[0..4] как поэлементную сумму всех элементов
           каждой строки матрицы состояния (все 5 столбцов).
        3. Конкатенирует x[0..3] в строку str2 длиной 16 символов.
        4. Обновляет state[0][0] результатом C_block([str2, str1], out_size=4).
        5. Применяет перестановки: mix_cols → shatter_blocks → shift_rows.

        Args:
            state (list[list[str]]): Матрица 5×5, каждый элемент — 4 символа.
            b_in (str): Входной блок длиной 4 символа.

        Returns:
            list[list[str]]: Обновлённое состояние матрицы 5×5.
        """
        a = state
        str1 = b_in + a[0][0] + b_in + a[0][0]
        x = ["____"] * 5
        for i in range(5):
            for j in range(5):
                x[i] = self.add_text(x[i], a[i][j])

        str2 = x[0] + x[1] + x[2] + x[3]

        a[0][0] = self.C_block([str2, str1], 4)  # Здесь возможно нужно поменять аргументы str местами
        a = self.mix_cols(a)
        a = self.shatter_blocks(a)
        a = self.shift_rows(a)
        return a

    def sponge_squeeze(self, state):
        """
        Фаза выжимки (Squeeze) губчатой конструкции.

        Алгоритм:
        1. Применяет перестановки: mix_cols → shatter_blocks → shift_rows.
        2. Вычисляет вектор x[0..4] как сумму элементов каждой строки (все 5 столбцов).
        3. Конкатенирует x[0..3] в строку длиной 16 символов.
        4. Получает 4-символьный блок через C_block([str], out_size=4).

        Args:
            state (list[list[str]]): Текущее состояние — матрица 5×5.

        Returns:
            list: [выходной_блок (4 символа), обновлённое_состояние].
        """
        a = state
        a = self.mix_cols(a)
        a = self.shatter_blocks(a)
        a = self.shift_rows(a)
        x = ["____"] * 5
        for i in range(5):
            for j in range(5):
                x[i] = self.add_text(x[i], a[i][j])
        str = x[0] + x[1] + x[2] + x[3]
        block = self.C_block([str], "4")
        return [block, a]

    def SpongeFun_hash(self, MSG):
        """
        Основная функция хеширования на основе губчатой конструкции (Sponge Function).

        Реализует полный цикл обработки сообщения:
        1. Выравнивание (padding) входного сообщения до длины, кратной 4.
        2. Фаза поглощения (absorb): последовательная обработка всех 4-символьных блоков.
        3. Фаза выжимки (squeeze): генерация 60-символьного хеша (15 блоков × 4 символа).

        Алгоритм работы:
        1. Инициализирует состояние state как матрицу 5×5, заполненную строками "____".
        2. Вычисляет количество символов дополнения K = (4 - len(MSG) % 4) % 4.
         - Если сообщение не кратно 4, добавляет символы '_' в конец.
        3. Разбивает дополненное сообщение на блоки по 4 символа:
         - Для каждого блока вызывает sponge_absorb для обновления состояния.
        4. Выполняет 15 итераций фазы squeeze:
         - На каждой итерации извлекает 4-символьный блок хеша.
         - Обновляет состояние для следующей итерации.
         - Конкатенирует извлечённые блоки в итоговую строку.
        5. Возвращает хеш длиной 60 символов.

        Args:
            MSG (str): Входное сообщение для хеширования (любой длины). Допустимые символы: русский алфавит (А-Я, Ё), '_', пробел.

        Returns:
            str: Хеш-значение длиной 60 символов (15 блоков по 4 символа). Каждый символ принадлежит алфавиту шифра (0-31).

        Note:
            - Длина выхода фиксирована (60 символов) — для изменения длины необходимо модифицировать количество итераций в фазе squeeze.
            - Padding осуществляется добавлением символов '_' (нулевое значение), что эквивалентно добавлению нулевых бит в бинарных хеш-функциях.
            - Конструкция устойчива к коллизиям благодаря многократному применению нелинейных преобразований (C_block, mix_cols, shatter_blocks).
            - Для хеширования сообщений >1000 символов рекомендуется увеличить размер состояния или количество раундов перестановки.
                """
        msg = len(MSG)
        out = ""
        state = [["____", "____", "____", "____", "____"],
                 ["____", "____", "____", "____", "____"],
                 ["____", "____", "____", "____", "____"],
                 ["____", "____", "____", "____", "____"],
                 ["____", "____", "____", "____", "____"]]
        K = 4 - msg % 4
        if K < 4:
            for k in range(K):
                MSG += "_"
        M = len(MSG) // 4
        for i in range(M):
            tmp = MSG[i * 4: i * 4 + 4]
            state = self.sponge_absorb(state, tmp)
        out = ""
        for i in range(16):
            TMP = self.sponge_squeeze(state)
            out += TMP[0]
            state = TMP[1]
        return out

    def block2num(self, block_in):
        """
        Преобразует 4-символьный блок в числовое значение (представление в базе-32).

        Алгоритм:
        1. Проверяет, что входной блок содержит ровно 4 символа.
        2. Преобразует каждый символ блока в числовой индекс (0-31).
        3. Вычисляет итоговое число как сумму: index[i] * 32^(3-i) для i=0..3 (старший символ имеет наибольший вес).
        Args:
            block_in (str): Входной блок длиной ровно 4 символа.
        Returns:
            int: Числовое значение в диапазоне [0, 32^4 - 1] = [0, 1048575], либо строка "input_error" при неверной длине входа.
        """
        out = "input_error"
        if len(block_in) == 4:
            out = 0
            pos = 1
            tmp = self.text2array(block_in)
            for i in range(3, -1, -1):
                out += pos * tmp[i]
                pos = 32 * pos
        return out

    def div(self, num_in, den_in):
        """
        Выполняет целочисленное деление с усечением к нулю.

        Использует math.trunc для обеспечения корректного поведения при делении отрицательных чисел (в отличие от оператора // в Python).
        Args:
            num_in: Делимое (число).
            den_in: Делитель (число).
        Returns:
            int: Целая часть результата деления, усечённая к нулю.
        """
        return math.trunc(num_in / den_in)

    def num2block(self, num_in):
        """
        Преобразует числовое значение в 4-символьный блок (представление в базе-32).

        Алгоритм:
        1. Инициализирует массив из 4 нулей.
        2. Последовательно извлекает младшие разряды числа по модулю 32.
        3. Заполняет массив справа налево (от младшего символа к старшему).
        4. Преобразует массив индексов обратно в строку символов.

        Args:
            num_in (int): Числовое значение для преобразования.

        Returns:
            str: 4-символьный блок, представляющий входное число в базе-32.
                """
        rem = num_in
        tmp = [0, 0, 0, 0]
        for i in range(4):
            tmp[3-i] = rem % 32
            rem = self.div(rem, 32)
        return self.array2text(tmp)

    def dec2bin(self, num_in):
        """
        Преобразует десятичное число в 20-битную бинарную строку.
        Args:
            num_in (int): Десятичное число (должно помещаться в 20 бит).

        Returns:
            str: Бинарная строка длиной ровно 20 символов (с ведущими нулями).
        """
        return f"{num_in:020b}"

    def bin2dec(self, bin_in):
        """
        Преобразует бинарную строку в десятичное число.

        Args:
            bin_in (str): Бинарная строка (символы '0' и '1').

        Returns:
            int: Десятичное значение бинарного числа.
                """
        return int(bin_in, 2)

    def initialize_PRNG(self, seed_in):
        """
        Инициализирует генератор псевдослучайных чисел (PRNG) на основе входного ключа.

        Алгоритм инициализации:
        1. Определяет четыре константных 16-символьных блока ("вектора инициализации").
        2. Для каждой константы вычисляет value[i] = C_block([const[i], seed_in], 16).
        3. Генерирует секретный ключ: secret = C_block(value, 16).
        4. Для каждого из 4-х блоков выполняет 4 итерации нелинейного смешивания:
            - Накопительное сложение с константой
            - Применение C_block для генерации 4-символьных подблоков
            - Конкатенация результатов в промежуточный буфер
        5. Извлекает из каждого буфера подстроку длиной 12 символов (позиции 4-15).

        Args:
            seed_in (str): Входной ключ/сид для инициализации (длина 16 символов).

        Returns:
            list[str]: Список из четырёх строк длиной 12 символов каждая, используемых как начальные состояния для LFSR.

        Note:
            - Функция использует многократное применение C_block для обеспечения лавинного эффекта: малое изменение seed_in радикально меняет выход.
            - Возвращаемые значения предназначены для инициализации трёх параллельных регистров сдвига (LFSR) в генераторе потокового шифра.
                """
        const = ["ПЕРВОЕ_АКТЕРСТВО",
                 "ВТОРОЙ_ДАЛЬТОНИК",
                 "ТРЕТЬЯ_САДОВНИЦА",
                 "ЧЕТВЕРТЫЙ_ГОБЛИН"]
        value = ["", "", "", ""]
        for i in range(4):
            value[i] = self.C_block([const[i], seed_in], 16)
        secret = self.C_block(value, 16)
        out = ['', '', '', '']
        for i in range(4):
            tmp = value[i]
            TMP = ""
            for j in range(4):
                tmp = self.add_text(tmp, const[i])
                TMP += self.C_block([tmp, secret], 4)
                tmp = self.add_text(tmp, TMP)
            out[i] = TMP[4:4+12]
        return out

    def block2bin(self, block_in):
        """
        Преобразует 4-символьный блок в 20-битную бинарную строку.

        Комбинирует две операции:
            1. block2num: блок → число (база-32)
            2. dec2bin: число → бинарная строка

        Args:
            block_in (str): Входной блок длиной 4 символа.

        Returns:
            str: Бинарная строка длиной 20 бит, либо "input_error" при неверной длине входного блока.
                """
        tmp = self.block2num(block_in)
        return self.dec2bin(tmp)

    def bin2block(self, bin_in):
        """
        Преобразует 20-битную бинарную строку в 4-символьный блок.

        Комбинирует две операции:
            1. bin2dec: бинарная строка → число
            2. num2block: число → блок (база-32)

        Args:
            bin_in (str): Бинарная строка длиной 20 бит.

        Returns:
            str: 4-символьный блок, представляющий входное бинарное значение.
                """
        tmp = self.bin2dec(bin_in)
        return self.num2block(tmp)

    def push_reg(self, bin_in: str, bool_in):
        """
        Выполняет сдвиг бинарного регистра влево с записью нового бита в младший разряд.

        Алгоритм:
            1. Создаёт копию входной строки.
            2. Сдвигает все биты на одну позицию влево (бит на позиции i+1 → позиция i).
            3. Записывает новый бит (bool_in) в старшую позицию (индекс len-1).
            4. Возвращает обновлённую строку.

        Args:
            bin_in (str): Исходная бинарная строка (регистр).
            bool_in: Новый бит для записи (0 или 1, или их строковое представление).

        Returns:
            str: Обновлённая бинарная строка после сдвига и записи нового бита.
                """
        out = [''] * len(bin_in)
        n = len(bin_in) - 2
        for i in range(n, -1, -1):
            out[i] = bin_in[i+1]
        index = len(bin_in) - 1
        out[index] = str(bool_in)
        res = ''.join(out)
        return res

    def taps2bin(self, taps_in):
        """
        Преобразует список позиций отводов (taps) LFSR в 20-битную бинарную маску.

        Алгоритм:
            1. Сортирует позиции отводов по убыванию.
            2. Определяет старшую позицию отвода для вычисления сдвига.
            3. Заполняет выходной массив:
                - Ведущие нули до позиции (20 - last_tap)
                - Единицы на позициях, соответствующих отводам
                - Нули на остальных позициях
            4. Заменяет все оставшиеся символы '_' на '0'.

        Args:
            taps_in (list[int]): Список позиций отводов (1-based, от 1 до 20).

        Returns:
            str: Бинарная строка длиной 20 символов, где '1' обозначает активный отвод.

        Note:
            - Позиции в taps_in считаются от старшего бита (позиция 1 = левый край).
            - Результат используется как маска для вычисления обратной связи в LFSR.
                """
        out = ['_'] * 20
        taps = sorted(taps_in, reverse=True)
        last = taps[0]
        y = 20 - last
        if y > 0:
            for i in range(y):
                out[i] = "0"
        j = 0
        for i in range(last):
            if last - i == taps[j]:
                out[y + i] = "1"
                j += 1
            else:
                out[y + i] = "0"
            if j > len(taps) - 1:
                break
        for i in range(len(out)):
            if out[i] == "_":
                out[i] = "0"
        res = ''.join(out)
        return res

    def LFSR_push(self, state_in, taps_in):
        """
        Выполняет один такт работы линейного регистра сдвига с обратной связью (LFSR).

        Алгоритм:
            1. Вычисляет бит обратной связи как сумму по модулю 2 произведений соответствующих битов состояния и маски отводов (операция AND + XOR).
            2. Сдвигает регистр через push_reg, записывая вычисленный бит в младший разряд.
        Args:
            state_in (str): Текущее состояние регистра (бинарная строка).
            taps_in (str): Маска отводов (бинарная строка той же длины).

        Returns:
            str: Новое состояние регистра после одного такта сдвига.
                """
        N = min(len(state_in), len(taps_in))
        tmp = 0
        for i in range(N):
            tmp += int(state_in[i]) & int(taps_in[i])
        out = self.push_reg(state_in, tmp % 2)
        return out

    def LFSR_next(self, state_in, taps_in):
        """
        Генерирует последовательность из 20 бит выходного потока LFSR.

        Алгоритм:
            1. Инициализирует пустой список для сбора выходных битов.
            2. Выполняет 20 тактов работы LFSR:
                - На каждом такте обновляет состояние через LFSR_push
                - Извлекает младший бит нового состояния (позиция 19) в выходной поток
            3. Конкатенирует собранные биты в строку.

        Args:
            state_in (str): Начальное состояние регистра (20 бит).
            taps_in (str): Маска отводов (20 бит).

        Returns:
            tuple[str, str]: Кортеж из:
                - выходной поток (20 бит)
                - финальное состояние регистра после 20 тактов
                """
        state = state_in
        stream = []
        for i in range(20):
            state = self.LFSR_push(state, taps_in)
            stream.append(state[19])
        stream = "".join(stream)
        return stream, state

    def AS_LFSR_push(self, state_in, taps_in):
        """
        Выполняет один такт работы генератора с чередующимися шагами (Alternating-Step LFSR).
        Алгоритм:
            1. Обновляет три параллельных LFSR (state_in[0], [1], [2]) через LFSR_push.
            2. Использует младший бит первого регистра (lfsr0[19]) как управляющий:
                - Если 0: выходной бит берётся из lfsr1[19]
                - Если 1: выходной бит берётся из lfsr2[19]
            3. Возвращает выходной бит и обновлённое состояние всех трёх регистров.

        Args:
            state_in (list[str]): Список из трёх 20-битных строк (состояния LFSR).
            taps_in (list[str]): Список из трёх масок отводов для каждого LFSR.

        Returns:
            tuple[str, list[str]]: Кортеж из:
                - выходной бит ('0' или '1')
                - список обновлённых состояний трёх регистров
                """
        lfsr0 = self.LFSR_push(state_in[0], taps_in[0])
        lfsr1 = self.LFSR_push(state_in[1], taps_in[1])
        lfsr2 = self.LFSR_push(state_in[2], taps_in[2])
        if lfsr0[19] == "0":
            stream = lfsr1[19]
        else:
            stream = lfsr2[19]
        state_out = [lfsr0, lfsr1,lfsr2]
        return stream, state_out

    def seed2bins(self, array_in):
        """
        Преобразует массив 4-символьных блоков в список 20-битных бинарных строк.

        Предназначена для подготовки начальных состояний LFSR из данных, сгенерированных функцией initialize_PRNG.

        Args:
            array_in (list[str]): Список из трёх 4-символьных блоков.

        Returns:
            list[str]: Список из трёх 20-битных бинарных строк.
                """
        out = []
        for i in range(3):
            out.append(self.block2bin(array_in[i]))
        return out

    def AS_LFSR_next(self,state_in, taps_in):
        """
        Генерирует последовательность из 20 бит выходного потока AS-LFSR.

        Алгоритм:
            1. Инициализирует пустой список для сбора выходных битов.
            2. Выполняет 20 тактов работы AS-LFSR:
                - На каждом такте обновляет состояние через AS_LFSR_push
                - Добавляет выходной бит в поток
            3. Конкатенирует собранные биты в строку.

        Args:
            state_in (list[list[str]]): Начальное состояние трёх LFSR.
            taps_in (list[str]): Маски отводов для трёх LFSR.

        Returns:
            tuple[str, list[list[str]]]: Кортеж из:
                - выходной поток (20 бит)
                - финальное состояние регистров после 20 тактов
                """
        state_set = state_in
        stream = []
        for i in range(20):
            tmp = self.AS_LFSR_push(state_set, taps_in)
            state_set = tmp[1]
            stream.append(tmp[0])
        stream = "".join(stream)
        return stream, state_set


    def C_AS_LFSR_next(self, init_flag, state_in, seed_in, set_in):
        """
        Генерация псевдослучайного потока на основе комбинированного AS-LFSR.

        Алгоритм:
        1. Режим инициализации (init_flag == "up"):
           - Генерирует 4 блока по 12 символов через initialize_PRNG
           - Преобразует каждый блок в три 20-битных состояния для 4-х групп LFSR
        2. Режим продолжения (init_flag == "down"): использует переданное состояние.
        3. Генерация: 4 итерации × 4 под-итерации:
           - Для каждой из 4-х групп масок выполняет 4 такта AS-LFSR
           - Объединяет выходы трёх регистров группы через XOR
           - Преобразует 20 бит в 4-символьный блок
        4. Возвращает 64-символьный поток и обновлённое состояние.

        Args:
            init_flag (str): "up" — инициализация, "down" — продолжение.
            state_in: Состояние регистров (при continue).
            seed_in (str): Сид для инициализации (16 символов).
            set_in (list[list[str]]): 4 набора масок отводов для LFSR.

        Returns:
            str | list: При успехе — [поток (64 символа), состояние],
                        при ошибке — "something_wrong".
        """
        out = "something_wrong"
        stream = ""
        check = 0
        state = []
        if init_flag == "up":
            INIT = self.initialize_PRNG(seed_in)
            for i in range(4):
                state.append(self.seed2bins([INIT[i][0:4], INIT[i][4:8], INIT[i][8:12]]))
                check = 1
        elif init_flag == "down":
            state = state_in
            check = 1
        if check:
            for j in range(4):
                for k in range(4):
                    T = self.AS_LFSR_next(state[k], set_in[j])
                    state[k] = T[1]
                    if k == 0:
                        tmp = T[0]
                    else:
                        tmp_list = []
                        for i in range(20):
                            tmp_list.append(str((int(T[0][i]) + int(tmp[i])) % 2))
                        tmp = "".join(tmp_list)
                stream += self.bin2block(tmp)
            out = [stream, state]
        return out

    def subblocks_xor(self, block_a_in, block_b_in):
        """
        Выполняет побитовое исключающее ИЛИ (XOR) двух 4-символьных блоков.

        Алгоритм:
        1. Преобразует каждый входной блок в числовое значение (база-32).
        2. Конвертирует числа в 20-битные бинарные строки.
        3. Выполняет поразрядное сложение по модулю 2 (XOR).
        4. Преобразует результат обратно в 4-символьный блок.
        Args:
            block_a_in (str): Первый блок длиной 4 символа.
            block_b_in (str): Второй блок длиной 4 символа.

        Returns:
            str: Результат XOR-операции — блок длиной 4 символа.

        Note:
            Операция обратима: subblocks_xor(subblocks_xor(a, b), b) == a
        """
        decA = self.block2num(block_a_in)
        decB = self.block2num(block_b_in)
        binA = self.dec2bin(decA)
        binB = self.dec2bin(decB)
        binO = []
        for i in range(len(binA)):
            binO.append(str((int(binA[i]) + int(binB[i])) % 2))
        binO = "".join(binO)
        decO = self.bin2dec(binO)
        return self.num2block(decO)

    def block_xor(self, block_a_in, block_b_in):
        """
        Выполняет побитовое XOR двух блоков произвольной длины (кратной 4).

        Алгоритм:
        1. Разбивает входные блоки на подблоки по 4 символа.
        2. Применяет subblocks_xor к каждой паре подблоков.
        3. Конкатенирует результаты в итоговую строку.

        Args:
            block_a_in (str): Первый блок (длина кратна 4).
            block_b_in (str): Второй блок (длина кратна 4, совпадает с первым).

        Returns:
            str: Результат XOR-операции — строка той же длины, что и входы.

        Raises:
            IndexError: Если длины блоков не совпадают или не кратны 4.
        """
        nb = self.div(len(block_a_in), 4)
        out = ""
        for i in range(nb):
            tmpA = block_a_in[i * 4: i * 4 + 4]
            tmpB = block_b_in[i * 4: i * 4 + 4]
            out += self.subblocks_xor(tmpA, tmpB)
        return out

    def produce_round_keys(self, key_in, num_in, LFSR_set):
        """
        Генерирует набор раундовых ключей для сети Фейстеля на основе C-AS-LFSR.

        Алгоритм:
        1. Инициализирует генератор в режиме "up" с использованием seed_in=key_in.
        2. Сохраняет первый сгенерированный 64-символьный блок как K₀.
        3. При num_in > 1 выполняет (num_in - 1) дополнительных итераций в режиме "down",
           генерируя ключи K₁...Kₙ последовательно из обновляемого состояния.
        4. Возвращает список из (num_in + 1) ключей длиной 64 символа каждый.

        Args:
            key_in (str): Мастер-ключ длиной 16 символов для инициализации генератора.
            num_in (int): Количество раундов шифрования (определяет число ключей: num_in + 1).
            LFSR_set (list[list[str]]): Набор из 4-х групп масок отводов для LFSR.

        Returns:
            list[str]: Список раундовых ключей [K₀, K₁, ..., Kₙ], каждый длиной 64 символа.

        Note:
            - K₀ и Kₙ используются для начального и финального whitening (XOR с блоком).
            - K₁...Kₙ₋₁ подаются на входы раундов функции Feistel.
            - Состояние генератора сохраняется между вызовами для обеспечения детерминированности.
        """
        out = []
        gsk = self.C_AS_LFSR_next("up", -1, key_in, LFSR_set)
        out.append(gsk[0])
        intern = gsk[1]

        if num_in > 1:
            for i in range(1, num_in):
                gsk = self.C_AS_LFSR_next("down", intern, -1, LFSR_set)
                out.append(gsk[0])
                intern = gsk[1]
        return out

    def frw_p_scitala(self, block_in):
        """
        Выполняет прямое перемешивание по алгоритму "Сцитала" (Scytale cipher).

        Алгоритм:
        1. Разделяет входной блок на две части:
           - tmpA: символы с индексами [0 : q + f] (первая половина + возможный лишний символ)
           - tmpB: символы с индексами [q + f : конец] (вторая половина)
        2. Выполняет попеременное чередование символов из tmpA и tmpB:
           - На чётных позициях: сначала символ из tmpA, затем из tmpB
           - На нечётных позициях: сначала из tmpB, затем из tmpA
        3. При нечётной длине добавляет последний символ tmpA в конец результата.

        Args:
            block_in (str): Входная строка произвольной длины.

        Returns:
            str: Перемешанная строка той же длины, что и входная.

        Note:
            - Является инволюцией с учётом inv_p_scitala: inv_p_scitala(frw_p_scitala(x)) == x
            - Используется как элемент диффузии в структуре Фейстеля.
        """
        q = math.floor(len(block_in)/2)
        f = len(block_in) % 2
        tmpA = block_in[0 : q + f]
        tmpB = block_in[q + f : 2 * q + f]
        out = ''
        for i in range(q + 1):
            if i % 2 == 0:
                out += tmpA[i : i + 1]
                out += tmpB[i: i + 1]
            else:
                out += tmpB[i: i + 1]
                out += tmpA[i: i + 1]
        if f == 1:
            out += tmpA[q + f : q + f + 1]
        return out

    def inv_p_scitala(self, block_in):
        """
        Выполняет обратное перемешивание по алгоритму "Сцитала".

        Алгоритм:
        1. Инициализирует два буфера tmpA и tmpB для восстановления половин.
        2. Проходит по входной строке с шагом 2, распределяя символы:
           - На чётных итерациях: символ 2i → tmpA, символ 2i+1 → tmpB
           - На нечётных итерациях: символ 2i → tmpB, символ 2i+1 → tmpA
        3. При нечётной длине добавляет последний символ в tmpA.
        4. Конкатенирует tmpA + tmpB для получения исходной строки.

        Args:
            block_in (str): Перемешанная строка (результат frw_p_scitala).

        Returns:
            str: Восстановленная исходная строка.

        Note:
            - Должна применяться к результату frw_p_scitala для корректного восстановления.
            - Инвариант: inv_p_scitala(frw_p_scitala(x)) == x для любой строки x.
        """
        q = math.floor(len(block_in) / 2)
        f = len(block_in) % 2
        tmpA = ""
        tmpB = ""
        out = ""
        for i in range(q):
            if i % 2 == 0:
                tmpA += block_in[2 * i : 2 * i + 1]
                tmpB += block_in[2 * i + 1: 2 * i + 2]
            else:
                tmpB += block_in[2 * i: 2 * i + 1]
                tmpA += block_in[2 * i + 1: 2 * i + 2]
        if f == 1:
            tmpA += block_in[2 * q: 2 * q + 1]
        out = tmpA + tmpB
        return out

    def frw_routine_feistel(self, block_in, key_in):
        """
        Выполняет один раунд функции Фейстеля для 8-символьного блока.

        Алгоритм:
        1. Разделяет входной блок на левую (L) и правую (R) половины по 4 символа.
        2. Применяет нелинейную функцию F = frw_s_caesar_m(R, key_in) к правой половине.
        3. Обновляет левую половину: L' = L ⊕ F (поэлементное сложение по модулю 32).
        4. Формирует выходной блок как конкатенацию: R || L'.

        Args:
            block_in (str): Входной блок длиной 8 символов.
            key_in (str): Раундовый ключ длиной 16 символов.

        Returns:
            str: Результат раунда — блок длиной 8 символов.

        Note:
            - Обратная операция выполняется функцией inv_routine_feistel.
            - Структура обеспечивает обратимость без требования обратимости функции F.
        """
        left = block_in[0 : 4]
        right = block_in[4 : 8]
        tmp = self.frw_s_caesar_m(right, key_in)
        left = self.add_text(tmp, left)
        out = right + left
        return out

    def inv_routine_feistel(self, block_in, key_in):
        """
        Выполняет обратный раунд функции Фейстеля для восстановления 8-символьного блока.

        Алгоритм:
        1. Разделяет входной блок на левую (предыдущая R) и правую (предыдущая L') половины.
        2. Применяет нелинейную функцию F = frw_s_caesar_m(L, key_in) к левой половине.
        3. Восстанавливает исходную правую половину: R = R' ⊖ F (вычитание по модулю 32).
        4. Формирует выходной блок как конкатенацию: R || L.

        Args:
            block_in (str): Блок длиной 8 символов (результат прямого раунда).
            key_in (str): Раундовый ключ длиной 16 символов (тот же, что при шифровании).

        Returns:
            str: Восстановленный блок длиной 8 символов.

        Note:
            - Порядок половин на входе: [старая правая] + [новая левая].
            - Использует ту же функцию frw_s_caesar_m, что и прямой раунд (свойство Фейстеля).
        """
        l = len(block_in)
        left =  block_in[0 : l // 2]
        right = block_in[l // 2 : l]
        tmp = self.frw_s_caesar_m(left, key_in)
        right = self.sub_text(right, tmp)
        out = right + left
        return out

    def bit_swap(self, block_in):
        """
        Выполняет побитовую перестановку: меняет местами соседние биты в первом 4-символьном подблоке.

        Алгоритм:
        1. Преобразует первые 4 символа блока в 20-битную бинарную строку.
        2. Для каждой пары бит (2i, 2i+1), где i=0..9, меняет их местами.
        3. Преобразует модифицированную битовую строку обратно в 4 символа.
        4. Конкатенирует результат с неизменённой второй половиной блока (символы 4-7).

        Args:
            block_in (str): Входной блок длиной 8 символов.

        Returns:
            str: Блок длиной 8 символов с переставленными битами в первой половине.

        Note:
            - Операция обратима: bit_swap(bit_swap(x)) == x.
            - Применяется только к первым 4 символам; вторая половина остаётся без изменений.
        """
        b = list(self.block2bin(block_in[0 : 4]))
        for i in range(10):
            t = b[2 * i]
            b[2 * i] = b[2 * i + 1]
            b[2 * i + 1] = t
        b = "".join(b)
        block_out = self.bin2block(b) + block_in[4 : 8]
        return block_out

    def bit_shift(self, block_in):
        """
        Выполняет циклический сдвиг битов влево на 1 позицию в первом 4-символьном подблоке.

        Алгоритм:
        1. Преобразует первые 4 символа в 20-битную бинарную строку.
        2. Сохраняет старший бит (позиция 19).
        3. Сдвигает все биты на одну позицию вправо по индексу (бит i → позиция i+1).
        4. Записывает сохранённый старший бит в младшую позицию (индекс 0).
        5. Преобразует результат обратно в 4 символа и конкатенирует с неизменённой второй половиной.

        Args:
            block_in (str): Входной блок длиной 8 символов.

        Returns:
            str: Блок длиной 8 символов со сдвинутыми битами в первой половине.

        Note:
            - Циклический сдвиг: бит, "вышедший" за левый край, возвращается справа.
            - Обратная операция: bit_shift_r.
        """
        b = list(self.block2bin(block_in[0 : 4]))
        t = b[19]
        for i in range(19, 0, -1):
            b[i] = b[i-1]
        b[0] = t
        b = "".join(b)
        block_out = self.bin2block(b) + block_in[4 : 8]
        return block_out

    def bit_shift_r(self, block_in):
        """
        Выполняет циклический сдвиг битов вправо на 1 позицию в первом 4-символьном подблоке.

        Алгоритм:
        1. Преобразует первые 4 символа в 20-битную бинарную строку.
        2. Сохраняет младший бит (позиция 0).
        3. Сдвигает все биты на одну позицию влево по индексу (бит i → позиция i-1).
        4. Записывает сохранённый младший бит в старшую позицию (индекс 19).
        5. Преобразует результат обратно в 4 символа и конкатенирует с неизменённой второй половиной.

        Args:
            block_in (str): Входной блок длиной 8 символов.

        Returns:
            str: Блок длиной 8 символов со сдвинутыми битами в первой половине.

        Note:
            - Является обратной операцией к bit_shift.
            - Инвариант: bit_shift_r(bit_shift(x)) == x для любого 8-символьного блока.
        """
        b = list(self.block2bin(block_in[0 : 4]))
        t = b[0]
        for i in range(19):
            b[i] = b[i+1]
        b[19] = t
        b = "".join(b)
        block_out = self.bin2block(b) + block_in[4 : 8]
        return block_out

    def frw_inner_feistel(self, block_in, key_in, r_in):
        """
        Выполняет прямое преобразование внутреннего цикла Фейстеля.

        Алгоритм:
        1. Применяет предварительное перемешивание: frw_p_scitala → bit_swap.
        2. Выполняет r_in итераций основного цикла:
           - Раунд Фейстеля: frw_routine_feistel с ключом key_in
           - Побитовый сдвиг влево: bit_shift
        3. Применяет финальное перемешивание: bit_swap → frw_p_scitala.

        Args:
            block_in (str): Входной блок длиной 8 символов.
            key_in (str): Раундовый ключ длиной 16 символов.
            r_in (int): Количество итераций внутреннего цикла (рекомендуется ≥ 2).

        Returns:
            str: Зашифрованный блок длиной 8 символов.

        Note:
            - Пред- и пост-обработка (Scytale + bit_swap) усиливают диффузию.
            - Обратная операция: inv_inner_feistel с тем же key_in и r_in.
        """
        tmp = self.bit_swap(self.frw_p_scitala(block_in))
        for i in range(r_in):
            tmp = self.frw_routine_feistel(tmp, key_in)
            tmp = self.bit_shift(tmp)
        out = self.frw_p_scitala(self.bit_swap(tmp))
        return out

    def inv_inner_feistel(self, block_in, key_in, r_in):
        """
        Выполняет обратное преобразование внутреннего цикла Фейстеля.

        Алгоритм (в порядке, обратном прямому шифрованию):
        1. Применяет предварительное перемешивание: bit_swap → inv_p_scitala.
        2. Выполняет r_in итераций в обратном порядке (от r_in-1 до 0):
           - Побитовый сдвиг вправо: bit_shift_r
           - Обратный раунд Фейстеля: inv_routine_feistel с ключом key_in
        3. Применяет финальное перемешивание: bit_swap → inv_p_scitala.

        Args:
            block_in (str): Зашифрованный блок длиной 8 символов.
            key_in (str): Раундовый ключ длиной 16 символов (тот же, что при шифровании).
            r_in (int): Количество итераций (должно совпадать с прямым шифрованием).

        Returns:
            str: Расшифрованный блок длиной 8 символов.

        Note:
            - Критически важно выполнять итерации в обратном порядке.
            - Инвариант: inv_inner_feistel(frwd_inner_feistel(x, k, r), k, r) == x.
        """
        tmp = self.bit_swap(self.inv_p_scitala(block_in))
        for i in range(r_in - 1, -1, -1):
            tmp = self.bit_shift_r(tmp)
            tmp = self.inv_routine_feistel(tmp, key_in)
        out = self.inv_p_scitala(self.bit_swap(tmp))
        return out

    def round_feistel(self, block_in, key_in):
        """
        Выполняет полный раунд сети Фейстеля для 16-символьного блока.

        Алгоритм:
        1. Разделяет входной блок на левую (L, 8 символов) и правую (R, 8 символов) половины.
        2. Применяет внутреннюю функцию Фейстеля к правой половине: F = frw_inner_feistel(R, key_in, r_in=2).
        3. Обновляет левую половину: L' = L ⊕ F (побитовое XOR через block_xor).
        4. Формирует выходной блок как конкатенацию: R || L'.

        Args:
            block_in (str): Входной блок длиной 16 символов.
            key_in (str): Раундовый ключ длиной 64 символа.

        Returns:
            str: Результат раунда — блок длиной 16 символов.

        Note:
            - Внутренний цикл выполняется с фиксированным r_in=2.
            - Обратимость обеспечивается структурой Фейстеля без требования обратимости F.
        """
        left = block_in[0:8]
        right = block_in[8:16]
        tmp = self.frw_inner_feistel(right, key_in, 2)
        left =self.block_xor(tmp, left)
        out =   right + left
        return out

    def swap_blocks(self, block_in):
        """
        Меняет местами левую и правую половины 16-символьного блока.

        Алгоритм:
        1. Разделяет блок на две части по 8 символов: left = [0:8], right = [8:16].
        2. Возвращает конкатенацию: right + left.

        Args:
            block_in (str): Входной блок длиной 16 символов.

        Returns:
            str: Блок длиной 16 символов с переставленными половинами.

        Note:
            - Операция является инволюцией: swap_blocks(swap_blocks(x)) == x.
            - Используется в инвертированной сети Фейстеля для корректного порядка раундов.
        """
        left = block_in[0 : 8]
        right = block_in[8 : 16]
        out = right + left
        return out

    def frw_feistel(self, block_in, keys_in, r_in):
        """
        Выполняет прямое шифрование на основе сети Фейстеля.

        Алгоритм:
        1. Применяет начальное whitening: блок ⊕ K₀ (через block_xor).
        2. Выполняет r_in раундов:
           - На каждом раунде применяет round_feistel с соответствующим ключом Kᵢ.
        3. Применяет финальное whitening: результат ⊕ Kₙ₊₁.

        Args:
            block_in (str): Открытый текст — блок длиной 16 символов.
            keys_in (list[str]): Список раундовых ключей [K₀, K₁, ..., Kₙ₊₁] длиной 64 символа каждый.
            r_in (int): Количество раундов шифрования.

        Returns:
            str: Зашифрованный блок длиной 16 символов.

        Note:
            - Требуется (r_in + 2) ключей: для initial/final whitening и r_in раундов.
            - Ключи должны быть сгенерированы функцией produce_round_keys.
            - Обратная операция: inv_feistel с тем же набором ключей.
        """
        key_set = keys_in
        block = self.block_xor(block_in, key_set[0])
        for i in range(1, r_in + 1):
            block = self.round_feistel(block, key_set[i])
        out = self.block_xor(block, key_set[r_in + 1])
        return out

    def inv_feistel(self, block_in, keys_in, r_in):
        """
        Выполняет обратное шифрование (расшифрование) на основе сети Фейстеля.

        Алгоритм (в порядке, обратном прямому шифрованию):
        1. Применяет обратное финальное whitening: блок ⊕ Kₙ₊₁.
        2. Меняет половины блока местами (swap_blocks) для коррекции порядка.
        3. Выполняет r_in раундов в обратном порядке (от r_in до 1):
           - Применяет round_feistel (та же функция, что при шифровании) с ключом Kᵢ.
        4. Меняет половины обратно (swap_blocks).
        5. Применяет обратное начальное whitening: результат ⊕ K₀.

        Args:
            block_in (str): Шифротекст — блок длиной 16 символов.
            keys_in (list[str]): Список раундовых ключей [K₀, K₁, ..., Kₙ₊₁] (тот же, что при шифровании).
            r_in (int): Количество раундов (должно совпадать с прямым шифрованием).

        Returns:
            str: Расшифрованный блок (открытый текст) длиной 16 символов.

        Note:
            - Использует ту же функцию round_feistel, что и шифрование (свойство сети Фейстеля).
            - Ключи применяются в обратном порядке, кроме whitening-ключей K₀ и Kₙ₊₁.
            - Инвариант: inv_feistel(frwd_feistel(x, K, r), K, r) == x.
        """
        key_set = keys_in
        block = self.block_xor(block_in, key_set[r_in + 1])
        block = self.swap_blocks(block)
        for i in range(r_in, 0, -1):
            block = self.round_feistel(block, key_set[i])
        block = self.swap_blocks(block)
        out = self.block_xor(block, key_set[0])
        return out
