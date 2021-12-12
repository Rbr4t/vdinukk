#siia tulevad meie mängu klassid, pärast impordime need main faili VÕI TEGELIKULT MITTE
class Player:
    def __init__(self):
        self.x = 320
        self.y = 240
        self.vx = 0
        self.vy = 0
        self.img = pygame.image.load(player_image)
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
