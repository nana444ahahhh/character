import os
import sys
import pygame


def load_image(name, colorkey=None, transform=None):
    fullname = os.path.join("data/", name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('эээ стрелочник')
    screen = pygame.display.set_mode((400, 400))

    running = True
    all_sprites = pygame.sprite.Group()
    cursor = pygame.sprite.Sprite()
    cursor.image = load_image("creature.png")
    cursor.rect = cursor.image.get_rect()
    all_sprites.add(cursor)
    pygame.mouse.set_visible(False)
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    cursor.rect.top += 10
                if pygame.key.get_pressed()[pygame.K_UP]:
                    cursor.rect.top -= 10
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    cursor.rect.left += 10
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    cursor.rect.left -= 10

                all_sprites.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))
