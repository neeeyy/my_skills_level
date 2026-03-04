def sum_num(a, b):
    return a+b

def del_num(a, b):
    return a/b

@pytest.mark.maths
class Test_math:

    def test_add(self):
        assert sum_num(5,2) == 7

    def test_del(self):
        assert del_num(5,2) == 2.5

    def test_del_zero(self):
        with pytest.raises(ZeroDivisionError):
            del_num(5, 0)


def sums(a, b):
    return a+b
def mmultipy(a,b):
    return a * b
def word(text):
    return text

nums = [1,2,3,4,5]

def pali(text):
    text = text.lower()
    return text == text[::-1]

text = 'Level'

def sum_list(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

result = [2,3,5]
response_status = 200
user = {"name": "Alex", "age": 25}
texts = "cat dog cat"
words = texts.split()

def max_num(nums):
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    return max

def min_num(nums):
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
    return  min

numbers = [5,10,3,8]