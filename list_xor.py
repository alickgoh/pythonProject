def list_xor(n, list1, list2):
    n_list = []
    m_list = []
    max_list1 = max(list1)
    max_list2 = max(list2)

    for i in range(len(list1)):
        if list1[i] == n:
            n_list.append(n)
        set(n_list)

    for z in range(len(list2)):
        if list2[z] == n:
            m_list.append(n)

    for k in range(max_list1 + max_list2):
        if n_list[k] == m_list[k]:
            return False

    if len(n_list) == 1:
        return True
    elif len(n_list) == 0:
        return False


print(list_xor(1, [1, 2, 3], [4, 5, 6]))
