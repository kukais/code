# -*- coding:UTF-8 -*- #


def bagua_encode(strs):
    # 示例：将普通 ASCII 字符串 "hello" 转换为其二进制形式（每字符）
    binary_representation = ''.join(format(ord(c), '08b') for c in strs)
    # print(binary_representation)

    # 确保二进制串长度是3的倍数，如果有余数，则在最后填充0以确保能整除
    if len(binary_representation) % 3 != 0:
        binary_representation += '0' * (3 - len(binary_representation) % 3)
    binary_groups = [binary_representation[i:i + 3] for i in range(0, len(binary_representation), 3)]
    # print(binary_groups)

    strings = ''
    character_array = ['乾', '兑', '离', '震', '巽', '坎', '艮', '坤']
    # 遍历二进制组列表，并将每个组转换为八进制形式
    for binary_group in binary_groups:
        # 使用int()函数将二进制字符串转换为整数（以2为基数），然后使用oct()将其转换为八进制表示形式。
        octal_value = int(binary_group, 2)
        str0 = character_array[octal_value]
        strings = strings + str0

    return strings


def bagua_decode(strs):
    # 定义字符集与数字之间的映射关系，用于解码操作
    character_to_number = {'乾': 0, '兑': 1, '离': 2, '震': 3,
                           '巽': 4, '坎': 5, '艮': 6, '坤': 7}

    # 将输入的字符串转换为字符列表，因为解码操作需要逐个处理字符
    decoded_list = []
    for char in strs:
        num = character_to_number[char]
        # 将每个数字通过 int 转换回二进制并填充至3位
        binary_str = format(num, '03b')
        decoded_list.append(binary_str)
    # 合并所有转换后的二进制字符串
    binary_string = ''.join(decoded_list)

    # 将输入字符串分割成8位一组的子串，并转换为整数再转换为相应的字符。
    ascii_strings = ''
    for i in range(0, len(binary_string), 8):
        eight_bit_chunk = binary_string[i:i + 8]  # 提取8位二进制数
        if len(eight_bit_chunk) == 8:  # 检查长度是否为8位
            ascii_char = chr(int(eight_bit_chunk, 2))  # 将二进制数转换为整数，然后转换为ASCII字符
            ascii_strings += ascii_char  # 将ASCII字符添加到结果字符串中
        else:
            continue  # 这里选择跳过不满足8位的子串
    return ascii_strings


if __name__ == '__main__':
    ascii_string = 'hello123'
    encode_string = bagua_encode(ascii_string)
    # 打印转换后的字符串
    print(f'加密：{encode_string}')

    decod_string = bagua_decode(encode_string)
    print(f'解密：{decod_string}')
