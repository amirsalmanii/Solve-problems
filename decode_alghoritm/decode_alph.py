engAlph = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
engWhitespaces = ('!', '?', ',', '.', ' ', ';', '"', "'")

try:
    client_numbers = input('enter numbers like: 2,33,24 for decode ..: ').split(',')
    client_numbers = [int(num) for num in client_numbers]
except ValueError:
    print('wrong format input')
    exit()


finall_res = []
tmp = 1
for clnum in client_numbers:
    if tmp == 1 or tmp == 2:
        res = clnum % 27
    else:
        res = clnum % 9
    
    if res != 0:
        if tmp == 1:
            finall_res.append(engAlph[res - 1].upper())  # upper case added
        if tmp == 2:
            finall_res.append(engAlph[res - 1])  # lower case added
        if tmp == 3:
            finall_res.append(engWhitespaces[res - 1])  #white space added
    elif res == 0:
        tmp += 1
        if tmp == 4:
            tmp = 1

join_res = ''.join(finall_res)
print(join_res)



