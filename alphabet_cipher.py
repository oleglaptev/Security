import copy


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
        Выполняет комплексное преобразование блока (Compression block) —
        основной узел алгоритма, объединяющий смешивание, нелинейные
        подстановки и сжатие.

        Алгоритм работы:
        1. Инициализирует массив констант C четырьмя предопределёнными
           16-символьными строками ("векторами инициализации").
        2. Проверяет, что все входные блоки имеют длину 16 символов.
        3. Поэлементно складывает каждый входной блок с соответствующей
           константой из C (операция add_text).
        4. Применяет каскад преобразований:
           a. mixinputs(C) — смешивание четырёх блоков
           b. core_Caesar(C[0], C[2]) — ядровое преобразование пары блоков
           c. core_Caesar(C[3], C[1]) — второе ядровое преобразование
           d. confuse(TMP1, TMP2) — операция конфузии результатов
           e. core_Caesar(TMP3, TMP1) — финальное ядровое преобразование
        5. Сжимает результат до размера out_size через compress().

        Args:
            IN_ARR (list[str]): Список из четырёх 16-символьных строк.
            out_size (int): Желаемый размер выходного блока (16, 8 или 4).

        Returns:
            str: Преобразованный и сжатый блок, либо "input_error"
                 при нарушении требований к входным данным.

        Note:
            Функция реализует структуру типа "сеть Фейстеля" с многократным
            применением нелинейных преобразований для обеспечения криптостойкости.
            Константы C служат для предотвращения тривиальных коллизий при
            нулевых или повторяющихся входах.
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
        1. Инициализирует X_i как "_____" (5 символов подчеркивания)
        2. Для каждого j (0..4): X_i = add_txt(X_i, a[j,i])
        3. Вычисляет q = (i+1) mod 5
        4. Для каждого j (0..4):
           - tmp = add_txt(X_i, a[j,q])
           - a[j,q] = sub_txt(tmp, a[j,i])

        Args:
            STATE: Матрица состояния 5x5

        Returns:
            list: Модифицированная матрица состояния
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

        Принимает текущее состояние матрицы 5×5 и входной блок данных,
        смешивает их с использованием нелинейного преобразования C_block,
        затем применяет раунд перестановки для обеспечения диффузии.

        Алгоритм работы:
        1. Формирует строку str1 путём конкатенации: b_in + state[0][0] + b_in + state[0][0]
        (удвоенное чередование входного блока и элемента состояния для усиления связи).
        2. Вычисляет вектор строк x[0..3] как поэлементную сумму строк матрицы состояния
        (исключая последний столбец) — это создаёт «контрольную сумму» состояния.
        3. Конкатенирует x[0..3] в единую строку str2 длиной 16 символов.
        4. Обновляет элемент state[0][0] результатом C_block([str1, str2], out_size="4"):
        - C_block выполняет смешивание, нелинейные подстановки и сжатие.
        - Результат (4 символа) записывается обратно в «якорную» ячейку состояния.
        5. Применяет три этапа перестановки состояния:
        - mix_cols: перемешивание столбцов с использованием сложения/вычитания.
        - shatter_blocks: циклический сдвиг символов в диагональных блоках.
        - shift_rows: циклический сдвиг строк матрицы состояния.
        Args:
        state (list[list[str]]): Текущее состояние — матрица 5×5,
                    где каждый элемент — строка из 4 символов.
        b_in (str): Входной блок данных длиной ровно 4 символа.

        Returns:
            list[list[str]]: Обновлённое состояние матрицы 5×5 после поглощения блока.

        Note:
            - Элемент state[0][0] выступает в роли «точки ввода» для новых данных.
            - Порядок операций (C_block → mix_cols → shatter_blocks → shift_rows)
                обеспечивает лавинный эффект: изменение одного бита входа влияет
                на всё состояние после нескольких раундов.
            - Функция не проверяет длины входных параметров — корректность
                гарантируется вызывающим кодом (SpongeFun_hash).
        """
        a = state
        str1 = b_in + a[0][0] + b_in + a[0][0]
        x = ["____"] * 4
        for i in range(4):
            for j in range(4):
                x[i] = self.add_text(x[i], a[i][j])

        str2 = x[0] + x[1] + x[2] + x[3]

        a[0][0] = self.C_block([str1, str2], "4")  # Здесь возможно нужно поменять аргументы str местами
        a = self.mix_cols(a)
        a = self.shatter_blocks(a)
        a = self.shift_rows(a)
        return a

    def sponge_squeeze(self, state):
        """
                Фаза выжимки (Squeeze) губчатой конструкции (Sponge Construction).

                Извлекает выходной блок хеша из текущего состояния, применяя
                перестановку и нелинейное преобразование для обеспечения
                криптографической стойкости выходных данных.

                Алгоритм работы:
                1. Применяет к состоянию три этапа перестановки (в том же порядке,
                   что и в absorb, но без предварительного смешивания с входом):
                   - mix_cols: перемешивание столбцов.
                   - shatter_blocks: сдвиг символов в диагональных блоках.
                   - shift_rows: сдвиг строк матрицы.
                2. Вычисляет вектор строк x[0..3] как поэлементную сумму строк матрицы
                   (исключая последний столбец) — аналогично фазе absorb.
                3. Конкатенирует x[0..3] в строку str длиной 16 символов.
                4. Пропускает str через C_block([str], out_size="4") для получения
                   4-символьного выходного блока.
                5. Возвращает кортеж: [выходной_блок, обновлённое_состояние].

                Args:
                    state (list[list[str]]): Текущее состояние — матрица 5×5,
                                             где каждый элемент — строка из 4 символов.

                Returns:
                    list: Список из двух элементов:
                        - [0] (str): Извлечённый блок хеша длиной 4 символа.
                        - [1] (list[list[str]]): Обновлённое состояние для следующей итерации.

                Note:
                    - Возврат обновлённого состояния позволяет выполнять многократную
                      выжимку для генерации хеша произвольной длины.
                    - Порядок перестановок идентичен фазе absorb, что обеспечивает
                      симметричность конструкции и упрощает криптоанализ.
                    - Использование C_block на финальном шаге добавляет нелинейность
                      и затрудняет восстановление состояния по выходным данным.
                """
        a = state
        a = self.mix_cols(a)
        a = self.shatter_blocks(a)
        a = self.shift_rows(a)
        x = ["____"] * 4
        for i in range(4):
            for j in range(4):
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
                            MSG (str): Входное сообщение для хеширования (любой длины).
                                      Допустимые символы: русский алфавит (А-Я, Ё), '_', пробел.

                        Returns:
                            str: Хеш-значение длиной 60 символов (15 блоков по 4 символа).
                                 Каждый символ принадлежит алфавиту шифра (0-31).

                        Note:
                            - Длина выхода фиксирована (60 символов) — для изменения длины
                              необходимо модифицировать количество итераций в фазе squeeze.
                            - Padding осуществляется добавлением символов '_' (нулевое значение),
                              что эквивалентно добавлению нулевых бит в бинарных хеш-функциях.
                            - Конструкция устойчива к коллизиям благодаря многократному применению
                              нелинейных преобразований (C_block, mix_cols, shatter_blocks).
                            - Для хеширования сообщений >1000 символов рекомендуется увеличить
                              размер состояния или количество раундов перестановки.
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
        for i in range(15):
            TMP = self.sponge_squeeze(state)
            out += TMP[0]
            state = TMP[1]
        return out
