def import_file(name):
    with open(name, 'r', encoding='utf8') as file_1:
        polinomial = [i for i in file_1.read().replace('^', '').split()]
        count = 0
        for i in polinomial:
            if i == '-' and polinomial[count + 1][0] == 'x':
                polinomial[count + 1] = polinomial[count] + '1' + polinomial[count + 1]
            if i == '-' and polinomial[count + 1][0].isdigit():
                polinomial[count + 1] = polinomial[count] + polinomial[count + 1]
            if i == '+' or i == '-':
                polinomial.pop(count)
            count += 1
        return polinomial


def export_file(pol):
    with open('p1.txt', 'w', encoding='utf8') as file:
        file.write(pol)


def dict_from_polinomial(pol):
    result_dict = {}
    for i in pol:
        if 'x' not in i:
            i = i + 'x' + '0'
        if i[i.find('x') + 1:] == '':
            i = i + '1'
        if i[:i.find('x')] == '':
            i = '1' + i
        elif i[:i.find('x')] == '-':
            i = i.replace('-x', '-1x')
        if int(i[i.find('x') + 1:]) in result_dict.keys():
            result_dict[int(i[i.find('x') + 1:])] += int(i[0:i.find('x')])
        else:
            result_dict[int(i[i.find('x') + 1:])] = int(i[0:i.find('x')])
    return result_dict


def summ_pol(dict1, dict2):
    result = {}
    if max(dict1.keys()) > max(dict2.keys()):
        max_coef = max(dict1.keys())
    else:
        max_coef = max(dict2.keys())
    for i in range(max_coef, -1, -1):
        if i in dict1.keys() or i in dict2.keys():
            result[i] = (dict1[i] if i in dict1.keys() else 0) + (dict2[i] if i in dict2.keys() else 0)
            if result[i] == 0:
                del result[i]
    return result


def get_polinomial(dict):
    result = ''
    list_keys = sorted(dict.keys(), reverse=True)
    if not list_keys:
        return 0
    for i in list_keys:
        if i > 1:
            result = result + str(abs(dict[i]) if list_keys.index(i) != 0 else dict[i]) + 'x^' + str(i)
        if i == 1:
            result = result + str(abs(dict[i]) if list_keys.index(i) != 0 else dict[i]) + 'x'
        if i == 0:
            result = result + str(abs(dict[i]) if list_keys.index(i) != 0 else dict[i])
        if i > list_keys[-1]:
            if dict[list_keys[list_keys.index(i) + 1]] > 0:
                result = result + ' + '
            else:
                result = result + ' - '
    if result[0] == '1' and result[1] == 'x':
        result = result.replace('1x', 'x', 1)
    return result.replace(' 1x', ' x').replace('-1x', '-x')


first_dict = dict_from_polinomial(import_file('p1.txt'))
second_dict = dict_from_polinomial(import_file('p2.txt'))
result_dict = summ_pol(first_dict, second_dict)
export_file(get_polinomial(result_dict))
print(f'({get_polinomial(first_dict)}) + ({get_polinomial(second_dict)}) = {get_polinomial(result_dict)}')