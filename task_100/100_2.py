
def counting_options():
    path = 'task_100/input.txt'
    data = open(path, 'r')
    size = int(data.read())
    data.close()

    if size % 2 != 0: print("Число не четное!") 
    
    max_num = int(1 * (10 ** size))
    count = 0
    num = 0
    for i in range(max_num):
        num = str(num)
        num = num.zfill(size)
        num1 = num[: int(size / 2)] 
        num2 = num[int(size / 2): int(size)]
        if num1 == num2 or num1 == num2[::-1]:
            count += 1
            num = int(num)
        else:
            num1 = list(num1)
            num2 = list(num2) 
            if sum([int(item) for item in num1]) == sum([int(item) for item in num2]): 
                count += 1
                print(num, end=' ')
            num = int(num)
        num += 1

    data = open('task_100/out.txt', 'a')
    data.write(str('{}\n'.format(count)))
    data.close()

counting_options()

