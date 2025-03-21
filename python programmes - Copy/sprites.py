import random
import pygame
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2


BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')


YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
class Sprite(pygame.sprite.Sprite):
 
 def __init__(self,color,height,width):
  super().__init__( )
  self.image=pygame.Surface([width,height])
  self.image.fill(color)
  self.rect = self.image.get_rect()
  self.velocity = [random.choice([-1,1]), random([-1,1])]
 def update(self):
   self.rect.move_ip(self.velocity)
   boundary_hit= False

   if self.rect. top <=0 or self.rect.bottom>=400:
    self.velocity[1 ]= -self.velocity[1]
    boundary_hit = True

   if self.rect. left <=0 or self.rect.right>=400:
    self.velocity[0 ]= -self.velocity[0]
    boundary_hit= True
    
    dary_hit = True
   if boundary_hit:
     pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
 def change_color(self):
  
  self.image.fill(random.choice[YELLOW,MAGENTA,ORANGE,WHITE])
  all_sprites_list = pygame.sprite.Group()

  sp1 = Sprite(WHITE,20,30)

  sp1.rect.x=0
  sp1.rect.y=0
  screen = pygame.display.set_mode((500,400))
  screen.fill(BLUE)
  exit= False

  clock=pygame.time.Clock()
  while not exit:
   for event in pygame.event.get():

    if event.type==pygame.QUIT:
      exit=True

    elif event.type== SPRITE_COLOR_CHANGE_EVENT:
     sp1.change_color()

     all_sprites_list.update()
     screen.fill(BLUE)

     all_sprites_list.update()
     screen.fill(BLUE)

     all_sprites_list.draw(screen)

     pygame.display.flip()
     clock.tick(240)

     pygame.quit()