import random

ALLOWED_FIELD_VALUES = ['11', '12', '13', '21', '22', '23', '31', '32', '33']


def empty_board():
    board = {
        '1': {'1': ' ', '2': ' ', '3': ' '},
        '2': {'1': ' ', '2': ' ', '3': ' '},
        '3': {'1': ' ', '2': ' ', '3': ' '}
    }
    return board


def show_board(input_board):
    f = 'Aktualna plansza:\n'
    for k, v in input_board.items():
        if k != '1':
            f += "----------\n"
        f += f"{v['1']} | {v['2']} | {v['3']}\n"
    return f


def show_field_numbers(input_board):
    f = 'Numeracja planszy:\n'
    for k, v in input_board.items():
        if k != '1':
            f += "------------\n"
        f += f"{k}1 | {k}2 | {k}3\n"
    return f


def is_chosen_field_taken(input_board, input_field_nr):
    input_field_row = input_field_nr[0]
    input_field_col = input_field_nr[1]

    if input_board[input_field_row][input_field_col] != ' ':
        return True
    return False


def choose_field(input_board, input_field_nr, sign):
    input_field_row = input_field_nr[0]
    input_field_col = input_field_nr[1]
    input_board[input_field_row][input_field_col] = sign


def is_game_finished(input_board, input_game_mode):
    number_of_empty_fields = 9
    for r in input_board.values():
        for f in r.values():
            if f != ' ':
                number_of_empty_fields -= 1
                if number_of_empty_fields <= 0:
                    return {'finished': True, 'message': 'Remis!'}

    for sign in ['X', 'O']:
        if ((input_board['1']['1'] == sign and input_board['1']['2'] == sign and input_board['1']['3'] == sign) or
                (input_board['2']['1'] == sign and input_board['2']['2'] == sign and input_board['2'][
                    '3'] == sign) or
                (input_board['3']['1'] == sign and input_board['3']['2'] == sign and input_board['3'][
                    '3'] == sign) or
                (input_board['1']['1'] == sign and input_board['2']['1'] == sign and input_board['3'][
                    '1'] == sign) or
                (input_board['1']['2'] == sign and input_board['2']['2'] == sign and input_board['3'][
                    '2'] == sign) or
                (input_board['1']['3'] == sign and input_board['2']['3'] == sign and input_board['3'][
                    '3'] == sign) or
                (input_board['1']['1'] == sign and input_board['2']['2'] == sign and input_board['3'][
                    '3'] == sign) or
                (input_board['1']['3'] == sign and input_board['2']['2'] == sign and input_board['3'][
                    '1'] == sign)):
            if input_game_mode == 1:
                if sign == 'X':
                    return {'finished': True, 'message': 'Wygrałeś!'}
                elif sign == 'O':
                    return {'finished': True, 'message': 'Przegrałeś...'}
            elif input_game_mode == 2:
                if sign == 'X':
                    return {'finished': True, 'message': 'Gracz nr 1 (X) zwycięża!'}
                elif sign == 'O':
                    return {'finished': True, 'message': 'Gracz nr 2 (O) zwycięża!'}
    return {'finished': False, 'message': ''}


def randomize_field_number(input_board):
    while True:
        randomized_field_nr = random.choice(ALLOWED_FIELD_VALUES)
        if input_board[randomized_field_nr[0]][randomized_field_nr[1]] == ' ':
            return randomized_field_nr
