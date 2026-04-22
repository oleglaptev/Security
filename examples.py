from alphabet_cipher import AlphabetCipher

cipher = AlphabetCipher()
'''
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
print()

print("-" * 30 + "Ядро с функцией шифрования" + "-" * 50)
IN1 = "ХОРОШО_БЫТЬ_ВАМИ"
IN2 = "КЬЕРКЕГОР_ПРОПАЛ"
core_Caesar1 = cipher.core_Caesar(IN1, IN2)
core_Caesar2 = cipher.core_Caesar(IN2, IN1)
print(f"Сложение {IN1} и {IN2} ядром с шифром Цезаря :", core_Caesar1)
print(f"Сложение {IN2} и {IN1} ядром с шифром Цезаря :", core_Caesar2)
print()

print("-" * 30 + "Confuse" + "-" * 50)
IN = "ХОРОШО_БЫТЬ_ВАМИ"
IN1 = "КЬЕРКЕГОР_ПРОПАЛ"
IN2 = "ХОРОШО_ПРОБРОСИЛ"
confuse1 = cipher.confuse(IN, IN1)
confuse2 = cipher.confuse(IN, IN2)
confuse3 = cipher.confuse(IN, IN)
print(f"Confuse {IN} и {IN1}:", confuse1)
print(f"Confuse {IN} и {IN2}:", confuse2)
print(f"Confuse {IN} и {IN}:", confuse3)
print()
print("-" * 30 + "C-блок" + "-" * 50)
IN1 = ["ХОРОШО_БЫТЬ_ВАМИ"]
IN2 = ["ХОРОШО_БЫТЬ_ВАМИ",
       "________________",
       "________________",
       "________________"]
IN3 = ["ХОРОШО_БЫТЬ_ВАМИ",
       "________А_______"]
IN4 = ["ХОРОШО_БЫТЬ_ВАМИ",
       "___А____________"]
IN5 = ["ХОРОШО_БЫТЬ_ВАМИ", "КЬЕРКЕГОР_ПРОПАЛ"]
IN6 = ["ЧЕРНЫЙ_АББАТ_ПОЛ", "ХОРОШО_БЫТЬ_ВАМИ", "КЬЕРКЕГОР_ПРОПАЛ"]
IN7 = ["______А_________",
       "________________",
       "________________",
       "________________"]
IN8 = ["________________",
       "________________",
       "________________",
       "________________"]
IN9 = ["_____А__________",
       "___________А____",
       "_А______________",
       "____________А___"]
outlen = "16"
c = cipher.C_block(IN1, outlen)
print(f"С-блок {IN1} с длиной {outlen}:", c)
c = cipher.C_block(IN2, outlen)
print(f"С-блок {IN2} с длиной {outlen}:", c)
c = cipher.C_block(IN3, outlen)
print(f"С-блок {IN3} с длиной {outlen}:", c)
c = cipher.C_block(IN4, outlen)
print(f"С-блок {IN4} с длиной {outlen}:", c)
outlen = "8"
c = cipher.C_block(IN1, outlen)
print(f"С-блок {IN1} с длиной {outlen}:", c)
c = cipher.C_block(IN2, outlen)
print(f"С-блок {IN2} с длиной {outlen}:", c)
c = cipher.C_block(IN3, outlen)
print(f"С-блок {IN3} с длиной {outlen}:", c)
c = cipher.C_block(IN4, outlen)
print(f"С-блок {IN4} с длиной {outlen}:", c)
outlen = "16"
c = cipher.C_block(IN5, outlen)
print(f"С-блок {IN5} с длиной {outlen}:", c)
outlen = "8"
c = cipher.C_block(IN5, outlen)
print(f"С-блок {IN5} с длиной {outlen}:", c)
outlen = "5"
c = cipher.C_block(IN5, outlen)
print(f"С-блок {IN5} с длиной {outlen}:", c)
outlen = "16"
c = cipher.C_block(IN6, outlen)
print(f"С-блок {IN6} с длиной {outlen}:", c)
outlen = "8"
c = cipher.C_block(IN6, outlen)
print(f"С-блок {IN6} с длиной {outlen}:", c)
outlen = "4"
c = cipher.C_block(IN6, outlen)
print(f"С-блок {IN6} с длиной {outlen}:", c)
outlen = "16"
c = cipher.C_block(IN7, outlen)
A = c
print(f"С-блок {IN7} с длиной {outlen}:", c)
outlen = "8"
c = cipher.C_block(IN7, outlen)
print(f"С-блок {IN7} с длиной {outlen}:", c)
outlen = "4"
c = cipher.C_block(IN7, outlen)
print(f"С-блок {IN7} с длиной {outlen}:", c)
outlen = "16"
c = cipher.C_block(IN8, outlen)
B = c
print(f"С-блок {IN8} с длиной {outlen}:", c)
outlen = "8"
c = cipher.C_block(IN8, outlen)
print(f"С-блок {IN8} с длиной {outlen}:", c)
outlen = "4"
c = cipher.C_block(IN8, outlen)
print(f"С-блок {IN8} с длиной {outlen}:", c)
outlen = "16"
c = cipher.C_block(IN9, outlen)
C = c
print(f"С-блок {IN9} с длиной {outlen}:", c)
outlen = "8"
c = cipher.C_block(IN9, outlen)
print(f"С-блок {IN9} с длиной {outlen}:", c)
outlen = "4"
c = cipher.C_block(IN9, outlen)
print(f"С-блок {IN9} с длиной {outlen}:", c)
print(f"{A} - {C} = ", cipher.sub_text(A, C))
print(f"{A} - {B} = ", cipher.sub_text(A, B))
print(f"{B} - {C} = ", cipher.sub_text(B, C))
print()
print("-" * 30 + "Внутренние функции для губки" + "-" * 50)
state0 = [["____", "____", "____", "____", "____"],
          ["__А_", "____", "____", "____", "____"],
          ["____", "____", "____", "____", "____"],
          ["____", "____", "____", "____", "____"],
          ["____", "____", "____", "____", "____"]]
print("Состояние 0:")
print(*state0, sep="\n", end="\n")
state11 = cipher.mix_cols(state0)
print("Состояние 1:")
print(*state11, sep="\n", end="\n")
print()
state12 = cipher.shatter_blocks(state11)
print("Состояние 2:")
print(*state12, sep="\n", end="\n")
print()
state13 = cipher.shift_rows(state12)
print("Состояние 3:")
print(*state13, sep="\n", end="\n")
print()
state21 = cipher.mix_cols(state13)
print("Состояние 4:")
print(*state21, sep="\n", end="\n")
print()
state22 = cipher.shatter_blocks(state21)
print("Состояние 5:")
print(*state22, sep="\n", end="\n")
print()
state23 = cipher.shift_rows(state22)
print("Состояние 6:")
print(*state23, sep="\n", end="\n")
print()
state31 = cipher.mix_cols(state23)
print("Состояние 7:")
print(*state31, sep="\n", end="\n")
print()
state32 = cipher.shatter_blocks(state31)
print("Состояние 8:")
print(*state32, sep="\n", end="\n")
print()
state33 = cipher.shift_rows(state32)
print("Состояние 9:")
print(*state33, sep="\n", end="\n")
print()
state41 = cipher.mix_cols(state33)
print("Состояние 10:")
print(*state41, sep="\n", end="\n")
print()
state42 = cipher.shatter_blocks(state41)
print("Состояние 11:")
print(*state42, sep="\n", end="\n")
print()
state43 = cipher.shift_rows(state42)
print("Состояние 12:")
print(*state43, sep="\n", end="\n")
print()

print()
print("-" * 30 + "Губка" + "-" * 50)
state0 = [["____", "____", "____", "____", "____"],
          ["____", "____", "____", "____", "____"],
          ["____", "____", "____", "____", "____"],
          ["____", "____", "____", "____", "____"],
          ["____", "____", "____", "____", "____"]]
IN1 = "_А__"
IN2 = "ВИЛЯ"
IN3 = "ОЗЛ_"
IN4 = "___М"
print("-" * 30 + "Впитывание" + "-" * 50)
print("Состояние 0:")
print(*state0, sep="\n", end="\n")
state1 = cipher.sponge_absorb(state0, IN1)
print("Состояние 1:")
print(*state1, sep="\n", end="\n")
print()
state2 = cipher.sponge_absorb(state1, IN2)
print("Состояние 2:")
print(*state2, sep="\n", end="\n")
print()
state3 = cipher.sponge_absorb(state2, IN3)
print("Состояние 3:")
print(*state3, sep="\n", end="\n")
print()
state4 = cipher.sponge_absorb(state3, IN3)
print("Состояние 4:")
print(*state4, sep="\n", end="\n")
print()
print("-" * 30, "Выжимание", "-" * 50)
stateX = [["БЫ_Щ", "ЙЖ_Б", "ЮФ_Е", "БЫ_Щ", "ЮД_Е"],
          ["Ы_ЩБ", "Ж_БЙ", "Ф_ЕЮ", "Ы_ЩБ", "Л_ЗЗ"],
          ["Ы_ЩБ", "Ж_БЙ", "Ф_ЕЮ", "У_ЧЧ", "Д_ЕЮ"],
          ["Ы_ЩБ", "Ж_БЙ", "Ь_ЗЗ", "Ы_ЩБ", "Д_ЕЮ"],
          ["Ы_ЩБ", "____", "Ф_ЕЮ", "Ы_ЩБ", "Д_ЕЮ"]]
print("Состояние 0:")
print(*stateX, sep='\n', end="\n")
state1x = cipher.sponge_squeeze(stateX)
print("Состояние 1:")
print(state1x[0])
print(*state1x[1], sep='\n', end="\n")
print()
state2x = cipher.sponge_squeeze(state1x[1])
print("Состояние 2:")
print(state2x[0])
print(*state2x[1], sep='\n', end="\n")
print()
state3x = cipher.sponge_squeeze(state2x[1])
print("Состояние 3:")
print(state3x[0])
print(*state3x[1], sep='\n', end="\n")
print()
print("-" * 30 + "Хеш" + "-" * 50)
IN1 = "КАТЕГОРИЧЕСКИЙ_ИМПЕРАТИВ"
hash1 = cipher.SpongeFun_hash(IN1)
print(f"Хеш от {IN1}:", hash1)
print()
IN2 = "_____________________________________________________________"
hash2 = cipher.SpongeFun_hash(IN2)
print(f"Хеш от {IN2}:", hash2)
print()
IN3 = "______________________А______________________________________"
hash3 = cipher.SpongeFun_hash(IN3)
print(f"Хеш от {IN3}:", hash3)
print()
IN4 = "________А____________________________________________________"
hash4 = cipher.SpongeFun_hash(IN4)
print(f"Хеш от {IN4}:", hash4)
print()
print(f"Разница хеша от {IN2} и от {IN3}:")
print(cipher.sub_text(hash2, hash3))
print()
print(f"Разница хеша от {IN2} и от {IN4}:")
print(cipher.sub_text(hash2, hash4))
print()
IN5 = "ПЕТЯ_ПИЛ_ПИВО_В_КАЛЬЯННОЙ_И_КУРИЛ_БАМБУК_ЧЕРЕЗ_АНАНАС_ТЧК_НАСТЯ_ПИЛА_ВОДУ_И_НЕ_ПОШЛА_В_КАЛЬЯННУЮ_ЗПТ_ЧТОБЫ_ВЫСПАТЬСЯ"
IN6 = "ЗОЛОТЫЕ_ВРЕМЕНА_ПРОШЛИ_ТЧК_НАСТАЛА_ПОРА_ГРУЗИТЬ_АПЕЛЬСИНЫ_БОЧКАМИ_И_НЕ_ОГЛЯДЫВАТЬСЯ_НАЗАД_ТЧК_КОГДАТО_СНОВА_МЫ_БУДЕМ_ТАМ_ГДЕ_НАС_ЖДУТ_ТЧК"
f1 =cipher.SpongeFun_hash(IN5)
g1 =cipher.SpongeFun_hash(IN6)
print(f"Хеш от {IN5}:")
print(f1)
print(f"Хеш от {IN6}:")
print(g1)

'''
print("-" * 30 + "Вспомогательные для генераторов" + "-" * 50)
block1 = "АБВГ"
block2 = "_ЯЗЬ"
block3 = "ЯЯЯЯ"
b2n1 = cipher.block2num(block1)
b2n2 = cipher.block2num(block2)
b2n3 = cipher.block2num(block3)
print(f"{block1} в число: ", b2n1)
print(f"{block2} в число: ", b2n2)
print(f"{block3} в число: ", b2n3)
num_in = 123
den_in = 2
res = cipher.div(num_in, den_in)
print(f"Деление с отбрасыванием дробной части {num_in} на {den_in}: {res}")
n2b1 = cipher.num2block(b2n1)
n2b2 = cipher.num2block(b2n2)
n2b3 = cipher.num2block(b2n3)
print(f"{b2n1} в блок: ", n2b1)
print(f"{b2n2} в блок: ", n2b2)
print(f"{b2n3} в блок: ", n2b3)
bin1 = cipher.dec2bin(b2n1)
bin2 = cipher.dec2bin(b2n2)
bin3 = cipher.dec2bin(b2n3)
print(f"{b2n1} в двоичной СС: ", bin1)
print(f"{b2n2} в двоичной СС: ", bin2)
print(f"{b2n3} в двоичной СС: ", bin3)
dec1 = cipher.bin2dec(bin1)
dec2 = cipher.bin2dec(bin2)
dec3 = cipher.bin2dec(bin3)
print(f"{bin1} в десятичной СС: ", dec1)
print(f"{bin2} в десятичной СС: ", dec2)
print(f"{bin3} в десятичной СС: ", dec3)
print()
print("-" * 30 + "Инициализация" + "-" * 50)
IN1 = "ХОРОШО_БЫТЬ_ВАМИ"
IN2 = "________________"
IN3 = "ХОРОШО_ВЫТЬ_ВАМИ"
IN4 = "___А____________"
prng1 = cipher.initialize_PRNG(IN1)
prng2 = cipher.initialize_PRNG(IN2)
prng3 = cipher.initialize_PRNG(IN3)
prng4 = cipher.initialize_PRNG(IN4)
print(f'От "{IN1}":')
print(*prng1, sep="\n", end="\n")
print(f"От {IN2}:")
print(*prng2, sep="\n", end="\n")
print(f"От {IN3}:")
print(*prng3, sep="\n", end="\n")
print(f"От {IN4}:")
print(*prng4, sep="\n", end="\n")
print()
arg1 = "____"
res1 = cipher.block2bin(arg1)
print(f"{arg1} в бинарном виде: {res1}")
print("Обратно:", cipher.bin2block(res1))
arg2 = "___А"
res2 = cipher.block2bin(arg2)
print(f"{arg2} в бинарном виде: {res2}")
print("Обратно:", cipher.bin2block(res2))
arg3 = "__Б_"
res3 = cipher.block2bin(arg3)
print(f"{arg3} в бинарном виде: {res3}")
print("Обратно:", cipher.bin2block(res3))
arg4 = "__БГ"
res4 = cipher.block2bin(arg4)
print(f"{arg4} в бинарном виде: {res4}")
print("Обратно:", cipher.bin2block(res4))
b1 = cipher.push_reg(res1, 1)
b2 = cipher.push_reg(res2, 0)
b3 = cipher.push_reg(res3, 1)
b4 = cipher.push_reg(res4, 0)

