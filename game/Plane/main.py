import pygame 
import random


class plane_game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((600,700))
        pygame.display.set_caption('plane Game')

        self.plane = pygame.image.load('maybay/assets/maybay.png')
        self.bg = pygame.image.load('maybay/assets/background.jpg')
        self.bullet = pygame.image.load('maybay/assets/bullet.png') 
        self.xplane, self.yplane = 253.5 , 500 
        self.xbullet, self.ybullet = [20 , 220, 420] , 20
        self.indexbullet = 1 
        self.indexbullet2 = 1
        self.gameplay = False
        self.game_score = 0 
        self.level = 5
        self.up = 0 

        self.running = True
    def check(self):
        if (self.ybullet + 160 > self.yplane) and (self.ybullet < self.yplane + 96):
            if ((self.xbullet[self.indexbullet] + 160 > self.xplane) and self.xbullet[self.indexbullet] < self.xplane + 93 or ((self.xbullet[self.indexbullet2] + 160 >self.xplane) and (self.xbullet[self.indexbullet2] < self.xplane + 93))):
                self.gameplay = False
                self.xplane, self.yplane = 253.5 , 500 
                self.xbullet, self.ybullet = [20 , 220, 420] , 40
                self.indexbullet = 1 
                self.indexbullet2 = 1
                
                

             
    def fbullet(self):
        self.screen.blit(self.bullet, (self.xbullet[self.indexbullet] , self.ybullet))
        self.screen.blit(self.bullet, (self.xbullet[self.indexbullet2] , self.ybullet))
        self.ybullet += self.level
        if self.ybullet > 600 :
            self.ybullet = 20
            self.indexbullet = random.randint(0,2)
            self.indexbullet2 = random.randint(0,2)
            self.game_score += 1
            self.up += 1 
            
            if (self.up == 5):
                self.level += 1
                self.up = 0
                print("tang level ")


            

    def view_score(self):
        gamefont = pygame.font.Font(None,40)
        font = gamefont.render(f"Score: {self.game_score}", True , (250,0,0))
        self.screen.blit(font,(100,10))
       

    def run(self):
        
        while self.running:
            
            if (self.gameplay):
                self.clock.tick(60)
                self.screen.blit(self.bg , (0,0))
                self.screen.blit(self.plane , (self.xplane, self.yplane))
                self.fbullet()
                self.check()
                self.view_score()
                


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if (((event.key == pygame.K_a) or (event.key == pygame.K_LEFT))) and (not(self.xplane == 53.5)):
                            
                            self.xplane -= 200
                        if (((event.key == pygame.K_d) or (event.key == pygame.K_RIGHT))) and (not(self.xplane == 453.5)):
                        
                            self.xplane += 200
                        if (event.key == pygame.K_SPACE) and (self.gameplay == False) :
                            self.gameplay = True
                pygame.display.update()
            
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_SPACE) and (self.gameplay == False) :
                            self.gameplay = True
                            self.game_score = 0
                            self.level = 5 
                            self.up = 0
    


if __name__ == "__main__":
    plane = plane_game()
    plane.run()
