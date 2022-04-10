#vaarinpain_ristinolla


class Vaarinpain:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Väärinpäinristinolla") #Name of the game
        self.screen = pygame.display.set_mode((1200, 900)) #Screen
        self.game_screen = pygame.display.set_mode((1200, 900))
        self.font = pygame.font.SysFont("Arial", 30)
        self.big_font = pygame.font.SysFont("Comic Sans MS", 50)
        self.again = True
        self.klok = pygame.time.Clock()

        self.user1 = ""
        self.user2 = ""
        self.user3 = ""
        self.user4 = ""
        self.start_screen()

    def start_screen(self):
        #self.again = False
        self.screen.fill((0, 50, 0))
        game_begin = self.font.render("START GAME: PRESS ->         G", True, (255, 255, 255))
        game_instructions = self.font.render("INSTRUCTIONS: PRESS ->      I", True, (255, 255, 255))
        game_stats = self.font.render("STATS: PRESS ->                      S", True, (255, 255, 255))
        game_exit = self.font.render("EXIT: PRESS ->                         E", True, (255, 255, 255))
        self.screen.blit(game_begin, (450, 200))
        self.screen.blit(game_instructions, (450, 240))
        self.screen.blit(game_stats, (450, 280))
        self.screen.blit(game_exit, (450, 320))
        pygame.display.flip()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_g:
                        self.game_mode()
                    if e.key == pygame.K_i:
                        self.instructions()
                    if e.key == pygame.K_s:
                        pass
                    if e.key == pygame.K_e:
                        exit()

    def instructions(self):
        self.screen.fill((0, 0, 50))
        instructions_on_screen = self.font.render("LOZER IS THE ONE, THAT GET 3 IN ROW", True, (255, 255, 255))
        start_return = self.font.render("RETURN: PRESS ->   R", True, (255, 255, 255))
        wiki_instructions = self.screen.blit(self.font.render("CLICK HERE FOR WIKI", True, (0,200,0)), (50, 80))
        self.screen.blit(instructions_on_screen, (300, 200))
        self.screen.blit(start_return, (400, 240))
        pygame.display.flip()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_r:
                        self.start_screen()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    pos = e.pos
                    if wiki_instructions.collidepoint(pos):
                        webbrowser.open(r"https://en.wikipedia.org/wiki/Tic-tac-toe")

    def game_mode(self):
        self.screen.fill((50, 0, 0))
        two = self.font.render("2-p", True, (255, 0, 255))
        three = self.font.render("3-p", True, (255, 255, 0))
        four = self.font.render("4-p", True, (0, 255, 255))
        select = self.font.render("CLICK GAME MODE", True, (255, 255, 255))

        txt2 = self.screen.blit(self.font.render("3x3", True, (255, 0, 255)), (200, 440))
        fxf2 = self.screen.blit(self.font.render("5x5", True, (255, 0, 255)), (200, 660))
        fxf3 = self.screen.blit(self.font.render("5x5", True, (255, 255, 0)), (550, 440))
        sxs3 = self.screen.blit(self.font.render("7x7", True, (255, 255, 0)), (550, 660))
        sxs4 = self.screen.blit(self.font.render("7x7", True, (0, 255, 255)), (900, 440))
        tenxten4 = self.screen.blit(self.font.render("10x10", True, (0, 255, 255)), (900, 660))

        self.screen.blit(select, (500, 100))
        self.screen.blit(two, (200, 200))
        self.screen.blit(three, (550, 200))
        self.screen.blit(four, (900, 200))
        pygame.display.flip()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    pos = e.pos
                    if txt2.collidepoint(pos):
                        self.two_player("3")
                    if fxf2.collidepoint(pos):
                        self.two_player("5")
                    if fxf3.collidepoint(pos):
                        self.three_player("5")
                    if sxs3.collidepoint(pos):
                        self.three_player("7")
                    if sxs4.collidepoint(pos):
                        self.four_player("7")
                    if tenxten4.collidepoint(pos):
                        self.four_player("10")

    def two_player(self, n):
        m = 1
        self.screen.fill((255, 0, 255))
        pygame.display.flip()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.KEYDOWN:
                    if m == 1:
                        if e.key == pygame.K_BACKSPACE:
                            self.user1 = self.user1[:-1]
                        elif e.key == pygame.K_RETURN and len(self.user1) > 0:
                            m += 1
                        else:
                            if len(self.user1) == 8:
                                self.user1 = self.user1[:-1]
                            self.user1 += e.unicode
                    elif m == 2:
                        if e.key == pygame.K_BACKSPACE:
                            self.user2 = self.user2[:-1]
                        elif e.key == pygame.K_RETURN and len(self.user2) > 0:
                            self.play_setup(int(n), m)
                        else:
                            if len(self.user2) == 8:
                                self.user2 = self.user2[:-1]
                            self.user2 += e.unicode
                self.screen.fill((255, 0, 255))
                size = self.screen.blit(self.big_font.render(n + " IS THE TABLE SIZE", True, (0, 0, 0)), (300, 100))
                info = self.screen.blit(self.big_font.render("INPUT PLAYER NAME (1-8 char) + ENTER", True, (0, 0, 0)), (100, 300))
                text = self.screen.blit(self.font.render(self.user1, True, (0,0,0)), (450, 500))
                text2 = self.screen.blit(self.font.render(self.user2, True, (0,0,0)), (450, 525))
            pygame.display.flip()


    def three_player(self, n):
        self.screen.fill((255, 255, 0))
        size = self.big_font.render(n + " IS THE TABLE SIZE", True, (0, 0, 0))
        sorry = self.screen.blit(self.big_font.render("SORRY BUT IT'S NOT READY.. -> R TO RETURN", True, (0, 0, 0)), (10, 200))
        self.screen.blit(size, (300, 100))
        pygame.display.flip()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_r:
                        self.start_screen()

    def four_player(self, n):
        self.screen.fill((0, 255, 255))
        size = self.big_font.render(n + " IS THE TABLE SIZE", True, (0, 0, 0))
        sorry = self.screen.blit(self.big_font.render("SORRY BUT IT'S NOT READY.. -> R TO RETURN", True, (0, 0, 0)), (10, 200))
        self.screen.blit(size, (300, 100))
        pygame.display.flip()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_r:
                        self.start_screen()

    def play_setup(self, n, m):
        self.game_screen.fill((255, 255, 255))
        line_c = (0,0,0)
        nill = 1
        while nill <= n:
            pygame.draw.line(self.game_screen, line_c, (1200 / n * nill, 0), (1200 / n * nill, 900), 7)
            pygame.draw.line(self.game_screen, line_c, (0, 900 / n * nill), (1200, 900 / n * nill), 7)
            nill += 1
        pygame.display.flip()
        self.play(n,m) 

    def play(self, n, m):
        player = [self.user1,self.user2]
        board = [[0,0,0],[0,0,0],[0,0,0]]
        index = 0
        square = (1200/n, 900/n)
        square_player1 = pygame.Surface(square,flags=pygame.HWSURFACE)
        square_player1.fill(color='red')
        square_player2 = pygame.Surface(square,flags=pygame.HWSURFACE)
        square_player2.fill(color='blue')
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    pos = e.pos
                    if player[index] == self.user1:
                        if 0 < pos[0] < 1200 / n:
                            if 0 < pos[1] < 900 / n:
                                if board[0][0] == 0:
                                    board[0][0] = 1
                                    self.game_screen.blit(square_player1, (0,0))
                                else:
                                    continue
                            if 900 / n < pos[1] < 900 / n*2:
                                if board[1][0] == 0:
                                    board[1][0] = 1
                                    self.game_screen.blit(square_player1, (0,900/n))
                                else:
                                    continue
                            if 900 / n*2 < pos[1] < 900 / n*3:
                                if board[2][0] == 0:
                                    board[2][0] = 1
                                    self.game_screen.blit(square_player1, (0,900/n*2))
                                else:
                                    continue
                        if 1200 / n < pos[0] < 1200 / n*2:
                            if 0 < pos[1] < 900 / n:
                                if board[0][1] == 0:
                                    board[0][1] = 1
                                    self.game_screen.blit(square_player1, (400,0))
                                else:
                                    continue
                            if 900 / n < pos[1] < 900 / n*2:
                                if board[1][1] == 0:
                                    board[1][1] = 1
                                    self.game_screen.blit(square_player1, (400,900/n))
                                else:
                                    continue
                            if 900 / n*2 < pos[1] < 900 / n*3:
                                if board[2][1] == 0:
                                    board[2][1] = 1
                                    self.game_screen.blit(square_player1, (400,900/n*2))
                                else:
                                    continue
                        if 1200 / n*2 < pos[0] < 1200 / n*3:
                            if 0 < pos[1] < 900 / n:
                                if board[0][2] == 0:
                                    board[0][2] = 1
                                    self.game_screen.blit(square_player1, (800,0))
                                else:
                                    continue
                            if 900 / n < pos[1] < 900 / n*2:
                                if board[1][2] == 0:
                                    board[1][2] = 1
                                    self.game_screen.blit(square_player1, (800,900/n))
                                else:
                                    continue
                            if 900 / n*2 < pos[1] < 900 / n*3:
                                if board[2][2] == 0:
                                    board[2][2] = 1
                                    self.game_screen.blit(square_player1, (800,900/n*2))
                                else:
                                    continue

                    if player[index] == self.user2:
                        if 0 < pos[0] < 1200 / n:
                            if 0 < pos[1] < 900 / n:
                                if board[0][0] == 0:
                                    board[0][0] = 2
                                    self.game_screen.blit(square_player2, (0,0))
                                else:
                                    continue
                            if 900 / n < pos[1] < 900 / n*2:
                                if board[1][0] == 0:
                                    board[1][0] = 2
                                    self.game_screen.blit(square_player2, (0,900/n))
                                else:
                                    continue
                            if 900 / n*2 < pos[1] < 900 / n*3:
                                if board[2][0] == 0:
                                    board[2][0] = 2
                                    self.game_screen.blit(square_player2, (0,900/n*2))
                                else:
                                    continue
                        if 1200 / n < pos[0] < 1200 / n*2:
                            if 0 < pos[1] < 900 / n:
                                if board[0][1] == 0:
                                    board[0][1] = 2
                                    self.game_screen.blit(square_player2, (400,0))
                                else:
                                    continue
                            if 900 / n < pos[1] < 900 / n*2:
                                if board[1][1] == 0:
                                    board[1][1] = 2
                                    self.game_screen.blit(square_player2, (400,900/n))
                                else:
                                    continue
                            if 900 / n*2 < pos[1] < 900 / n*3:
                                if board[2][1] == 0:
                                    board[2][1] = 2
                                    self.game_screen.blit(square_player2, (400,900/n*2))
                                else:
                                    continue
                        if 1200 / n*2 < pos[0] < 1200 / n*3:
                            if 0 < pos[1] < 900 / n:
                                if board[0][2] == 0:
                                    board[0][2] = 2
                                    self.game_screen.blit(square_player2, (800,0))
                                else:
                                    continue
                            if 900 / n < pos[1] < 900 / n*2:
                                if board[1][2] == 0:
                                    board[1][2] = 2
                                    self.game_screen.blit(square_player2, (800,900/n))
                                else:
                                    continue
                            if 900 / n*2 < pos[1] < 900 / n*3:
                                if board[2][2] == 0:
                                    board[2][2] = 2
                                    self.game_screen.blit(square_player2, (800,900/n*2))
                                else:
                                    continue

                    self.board_c(board, player[index], n, m)
                    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
                        self.draw()
                    index += 1
                    if index == len(player):
                        index = 0
                    
                pygame.display.flip()

    def board_c(self, board, p, n, m):

        for i in range(0,3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
                self.loze_screen(p)
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
                self.loze_screen(p)
        if board[0][0] == board[1][1] == board[2][2] and board[1][1] != 0:
            self.loze_screen(p)
        if board[0][2] == board[1][1] == board[2][0] and board[1][1] != 0:
            self.loze_screen(p)
        #self.play(n, m)
    
    def loze_screen(self, p):
        self.screen.fill((0, 50, 0))
        lozer = self.screen.blit(self.big_font.render("GAME LOZER "+p, True, (255, 255, 0)), (300, 220))
        again = self.screen.blit(self.big_font.render("AGAIN -> A", True, (255, 255, 0)), (300, 440))
        pygame.display.flip()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_a:
                        self.start_again()

    def draw(self):
        self.screen.fill((0, 50, 0))
        draw = self.screen.blit(self.big_font.render("DRAW", True, (255, 255, 0)), (300, 220))
        again = self.screen.blit(self.big_font.render("AGAIN -> A", True, (255, 255, 0)), (300, 440))
        pygame.display.flip()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_a:
                        self.start_again()

    def start_again(self):
        self.user1 = ""
        self.user2 = ""
        self.user3 = ""
        self.user4 = ""
        self.start_screen()

if __name__=="__main__":
    import pygame
    import webbrowser
    Vaarinpain()