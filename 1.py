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

    def encrypt(self, text: str):
        """
        Кодирует текстовую строку в список 5-битных бинарных кодов.

        Args:
            text: Исходная строка для шифрования. Автоматически приводится к верхнему регистру.

        Returns:
            Список строк, где каждый элемент — 5-битный бинарный код соответствующего символа.

        Raises:
            KeyError: Если в тексте встречается неподдерживаемый символ.
        """
        res = []
        for char in text.upper():
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

    def frw_cesar(self, text: str, key: str):
        """
        Шифрует текст с использованием шифра Цезаря с заданным ключом-символом.

        Алгоритм:
        1. Берет первый символ из ключа
        2. Для каждого символа входного текста складывает его с ключом
           по модулю 32 (используя add_symbols)
        3. Возвращает зашифрованный текст

        Args:
            text: Исходный текст для шифрования
            key: Ключ - символ для сдвига (используется первый символ)

        Returns:
            Зашифрованный текст (str)
        """
        out = ""
        key_1 = key[0]
        for i in range(len(text)):
            out += self.add_symbols(text[i] , key_1)
        return out

    def inv_cesar(self, text: str, key: str) -> str:
        """
        Расшифровывает текст, зашифрованный шифром Цезаря, с использованием заданного ключа-символа.

        Алгоритм:
        1. Берет первый символ из ключа
        2. Для каждого символа входного текста вычитает ключ из символа
           по модулю 32 (используя subtract_symbols)
        3. Возвращает расшифрованный текст

        Args:
            text: Зашифрованный текст для расшифровки
            key: Ключ - символ, использованный при шифровании (используется первый символ)

        Returns:
            Расшифрованный текст (str)
        """
        out = ""
        key_1 = key[0]
        for i in range(len(text)):
            out += self.subtract_symbols(text[i], key_1)
        return out

    def frw_poly_cesar(self, text: str, key: str) -> str:
        """
        Шифрует текст с использованием полиалфавитного шифра Цезаря.

        Алгоритм:
        1. Для каждого символа текста вычисляется позиция в ключе (по модулю длины ключа)
        2. Накопительным итогом складываются символы ключа
        3. Каждый символ текста складывается с текущим значением накопленной суммы ключа

        Args:
            text: Исходный текст для шифрования
            key: Ключ - строка символов

        Returns:
            Зашифрованный текст (str)
        """
        out = ""
        t_k = "_"
        key_len = len(key)
        for i in range(len(text)):
            t_k = self.add_symbols(t_k, key[i % key_len])
            out += self.add_symbols(text[i], t_k)
        return out

    def inv_poly_cesar(self, text: str, key: str) -> str:
        """
        Расшифровывает текст, зашифрованный полиалфавитным шифром Цезаря.

        Алгоритм:
        1. Инициализирует накопитель t_k значением '_' (0).
        2. Проходит по зашифрованному тексту.
        3. На каждом шаге обновляет t_k, добавляя к нему символ ключа (циклически).
        4. Расшифровывает символ: вычитает текущее t_k из символа шифротекста.

        Args:
            text: Зашифрованный текст.
            key: Ключ, использованный при шифровании.

        Returns:
            Расшифрованный исходный текст (str).
        """
        out = ""
        t_k = "_"
        key_len = len(key)

        for i in range(len(text)):
            t_k = self.add_symbols(t_k, key[i % key_len])
            out += self.subtract_symbols(text[i], t_k)

        return out


cipher = AlphabetCipher()



