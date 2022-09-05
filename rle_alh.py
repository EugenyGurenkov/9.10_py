def compression(string):
    count = 1
    result = string
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        if (string[i] != string[i + 1] or i == len(string) - 2) and count > 2:
            result = result.replace(str(count * string[i]), f'{str(count)}{string[i]}')
            count = 1
    return result


def decompression(string):
    count = ''
    result = string
    for i in range(len(string)):
        if string[i].isdigit():
            count = count + string[i]
        if not string[i].isdigit() and count != '':
            result = result.replace(count, f'{(int(count) - 1) * string[i]}')
            count = ''
    return result


text = input()
print(compression(text))
print(decompression(text))