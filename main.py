import time

from exceptions import IncorrectInput, FieldTaken
from functions import show_field_numbers, ALLOWED_FIELD_VALUES, is_chosen_field_taken, choose_field, show_board, \
    is_game_finished, randomize_field_number, empty_board

QUIT = False
while not QUIT:
    board = empty_board()
    print('Wybierz tryb gry, 1 (przeciw komputerowi), 2 (przeciw drugiemu graczowi), 0 (zakończ program)')
    try:
        game_mode = input().strip()
        if game_mode != '1' and game_mode != '2' and game_mode != '0':
            raise IncorrectInput()
        game_mode = int(game_mode)

        if game_mode == 0:
            print('Kończę program.')
            QUIT = True
    except IncorrectInput as e:
        print(e)
    else:
        if not QUIT:
            print(show_field_numbers(board))

            current_sign = 'X'
            game_finished = False
            while not game_finished:
                field_chosen = False
                while not field_chosen:
                    print(f'Podaj numer pola, gdzie wstawić "{current_sign}":')
                    try:
                        field_nr = input()
                        if field_nr not in ALLOWED_FIELD_VALUES:
                            raise IncorrectInput()
                        if is_chosen_field_taken(board, field_nr):
                            raise FieldTaken()
                    except IncorrectInput as e:
                        print(e)
                    except FieldTaken as e:
                        print(e)
                    else:
                        field_chosen = True
                        choose_field(board, field_nr, current_sign)
                        print(show_board(board))
                        result = is_game_finished(board, game_mode)
                        if result['finished']:
                            print(result['message'])
                            game_finished = True

                        if not game_finished:
                            if game_mode == 2:
                                if current_sign == 'X':
                                    current_sign = 'O'
                                else:
                                    current_sign = 'X'
                            elif game_mode == 1:
                                print('Komputer myśli...')
                                time.sleep(1)
                                field_nr = randomize_field_number(board)
                                choose_field(board, field_nr, 'O')
                                print(f'Komputer wybrał pole nr "{field_nr}"')
                                print(show_board(board))
                                result = is_game_finished(board, game_mode)
                                if result['finished']:
                                    print(result['message'])
                                    game_finished = True
