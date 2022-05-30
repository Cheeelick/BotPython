def f(lul):
    n = []
    for i in lul:
        if i not in n and i[0] is not None:
            n.append(i)
    return n


# можно оптимизировать
def trans(matrix):
    trans_matrix = [[0 for j in range(len(matrix))]
                    for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


def main(matrix):
    matrix = f(matrix)
    trans_matrix = trans(matrix)
    trans_matrix = f(trans_matrix)
    matrix = trans(trans_matrix)
    for i in range(len(matrix)):
        matrix[i][0] = matrix[i][0].split(' ')
        matrix[i][0] = \
            matrix[i][0][2] + ' ' + matrix[i][0][0][0] + '.' + matrix[i][0][1]
        matrix[i][1] = matrix[i][1].replace('\n', '')
        matrix[i][1] = matrix[i][1].replace('-', '/')
        matrix[i][2] = \
            matrix[i][2][3:6] + matrix[i][2][7:10] + matrix[i][2][-4:]
    return matrix


if __name__ == '__main__':
    print(main(
        [[None, None, None, None, None],
         ['Иван Ч. Шевко', None, '00-04-25', '00-04-25', '+7 911 959-5554'],
         ['Мирон Н. Сетяк', None, '00-10-22', '00-10-22', '+7 029 473-4893'],
         ['Айдар Ц. Воробий', None, '01-04-06', '01-04-06', '+7 302 344-3547'],
         ['Иван Ч. Шевко', None, '00-04-25', '00-04-25', '+7 911 959-5554'],
         [None, None, None, None, None],
         ['Арсений Ф. Сисибян', None, '03-08-11', '03-08-11', '+7 389 449-2981']]
    ))
