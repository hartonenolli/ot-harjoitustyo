#vaarinpain_ristinolla

import pygame
import webbrowser

class Vaarinpain:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Väärinpäinristinolla") #Name of the game
        self.screen = pygame.display.set_mode((1200, 900)) #Screen
        self.font = pygame.font.SysFont("Arial", 30)
        self.again = True
        self.klok = pygame.time.Clock()
        self.start_screen()

    def start_screen(self):
        self.again = False
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


        txt2 = self.font.render("3x3", True, (255, 0, 255))
        fxf2 = self.font.render("5x5", True, (255, 0, 255))
        fxf3 = self.font.render("5x5", True, (255, 255, 0))
        sxs3 = self.font.render("7x7", True, (255, 255, 0))
        sxs4 = self.font.render("7x7", True, (0, 255, 255))
        tenxten4 = self.font.render("10x10", True, (0, 255, 255))

        self.screen.blit(select, (500, 100))
        self.screen.blit(two, (200, 200))
        self.screen.blit(three, (550, 200))
        self.screen.blit(four, (900, 200))
        self.screen.blit(txt2, (200, 440))
        self.screen.blit(fxf2, (200, 660))
        self.screen.blit(fxf3, (550, 440))
        self.screen.blit(sxs3, (550, 660))
        self.screen.blit(sxs4, (900, 440))
        self.screen.blit(tenxten4, (900, 660))
        pygame.display.flip()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type is pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if 200 < x < 250 and 450 < y < 470:
                        print("3x32")
                        #input()
                    if 200 < x < 250 and 670 < y < 690:
                        print("5x52")
                    if 550 < x < 600 and 450 < y < 470:
                        print("5x53")
                    if 550 < x < 600 and 670 < y < 690:
                        print("7x73")
                    if 900 < x < 950 and 450 < y < 470:
                        print("7x74")
                    if 900 < x < 980 and 670 < y < 690:
                        print("10x104")
                    #print(x,y)

        def two_player():
            pass
    
    def start_again(self):
        if self.again == True:
            self.start_screen()

if __name__=="__main__":
    c = VaarinPain()
