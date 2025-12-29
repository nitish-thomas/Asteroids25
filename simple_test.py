import asyncio
import pygame

async def main():
    print("===== STARTING SIMPLE TEST =====")
    pygame.init()
    print("Pygame initialized")
    
    screen = pygame.display.set_mode((800, 600))
    print("Screen created")
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  # Black background
        pygame.draw.circle(screen, (255, 255, 255), (400, 300), 50)  # White circle
        
        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(60)
    
    print("Game ended")

asyncio.run(main())