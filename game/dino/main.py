import pygame 

class dino:
    def __init__(self):
        pygame.init()
        self.xbg , self.ybg = 0, 0 
        self.xdino , self.ydino = 100, 220
        self.xtree , self.ytree = 500, 230 
        self.screen = pygame.display.set_mode((600,300))
        self.running = True 
        self.bg = pygame.image.load('dino/dino/assets/background.jpg')
        self.dino = pygame.image.load('dino/dino/assets/dinosaur.png')
        self.tree = pygame.image.load('dino/dino/assets/tree.png')
        self.clock = pygame.time.Clock()
        self.jump = False
        self.gameplay = True 
        self.score = 0 
        self.leveltree = 10
        self.leveldino = 9
        self.up = 0


    def view_score(self):
        
        gamefont = pygame.font.Font(None, 40)
        font = gamefont.render(f"Score: {self.score}", True , (250,0,0))
        self.screen.blit(font,(100,50))


    def background(self):
        self.screen.blit(self.bg, (self.xbg, self.ybg))
        self.screen.blit(self.bg, (self.xbg + 600 , self.ybg))
        self.xbg -= 5 
        if self.xbg == -600 :
            self.xbg = 0
    def Treee(self):
        self.screen.blit(self.tree, (self.xtree, self.ytree))
        self.xtree -= self.leveltree
        if self.xtree < -10 :
            self.xtree = 500
            self.score += 1 
            self.up += 1
            if self.up == 10 :
                self.up = 0
                self.leveltree = (self.leveltree*110)/100
                #self.leveldino = (self.leveldino*110)/100
    def check(self):
        if ((self.xtree<self.xdino+40) and (self.xtree > self.xdino - 40)) and ((self.ydino+40 > self.ytree)):
            self.gameplay = False
            self.xbg , self.ybg = 0, 0 
            self.xdino , self.ydino = 100, 220
            self.xtree , self.ytree = 500, 230 
            self.leveltree = 10
            self.score = 0
    def dinojump(self):
        if (self.jump) and (self.ydino > 100):
            self.ydino -= (self.leveldino)
        else :
            self.jump = False
    def newton(self):
        if (not(self.jump) and not(self.ydino == 220)):
            self.ydino += (self.leveldino)
            
    def dinosaur(self):
        self.screen.blit(self.dino , (self.xdino, self.ydino))

    def run(self):
        while self.running:
            if (self.gameplay):
                self.clock.tick(60)
                self.background()
                self.Treee()
                self.dinosaur()
                self.dinojump()
                self.newton()
                self.view_score()
                self.check()
                
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False 
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_SPACE) and self.gameplay:
                            print("space")
                            if (self.ydino == 220):
                                self.jump = True
                pygame.display.update()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and not(self.gameplay):
                            self.gameplay = True

if __name__ == "__main__":
    dino = dino()
    dino.run()
