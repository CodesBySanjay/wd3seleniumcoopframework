import pygame
import random

pygame.init()
size = 540
screen = pygame.display.set_mode((size, size + 60))
pygame.display.set_caption("Sudoku Generator & Solver")
font = pygame.font.SysFont("comicsans", 40)
font_small = pygame.font.SysFont("comicsans", 24)
font_large = pygame.font.SysFont("comicsans", 50)
cell_size = size // 9

grid = [[0 for _ in range(9)] for _ in range(9)]
original = [[0 for _ in range(9)] for _ in range(9)]
selected = None
check_popup = None

def draw_grid():
    for i in range(10):
        thick = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * cell_size), (size, i * cell_size), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, size), thick)

def draw_numbers():
    for i in range(9):
        for j in range(9):
            num = grid[i][j]
            if num != 0:
                color = (0, 0, 0) if original[i][j] != 0 else (0, 0, 200)
                text = font.render(str(num), True, color)
                screen.blit(text, (j * cell_size + 18, i * cell_size + 12))

def draw_selected():
    if selected:
        i, j = selected
        pygame.draw.rect(screen, (255, 0, 0), (j * cell_size, i * cell_size, cell_size, cell_size), 3)

def valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_x, box_y = row // 3 * 3, col // 3 * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if valid(board, i, j, num):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def check_solution(board):
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == 0 or not valid_for_check(board, i, j, num):
                return False
    return True

def valid_for_check(board, row, col, num):
    for i in range(9):
        if i != col and board[row][i] == num:
            return False
        if i != row and board[i][col] == num:
            return False
    box_x, box_y = row // 3 * 3, col // 3 * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if (i, j) != (row, col) and board[i][j] == num:
                return False
    return True

def fill_board(board):
    numbers = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                random.shuffle(numbers)
                for num in numbers:
                    if valid(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def remove_cells(board, attempts=40):
    count = 0
    while count < attempts:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if board[i][j] != 0:
            board[i][j] = 0
            count += 1

def generate_new_puzzle():
    global grid, original, check_popup
    full_grid = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(full_grid)
    puzzle = [row[:] for row in full_grid]
    remove_cells(puzzle, attempts=40)
    grid = [row[:] for row in puzzle]
    original = [row[:] for row in puzzle]
    check_popup = None

def draw_popup(message, color):
    popup_rect = pygame.Rect(90, 200, 360, 140)
    pygame.draw.rect(screen, (255, 255, 255), popup_rect)
    pygame.draw.rect(screen, color, popup_rect, 4)
    text = font_large.render(message, True, color)
    screen.blit(text, (popup_rect.centerx - text.get_width() // 2, popup_rect.y + 25))
    hint = font_small.render("Click anywhere to close", True, (80, 80, 80))
    screen.blit(hint, (popup_rect.centerx - hint.get_width() // 2, popup_rect.y + 90))

generate_new_puzzle()

running = True
while running:
    screen.fill((255, 255, 255))
    draw_grid()
    draw_numbers()
    draw_selected()
    msg = font_small.render("R: New | S: Solve | C: Check | Q: Quit", True, (50, 50, 50))
    screen.blit(msg, (size//2 - msg.get_width()//2, size + 15))

    if check_popup:
        draw_popup(*check_popup)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if check_popup:
                check_popup = None
            elif y < size:
                row = y // cell_size
                col = x // cell_size
                selected = (row, col)

        elif event.type == pygame.KEYDOWN and not check_popup:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_r:
                generate_new_puzzle()
                selected = None
            elif event.key == pygame.K_s:
                board_copy = [row[:] for row in grid]
                solve(board_copy)
                grid = board_copy
            elif event.key == pygame.K_c:
                correct = check_solution(grid)
                check_popup = ("Correct!" if correct else "Incorrect!", (0, 180, 0) if correct else (180, 0, 0))
            elif selected:
                i, j = selected
                if original[i][j] == 0:
                    if event.unicode.isdigit():
                        num = int(event.unicode)
                        grid[i][j] = num if 1 <= num <= 9 else 0
                    elif event.key in (pygame.K_BACKSPACE, pygame.K_DELETE, pygame.K_0):
                        grid[i][j] = 0

pygame.quit()
