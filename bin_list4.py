#
int4 = ['{:04b}'.format(i).translate({49: 73, 48: 79}) for i in range(50)]
#
# # print(f'{int4[8::]}\n{int4[0:8]}')
# #
# print(f'{" ".join(int4[0:8])} {" ".join(int4[8::])}')
#
# def lit_inv(line:str) -> str:
#     return line.translate({73: 79, 79: 73})
#
# # print(lit_inv(int4[5]))
#
minus_index = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: -8, 9: -7, 10: -6, 11: -5, 12: -4, 13: -3, 14: -2, 15: -1}

all4 = {int4[i] :minus_index[int4.index(int4[i])] for i in range(len(minus_index))}

# print(all4[lit_inv('IOIO')])

text13 = bytearray('Объекты bytearray являются изменяемыми', encoding='utf-8')

text13[0:2], text13[-1] = b'\x4f', 0

b = 183 #'{:08b}'.format(183)

print(b:=int(b) >> 2)

print(b:=int(b) << 4)

mask = 0b11111111

print(b8 :=b & mask)

# rus_eng = ''.maketrans()

_line_ = 'Привет!'

def rus_to_eng_value(line:str) -> str:

    line.lower()

    rus_eng = {1072: 97, 1073: 98, 1094: 99, 1076: 100, 1077: 101, 1092: 102, 1075: 103, 1093: 104, 1080: 105,
               1078: 106, 1082: 107, 1083: 108, 1084: 109, 1085: 110, 1086: 111, 1087: 112, 1088: 114, 1089: 115,
               1090: 116, 1102: 117, 1074: 118, 1081: 121, 1079: 122}

    return line.translate(rus_eng)

# print(rus_to_eng_value(_line_))

_line_ = list(_line_)

def rus_to_eng_link(line:list) -> None:

    for i in range(len(line)):
            line[i] = line[i].lower()

            rus_eng = {1072: 97, 1073: 98, 1094: 99, 1076: 100, 1077: 101, 1092: 102, 1075: 103, 1093: 104, 1080: 105,
                       1078: 106, 1082: 107, 1083: 108, 1084: 109, 1085: 110, 1086: 111, 1087: 112, 1088: 114, 1089: 115,
                       1090: 116, 1102: 117, 1074: 118, 1081: 121, 1079: 122}

            line[i] = line[i].translate(rus_eng)


# print(rus_to_eng_value(line))

rus_to_eng_link((_line_))

print(''.join(_line_))

int4_values = {val:e for e,val in enumerate(int4)}

def adding_int4(value1:str, value2:str) -> str:
    int4_values = {val: e for e, val in enumerate(int4)}
    int4_answears = {e:val  for e, val in enumerate(int4)}
    sum = int4_values[value1] + int4_values[value2]
    return int4_answears[sum]


def substraction_int4(value1:str, value2:str) -> str:
    int4_values = {val: e for e, val in enumerate(int4)}
    int4_answers = {e:val  for e, val in enumerate(int4)}
    subs = int4_values[value1] - int4_values[value2]
    return int4_answers[subs]


print(adding_int4('IOII', 'IIOO'))

print(substraction_int4('IIOO','OOII'))

def medical_card_update(text:str, card:str=None) -> None:
    if card == None: card = '{}.txt'.format(input('Type new card name: '))
    with open(f'{card}.txt', 'a') as card:
        card.writelines('{}\n'.format(text))

medical_card_update('Hi, my name is Gleb!', 'Gleb_card2')
