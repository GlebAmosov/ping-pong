from pygame import*
class hero(sprite.Sprite):
    def __init__(self, size_x, size_y, spead, x, y, image1):
        super().__init__() 
        self.image = transform.scale(image.load(image1),(size_x, size_y))#transform.scale(изменяет размеры изображения под размер окна - уменьшает или увеличивает)
        self.spead = spead
        self.rect = self.image.get_rect()#self.image.get_rect(создает область)
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class UFO(hero):
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and  self.rect.y >5:
            self.rect.y -= self.spead 
        if keys[K_DOWN] and  self.rect.y <850:
            self.rect.y += self.spead 
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and  self.rect.y >5:
            self.rect.y -= self.spead 
        if keys[K_s] and  self.rect.y <850:
            self.rect.y += self.spead 
moon = hero(150, 150, 0, 960,540, 'moon.png')
ufoR = UFO(180, 180, 10, 0, 500, 'нло л.png')
ufoL = UFO(180, 180, 10, 1740, 500, 'нло прав.png')
speed_x = 10
speed_y = 10
window = display.set_mode((1920, 1080))
display.set_caption('Космический_Пинг-понг')
background = transform.scale(image.load('cosmo.jpg'),(1920,1080))
game = True
clock = time.Clock()
game_over = False
alianR = hero(500, 500, 0, 750, 400, 'пришелец прав.png')
alianL = hero(500, 500, 0, 750, 400, 'пришелец лев.png')
font.init()
font = font.Font(None, 200)
winL = font.render('Левый выиграл', True, (20, 142, 9))
winR = font.render('Правый выиграл', True, (252, 2, 217))#font.render(применяем шрифт к тексту)
mixer.init()
mixer.music.load('Музыка пинг-понг.ogg')
mixer.music.play()
vol = 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False   
        elif e.type == KEYDOWN:
                if e.key == K_r:
                    vol += 0.1
                    mixer.music.set_volume(vol)
                if e.key == K_f:
                    vol -= 0.1
                    mixer.music.set_volume(vol)  
    if not game_over:
        window.blit(background,(0,0))
        moon.reset()
        moon.rect.x += speed_x
        moon.rect.y += speed_y
        ufoL.reset()
        ufoR.reset()
        ufoL.update_R()
        ufoR.update_L()
        if sprite.collide_rect(ufoL,moon) or sprite.collide_rect(ufoR, moon):
            speed_y *= -1
            speed_x *= -1
        if moon.rect.y <0 or moon.rect.y >930:
            speed_y *= -1
        if moon.rect.x <0:
            game_over = True
            alianR.reset()
            window.blit(winR, (350, 100))
        if moon.rect.x >1790:
            game_over = True
            alianL.reset()
            window.blit(winL, (420, 200))
    display.update()
    clock.tick(60)










