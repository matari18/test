def knapsak_dynamic_pr(weights: list[int], values: list[int], max_weight: int) -> int:
    """
    Решение задачи о рюкзаке методом динамического программирования.
    :param weights: массив весов предметов.
    :param values: массив ценностей предметов.
    :param max_weight: максимальная вместимость рюкзака.
    :return: максимальная ценность, которую можно уместить в рюкзак.
    """

    matrix = [[0 for x in range(max_weight + 1)] for y in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        value = values[i - 1]
        weight = weights[i - 1]

        for j in range(1, max_weight + 1):
            matrix[i][j] = matrix[i - 1][j]

            if j >= weight and matrix[i - 1][j - weight] + value > matrix[i][j]:
                matrix[i][j] = max(matrix[i][j], matrix[i - 1][j - weight] + value)

    return matrix[-1][-1]


# Проверка
w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
k = 5
print(knapsak_dynamic_pr(w, v, k))
