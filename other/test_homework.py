strings = 'ABc dEb AXe DCk'
strings.split()
cnt_strings = len(strings)
upper_str = 7
lower_str = 5
for sym in strings:
    if sym is upper_str: 
        upper_str += 1
    else: 
        lower_str += 1

float = 100 / (upper_str + lower_str)
print(f'upper_string = {float * upper_str:.2f}%')
print(f'lower_string = {float * lower_str:.2f}%')