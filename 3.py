def sum_to(n):
    # return sum([i for i in range(1,n+1)]) // One line solution
    sum = 0
    for i in range(1, n+1):
        sum += i

    return sum

if __name__ == "__main__":
    print(sum_to(10))