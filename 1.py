class AlphabetCipher:
    def __init__(self):
        # 1. Основная база данных: Символ -> 5-битный Код
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

        # Обратный словарь: Код -> Символ
        self.code_to_symbol = {code: symbol for symbol, code in self.symbol_to_code.items()}

        # 2. Индексы (Номер 0-31)
        self.number_to_symbol = {}
        self.symbol_to_number = {}

        for symbol, code in self.symbol_to_code.items():
            # int(code, 2) переводит бинарную строку в десятичное число
            number = int(code, 2)
            self.number_to_symbol[number] = symbol
            self.symbol_to_number[symbol] = number

    def get_symbol_by_number(self, number):
        """Возвращает символ по номеру (0-31)"""
        if 0 <= number <= 31:
            return self.number_to_symbol[number]
        raise ValueError("Номер должен быть в диапазоне от 0 до 31")

    def get_number_by_symbol(self, symbol):
        """Возвращает номер (0-31) по символу"""
        if symbol in self.symbol_to_number:
            return self.symbol_to_number[symbol]
        raise ValueError(f"Символ '{symbol}' отсутствует в алфавите")

    def encrypt(self, text):
        """Шифрует текст в бинарный код"""
        res = []
        for char in text.upper():
            res.append(self.symbol_to_code[char])
        return "".join(res)

    def decrypt(self, binary_text):
        """Расшифровывает бинарный код обратно в текст"""
        symbols = []
        for i in range(0, len(binary_text), 5):
            code = binary_text[i: i + 5]
            symbols.append(self.code_to_symbol.get(code, '?'))
        return "".join(symbols)

    def add_numbers(self, num1, num2):
        """Сложение с циклическим переносом (mod 32)"""
        return (num1 + num2) % 32

    def subtract_numbers(self, num1, num2):
        """Вычитание с циклическим заимствованием (mod 32)"""
        return (num1 - num2) % 32

    def add_symbols(self, symbol1, symbol2):
        """Сложение двух символов: возвращает символ"""
        num1 = self.symbol_to_number[symbol1]
        num2 = self.symbol_to_number[symbol2]
        result_num = self.add_numbers(num1, num2)
        return self.number_to_symbol[result_num]

    def subtract_symbols(self, symbol1, symbol2):
        """Вычитание двух символов: возвращает символ"""
        num1 = self.symbol_to_number[symbol1]
        num2 = self.symbol_to_number[symbol2]
        result_num = self.subtract_numbers(num1, num2)
        return self.number_to_symbol[result_num]







