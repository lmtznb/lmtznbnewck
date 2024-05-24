import re
x=input('输入一行字符')
digits = re.findall(r'\d',x)
digits_str =''.join(digits)
print('数字字符的长度：',len(digits_str))