x = 1222221
if x > 0:
    x_str = str(x)
    x_list = list(str(x))
    x_list.reverse()
    y = ''.join(x_list)
    y_int = eval(y)
    if y_int-x == 0:
        print('true')
    else:
        print('false')
