# matrix creation
matrix = [['-'] * 3,
          ['-'] * 3,
          ['-'] * 3, ]


# matrix func
def objectmatrix(f):
    print("  0 1 2")
    for i in range(len(matrix)):
        print(str(i), *matrix[i])


objectmatrix(matrix)


def usersinput(f):
    while True:
        global x, y
        place = input('coordinates:').split()
        if len(place) != 2:
            print('need two coordinates (write with spacebar)')
            continue

        if not (place[0].isdigit() and place[1].isdigit()):
            print('only numbers is allowed.')
            continue

        x, y = map(int, place)

        if not (0 <= x < 3 and 0 <= y < 3):
            print('you are out of range. Numbers from 0 to 2 are accepted')
            continue

        if f[x][y] != '-':
            print('cell is occupied')
            continue
        break
    return x, y


usersinput(matrix)


def win(f, user):
    def check(cell1, cell2, cell3, user):
        if cell1 == user and cell2 == user and cell3 == user:
            return True

    for n in range(3):
        if check(f[n][0], f[n][1], f[n][2], user) or check(f[0][n], f[1][n], f[2][n], user) \
                or check(f[0][0], f[1][1], f[2][2], user) or check(f[2][0], f[1][1], f[0][2], user):
            return True
    return False


counter = 0
while True:
    counter = counter + 1
    if counter % 2 == 0:
        print('x turn')
        user = 'x'
    else:
        user = '0'
        print('0 turn')
    objectmatrix(matrix)
    x, y = usersinput(matrix)
    matrix[x][y] = user
    if counter == 9:
        objectmatrix(matrix)
        print('tie')
        break
    if win(matrix, user):
        objectmatrix(matrix)
        print(user, 'win')
        break
