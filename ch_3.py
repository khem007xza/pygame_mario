import pygame

pygame.init()

screen_width = 1000
screen_height = 1000

tile_size = 50

dis = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

class Player():
	def __init__(self, x, y):
		self.image_left = []
		self.image_right = []
		self.index = 0
		self.counter = 0
		for num in range(1,6):
			img_left = pygame.image.load("image\player"+str(num)+".png")
			img_left = pygame.transform.scale(img_left, (40,80))
			img_right = pygame.transform.flip(img_left, True, False)
			
			self.image_left.append(img_left)
			self.image_right.append(img_right)

		self.image = self.image_left[3]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0
	
	def update(self):
		dx = 0
		dy = 0

		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE] and self.jumped == False:
			self.vel_y = -15
			self.jumped = True
		if key[pygame.K_SPACE] == False:
			self.jumped = False
		if key[pygame.K_LEFT]:
			dx -= 5
			self.counter +=1
			self.direction = 1
		if key[pygame.K_RIGHT]:
			dx += 5
			self.counter += 1
			self.direction = -1

		if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
			self.counter = 0
			self.index = 0

		if self.direction == 1:
			self.image = self.image_left[self.index]
		if self.direction == -1:
			self.image = self.image_right[self.index]



		walk_cooldown = 5
		if self.counter > walk_cooldown:
			self.counter = 0
			self.index += 1
			if self.index >= len(self.image_left):
				self.index = 0
			if self.direction == 1:
				self.image = self.image_left[self.index]
			if self.direction == -1:
				self.image = self.image_right[self.index]

		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y

		for tile in world.tile_list:
				
				if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0
				
				if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				
					if self.vel_y < 0:
						dy = tile[1].bottom - self.rect.top
						self.vel_y = 0
					
					elif self.vel_y >= 0:
						dy = tile[1].top - self.rect.bottom
						self.vel_y = 0
		
		self.rect.x += dx
		self.rect.y += dy
		dis.blit(self.image, self.rect)
		

class World():	
	def __init__(self, data):
		self.tile_list = []

		map_dic = {
			"1" : pygame.transform.scale(pygame.image.load("image\dirt.png"), (tile_size, tile_size)),
			"2" : pygame.transform.scale(pygame.image.load("image\grass.png"), (tile_size, tile_size)),
		}
	
		row_count = 0
		
		for row in data:
			col_count = 0
			for tile in row:
				
				if tile != 0:
					img = map_dic[str(tile)]
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)

				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			dis.blit(tile[0], tile[1])

world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


player = Player(100, screen_height - 130)
world = World(world_data)
sky = pygame.image.load("image\sky.png")

run = True
while run:
	dis.blit(sky, (0,0))
	world.draw()
	player.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()
pygame.quit()