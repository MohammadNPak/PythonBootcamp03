# n = int(input())

# prices=[]
# for i in range(n):
#     prices.append(int(input()))

# print(prices)

# for price in prices:
#     print(price)


def split(s, char):
    start = 0
    end = 0
    output = []
    while end <= len(s):
        if s[end:end+len(char)] == char or end == len(s):
            # print(s[start:end])
            output.append(s[start:end])
            start = end + len(char)
        end += 1
    return output

# days1 = split(input())
# days2 = split(input())
# days3 = split(input())


# days_list = split(days, " ")
# print(days_list)
n1 = int(input())
test1 = split(input(), " ")
n2 = int(input())
test2 = split(input(), " ")
n3 = int(input())
test3 = split(input(), " ")


def common_days(days1, days2, days3):
    days = [days1, days2, days3]
    common_day = []
    for day in days:
        for i in day:
            if i not in common_day:
                common_day.append(i)
    return common_day

print(7-len(common_days(test1, test2, test3)))
