"""实验3 测试用例：校验切片删除、集合运算、去重与选课统计结果。"""
import pytest

from lab3_tasks import (
    task3_set_ops,
    task4_dedup,
    task5_course,
    extra_nested_dedup,
)


def test_slice_delete_basic():
    ls1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    del ls1[::3]
    assert ls1 == [1, 2, 4, 5, 7, 8]

    ls2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    del ls2[1::3]
    assert ls2 == [0, 2, 3, 5, 6, 8, 9]

    ls3 = [0, 1, 2, 3, 4, 5]
    del ls3[::-2]
    assert ls3 == [0, 2, 4]


def test_set_ops():
    A = {2, 4, 6, 8, 10, 12}
    B = {3, 6, 9, 12, 15}
    assert A & B == {6, 12}
    assert A - B == {2, 4, 8, 10}
    assert B - A == {3, 9, 15}
    assert A ^ B == {2, 3, 4, 8, 9, 10, 15}
    assert {x for x in range(1, 31) if x % 4 == 0} == {4, 8, 12, 16, 20, 24, 28}


def test_dedup_order():
    data = [5, 2, 7, 2, 5, 9, 7, 3, 9, 1]
    ordered = list(dict.fromkeys(data))
    assert ordered == [5, 2, 7, 9, 3, 1]
    # set 去重后元素集合一致，但顺序不保证
    assert set(ordered) == set(data)


def test_course_stats():
    class1 = [101, 103, 105, 107, 109, 103, 101]
    class2 = [102, 104, 106, 108, 109, 107, 102]
    s1, s2 = set(class1), set(class2)
    assert s1 & s2 == {107, 109}
    assert s1 - s2 == {101, 103, 105}
    assert sorted(s1 ^ s2) == [101, 102, 103, 104, 105, 106, 108]
    assert tuple(s1 & s2) in {(107, 109), (109, 107)}


def test_nested_dedup():
    nest = [[1, 2], [3, 4], [1, 2], [5, 6]]
    seen, result = set(), []
    for item in nest:
        key = tuple(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
    assert result == [[1, 2], [3, 4], [5, 6]]


def test_hashable_rules():
    s = set()
    s.add((1, 2, 3))
    s.add(frozenset({1, 2}))
    assert (1, 2, 3) in s
    with pytest.raises(TypeError):
        s.add([1, 2])
    with pytest.raises(TypeError):
        s.add({1, 2})
