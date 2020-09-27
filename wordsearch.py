# Assumption 1 : Board has only alphabets and blanks. Checks are not performed for special / numeric characters.
# Assumption 2 : Input is in n*n format.
# Assumption 3 : Board characters and wordlist are provided as input.

# Input
wordlist = ['cat','bat','raw','at','war','tab']

board = (
        ['c','a','t'],
        ['b','a','t'],
        ['r','a','w']
)

try :
    board_length = len(board)
    words_found = []
    # Problem statement mentions Straight line hence diagonal parsing is not implemented

    for i in range(board_length):
        for row in range(board_length):
            vertical_word,horizontal_word,reverse_vertical_word,reverse_horizontal_word  = '','','',''
            for col in range(board_length-i):
                vertical_word  = vertical_word + (board[col+i][row])
                horizontal_word = horizontal_word + (board[row][col+i])
                reverse_vertical_word = reverse_vertical_word + (board[board_length - col -1 -i][board_length - row -1 -i])
                reverse_horizontal_word = reverse_horizontal_word + (board[board_length - row - 1-i][board_length - col - 1-i])

                if vertical_word in wordlist:
                    words_found.append(vertical_word)
                if horizontal_word in wordlist:
                    words_found.append(horizontal_word)
                if reverse_vertical_word in wordlist:
                    words_found.append(reverse_vertical_word)
                if reverse_horizontal_word in wordlist:
                    words_found.append(reverse_horizontal_word)
    words_found_set = set(words_found)
    unique_words_found = list(words_found_set)

    print (unique_words_found)
except :
    raise

# Note : No separate processing is required for blanks as words with blanks will not be part of word list.