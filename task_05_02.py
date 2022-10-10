# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся
#  в отдельных текстовых файлах.

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

def code_text(name_text_file):
    with open(name_text_file, 'r', encoding='UTF-8') as file_in:
        file_lines_list = file_in.readlines()
        file_symbols_list = [list(file_lines_list[i])
                             for i in range(len(file_lines_list))]
        code_symbols_list = []
        for i in range(len(file_symbols_list)):
            end_str = False
            if '\n' in file_symbols_list[i]:
                file_symbols_list[i].pop(-1)
                end_str = True
            if file_symbols_list[i] != []:
                now_symbol = file_symbols_list[i][0]
                count = 1
                for j in range(1, len(file_symbols_list[i])):
                    if now_symbol == file_symbols_list[i][j]:
                        count += 1
                    else:
                        code_symbols_list.append(str(count) + now_symbol)
                        now_symbol = file_symbols_list[i][j]
                        count = 1
                code_symbols_list.append(str(count) + now_symbol)
            if end_str:
                code_symbols_list.append('\n')
    return code_symbols_list


def write_code_file(code_symbol_list, name_code_file_make):
    with open(name_code_file_make, 'w', encoding='UTF-8') as file_in:
        file_in.write(''.join(code_symbols_list))
    return


def decode_file(name_code_file_decode):
    with open(name_code_file_decode, 'r', encoding='UTF-8') as file_in: 
        file_lines_list = file_in.readlines()
        file_symbols_list = [list(file_lines_list[i])
                             for i in range(len(file_lines_list))]
        decode_symbols_list = []
        for i in range(len(file_symbols_list)):
            end_str = False
            if '\n' in file_symbols_list[i]:
                file_symbols_list[i].pop(-1)
                end_str = True
            if file_symbols_list[i] != []:
                count_digits = file_symbols_list[i][0]
                for j in range(1, len(file_symbols_list[i])):
                    if file_symbols_list[i][j].isdigit():
                        count_digits += file_symbols_list[i][j]
                    else:
                        decode_symbols_list.append(int(count_digits) * file_symbols_list[i][j])
                        count_digits = ''
            if end_str:
                decode_symbols_list.append('\n')
    return decode_symbols_list

def write_decode_file(decode_symbol_list, name_txt_file_in):
    with open(name_txt_file_in, 'w', encoding='UTF-8') as file_in:
        file_in.write(''.join(decode_symbols_list))
    with open(name_txt_file_in, 'r', encoding='UTF-8') as file_in:
        out = file_in.readlines()
        print("".join(out))
    return


name_txt_file_in = input('Enter the name of the file with the text: ')
name_code_file_make = input('Enter the file name to record: ')
name_code_file_decode = input('Enter the name of the file to decode: ')

code_symbols_list = code_text(name_txt_file_in)
write_code_file(code_symbols_list, name_code_file_make)

decode_symbols_list = decode_file(name_code_file_decode)
write_decode_file(decode_symbols_list, name_txt_file_in)

