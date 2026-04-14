from alphabet_cipher import AlphabetCipher


cipher = AlphabetCipher()
print("-" * 30 + "Простые операции" + "-" * 50)
print('Символ "О" в номер:', cipher.get_number_by_symbol("О"))
print('Символ "Ж" в номер:', cipher.get_number_by_symbol("Ж"))
print('Номер 7 в символ:', cipher.get_symbol_by_number(7))
print('Номер 14 в символ:', cipher.get_symbol_by_number(14))
print()

print("-" * 30 + "Операции с текстом" + "-" * 50)
list_indices = [cipher.get_number_by_symbol(elem) for elem in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ_"]
print('Текст алфавита в массив номеров:', *list_indices)
string_alph = "".join([cipher.get_symbol_by_number(elem) for elem in list_indices])
print('Массив номеров в текст алфавита:', string_alph)
print('Сложение символов: Я + Ж = ', cipher.add_symbols("Я", "Ж"))
print('Вычитание символов: Е - Ж = ', cipher.subtract_symbols("Е", "Ж"))
TT1 = "ЕЖИК"
TT2 = "В_ТУМАНЕ"
TT3 = "БАРОН"
TT4 = "ВАРАН"
TT5 = cipher.add_text(TT1, TT2)
TT6 = cipher.sub_text(TT3, TT4)
print("Сложение текста: ЕЖИК + В_ТУМАНЕ =", TT5)
print("Вычитание текста: БАРОН - ВАРАН =", TT6)
print("Сложение текста: Я__Н_ + ВАРАН =", cipher.add_text(TT6, TT4))
print("Вычитание текста: ИЖЬЯМАНЕ - В_ТУМАНЕ =", cipher.sub_text(TT5, TT2))
print("Вычитание текста: ИЖЬЯМАНЕ - ЕЖИК =", cipher.sub_text(TT5, TT1))
print()

print("-" * 30 + "Простой шифр Цезаря" + "-" * 50)
IN = "ОЛОЛО_КРИНЖ"
K1 = "_"
K2 = "Х"
caesar_k1 = cipher.frw_caesar(IN, K1)
print(f"Перевод {IN} простым шифром Цезаря с ключом {K1} :", caesar_k1)
caesar_k2 = cipher.frw_caesar(IN, K2)
print(f"Перевод {IN} простым шифром Цезаря с ключом {K2} :", caesar_k2)
inv1 = cipher.inv_caesar(caesar_k1, K1)
print(f"Обратный перевод {caesar_k1} простого шифра Цезаря с ключом {K1} :", inv1)
inv2 = cipher.inv_caesar(caesar_k2, K2)
print(f"Обратный перевод {caesar_k2} простого шифра Цезаря с ключом {K2} :", inv2)
print()

print("-" * 30 + "Полиалфавитный шифр Цезаря" + "-" * 50)
IN = "ОЛОЛО_КРИНЖ"
K1 = "Х"
K2 = "ПАНТЕОН"
poly_caesar_k1 = cipher.frw_poly_caesar(IN, K1)
print(f"Перевод {IN} полиалфавитным шифром Цезаря с ключом {K1} :", poly_caesar_k1)
poly_caesar_k2 = cipher.frw_poly_caesar(IN, K2)
print(f"Перевод {IN} полиалфавитным шифром Цезаря с ключом {K2} :", poly_caesar_k2)
poly_inv1 = cipher.inv_poly_caesar(poly_caesar_k1, K1)
print(f"Обратный перевод {poly_caesar_k1} полиалфавитного шифра Цезаря с ключом {K1} :", poly_inv1)
poly_inv2 = cipher.inv_poly_caesar(poly_caesar_k2, K2)
print(f"Обратный перевод {poly_caesar_k2} полиалфавитного шифра Цезаря с ключом {K2} :", poly_inv2)
print()

print("-" * 30 + "Шифр Цезаря с S-блоками" + "-" * 50)
K1 = "ХОРОШО_БЫТЬ_ВАМИ"
K2 = "ЧЕРНОВОЙ_АХИЛЛЕС"
IN1 = "БЛОК"
IN2 = "ВЛОГ"
out11 = cipher.frw_S_caesar(IN1, K1)
out21 = cipher.frw_S_caesar(IN1, K2)
out12 = cipher.frw_S_caesar(IN2, K1)
out22 = cipher.frw_S_caesar(IN2, K2)
print(f"Перевод {IN1} шифром Цезаря c S-блоком с ключом {K1} :", out11)
print(f"Перевод {IN1} шифром Цезаря c S-блоком  с ключом {K2} :", out21)
print(f"Перевод {IN2} шифром Цезаря c S-блоком с ключом {K1} :", out12)
print(f"Перевод {IN2} шифром Цезаря c S-блоком  с ключом {K2} :", out22)
INr11 = cipher.inv_S_caesar(out11, K1)
INr21 = cipher.inv_S_caesar(out21, K2)
INr12 = cipher.inv_S_caesar(out12, K1)
INr22 = cipher.inv_S_caesar(out22, K2)
print(f"Обратный перевод {out11} шифра Цезаря c S-блоком с ключом {K1} :", INr11)
print(f"Обратный перевод {out21} шифра Цезаря c S-блоком с ключом {K2} :", INr21)
print(f"Обратный перевод {out12} шифра Цезаря c S-блоком с ключом {K1} :", INr12)
print(f"Обратный перевод {out22} шифра Цезаря c S-блоком с ключом {K2} :", INr22)
INe11 = cipher.inv_S_caesar(out11, K2)
INe21 = cipher.inv_S_caesar(out21, K1)
INe12 = cipher.inv_S_caesar(out12, K2)
INe22 = cipher.inv_S_caesar(out22, K1)
print(f"Обратный перевод {out11} шифра Цезаря c S-блоком с ключом {K2} :", INe11)
print(f"Обратный перевод {out21} шифра Цезаря c S-блоком с ключом {K1} :", INe21)
print(f"Обратный перевод {out12} шифра Цезаря c S-блоком с ключом {K2} :", INe12)
print(f"Обратный перевод {out22} шифра Цезаря c S-блоком с ключом {K1} :", INe22)
print()

print("-" * 30 + "Дополнительная операция диффузии" + "-" * 50)
K1 = "ХОРОШО_ВЫТЬ_ВАМИ"
K2 = "ХОРОШО_БЫТЬ_ВАМИ"
K3 = "ХОРОШО_ВЫТЬ_БАМИ"
IN1 = "БЛОК"
IN2 = "БРОК"
OUT1 = cipher.frw_merge_block(IN1, K1)
OUT2 = cipher.frw_merge_block(IN2, K1)
OUT3 = cipher.frw_merge_block(IN1, K2)
OUT4 = cipher.frw_merge_block(IN2, K2)
print(f"Перевод {IN1} шифром Цезаря c диффузией с ключом {K1} :", OUT1)
print(f"Перевод {IN2} шифром Цезаря c диффузией с ключом {K1} :", OUT2)
print(f"Перевод {IN1} шифром Цезаря c диффузией с ключом {K2} :", OUT3)
print(f"Перевод {IN2} шифром Цезаря c диффузией с ключом {K2} :", OUT4)
INV1 = cipher.inv_merge_block(OUT1, K1)
INV2 = cipher.inv_merge_block(OUT2, K1)
INV3 = cipher.inv_merge_block(OUT3, K1)
INV4 = cipher.inv_merge_block(OUT4, K1)
print(f"Обратный перевод {OUT1} шифра Цезаря c диффузией с ключом {K1} :", INV1)
print(f"Обратный перевод {OUT2} шифра Цезаря c диффузией с ключом {K1} :", INV2)
print(f"Обратный перевод {OUT3} шифра Цезаря c диффузией с ключом {K1} :", INV3)
print(f"Обратный перевод {OUT4} шифра Цезаря c диффузией с ключом {K1} :", INV4)
INV5 = cipher.inv_merge_block(OUT1, K2)
INV6 = cipher.inv_merge_block(OUT2, K2)
INV7 = cipher.inv_merge_block(OUT3, K2)
INV8 = cipher.inv_merge_block(OUT4, K2)
print(f"Обратный перевод {OUT1} шифра Цезаря c диффузией с ключом {K2} :", INV5)
print(f"Обратный перевод {OUT2} шифра Цезаря c диффузией с ключом {K2} :", INV6)
print(f"Обратный перевод {OUT3} шифра Цезаря c диффузией с ключом {K2} :", INV7)
print(f"Обратный перевод {OUT4} шифра Цезаря c диффузией с ключом {K2} :", INV8)
INV9 = cipher.inv_merge_block(OUT1, K3)
INV10 = cipher.inv_merge_block(OUT2, K3)
INV11 = cipher.inv_merge_block(OUT3, K3)
INV12 = cipher.inv_merge_block(OUT4, K3)
print(f"Обратный перевод {OUT1} шифра Цезаря c диффузией с ключом {K3} :", INV9)
print(f"Обратный перевод {OUT2} шифра Цезаря c диффузией с ключом {K3} :", INV10)
print(f"Обратный перевод {OUT3} шифра Цезаря c диффузией с ключом {K3} :", INV11)
print(f"Обратный перевод {OUT4} шифра Цезаря c диффузией с ключом {K3} :", INV12)
print()

print("-" * 30 + "Модификация S-блоков" + "-" * 50)
OUT1 = cipher.frw_s_caesar_m(IN1, K1)
INV1 = cipher.inv_s_caesar_m(OUT1, K1)
print(f"Перевод {IN1} шифром Цезаря c модификацией S-блоков с ключом {K1} :", OUT1)
print(f"Обратный перевод {OUT1} шифра Цезаря c модификацией S-блоков с ключом {K1} :", INV1)