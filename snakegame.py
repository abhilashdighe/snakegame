from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import *

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        self.score = 0
        # direction will be 1 for right , 2 for down , 3 for left , 4 for up
        self.direction = 1
        self.curr_position_init = [ ( 200 , 200) , ( 180 , 200) , (160 , 200 ) , (140 , 200) , (120 , 200 )]
        self.iseaten = 1
        self.curr_position = self.curr_position_init
#        global curr_level
 #       print(curr_level)
  #      global s
        
    def shift(self , l ):
        return l[len(l)-1:] + l[:len(l)-1]
        
    def eaten(self , l , t):
        return [t]+ l

    def update(self):        
        self.font = pygame.font.Font(None , 17 )
        self.scorecard = self.font.render( "Your Score is : "+str(self.score) , True , (0,0,0) , (255,255,255))   
        self.scorerect = self.scorecard.get_rect()
        self.scorerect.centerx = 300
        self.scorerect.centery = 20
        self.screen.blit( self.scorecard , self.scorerect)
        if ( (self.curr_position[0] in self.curr_position[1:]) or self.curr_position[0][0] >= 800 or self.curr_position[0][0] <0 or self.curr_position[0][1] >=600 or self.curr_position[0][1] <0 ):
            for i in self.curr_position:
                pygame.draw.polygon( self.screen, ( 255,255,255) , [(i[0] , i[1]), (i[0] + 20 , i[1]) , (i[0] +20 , i[1] +20) , (i[0] , i[1] +20)] )

            self.curr_position = self.curr_position_init
            self.score = 0
            self.direction = 1
        
        if (self.iseaten == 1 ):
            self.target_position = ( randrange(0,40) *20 , randrange(0,30) * 20 )
            pygame.draw.polygon( self.screen, ( 255,0,0) , [(self.target_position[0] , self.target_position[1]), (self.target_position[0] + 20 , self.target_position[1]) , (self.target_position[0] +20 , self.target_position[1] +20) , (self.target_position[0] , self.target_position[1] +20)] )    
            self.iseaten = 0
            print(self.target_position)
        elif(self.curr_position[0] == self.target_position):
            self.score += 1
            self.iseaten = 1
            self.curr_position = self.eaten( self.curr_position , self.target_position)
#            if ( self.score % 5 == 0 ):
 #               curr_level +=10
  #              s.mainloop(curr_level)
           
            
            
        
    def keyUp(self, key):
        if ( key == 275 and self.direction != 3 ):
            self.direction = 1
        elif ( key == 274 and self.direction != 4 ):
            self.direction = 2
        elif ( key == 276 and self.direction != 1):
            self.direction = 3
        elif ( key == 273 and self.direction != 2):
            self.direction = 4
                
                
    def mouseUp(self, button, pos):
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        pass
        
    def draw(self):
        self.curr_position = self.shift(self.curr_position)   
#        pygame.draw.polygon( self.screen, ( 255,255,255) , [(self.curr_position[0][0] , self.curr_positon[0][1]), (self.curr_position[0][0] + 20 , self.curr_position[0][1]) , (self.curr_position[0][0] +20 , self.curr_position[0][1] +20) , (self.curr_position[0][0] , self.curr_position[0][1] +20)] )
        for i in self.curr_position:
            pygame.draw.polygon( self.screen, ( 255,255,255) , [(i[0] , i[1]), (i[0] + 20 , i[1]) , (i[0] +20 , i[1] +20) , (i[0] , i[1] +20)] )
            break
        if ( self.direction == 1):
            if ( self.curr_position[0][0] < 800):
                self.curr_position[0] = ( self.curr_position[1][0] + 20 , self.curr_position[1][1])
#            else:
 #               self.curr_position[0] = ( 0 , self.curr_position[1][1])
        elif( self.direction == 2 ):
            if ( self.curr_position[0][1] < 600):
                self.curr_position[0] = ( self.curr_position[1][0] , self.curr_position[1][1] + 20)
  #          else:
   #             self.curr_position[0] = (self.curr_position[1][0] , 0)
        elif( self.direction == 3):
            if (self.curr_position[0][0] >=0):
                self.curr_position[0] = ( self.curr_position[1][0] - 20 , self.curr_position[1][1])
  #          else:
  #              self.curr_position[0][0] = ( 780 , self.curr_position[1][1] )
        elif( self.direction == 4):
            if (self.curr_position[0][1] >= 0):
                self.curr_position[0] = ( self.curr_position[1][0] , self.curr_position[1][1] - 20)
  #          else:
  #              self.curr_position[0] = ( self.curr_position[1][0] , 580)
        for i in self.curr_position:
            pygame.draw.polygon( self.screen, ( 0 ,0 ,0) , [(i[0] , i[1]), (i[0] + 20 , i[1]) , (i[0] +20 , i[1] +20) , (i[0] , i[1] +20)] )
s = Starter()
curr_level = 10
s.mainLoop(curr_level)
