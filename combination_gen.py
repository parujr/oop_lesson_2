import copy

def gen_comb_list(list_set):
    '''
        Parameters:
            list_set: a list of lists where each contains at least one element

        Returns:
            a list of lists, each of which is made from a combination of elements in each list in list_set

        Examples:
            gen_comb_list([[1, 2, 3]]) returns [[1], [2], [3]]
            gen_comb_list([[1, 2, 3], [4, 5]]) returns [[1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5]]
            gen_comb_list(
            [[1, 2, 3], [4, 5], [6, 7, 8]]
            )


            from
            [[1, 2, 3],
            [4, 5],
            [6, 7, 8]]

            returns
            [1, 4, 6], list_set[0][0], list_set[1][0], list_set[2][0]
            [2, 4, 6], list_set[0][1], list_set[1][0], list_set[2][0]
            [3, 4, 6], list_set[0][2], list_set[1][0], list_set[2][0]

            [1, 5, 6], list_set[0][0], list_set[1][1], list_set[2][0]
            [2, 5, 6], list_set[0][1], list_set[1][1], list_set[2][0]
            [3, 5, 6], list_set[0][2], list_set[1][1], list_set[2][0]

            [1, 4, 7], list_set[0][0], list_set[1][0], list_set[2][1]
            [2, 4, 7], list_set[0][1], list_set[1][0], list_set[2][1]
            [3, 4, 7], list_set[0][2], list_set[1][0], list_set[2][1]

            [1, 5, 7], list_set[0][0], list_set[1][1], list_set[2][1]
            [2, 5, 7], list_set[0][1], list_set[1][1], list_set[2][1]
            [3, 5, 7], list_set[0][2], list_set[1][1], list_set[2][1]

            [1, 4, 8], list_set[0][0], list_set[1][0], list_set[2][2]
            [2, 4, 8], list_set[0][1], list_set[1][0], list_set[2][2]
            [3, 4, 8], list_set[0][2], list_set[1][0], list_set[2][2]

            [1, 5, 8], list_set[0][0], list_set[1][1], list_set[2][2]
            [2, 5, 8], list_set[0][1], list_set[1][1], list_set[2][2]
            [3, 5, 8]] list_set[0][2], list_set[1][1], list_set[2][2]
    '''

    if len(list_set) == 1:
        start_list = []
        for item in list_set[0]:
            start_list.append([item])
        return start_list
    comb_list_temp = gen_comb_list(list_set[0:-1])
    start_list = []
    for list_item in comb_list_temp:
        for val in list_set[-1]:
            temp_item = copy.deepcopy(list_item)
            temp_item.append(val)
            start_list.append(temp_item)
    return start_list