print(f"Сдвиг с добавлением бита справа {res1}:", b1)
print(f"В символы: {cipher.bin2block(b1)}")
print(f"Сдвиг без добавления бита справа {res2}:", b2)
print(f"В символы: {cipher.bin2block(b2)}")
print(f"Сдвиг с добавлением бита справа {res3}:", b3)
print(f"В символы: {cipher.bin2block(b3)}")
print(f"Сдвиг без добавления бита справа {res4}:", b4)
print(f"В символы: {cipher.bin2block(b4)}")
taps1 = [20, 17]
taps2 = [19, 18, 17, 4]
taps3 = [18, 11]
taps4 = [20, 19, 4, 3]
taps5 = [19, 18, 17, 13]
taps6 = [18, 17, 16, 13]
res1 = cipher.taps2bin(taps1)
res2 = cipher.taps2bin(taps2)
res3 = cipher.taps2bin(taps3)
res4 = cipher.taps2bin(taps4)
res5 = cipher.taps2bin(taps5)
res6 = cipher.taps2bin(taps6)

print(f"Вентили {taps1} в двоичном виде: {res1}")
print(f"Вентили {taps2} в двоичном виде: {res2}")
print(f"Вентили {taps3} в двоичном виде: {res3}")
print(f"Вентили {taps4} в двоичном виде: {res4}")
print(f"Вентили {taps5} в двоичном виде: {res5}")
print(f"Вентили {taps6} в двоичном виде: {res6}")

