x=input()
for l in x:
    abc=ord(l)
    print(f"{abc}")
    # 给码点加1
    abc1 = abc + 1
    # 输出加1后的码点
    print(f"加1后的Unicode码点是: {abc1}")

    # 尝试将加1后的码点转换为ASCII字符，并输出
    try:
        new_char = chr(abc1)
        print(f"对应的ASCII字符是: {new_char}")
    except ValueError:
        print(f"加1后的码点对应的字符不是有效的ASCII字符")

        # 为了清晰，可以在每个字母的处理后输出一个分隔符
    print("---")