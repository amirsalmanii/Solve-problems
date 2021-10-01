isbn = input('enter your isbn 10 or 13 ex:978-21...:\n').strip().replace('-','')


def compute_digits(isbn_number):
    result = 0
    global tens
    tens = False
    if len(isbn_number) == 13 and isbn_number.isnumeric():
        for index in range(len(isbn_number) - 1):
            if index % 2 == 0:
                result += int(isbn_number[index]) * 1
            elif index % 2 != 0:
                result += int(isbn_number[index]) * 3
        return result

    elif len(isbn_number) == 10 and isbn_number.isnumeric():  
        tens = True
        mul = 10
        result = 0
        for num in isbn[:-1]:
            result += int(num) * mul
            mul -= 1
        return result

    else:
        print('\nisbn has 13 digit wrong length entered')
        exit()


def find_check_digit(result):
    check_digits_validator = 0
    if tens == False:
        for num in range(1,10):
            check_digits_validator = result + num
            if check_digits_validator % 10 == 0:
                return num
    elif tens == True:
        for num in range(1,10):
            check_digits_validator = result + num
            if check_digits_validator % 11 == 0:
                return num


result_compute_digits = compute_digits(isbn)
valid_number = find_check_digit(result_compute_digits)


if int(isbn[-1]) == valid_number:
    print('\nYes You isbn Is Valid')
else:
    print('\nnot valid!')