seed = cipher.block2bin("КУБА")
T1 = "10010000000000000000"
s0 = cipher.LFSR_push(seed, T1)
print(f"Состояние 0: {s0}")
for i in range(1, 10):
    print(f"Состояние {i}:", cipher.LFSR_push(s0, T1))
    s0 = cipher.LFSR_push(s0, T1)

seed = cipher.block2bin("ОРИМ")
T1 = "10010000000000000000"
T2 = "01110000000000001000"
tmp1 = cipher.LFSR_next(seed, T1)
tmp2 = cipher.LFSR_next(seed, T2)
st1 = tmp1[1]
seq1 = tmp1[0]
st2 = tmp2[1]
seq2 = tmp2[0]
for i in range(10):
    print(f"Перевод в текст состояния {i} для первого набора:", cipher.bin2block(seq1))
    seq1, st1 = cipher.LFSR_next(seq1, T1)
    print(f"Перевод в текст состояния {i} для второго набора:", cipher.bin2block(seq2))
    seq2, st2 = cipher.LFSR_next(seq2, T2)

seed1 = "ЛЕРА"
seed2 = "КЛОН"
seed3 = "КОНЯ"
S1 = cipher.block2bin(seed1)
S2 = cipher.block2bin(seed2)
S3 = cipher.block2bin(seed3)
T1 = "10010000000000000000"
T2 = "01110000000000001000"
T3 = "00100000010000000000"
T = [T1, T2, T3]
S = [S1, S2, S3]
out1 = cipher.AS_LFSR_push(S, T)
print(out1)
out2 = cipher.AS_LFSR_push(out1[1], T)
print(out2)
out3 = cipher.AS_LFSR_push(out2[1], T)
print(out3)

tst = cipher.seed2bins(["ЛЕРА", "КЛОН", "КОНЯ"])
print(tst)

res = cipher.AS_LFSR_next(S, T)
for i in range(10):
    print(f"Перевод в текст состояния {i} для первого набора:",  cipher.bin2block(res[0]))
    res = cipher.AS_LFSR_next(res[1], T)

sets = [
    [cipher.taps2bin([19, 18]), cipher.taps2bin([18, 7]), cipher.taps2bin([17, 3])],
    [cipher.taps2bin([19, 18]), cipher.taps2bin([18, 7]), cipher.taps2bin([16, 14, 13, 11])],
    [cipher.taps2bin([19, 18]), cipher.taps2bin([18, 7]), cipher.taps2bin([15, 13, 12, 10])],
    [cipher.taps2bin([19, 18]), cipher.taps2bin([18, 7]), cipher.taps2bin([14, 5, 3, 1])]
]
seed = "АБВГДЕЖЗИЙКЛМНОП"
out = cipher.C_AS_LFSR_next("up", -1, seed, sets)
print(out[0])
print(*out[1], sep="\n")
