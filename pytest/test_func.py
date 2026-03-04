import pytest
from src.function import *

@pytest.mark.maths
class Test_math:

    def test_add(self):
        assert sum_num(5,2) == 7

    def test_del(self):
        assert del_num(5,2) == 2.5

    def test_del_zero(self):
        with pytest.raises(ZeroDivisionError):
            del_num(5, 0)


@pytest.mark.chatgpt
class Test_gpt:

    def test_sum(self):
        assert sums(5,2) == 7

    def test_multy(self):
        assert mmultipy(5,2) == 10

    def test_word(self):
        assert "auto" in word('automation')

    def test_in_list(self):
        assert 3 in nums
        assert 10 not in nums

    def test_pali(self):
        assert pali(text)

    def test_summ(self):
        assert 10 == sum_list(result)
        assert 5 < sum_list(result)
        assert 20 > sum_list(result)

    def test_response(self):
        assert response_status == 200

    def test_name_age(self):
        assert user['name'] == 'Alex'
        assert user['age'] > 18

    def test_word_count(self):
        assert texts.count('cat') == 2

    def test_max_min(self):
        assert max_num(numbers) == 10
        assert min_num(numbers) == 3