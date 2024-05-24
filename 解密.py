a=input()
a1=a[::-1]
print("逆序",a1)
a2=a1.swapcase()
print("大小写转换",a2)

def shift_letter(letter, shift):
    ascii_offset = ord('a') if letter.islower() else ord('A')
    shifted = (ord(letter) - ascii_offset + shift) % 26 + ascii_offset
    return chr(shifted)


# 为小写英文字母加23
lowercase_letters = a2
shifted_lowercase = ''.join(shift_letter(letter, 23) for letter in lowercase_letters)
# print(shifted_lowercase)

# 为大写英文字母加23
uppercase_letters =a2
shifted_uppercase = ''.join(shift_letter(letter, 23) for letter in uppercase_letters)
print('向左推移三个字母',shifted_uppercase)
