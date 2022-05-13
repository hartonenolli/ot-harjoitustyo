import webbrowser
import random
import pygame
from game_level import GameLevel
from database_ristinolla import Database


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

        height = len(self.level_map)
        width = len(self.level_map[0])

        self.display_height = height * 200
        self.display_width = width * 200

        self.three_player = False

        self.one_player = False

    def main(self, player):
        """Pääohjelma, jossa kello käy silmukan sisällä.
        Kutsutaan apufuntioita tarkastamaan peliruutu,
        klikkauksen käsittely, tarkastetaan häviäjä ja seuraava vuoro.

        Args:
            player: 1, 2 tai 3
        """
        self.screen_setup(player)

        clock = pygame.time.Clock()

        while True:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    self.event_handler(player, pos)

            pygame.display.update()

    def event_handler(self, player, pos):
        """Apufunktio käsittelemään main-funktion painalluksia"""
        if self.to_handle_click(player, pos) is False:
            self.main(player)
        self.screen_setup(player)
        pygame.display.update()
        pygame.time.wait(700)
        self.time_to_chek_for_lozer(player)
        self.next_turn(player)

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
            level = GameLevel(self.level_map, 200)
            level.all_sprites.draw(display)
            return

        display = pygame.display.set_mode(
            (7 * 200, 5 * 200))
        pygame.display.set_caption(str(player) + " TURN")
        level = GameLevel(self.level_map_vii, 200)
        level.all_sprites.draw(display)

    def time_to_chek_for_lozer(self, player):
        """Kutsuu GameLevel luokan apufunktioita
        Funtioissa tarkastetaan: onko häviäjää

        Args:
            player: 1, 2 tai 3
        """
        if self.three_player is False:
            if GameLevel.chek_loze(GameLevel, self.level_map) is True:
                if self.one_player is True and player == 2:
                    self.screen_setup(1)
                    pygame.display.update()
                    pygame.time.wait(700)
                self.end_screen(player)
            if self.one_player is True and player == 2:
                self.main(1)
            return
        if GameLevel.chek_loze(GameLevel, self.level_map_vii) is True:
            self.end_screen(player)

    def next_turn(self, player):
        """Tarkastaa minkä pelaajan vuoro on seuraavaksi
        Kutsuu sen jälkeen main funktiota
        """
        if self.one_player is True and player == 1:
            self.for_bot()
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

    def for_bot(self):
        """Pelin tekoäly.
        Tekoäly antaa satunnaisia arvoja pelikentältä ja tarkastaa
        häviääkö se sillä kolme kertaa."""
        times = 2
        while True:
            first = random.randint(0, 4)
            second = random.randint(0, 4)
            get_map = self.to_handle_click(2,
                                           (self.position_map[first][second]))
            if get_map is False:
                continue
            if GameLevel.chek_loze(GameLevel, self.level_map) is True and times >= 0:
                self.level_map[get_map[0]][get_map[1]] = 0
                times -= 1
                continue
            break
        self.time_to_chek_for_lozer(2)

    def start_screen(self):
        """Pelin alkuruudussa annetaan ohjeet pelaajalle
        Valintoina yksin-, kaksin-, kolminpeli, wikipedia, tilastot ja exit"""
        screen = pygame.display.set_mode(
            (self.display_width, self.display_height))
        pygame.display.set_caption("Alkuruutu")

        pygame.init()

        font = pygame.font.SysFont("Comic Sans MS", 30)

        screen.blit(font.render(
            "START GAME 1-P: PRESS R", True, (255, 0, 0)), (300, 200))
        screen.blit(font.render(
            "START GAME 2-P: PRESS G", True, (0, 255, 0)), (300, 240))
        screen.blit(font.render(
            "START GAME 3-P: PRESS B", True, (0, 0, 255)), (300, 280))
        screen.blit(font.render("TO WIKI: PRESS W",
                    True, (255, 255, 255)), (300, 320))
        screen.blit(font.render(
            "TIMES PLAYED: PRESS Y", True, (255, 255, 0)), (300, 360))
        screen.blit(font.render(
            "REVERCED TIC-TAC-TOE = AVOID 3 IN LINE", True, (0, 128, 128)), (200, 460))
        screen.blit(font.render("TO EXIT: PRESS P",
                    True, (128, 0, 128)), (300, 400))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_key_down(screen, event, font)

            pygame.display.update()

    def handle_key_down(self, screen, event, font):
        """Apufunktio käsittelemään alkuruudun napinpainalluksia"""
        if event.key == pygame.K_g:
            self.main(1)
        if event.key == pygame.K_b:
            self.three_player = True
            self.main(1)
        if event.key == pygame.K_r:
            self.one_player = True
            self.main(1)
        if event.key == pygame.K_w:
            webbrowser.open(
                r"https://en.wikipedia.org/wiki/Tic-tac-toe")
        if event.key == pygame.K_y:
            screen.blit(font.render(
                str(Database("datafile/tilastot.db").fech_amount_of_games(1)) + " TIMES PLAYED 1-P", True,
                (255, 0, 0)), (300, 520))
            total_2 = Database("datafile/tilastot.db").fech_amount_of_games(2)
            screen.blit(font.render(
                str(total_2) + " TIMES PLAYED 2-P", True, (0, 255, 0)), (300, 560))
            total_3 = Database("datafile/tilastot.db").fech_amount_of_games(3)
            screen.blit(font.render(
                str(total_3) + " TIMES PLAYED 3-P", True, (0, 0, 255)), (300, 600))
            screen.blit(font.render(
                str(Database("datafile/tilastot.db").fech_amount_of_games(1) + total_2 + total_3) + " TOTALTIMES PLAYED",
                True, (255, 255, 0)), (300, 640))
        if event.key == pygame.K_p:
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
        pygame.time.wait(5000)
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
        if self.three_player is True:
            Database("datafile/tilastot.db").add_game(3)
        elif self.one_player is True:
            Database("datafile/tilastot.db").add_game(1)
        else:
            Database("datafile/tilastot.db").add_game(2)
        self.three_player = False
        self.one_player = False

        self.start_screen()


if __name__ == "__main__":
    Ristinolla().start_screen()
