"""
实验3 Python 列表、元组、集合
任务1 切片删除深度探究
任务2 嵌套容器与可哈希辨析
任务3 集合运算与集合推导式
任务4 去重算法对比（保序 vs 无序）
任务5 综合设计：选课编号统计
"""


# ========== 任务1 切片删除深度探究 ==========
def task1_slice_delete():
    print("===== 任务1 切片删除探究 =====")

    # 1. 正步长步长 3：删除索引 0,3,6,9
    ls1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    del ls1[::3]
    print("del ls1[::3] →", ls1)

    # 2. 从索引 1 开始，步长 3：删除索引 1,4,7
    ls2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    del ls2[1::3]
    print("del ls2[1::3] →", ls2)

    # 3. 负步长 -2：从尾部往前，删除索引 5,3,1
    ls3 = [0, 1, 2, 3, 4, 5]
    del ls3[::-2]
    print("del ls3[::-2] →", ls3)

    # 拓展坑：for 遍历同时 remove，偶数删不干净
    ls4 = [1, 2, 3, 4, 5, 6]
    for i in ls4[:]:  # 安全写法：遍历副本
        if i % 2 == 0:
            ls4.remove(i)
    print("遍历副本后删除偶数 →", ls4)

    # 对照：直接遍历原列表（会漏删），单独演示
    ls4_bad = [1, 2, 3, 4, 5, 6]
    for i in ls4_bad:
        if i % 2 == 0:
            ls4_bad.remove(i)
    print("直接遍历原列表删除偶数（漏删）→", ls4_bad)


# ========== 任务2 嵌套容器与可哈希辨析 ==========
def task2_hashable():
    print("\n===== 任务2 可哈希测试 =====")
    s = set()

    # (1,2,3)：全部是不可变元素，元组可哈希 → 成功
    s.add((1, 2, 3))
    print("add (1,2,3) 成功，集合：", s)

    # (1,[2,3])：元组内嵌列表，列表不可哈希 → 整条元组不可哈希，报错
    try:
        s.add((1, [2, 3]))
    except TypeError as e:
        print("add (1,[2,3]) 报错：", e)

    # [1,2]：列表本身不可哈希 → 报错
    try:
        s.add([1, 2])
    except TypeError as e:
        print("add [1,2] 报错：", e)

    # frozenset({1,2})：固定集合，可哈希 → 成功
    s.add(frozenset({1, 2}))
    print("add frozenset({1,2}) 成功，集合：", s)

    # {1,2}：普通集合可变，不可哈希 → 报错
    try:
        s.add({1, 2})
    except TypeError as e:
        print("add {1,2} 报错：", e)


# ========== 任务3 集合运算 + 推导式 ==========
def task3_set_ops():
    print("\n===== 任务3 集合运算 + 推导式 =====")
    A = {2, 4, 6, 8, 10, 12}
    B = {3, 6, 9, 12, 15}

    print("交集 A & B：", A & B)
    print("并集 A | B：", A | B)
    print("差集 A - B：", A - B)
    print("差集 B - A：", B - A)
    print("对称差 A ^ B：", A ^ B)

    divisible_by_4 = {x for x in range(1, 31) if x % 4 == 0}
    print("1~30 中能被 4 整除的集合：", divisible_by_4)


# ========== 任务4 去重算法对比 ==========
def task4_dedup():
    print("\n===== 任务4 去重对比 =====")
    data = [5, 2, 7, 2, 5, 9, 7, 3, 9, 1]

    # 方案1：set 去重，简洁但丢失原始顺序
    res1 = list(set(data))
    print("list(set(data)) 去重（乱序）：", res1)

    # 方案2：手写循环，保留第一次出现顺序
    res2 = []
    for num in data:
        if num not in res2:
            res2.append(num)
    print("手写保序去重：", res2)

    # 拓展：dict.fromkeys 一行保序去重（Python 3.7+ 字典有序）
    res3 = list(dict.fromkeys(data))
    print("dict.fromkeys 保序去重：", res3)


# ========== 任务5 综合设计：选课统计 ==========
def task5_course():
    print("\n===== 任务5 综合选课处理 =====")
    class1 = [101, 103, 105, 107, 109, 103, 101]
    class2 = [102, 104, 106, 108, 109, 107, 102]

    # ① 保序去重，分别得到两个班不重复编号
    s1_ordered = list(dict.fromkeys(class1))
    s2_ordered = list(dict.fromkeys(class2))
    print("① 1班不重复编号（保序）：", s1_ordered)
    print("① 2班不重复编号（保序）：", s2_ordered)

    s1, s2 = set(class1), set(class2)

    # ② 同时选两门课：交集
    both = s1 & s2
    print("② 同时选两门课（交集）：", sorted(both))

    # ③ 只选其中一门：对称差
    only_one = s1 ^ s2
    print("③ 只选一门课（对称差）：", sorted(only_one))

    # ④ 选了1班没选2班：差集
    only_c1 = s1 - s2
    print("④ 只选1班（差集 s1 - s2）：", sorted(only_c1))

    # ⑤ 交集转元组
    t_both = tuple(both)
    print("⑤ 交集转元组：", t_both)
    # 元组内元素都是整数（可哈希），所以元组本身可哈希，还能再存入集合
    back_to_set = {t_both}
    print("⑥ 该元组再存入集合：", back_to_set)


# ========== 拓展：嵌套列表去重 ==========
def extra_nested_dedup():
    print("\n===== 拓展：嵌套列表去重 =====")
    nest = [[1, 2], [3, 4], [1, 2], [5, 6]]
    seen = set()
    result = []
    for item in nest:
        key = tuple(item)  # 内层 list 不可哈希，先转元组
        if key not in seen:
            seen.add(key)
            result.append(item)
    print("去重后嵌套列表：", result)


if __name__ == "__main__":
    task1_slice_delete()
    task2_hashable()
    task3_set_ops()
    task4_dedup()
    task5_course()
    extra_nested_dedup()
