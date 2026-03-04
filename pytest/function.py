def sum_num(a, b):
    return a+b

def del_num(a, b):
    return a/b

def mmultipy(a, b):
    return a * b

def pali(text):
    text = text.lower()
    return text == text[::-1]

def sum_list(nums):
    sum_num = 0
    for i in nums:
        sum_num += i
    return sum_num

def split_words(text):
    income_text = text.split()
    return income_text

def max_num(nums):
    max_num = nums[0]
    for i in nums:
        if i > max_num:
            max_num = i
    return max_num

def min_num(nums):
    min_num = nums[0]
    for i in nums:
        if i < min_num:
            min_num = i
    return  min_num
