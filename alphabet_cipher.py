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
        # Вектор коэффициентов для нелинейного преобразования ключа
        transform_coefficients = [1, -1, 1, 2, -2, 1, 1, 3, -1, 2]
        # Инициализация производного ключа нулевыми значениями ('_' = 0)
        derived_key = "____"
        # Расширение ключа: дублирование для возможности извлечения подстрок со сдвигом
        extended_key = key_input + key_input
        # Основной цикл генерации: 8 итераций для накопления нелинейных преобразований
        for i in range(8):
            # Вычисление начальной позиции для извлечения 4-символьной подстроки
            # Сдвиг на 2 позиции на каждой итерации (0, 2, 4, 6, 8, 10, 12, 14)
            start_position = i * 2
            # Извлечение подстроки длиной 4 символа из расширенного ключа
            key_substring = extended_key[start_position: start_position + 4]
            # Преобразование символов подстроки в числовые индексы (0-31)
            substring_indices = [self.get_number_by_symbol(char) for char in key_substring]
            # Массив для хранения преобразованных индексов
            transformed_indices = []
            # Нелинейное преобразование каждого из 4-х символов подстроки
            for k in range(4):
                # Вычисление индекса для доступа к вектору коэффициентов
                # Формула: (2 * i + k) mod 10
                coeff_index = (2 * i + k) % 10
                # Получение коэффициента из вектора и значения из подстроки
                coefficient = transform_coefficients[coeff_index]
                symbol_index = substring_indices[k]
                # Формула нелинейного преобразования: (64 + k + C[x] * B[k]) mod 32
                # 64 гарантирует положительность перед взятием mod
                transformed_index = (64 + k + coefficient * symbol_index) % 32
                transformed_indices.append(transformed_index)
            # Преобразование преобразованных индексов обратно в строку символов
            transformed_chunk = "".join([self.get_symbol_by_number(n) for n in transformed_indices])
            # Накопление результата: сложение с текущим derived_key по модулю 32
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
        # Проверка корректности входных данных
        if len(text_input) != 4 or len(key_input) != 16:
            return "input_error"
        # Инициализация выходного блока входным открытым текстом
        ciphertext_block = text_input
        # Генерация производного ключа (4 символа) из основного ключа (16 символов)
        # Используется нелинейное преобразование с вектором коэффициентов
        working_key = self._generate_s_key(key_input)
        # Применение полиалфавитного шифра Цезаря с накопительным сложением
        # Каждый символ текста складывается с накопительной суммой символов ключа
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
        # Проверка корректности входных данных
        if len(text_input) != 4 or len(key_input) != 16:
            return "input_error"
        # Инициализация выходного блока зашифрованным текстом
        plaintext_block = text_input
        # Генерация того же производного ключа (детерминированный процесс)
        # При одинаковом KEY_IN получится идентичный working_key
        working_key = self._generate_s_key(key_input)
        # Применение обратного полиалфавитного шифра Цезаря
        # Накопительное вычитание символов ключа из шифротекста
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
        # Проверка корректности входных данных
        if len(text_input) != 4 or len(key_input) != 16:
            return "input_error"
        # Преобразование ключа в массив числовых индексов (0-31)
        key_indices = [self.get_number_by_symbol(c) for c in key_input]
        # Вычисление контрольной суммы (permutation seed)
        # Знакопеременное сложение: +key[0] - key[1] + key[2] - key[3] ...
        # Результат по модулю 24 (так как 4! = 24 возможных перестановок)
        permutation_seed = 0
        for i in range(16):
            # Чередование знака: чётные позиции (+), нечётные (-)
            coefficient_sign = 1 if i % 2 == 0 else -1
            permutation_seed = (48 + permutation_seed + coefficient_sign * key_indices[i]) % 24
        # Генерация перестановки индексов [0,1,2,3] на основе seed
        # Используется модифицированный алгоритм Фишера-Йетса
        shuffle_indices = [0, 1, 2, 3]
        for k in range(3): # 3 шага для перестановки 4 элементов
            # Вычисление позиции для обмена
            swap_offset = permutation_seed % (4 - k)
            # Обновление seed для следующего шага (целочисленное деление)
            permutation_seed = (permutation_seed - swap_offset) // (4 - k)
            # Обмен элементов местами
            shuffle_indices[k], shuffle_indices[k + swap_offset] = shuffle_indices[k + swap_offset], shuffle_indices[k]
        # Преобразование входного блока в массив числовых индексов
        block_indices = [self.get_number_by_symbol(symbol) for symbol in text_input]
        # Диффузия - смешивание символов блока
        # Каждый символ складывается с другим в порядке, заданном перестановкой
        for j in range(4):
            # Индексы символов для операции сложения
            source_idx = shuffle_indices[(1 + j) % 4]
            target_idx = shuffle_indices[j % 4]
            # Циклическое сложение по модулю 32
            block_indices[source_idx] = (block_indices[source_idx] + block_indices[target_idx]) % 32
        # Преобразование массива индексов обратно в текстовую строку
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
        # Проверка корректности входных данных
        if len(text_input) != 4 or len(key_input) != 16:
            return "input_error"
        # Преобразование ключа в массив числовых индексов
        key_indices = [self.get_number_by_symbol(c) for c in key_input]
        # Вычисление той же контрольной суммы (permutation seed)
        # Знакопеременное сложение (идентично прямому алгоритму)
        permutation_seed = 0
        for i in range(16):
            coefficient_sign = 1 if i % 2 == 0 else -1
            permutation_seed = (48 + permutation_seed + coefficient_sign * key_indices[i]) % 24
        # Генерация той же перестановки индексов
        shuffle_indices = [0, 1, 2, 3]
        for k in range(3):
            swap_offset = permutation_seed % (4 - k)
            permutation_seed = (permutation_seed - swap_offset) // (4 - k)
            shuffle_indices[k], shuffle_indices[k + swap_offset] = shuffle_indices[k + swap_offset], shuffle_indices[k]
        # Преобразование входного блока в массив числовых индексов
        block_indices = [self.get_number_by_symbol(c) for c in text_input]
        # Обратная диффузия - восстановление исходного блока
        # Цикл идёт в обратном порядке (3, 2, 1, 0)
        # и используется вычитание вместо сложения
        for j in range(3, -1, -1):
            source_idx = shuffle_indices[(1 + j) % 4]
            target_idx = shuffle_indices[j % 4]
            # Циклическое вычитание по модулю 32
            # Добавление 32 гарантирует положительность результата
            block_indices[source_idx] = (32 + block_indices[source_idx] - block_indices[target_idx]) % 32
        # Преобразование массива индексов обратно в текстовую строку
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
        # Первичное перемешивание (диффузия)
        temp_block = self.frw_merge_block(text_input, key_input)
        # Нелинейная подстановка через S-блок (конфузия)
        temp_block = self.frw_S_caesar(temp_block, key_input)
        # Вторичное перемешивание (диффузия)
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
        # Обратное вторичному перемешиванию
        temp_block = self.inv_merge_block(text_input, key_input)
        # Обратная нелинейная подстановка через S-блок
        temp_block = self.inv_S_caesar(temp_block, key_input)
        # Обратное первичному перемешиванию
        plaintext_block = self.inv_merge_block(temp_block, key_input)
        return plaintext_block


cipher = AlphabetCipher()
