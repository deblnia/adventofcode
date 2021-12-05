from typing import List, Set, Iterable

input_file = "./inputs/day4.txt"

boards = []
with open(input_file, "r") as f:

    # first line -- readline singular  
    called_numbers = [int(x) for x in f.readline().strip().split(",")]

    # boards 
    board = []
    for line in f.readlines()[1:]:
        line = line.strip()
        if line:
            board.append([int(x) for x in line.split()])
        else: # blank line between boards 
            boards.append(board)
            board = []

# part 1 

def winning_board(bingo_board: Iterable [Iterable[int]], called_nums: Iterable[int]): 
    called_numbers = set(called_nums)
    # rows  
    for row in bingo_board:  
        if len(called_numbers.intersection(row)) == 5: 
            return True 
    # cols -- we know boards are 5x5 
    for l in range(5):
        col = [row[l] for row in bingo_board] 
        if len(called_numbers.intersection(col)) == 5: 
            return True 
    return False 

def find_score(bingo_board: Iterable[Iterable[int]], called_nums: Iterable[int]):
    flat = set(sum(bingo_board, []))                   
    unmarked_numbers = flat.difference(called_nums)
    winning_number = called_nums[-1]                          
    return sum(unmarked_numbers) * winning_number

drawn = []
for number in called_numbers:
    drawn.append(number)

# finding winning boards 
    winning_boards = [b for b in boards if winning_board(b, drawn)]
    
    if len(winning_boards) >= 1:
        winning_field = winning_boards[0]
        winning_number = number
        break

result = find_score(winning_field, called_numbers)

print(f'part 1: {result}')
assert(result == 33348)

# part 2 

drawn_numbers = called_numbers

winning_boards = [board for board in boards if winning_board(board, drawn_numbers)]

for i in range(len(boards) - 2, 0, -1):
    drawn_numbers = boards[:i]
    losing_boards = [x for x in winning_boards if not winning_board(x, drawn_numbers)]
    
    if len(losing_boards) >= 1:
        last_winning_field = losing_boards[0]
        winning_drawn_numbers = boards[:i + 1]
        break
    

result = find_score(last_winning_field, winning_drawn_numbers)

print(f'part 2: {result}')