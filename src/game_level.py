import pygame
from sprites.sprite_kuvat import Spritet


class GameLevel:
    def __init__(self, level_map, cell_size):
        """Alustetaan kuvat, jota pelissä käytetään
        Kutsutaan sen jälkeen spritejen alustavaa funktiota"""
        self.cell_size = cell_size
        self.white = pygame.sprite.Group()
        self.nalle = pygame.sprite.Group()
        self.pupu = pygame.sprite.Group()
        self.pojanamongus = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.initialize_sprites(level_map)

    def initialize_sprites(self, level_map):
        """Kuvien asettaminen pelikentälle
        Tarkastetaan annetun pelikentän kaikki arvot

        Arvo voi olla 0, 1, 2 tai 3
        Jokaiselle arvolle on oma kuva ja se lisätään kohtaan
        Kutsutaan GameLevel luokan perivää kuvaa arvoilla"""
        height = len(level_map)
        width = len(level_map[0])

        for y_hight in range(height):
            for x_widht in range(width):
                cell = level_map[y_hight][x_widht]
                normalized_x = x_widht * self.cell_size
                normalized_y = y_hight * self.cell_size

                if cell == 0:
                    self.white.add(Spritet("white.jpg", normalized_x, normalized_y))
                if cell == 1:
                    self.nalle.add(Spritet("nalle.jpg", normalized_x, normalized_y))
                if cell == 2:
                    self.pupu.add(Spritet("pupu.jpg", normalized_x, normalized_y))
                if cell == 3:
                    self.pojanamongus.add(
                        Spritet("pojanamongus.jpg", normalized_x, normalized_y))

        self.all_sprites.add(
            self.white,
            self.nalle,
            self.pupu,
            self.pojanamongus
        )

    def handle_click(self, player, cordinates, position_map, game_map):
        """Tarkastetaan onko annetussa ruudussa arvo 0

        Jos 0:
            palautetaan pelikartta
        Jos 1, 2 tai 3:
            palautetaan False
        """
        value = []
        for position_indx, position_list in enumerate(position_map):
            for symbol_indx, position_symbol in enumerate(position_list):
                if cordinates[0] >= position_symbol[0] and cordinates[1] >= position_symbol[1]:
                    value = [position_indx, symbol_indx]
        if game_map[value[0]][value[1]] != 0:
            return False
        game_map[value[0]][value[1]] = player
        return (value[0], value[1])

    def chek_loze(self, game_map):
        """Tarkastetaan onko häviäjää
        Käydään läpi jokainen kohta pelilaudalla
        Kutsutaan ja tarkastetaan: return_funktion_for_chek

        Jos True:
            palautetaan True
        Muuten:
            palautetaan False"""
        for position_indx, position_list in enumerate(game_map):
            for symbol_indx, _ in enumerate(position_list):
                if self.return_function_for_chek(self, game_map, position_list,
                                                 symbol_indx, position_indx) is True:
                    return True

        return False

    def return_function_for_chek(self, game_map, position_list, symbol_indx, position_indx):
        """Tarkastetaan kaikki eri vaihtoehdot häviämisen varalta
        Kolmen suora vaakaan, pystyyn tai vinoon

        Jos kaikki kolme on samoja palautetaan True

        Muuten palautetaan False"""
        if position_list[symbol_indx] == 0:
            return False
        if symbol_indx < len(position_list)-2:
            if (position_list[symbol_indx] ==
                position_list[symbol_indx+1] ==
                    position_list[symbol_indx+2]):
                return True
            if position_indx < 3:
                if (game_map[position_indx][symbol_indx] ==
                    game_map[position_indx+1][symbol_indx+1] ==
                        game_map[position_indx+2][symbol_indx+2]):
                    return True

        if position_indx < 3:
            if (game_map[position_indx][symbol_indx] ==
                game_map[position_indx+1][symbol_indx] ==
                    game_map[position_indx+2][symbol_indx]):
                return True
            if symbol_indx > 1:
                if (game_map[position_indx][symbol_indx] ==
                    game_map[position_indx+1][symbol_indx-1] ==
                        game_map[position_indx+2][symbol_indx-2]):
                    return True
        return False
