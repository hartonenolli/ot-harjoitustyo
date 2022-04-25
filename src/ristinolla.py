import pygame
from game_level import GameLevel
class Ristinolla:
    def __init__(self):
        self.LEVEL_MAP = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]

        self.POSITION_MAP = [[(0,0),(200,0),(400,0),(600,0),(800,0)],
                        [(0,200),(200,200),(400,200),(600,200),(800,200)],
                        [(0,400),(200,400),(400,400),(600,400),(800,400)],
                        [(0,600),(200,600),(400,600),(600,600),(800,600)],
                        [(0,800),(200,800),(400,800),(600,800),(800,800)],
                        ]

        self.CELL_SIZE = 200

    def main(self,player):
        height = len(self.LEVEL_MAP)
        width = len(self.LEVEL_MAP[0])
        display_height = height * self.CELL_SIZE
        display_width = width * self.CELL_SIZE

        display = pygame.display.set_mode((display_width, display_height))

        pygame.display.set_caption("Ristinolla")

        level = GameLevel(self.LEVEL_MAP, self.CELL_SIZE)

        pygame.init()

        clock = pygame.time.Clock()

        level.all_sprites.draw(display)
        
        running = True

        if GameLevel.c_loze(GameLevel, self.LEVEL_MAP) == True:
            display = pygame.display.set_mode((display_width, display_height))
            font = pygame.font.SysFont("Arial", 30)
            display.fill((255,255,255))
            display.blit(font.render("PLAYER " + str(player) + " WON", True, (0, 0, 0)), (display_width//2, display_height//2))
            

        while running:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if GameLevel.handle_click(GameLevel, player, pos, self.POSITION_MAP, self.LEVEL_MAP) == False:
                        continue
                    if player == 1:
                        self.main(2)
                    else:
                        self.main(1)

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    Ristinolla().main(1)
