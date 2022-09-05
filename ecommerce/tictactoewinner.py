# def winner_check(list_num):
#     first_list = list_num[0]
#     second_list = list_num[1]
#     third_list = list_num[2]
#     if (first_list[0] and first_list[1] and first_list[2]) \
#             or (first_list[0] and second_list[0] and third_list[0]) \
#             or (first_list[0] and second_list[1] and third_list[2]) == 1:
#         print("Player 1 is winner")
#
#
# winner_is_1 = [[1, 0, 0],
#                [1, 0, 0],
#                [1, 0, 0]]
# winner_check(winner_is_1)


def winner(game):
    for row in game:
        if game[0] == game[1] == game[2] != 0:
            print('Player %i wins' % row[0])
            return

    return print("no winner")


game = [[1, 1, 0],
        [1, 2, 0],
        [1, 1, 0]]

winner(game)