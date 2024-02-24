def convert(nums: str):
    # байты
    num_int = int(nums)
    if num_int >= 1024:
        num_int = round(num_int / 1024, 2)  # кБ
        if num_int >= 1024:
            num_int = round(num_int / 1024, 2)  # MБ
            return f'{str(num_int)}M'
        return f'{str(num_int)}K'
    else:
        return nums


with open('output', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    folder_count = 0
    file_count = 0
    for line in lines:
        try:
            if line.startswith('total'):
                line_list = line.strip().split()
                num = round(int(line_list[1]) / 1024, 2)
                line_list[1] = f'{str(num)}M'
                print(' '.join(line_list))
                continue
            elif line.startswith('d'):
                folder_count += 1
            else:
                file_count += 1
            line_list = line.strip().split()
            num = convert(line_list[4])
            line_list[4] = num
            strf = '{:12} {:>3} {:3} {:7} {:>6} {:3} {:>2} {:5} {:<}'.format(*line_list)
            print(strf)
        except IndexError as ex:
            print(f'{ex}, {line}')
    else:
        print(f'Всего папок {folder_count}\n'
              f'Всего files {file_count}')
