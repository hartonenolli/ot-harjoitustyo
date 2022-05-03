import webbrowser
import pygame
from game_level import GameLevel


class Ristinolla:
    def __init__(self):
        """Alustaa pelikentän, sisältää tietoa kuvien koordinaateista,
        pelin kulun seuranta ja kolminpelin valinta.
        """
        self.level_map = [[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]]

        self.level_map_vii = [[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0]]

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

        self.position_map_vii = [[(0, 0), (200, 0), (400, 0), (600, 0), (800, 0),
                                (1000, 0), (1200, 0)],
                                 [(0, 200), (200, 200), (400, 200),
                                  (600, 200), (800, 200), (1000, 200), (1200, 200)],
                                 [(0, 400), (200, 400), (400, 400),
                                  (600, 400), (800, 400), (1000, 400), (1200, 400)],
                                 [(0, 600), (200, 600), (400, 600),
                                  (600, 600), (800, 600), (1000, 600), (1200, 600)],
                                 [(0, 800), (200, 800), (400, 800),
                                  (600, 800), (800, 800), (1000, 800), (1200, 800)],
                                 ]

        self.cell_sizes = 200

        height = len(self.level_map)
        width = len(self.level_map[0])

        self.display_height = height * self.cell_sizes
        self.display_width = width * self.cell_sizes

        self.running = True

        self.three_player = False

    def main(self, player):
        """Pääohjelma, jossa kello käy silmukan sisällä.
        Kutsutaan apufuntioita tarkastamaan peliruutu,
        klikkauksen käsittely, tarkastetaan häviäjä ja seuraava vuoro.

        Args:
            player: 1, 2 tai 3
        """
        self.screen_setup(player)

        clock = pygame.time.Clock()

        while self.running:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if self.to_handle_click(player, pos) is False:
                        continue
                    self.time_to_chek_for_lozer(player)
                    self.next_turn(player)

            pygame.display.update()

        pygame.quit()

    def to_handle_click(self, player, pos):
        """Apufunktio, jolla ohjataan GameLevel luokaan klikkauksen tarkastusta varten.
        Tarkastetaan onko kolme pelaajaa vai kaksi.

        Args:
            player: 1,2 tai 3
            pos: (x-koordinaatit, y-koordinaatit)

        Returns: GameLevel luokasta False tai Peliruudukon
        """
        if self.three_player is False:
            return GameLevel.handle_click(GameLevel, player, pos, self.position_map,
                                          self.level_map)
        return GameLevel.handle_click(GameLevel, player, pos, self.position_map_vii,
                                      self.level_map_vii)

    def screen_setup(self, player):
        """Alustaa peliruudukon joko 5x5 tai 7x5 kokoiseksi
        Kertoo minkä pelaajan vuoro"""
        if self.three_player is False:
            display = pygame.display.set_mode(
                (self.display_width, self.display_height))
            pygame.display.set_caption(str(player) + " TURN")
            level = GameLevel(self.level_map, self.cell_sizes)
            level.all_sprites.draw(display)
            return

        display = pygame.display.set_mode(
            (7 * self.cell_sizes, 5 * self.cell_sizes))
        pygame.display.set_caption(str(player) + " TURN")
        level = GameLevel(self.level_map_vii, self.cell_sizes)
        level.all_sprites.draw(display)

    def time_to_chek_for_lozer(self, player):
        """Kutsuu GameLevel luokan apufunktioita
        Funtioissa tarkastetaan: onko häviäjää

        Args:
            player: 1, 2 tai 3
        """
        if self.three_player is False:
            if GameLevel.chek_loze(GameLevel, self.level_map) is True:
                self.end_screen(player)
            return
        if GameLevel.chek_loze(GameLevel, self.level_map_vii) is True:
            self.end_screen(player)

    def next_turn(self, player):
        """Tarkastaa minkä pelaajan vuoro on seuraavaksi
        Kutsuu sen jälkeen main funktiota
        """
        if self.three_player is False:
            if player == 1:
                self.main(2)
            self.main(1)
        elif self.three_player is True:
            if player == 1:
                self.main(2)
            elif player == 2:
                self.main(3)
            self.main(1)

    def start_screen(self):
        """Pelin alkuruudussa annetaan ohjeet pelaajalle
        Valintoina kaksin-, kolminpeli, wikipedia ja exit"""
        screen = pygame.display.set_mode(
            (self.display_width, self.display_height))
        pygame.display.set_caption("Alkuruutu")

        pygame.init()

        font = pygame.font.SysFont("Comic Sans MS", 30)

        game_begin_2 = font.render(
            "START GAME 2-P: PRESS G", True, (255, 255, 255))
        screen.blit(game_begin_2, (300, 200))
        game_begin_3 = font.render(
            "START GAME 3-P: PRESS T", True, (255, 255, 255))
        screen.blit(game_begin_3, (300, 240))
        wiki_w = font.render("TO WIKI: PRESS W", True, (255, 255, 255))
        screen.blit(wiki_w, (300, 280))
        instructions = font.render(
            "TRY NOT TO GET 3 IN LINE", True, (255, 255, 255))
        screen.blit(instructions, (300, 360))
        exit_info = font.render("TO EXIT: PRESS E", True, (255, 255, 255))
        screen.blit(exit_info, (300, 320))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        self.main(1)
                    if event.key == pygame.K_t:
                        self.three_player = True
                        self.main(1)
                    if event.key == pygame.K_w:
                        webbrowser.open(
                            r"https://en.wikipedia.org/wiki/Tic-tac-toe")
                    if event.key == pygame.K_e:
                        self.running = False
                        pygame.quit()

            pygame.display.update()

        pygame.quit()

    def end_screen(self, player):
        """Kerrotaan pelin häviäjä ja ruutu muuttuu valkoiseksi
        Odotetaan hetken, jonka jälkeen palautetaan pelikartta ja
        kolmen pelaajan vaihtoehto alkutilanteeseen.
        Kusutaan alkuruutua."""
        display = pygame.display.set_mode(
            (self.display_width, self.display_height))
        display.fill((255, 255, 255))
        font = pygame.font.SysFont("Comic Sans MS", 30)
        display.blit(font.render("PLAYER " + str(player) + " LOST",
                                 True, (0, 0, 0)), (self.display_width//2, self.display_height//2))
        pygame.display.update()
        pygame.time.wait(6000)
        self.level_map = [[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]]
        self.level_map_vii = [[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0]]
        self.three_player = False
        self.start_screen()


if __name__ == "__main__":
    Ristinolla().start_screen()
