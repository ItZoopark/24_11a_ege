# Задачи из Решу Егэ -------------------------
def f_27421():
    s = open("24_demo.txt").read().splitlines()[0]
    count = 1
    max_count = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    print(max_count)


def f_27686():
    s = open("24_27686.txt").read().splitlines()[0]
    to_find = 'X'
    while to_find in s:
        to_find += 'X'
    print(len(to_find) - 1)


f_27686()


def f_27686_na_maksimalkah():
    print(len(max(open('24_demo.txt').readline().replace('Z', ' ').replace('Y', ' ').split(), key=len)))


f_27686_na_maksimalkah()
# lst = ['XXXXX', 'Z', 'AVBS']
# print(max(lst, key=len))
