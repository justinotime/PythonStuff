import pygame


def main():
    pygame.init()
    
    size = width, height = 320, 240
    speed = [2,2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(black)


    pygame.quit()
    
if __name__ == "_main__":
    main()

