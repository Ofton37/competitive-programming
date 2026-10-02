while True:
    numbers = input()
    if numbers[0] == "-":
        break
    cnt = int(input())
    size = len(numbers)
    for i in range(cnt):
        num = int(input())
        numbers = numbers[num:size] + numbers[0:num]
    print(numbers)
    