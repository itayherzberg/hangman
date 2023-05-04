import calendar
from collections import Counter


# 2.3.3
def three_little_pigs():
    bricks = int(input("Enter three digits (each digit for one pig): "))

    total = 0
    bricks_save = bricks
    while bricks_save > 0:
        total += int(bricks_save % 10)
        bricks_save /= 10

    print(total)
    print(total // 3)
    print(int(total % 3))
    print(total / 3 == 0)


# 3.2.1
def convert_taki_words():
    print(
        "\"Shuffle, Shuffle, Shuffle\", say it together!\n Change colors and directions,\n Don't back down and stop the player!\n \tDo you want to play Taki?\n \tPress y\\n")


# 3.3.3
def decrypt_string():
    encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
    decrypted_message = ""

    for i in range(len(encrypted_message) - 1, -1, -2):
        decrypted_message += encrypted_message[i]

    print(decrypted_message)


# 3.4.2
def replace_first_appearance():
    string = input("Please enter a string: ")
    first_letter = string[0]

    string = string.replace(first_letter, 'e')
    string = string.replace('e', first_letter, 1)

    print(string)


# 3.4.3
def half_capitals_letter():
    string = input("Please enter a string: ")
    print(string[:len(string) // 2] + string[len(string) // 2:].upper())


# 4.2.2
def check_palindrome():
    string = input("Please enter a word: ")
    string = string.lower()
    string = string.replace(' ', '')

    if string == string[::-1]:
        print("OK")
    else:
        print("NOT")


# 4.2.3
def convert_temperature():
    temp_to_convert_from = input("Insert the temperature you would like to convert: ")
    only_temp = float(temp_to_convert_from[:-1])

    if temp_to_convert_from[-1] in {'F', 'f'}:
        converted_temp = (5 * only_temp - 160) / 9
        print(str(converted_temp) + 'C')
    else:
        converted_temp = (9 * only_temp + 32 * 5) / 5
        print(str(converted_temp) + 'F')


# 4.2.4
def find_day():
    day_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    date = input("Enter a date: ")
    date_as_lst = date.split('/')
    day = calendar.weekday(int(date_as_lst[2]), int(date_as_lst[1]), int(date_as_lst[0]))

    print(day_dict[day])


# 5.3.4
def last_early(my_str):
    my_str = my_str.lower()
    return my_str.find(my_str[-1]) != (len(my_str) - 1)


# 5.3.5
def distance(num1, num2, num3):
    if abs(num2 - num1) == 1 or abs(num3 - num1) == 1:
        if (abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2) or \
                (abs(num3 - num1) >= 2 and abs(num3 - num2) >= 2):
            return True
    return False


def fix_age(age):
    if age in {13, 14, 17, 18, 19}:
        return 0
    return age


# 5.3.6
def filter_teens(a=13, b=13, c=13):
    return fix_age(a) + fix_age(b) + fix_age(c)


# 5.3.7
def chocolate_maker(small, big, x):
    return (small + big * 5) >= x


# 6.1.2
def shift_left(my_list):
    my_list.append(my_list.pop(0))
    return my_list


# 6.2.4
def extend_list_x(list_x, list_y):
    for x in list_x:
        list_y.append(x)
    return list_y


# 6.3.1
def are_lists_equal(list1, list2):
    return sorted(list1) == sorted(list2)


# 6.3.2
def longest(my_list):
    return sorted(my_list, key=lambda s: len(s))[-1]


# 7.1.4
def squared_numbers(start, stop):
    my_lst = []

    while start <= stop:
        my_lst.append(start ** 2)
        start += 1

    return my_lst


# 7.2.1
def is_greater(my_list, n):
    return [x for x in my_list if x > n]


# 7.2.2
def numbers_letters_count(my_str):
    digit_count = 0
    for x in my_str:
        if x.isdigit():
            digit_count += 1

    return [digit_count, len(my_str) - digit_count]


# 7.2.4
def seven_boom(end_number):
    seven_boom_lst = [*range(end_number + 1)]

    for i in range(len(seven_boom_lst)):
        num = seven_boom_lst[i]
        if num % 7 == 0 or str(num).find('7') != -1:
            seven_boom_lst[i] = 'BOOM'

    return seven_boom_lst


# 7.2.5
def sequence_del(my_str):
    new_str = ''
    i = 0

    while i < len(my_str):
        new_str += my_str[i]
        letter = my_str[i]

        while i < len(my_str) and my_str[i] == letter:
            i += 1

    return new_str


# 7.2.6
def supermarket():
    products_str = input("Enter products: ")
    products_lst = products_str.split(',')

    op = int(input("Enter operation: "))
    while op != 9:
        if op == 1:
            print(products_lst)
        elif op == 2:
            print("Products' count: " + str(len(products_lst)))
        elif op == 3:
            product_name = input("Enter product name: ")
            if product_name in products_lst:
                print("Yes")
            else:
                print("No")
        elif op == 4:
            product_name = input("Enter product name: ")
            print("count: " + str(products_lst.count(product_name)))
        elif op == 5:
            product_name = input("Enter product name: ")
            products_lst.remove(product_name)
        elif op == 6:
            product_name = input("Enter product name: ")
            products_lst.append(product_name)
        elif op == 7:
            print([x for x in products_lst if len(x) < 3 and not x.isalpha()])
        elif op == 8:
            print(list(dict.fromkeys(products_lst)))

        op = int(input("Enter operation: "))


# 7.2.7
def arrow(my_char, max_length):
    for i in range(1, max_length + 1):
        print(my_char * i)
    for i in range(max_length - 1, 0, -1):
        print(my_char * i)


# 8.2.2
def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda tup: tup[1])


# 8.2.3
def mult_tuple(tuple1, tuple2):
    new_tuple = tuple()

    for x in tuple1:
        for y in tuple2:
            new_tuple = (*new_tuple, (x, y))
            new_tuple = (*new_tuple, (y, x))

    return new_tuple


def is_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)


# 8.2.4
def sort_anagrams(list_of_strings):
    new_lst = list()
    words_added = list()

    for string in list_of_strings:
        if string not in words_added:
            lst = [string]
            words_added.append(string)
            for string2 in list_of_strings[list_of_strings.index(string) + 1:]:
                if is_anagrams(string, string2):
                    lst.append(string2)
                    words_added.append(string2)
            new_lst.append(lst)

    return new_lst


# 8.3.2
def dict_func():
    my_dict = {'first_name': 'Mariah', 'last_name': 'Carey', 'birth_date': '27.03.1970',
               'hobbies': ['Sing', 'Compose', 'Act']}
    op = int(input("Enter an operation code: "))
    if op == 1:
        print(my_dict['last_name'])
    elif op == 2:
        birthday_date = my_dict['birth_date']
        print(birthday_date[birthday_date.index('.') + 1: birthday_date.index('.') + 3])
    elif op == 3:
        print(len(my_dict['hobbies']))
    elif op == 4:
        print(my_dict['hobbies'][-1])
    elif op == 5:
        my_dict['hobbies'].append('Cooking')
    elif op == 6:
        date_tuple = tuple(my_dict['birth_date'].split('.'))
        print(date_tuple)
    else:
        my_dict['age'] = 17
        print(my_dict['age'])


# 8.3.3
def count_chars(my_str):
    my_str = my_str.replace(' ', '')
    my_dict = dict()

    for letter in my_str:
        my_dict[letter] = my_str.count(letter)

    return my_dict


# 9.1.1
def are_files_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()


# 9.1.2
def manipulate_file():
    path = input("Enter a file path: ")
    task = input("Enter a task: ")

    with open(path) as f:
        if task == "sort":
            print(sorted(list(set(f.read().split()))))
        elif task == "rev":
            for line in f:
                print(line[::-1])
        elif task == "last":
            num = int(input("Enter a number: "))
            for line in (f.readlines()[-num:]):
                print(line, end='')


# 9.2.2
def copy_file_content(source, destination):
    with open(source, 'r') as a, open(destination, 'w') as b:
        b.write(a.read())


# 9.2.3
def who_is_missing(file_name):
    with open(file_name, 'r') as a, open("found.txt", 'w') as b:
        numbers = sorted(a.read().split(','))

        for i, number in enumerate(numbers, start=1):
            if int(number) != i:
                print(i)
                b.write(str(i))
                return


def is_longer(len1, len2):
    len1_parts = [int(x) for x in len1.split(':')]
    len2_parts = [int(x) for x in len2.split(':')]

    return (len1_parts[0] * 60 + len1_parts[1]) - (len2_parts[0] * 60 + len2_parts[1]) > 0


# 9.3.1
def my_mp3_playlist(file_path):
    with open(file_path, 'r') as f:
        max_song = ['', 0, '']
        artists_lst = list()
        max_song_len = '0:0'

        for line in f:
            song = line.split(';')

            if is_longer(song[2], max_song_len):
                max_song_len = song[2]
                max_song_len_name = song[0]

            max_song[1] += 1
            artists_lst.append(song[1])

        max_song[0] = max_song_len_name
        max_song[2] = max(set(artists_lst), key=artists_lst.count)

        print(tuple(max_song))


# 9.3.2
def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        content_lst = f.read().splitlines()

    while len(content_lst) < 3:
        content_lst.append('')

    if content_lst[2] == '':
        content_lst[2] = new_song
    else:
        content_lst[2] = content_lst[2].replace(content_lst[2][:content_lst[2].find(';')], new_song)

    new_content = '\n'.join(content_lst)

    with open(file_path, 'w') as f:
        f.write(new_content)

    print(new_content)


def main():
    my_mp4_playlist("C:\\Users\itayh\\Desktop\\copy.txt", "Python Love Story")


if __name__ == "__main__":
    main()
