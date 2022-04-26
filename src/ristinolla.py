import webbrowser
import pygame
from game_level import GameLevel


class Ristinolla:
    def __init__(self):
        self.level_map = [[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]]

        self.position_map = [[(0, 0), (200, 0), (400, 0), (600, 0), (800, 0)],
                             [(0, 200), (200, 200), (400, 200),
                              (600, 200), (800, 200)],
                             [(0, 400), (200, 400), (400, 400),
                              (600, 400), (800, 400)],
                             [(0, 600), (200, 600), (400, 600),
                              (600, 600), (800, 600)],
                             [(0, 800), (200, 800), (400, 800),
                              (600, 800), (800, 800)],
                             ]

        self.cell_sizes = 200

        height = len(self.level_map)
        width = len(self.level_map[0])

        self.display_height = height * self.cell_sizes
        self.display_width = width * self.cell_sizes

        self.running = True

    def main(self, player):

        display = pygame.display.set_mode(
            (self.display_width, self.display_height))

        pygame.display.set_caption("Ristinolla")

        level = GameLevel(self.level_map, self.cell_sizes)

        clock = pygame.time.Clock()

        level.all_sprites.draw(display)

        if GameLevel.c_loze(GameLevel, self.level_map) is True:
            display = pygame.display.set_mode(
                (self.display_width, self.display_height))
            display.fill((255, 255, 255))
            font = pygame.font.SysFont("Comic Sans MS", 30)
            display.blit(font.render("PLAYER " + str(player) + " WON",
                         True, (0, 0, 0)), (self.display_width//2, self.display_height//2))
            pygame.display.update()
            pygame.time.wait(6000)
            self.level_map = [[0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]]
            self.start_screen()

        while self.running:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if GameLevel.handle_click(GameLevel, player, pos, self.position_map, self.level_map) is False:
                        continue
                    if player == 1:
                        self.main(2)
                    else:
                        self.main(1)

            pygame.display.update()

        pygame.quit()

    def start_screen(self):

        screen = pygame.display.set_mode(
            (self.display_width, self.display_height))
        pygame.display.set_caption("Alkuruutu")

        pygame.init()

        font = pygame.font.SysFont("Comic Sans MS", 30)

        game_begin = font.render("START GAME: PRESS G", True, (255, 255, 255))
        screen.blit(game_begin, (300, 200))
        wiki_w = font.render("TO WIKI: PRESS W", True, (255, 255, 255))
        screen.blit(wiki_w, (300, 240))
        instructions = font.render(
            "TRY NOT TO GET 3 IN LINE", True, (255, 255, 255))
        screen.blit(instructions, (300, 280))
        exit = font.render("TO EXIT: PRESS E", True, (255, 255, 255))
        screen.blit(exit, (300, 320))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        self.main(1)
                    if event.key == pygame.K_w:
                        webbrowser.open(
                            r"https://en.wikipedia.org/wiki/Tic-tac-toe")
                    if event.key == pygame.K_e:
                        self.running = False

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    Ristinolla().start_screen()
