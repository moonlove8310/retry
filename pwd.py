ans = 'a123456'
i = 1
while i < 4:
    pwd = input('please input your password: ')
    if pwd != ans:
        if i == 3:
            print('sorry and goodbye')
            break
        else:
            print('wrong password! you have', 3 - i, 'time(s)')
    else:
        print('success')
        break
    i = i + 1
