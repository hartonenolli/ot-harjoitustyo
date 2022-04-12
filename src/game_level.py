from turtle import Turtle
import pygame
from sprites.White import White
from sprites.Nalle import Nalle
from sprites.Pupu import Pupu



class GameLevel:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.white = pygame.sprite.Group()
        self.nalle = pygame.sprite.Group()
        self.pupu = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.white.add(White(normalized_x, normalized_y))
                if cell == 1:
                    self.nalle.add(Nalle(normalized_x, normalized_y))
                if cell == 2:
                    self.pupu.add(Pupu(normalized_x, normalized_y))


        self.all_sprites.add(
            self.white,
            self.nalle,
            self.pupu
        )

    def handle_click(player, cordinates, position_map, game_map):
        value=[]
        for i, c in enumerate(position_map):
            for j, z in enumerate(c):
                if cordinates[0] > z[0] and cordinates[1] > z[1]:
                    value = [i,j]
        if game_map[value[0]][value[1]] != 0:
            return False
        game_map[value[0]][value[1]] = player

    def c_loze(game_map):
        for i, c in enumerate(game_map):
            for j, z in enumerate(c):
                if j < 3:
                    if c[j] == c[j+1] == c[j+2] and c[j] != 0:
                        return True
                    if i < 3:
                        if game_map[i][j] == game_map[i+1][j+1] == game_map[i+2][j+2] and game_map[i][j] != 0:
                            return True
                if i < 3:
                    if game_map[i][j] == game_map[i+1][j] == game_map[i+2][j] and game_map[i][j] != 0:
                        return True
                    if j > 1:
                        if game_map[i][j] == game_map[i+1][j-1] == game_map[i+2][j-2] and game_map[i][j] != 0:
                            return True
        return False

    def Lozer_info(player):
        print(player, "WON")
