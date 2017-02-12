def diagonal_reverse(matr):
    return [[x[i] for x in matr] for i in range(len(matr[0]))]


def input_matrix():
    try:
        n = int(raw_input("Enter matrix size \n"))
        matrix = []
        for i in range(0, n):
            line = raw_input()
            new_row = [elem for elem in line.split(',')]
            if len(new_row) > n:
                raise ValueError
            matrix.append(new_row)
    except ValueError:
        print "Incorect matrix size"
    return matrix

def print_result(result):
    matr = diagonal_reverse(result)
    for i in matr:
        print i

if __name__ == "__main__":
    data = input_matrix()
    print_result(data)