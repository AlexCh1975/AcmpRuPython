# Требуется вычислить количество N - значных счастливых билетов. Напомним, 
# что билет называется счастливым, если сумма первой половины его цифр равна 
# сумме другой его половины. Например, билет 064109 счастливый, т.к. 0+6+4=1+0+9.

# in  В единственной строке входного файла INPUT.TXT записано натуральное четное число 
#     N (N ≤ 100) – количество цифр в билете.

# out В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое 
#     число – количество N-значных счастливых билетов.

# Примеры
#     INPUT.TXT	OUTPUT.TXT
# 1	    4	         670
# 2	    6	        55252
# 3	    12	        39581170420

def get_sum_ticket(num, size):
    sum = 0
    num = int(num)
    for i in range(int(size)):
        sum += num % 10
        num //= 10      
    return sum   

def check_ticket_lucky(num, size):
    num = str(num)
    num = num.zfill(size)
    num1 = num[: int(size / 2)] 
    num2 = num[int(size / 2): int(size)] 

    sum_num1 = get_sum_ticket(num1, size / 2)
    sum_num2 = get_sum_ticket(num2, size / 2)

    if sum_num1 == sum_num2: 
        # print(num, end=' ')
        return 1
    else: return 0

def counting_options():
    path = 'task_100/input.txt'
    data = open(path, 'r')
    size = int(data.read())
    data.close()
    if size % 2 != 0: print("Число не четное!") 
    max_num = int(1 * (10 ** size))
    count = 0
    # print(max_num)
    num = 0
    for i in range(max_num):
        num = str(num)
        if num.count(num[: int(size / 2)]) == 2:
            # (num.count(num[0], 0, size) == size or)
            count += 1
            num = int(num)
        else: 
            count += check_ticket_lucky(num, size)
            num = int(num)
        num += 1
    data = open('task_100/out.txt', 'a')
    data.write(str('{}\n'.format(count)))
    data.close()

counting_options()

