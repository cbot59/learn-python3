def sock_merchant(number_socks, socks_list):
    counter = []
    total = 0
    for x in set(socks_list[:number_socks]):
        counter.append(socks_list.count(x))
        if socks_list.count(x) % 2 == 0:
            total = total + 1
    return total


n = int(input())
ar = list(map(int, input().rstrip().split()))

result = sock_merchant(n, ar)

print(str(result) + '\n')
