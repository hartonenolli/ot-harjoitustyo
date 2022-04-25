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

        for y_hight in range(height):
            for x_widht in range(width):
                cell = level_map[y_hight][x_widht]
                normalized_x = x_widht * self.cell_size
                normalized_y = y_hight * self.cell_size

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

    def handle_click(self, player, cordinates, position_map, game_map):
        value=[]
        for position_indx, position_list in enumerate(position_map):
            for symbol_indx, position_symbol in enumerate(position_list):
                if cordinates[0] > position_symbol[0] and cordinates[1] > position_symbol[1]:
                    value = [position_indx,symbol_indx]
        if game_map[value[0]][value[1]] != 0:
            return False
        game_map[value[0]][value[1]] = player
        return game_map

    def c_loze(self, game_map):
        for position_indx, position_list in enumerate(game_map):
            for symbol_indx, _ in enumerate(position_list):
                if symbol_indx < 3:
                    if position_list[symbol_indx] == position_list[symbol_indx+1] == position_list[symbol_indx+2] and position_list[symbol_indx] != 0:
                        return True
                    if position_indx < 3:
                        if game_map[position_indx][symbol_indx] == game_map[position_indx+1][symbol_indx+1] == game_map[position_indx+2][symbol_indx+2] and game_map[position_indx][symbol_indx] != 0:
                            return True
                if position_indx < 3:
                    if game_map[position_indx][symbol_indx] == game_map[position_indx+1][symbol_indx] == game_map[position_indx+2][symbol_indx] and game_map[position_indx][symbol_indx] != 0:
                        return True
                    if symbol_indx > 1:
                        if game_map[position_indx][symbol_indx] == game_map[position_indx+1][symbol_indx-1] == game_map[position_indx+2][symbol_indx-2] and game_map[position_indx][symbol_indx] != 0:
                            return True
        return False
