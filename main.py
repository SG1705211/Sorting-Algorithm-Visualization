import pygame
import random

# Button Setting,
BUTTON = {"width": 170, "height": 40, "border": 5, "radius": 2, "colour": [0, 0, 0]}

# Window Size
WINDOW_WIDTH = 1210
WINDOW_HEIGHT = 800

# Information for button
class ClickButton():
    def __init__(self, x, y, text):
        """
        :param x: int
        :param y: int
        :param text: str
        """
        self.x = x
        self.y = y
        self.text = text

    # draw function draws the whole button on the screen.
    def draw(self, win):
        # current rectagle
        rec = pygame.Rect(self.x, self.y, BUTTON["width"], BUTTON["height"])
        pygame.draw.rect(win, BUTTON["colour"], rec, BUTTON["border"], BUTTON["radius"])
        # to display the text.
        font = pygame.font.SysFont('Lato', 30)
        font_surface = font.render(self.text, True, (0, 0, 0))
        # to center the text, calculate the true coordinate.
        font_x = self.x + BUTTON["width"] / 2 - font_surface.get_width() / 2
        font_y = self.y + BUTTON["height"] / 2 - font_surface.get_height() / 2
        win.blit(font_surface, (font_x, font_y))

    def whether_hover(self, pos):
        if self.x < pos[0] < self.x + BUTTON["width"] and self.y < pos[1] < self.y + BUTTON["height"]:
            return True

        return False


# ------------------------------------------------------------
# Sorting Algorithem

def merge(dest, lis1, lis2, main_window, button_list, left_over):
    clock = pygame.time.Clock()
    pos1 = 0
    pos2 = 0
    len1 = len(lis1)
    len2 = len(lis2)
    for each_num in range(len1 + len2):
        clock.tick(30)
        if pos1 == len1 or (pos2 < len2 and lis1[pos1] > lis2[pos2]):
            dest[each_num] = lis2[pos2]
            total = lis1 + lis2 + left_over
            whole_list(main_window, total, button_list, {str(each_num): [153, 0, 0], str(pos2): [102, 204, 0]})
            pos2 += 1
        else:
            dest[each_num] = lis1[pos1]
            total = lis1 + lis2 + left_over
            whole_list(main_window, total, button_list, {str(each_num): [153, 0, 0], str(pos1): [102, 204, 0]})
            pos1 += 1


def mergesort(lis, window, button_list, left_over):
    each_len = len(lis)
    if each_len <= 1:
        return
    left_len = int(each_len / 2)
    right_len = each_len - left_len
    left = lis[:int(each_len / 2)]
    right = lis[int(each_len / 2):]
    mergesort(left, window, button_list, right + left_over)
    mergesort(right, window, button_list, left + left_over)
    merge(lis, left, right, window, button_list, left_over)


def selection_sort(lis, main_window, button_list):
    clock = pygame.time.Clock()
    lis_len = len(lis)
    for i in range(lis_len):
        clock.tick(15)
        pos = i
        for j in range(i + 1, lis_len):
            if lis[pos] > lis[j]:
                pos = j
        lis[i], lis[pos] = lis[pos], lis[i]
        # redraw the graph
        whole_list(main_window, lis, button_list, {str(i): [153, 0, 0], str(pos): [102, 204, 0]})


def insertionSort(lis, window, button_list):
    lis_len = len(lis)
    clock = pygame.time.Clock()
    for i in range(lis_len):
        j = i
        while j > 0 and lis[j - 1] > lis[j]:
            clock.tick(300)
            lis[j], lis[j - 1] = lis[j - 1], lis[j]
            whole_list(window, lis, button_list, {str(j): [153, 0, 0], str(j - 1): [102, 204, 0]})
            j -= 1


# random_list_generator() generates a random list of size 30
def random_list_generator():
    base_list = [0] * 60
    for each_num in range(60):
        base_list[each_num] = random.randint(1, 100)
    return base_list


# whole_list() prints the random list on the screen
def whole_list(window, random_list, button_list, special_index):
    # base dimension of each rectangle
    base_width = 10
    base_height = 5
    main_colour = [255, 255, 255]  # white
    # draw the background colour
    window.fill(main_colour)
    # the top text
    font = pygame.font.SysFont('Lato', 50)
    font_surface = font.render("The Sorting Algorithm Visualization", True, (0, 0, 0))
    font_x = WINDOW_WIDTH / 2 - font_surface.get_width() / 2
    font_y = 50
    window.blit(font_surface, (font_x, font_y))
    # draw the clickable button
    for each_button in button_list:
        each_button.draw(window)
    # draw the rectangle of list.
    for index, each_num in enumerate(random_list):
        rec_colour = [68, 144, 196]  # indigo
        # each little rectangle
        each_rect = pygame.Rect(10 + (base_width + 10) * index, 800 - each_num * base_height, base_width,
                                each_num * base_height)
        # change the colour if the index is special index.
        if str(index) in special_index:
            rec_colour = special_index[str(index)]
        pygame.draw.rect(window, rec_colour, each_rect, 0, 2)
    pygame.display.update()


def main():
    pygame.init()
    # initialization.
    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sorting Visualization")
    clock = pygame.time.Clock()

    # main loop
    run = True
    # The random list
    random_list = random_list_generator()
    # The button
    merge_button = ClickButton(180, 140, "Merge Sort")
    selection_button = ClickButton(820, 140, "Selection Sort")
    quicksort_button = ClickButton(500, 140, "Quick Sort")
    button_list = [merge_button, selection_button, quicksort_button]
    # draw the whole list
    whole_list(main_window, random_list, button_list, {})
    while run:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            # control the speed
            # sorting
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selection_button.whether_hover(pos):
                    whole_list(main_window, random_list, button_list, {})
                    selection_sort(random_list, main_window, button_list)
                    random_list = random_list_generator()
                    pygame.display.update()
                if merge_button.whether_hover(pos):
                    whole_list(main_window, random_list, button_list, {})
                    mergesort(random_list, main_window, button_list, [])
                    whole_list(main_window, random_list, button_list, {})
                    random_list = random_list_generator()
                if quicksort_button.whether_hover(pos):
                    whole_list(main_window, random_list, button_list, {})
                    insertionSort(random_list, main_window, button_list)
                    random_list = random_list_generator()
                pygame.display.update()
    pygame.quit()


main()
