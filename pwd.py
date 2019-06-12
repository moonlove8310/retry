pwd = input('please input your password: ')
ans = 'a123456'
i = 1
while i < 4:
    if pwd != ans:
        if i == 3:
            print('sorry and goodbye')
            break
        else:
            print('wrong password! you have', 3 - i, 'time(s)')
    else:
        print('success')
        break
    pwd = input('please input your password: ')
    i = i + 1
