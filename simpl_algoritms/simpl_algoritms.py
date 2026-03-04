def sum_num(nums):
    total = 0
    for i in nums:
        total += i
    return total

print(sum_num([4, 7, 1, 9]))


def dubles(nums):
    res = []
    for i in nums:
        if i not in res:
            res.append(i)
    return res

print(dubles([3, 1, 2, 3, 4, 2, 5]))


def pali(text):
    text = text.lower()
    return text == text[::-1]

print(pali("Level"))


def simpl(num):
    if num <= 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(simpl(37))


def second_num(nums):
    max_num = nums[0]
    second_max = float("-inf")

    for i in nums:
        if max_num < i:
            second_max = max_num
            max_num = i
        elif second_max < i < max_num:
            second_max = i

    return second_max

print(second_num([10, 5, 8, 10, 3]))


def long_word(text):
    text = text.split()
    res = {}

    for i in text:
        res[i] = len(i)

    sort_res = sorted(res.items(), key=lambda x: x[-1], reverse=True)
    return sort_res[0]

print(long_word("qa automation engineer"))


def unique(text):
    return len(text) == len(set(text))

print(unique("autmion"))


def long_words(text):
    res = {}
    texts = text.split()

    for i in texts:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1

    return res

print(long_words("cat dog cat bird dog cat"))


def balance(text):
    balance = 0

    for i in text:
        if i == "(":
            balance += 1
        elif i == ")":
            balance -= 1

        if balance < 0:
            return False

    if balance != 0:
        return False

    return True

print(balance("(())()"))


def fibo(nums):
    a, b = 0, 1
    res = []

    for i in range(nums):
        res.append(a)
        a, b = b, a + b

    return res

print(fibo(7))