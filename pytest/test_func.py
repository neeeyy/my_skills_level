from function import *
import pytest

numbers = [5,10,3,8]
response_status = 200
user = {"name": "Alex", "age": 25}

@pytest.mark.maths
class Test_math:

    def test_add(self):
        assert sum_num(5,2) == 7

    def test_del(self):
        assert del_num(5,2) == 2.5

    def test_del_zero(self):
        with pytest.raises(ZeroDivisionError):
            del_num(5, 0)

@pytest.mark.testtest
class Test_gpt:

    def test_multy(self):
        assert mmultipy(5,2) == 10

    def test_word(self):
        assert "auto" in 'automation'

    def test_in_list(self):
        assert 3 in numbers
        assert 11 not in numbers

    def test_pali(self):
        assert pali('Level')

    def test_summ(self):
        assert 26 == sum_list(numbers)
        assert 5 < sum_list(numbers)
        assert 27 > sum_list(numbers)

    def test_response(self):
        assert response_status == 200

    def test_name_age(self):
        assert user['name'] == 'Alex'
        assert user['age'] > 18

    def test_word_count(self):
        assert split_words("cat dog cat").count('cat') == 2

    def test_max_min(self):
        assert max_num(numbers) == 10
        assert min_num(numbers) == 3