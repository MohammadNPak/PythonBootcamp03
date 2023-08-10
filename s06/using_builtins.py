days = []
n1 = int(input())
days.extend(input().split())
n2 = int(input())
days.extend(input().split())
n3 = int(input())
days.extend(input().split())

days = set(days)
all_days_of_week = {"shanbe", "1shanbe", "2shanbe",
                    "3shanbe", "4shanbe", "5shanbe", "jome"}
answer = all_days_of_week.difference(days)
print(len(answer))
# curly braces