
def format_sign_list_value(value):
    num_main = ''
    for v in value:
        if v.isdigit():
            num_main = num_main + v
        else:
            break
    num_sub = value[len(num_main):]
    return num_main, num_sub