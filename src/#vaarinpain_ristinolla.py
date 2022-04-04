#vaarinpain_ristinolla

import pygame
import webbrowser

class VaarinPain:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Väärinpäinristinolla") #Name of the game
        screen = pygame.display.set_mode((1200, 900)) #Screen
        font = pygame.font.SysFont("Arial", 30)
        self.again = True
        klok = pygame.time.Clock()

        def start_screen():
            self.again = False
            screen.fill((0, 50, 0))
            game_begin = font.render("START GAME: PRESS ->         G", True, (255, 255, 255))
            game_instructions = font.render("INSTRUCTIONS: PRESS ->      I", True, (255, 255, 255))
            game_stats = font.render("STATS: PRESS ->                      S", True, (255, 255, 255))
            game_exit = font.render("EXIT: PRESS ->                         E", True, (255, 255, 255))
            screen.blit(game_begin, (450, 200))
            screen.blit(game_instructions, (450, 240))
            screen.blit(game_stats, (450, 280))
            screen.blit(game_exit, (450, 320))
            pygame.display.flip()
            while True:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        exit()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_g:
                            game_mode()
                        if e.key == pygame.K_i:
                            instructions()
                        if e.key == pygame.K_s:
                            pass
                        if e.key == pygame.K_e:
                            exit()

        def instructions():
            screen.fill((0, 0, 50))
            instructions_on_screen = font.render("LOZER IS THE ONE, THAT GET 3 IN ROW", True, (255, 255, 255))
            start_return = font.render("RETURN: PRESS ->   R", True, (255, 255, 255))
            wiki_instructions = screen.blit(font.render("CLICK HERE FOR MORE INFO", True, (0,200,0)), (50, 80))
            screen.blit(instructions_on_screen, (300, 200))
            screen.blit(start_return, (400, 240))
            pygame.display.flip()
            while True:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        exit()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_r:
                            start_screen()
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        pos = e.pos
                        if wiki_instructions.collidepoint(pos):
                            webbrowser.open(r"https://en.wikipedia.org/wiki/Tic-tac-toe")

        def game_mode():
            screen.fill((50, 0, 0))

            two = font.render("2-p", True, (255, 0, 255))
            three = font.render("3-p", True, (255, 255, 0))
            four = font.render("4-p", True, (0, 255, 255))
            select = font.render("CLICK GAME MODE", True, (255, 255, 255))


            txt2 = font.render("3x3", True, (255, 0, 255))
            fxf2 = font.render("5x5", True, (255, 0, 255))
            fxf3 = font.render("5x5", True, (255, 255, 0))
            sxs3 = font.render("7x7", True, (255, 255, 0))
            sxs4 = font.render("7x7", True, (0, 255, 255))
            tenxten4 = font.render("10x10", True, (0, 255, 255))

            screen.blit(select, (500, 100))
            screen.blit(two, (200, 200))
            screen.blit(three, (550, 200))
            screen.blit(four, (900, 200))
            screen.blit(txt2, (200, 440))
            screen.blit(fxf2, (200, 660))
            screen.blit(fxf3, (550, 440))
            screen.blit(sxs3, (550, 660))
            screen.blit(sxs4, (900, 440))
            screen.blit(tenxten4, (900, 660))
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

        if self.again == True:
            start_screen()

if __name__=="__main__":
    VaarinPain()