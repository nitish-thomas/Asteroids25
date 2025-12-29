import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger_web import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
import asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 


    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.Font(None, 36)

    #Container groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()


    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(f"Player created at: {player.position}")
    print(f"Updatable sprites: {len(updatable)}")
    print(f"Drawable sprites: {len(drawable)}")
    print(f"Screen size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    dt = 0

    #Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        
        updatable.update(dt)
        print(f"Frame - Asteroids: {len(asteroids)}, Shots: {len(shots)}, Score: {score}")
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide_with(shot):
                    if asteroid.radius >= 40:
                        score += 20
                    elif asteroid.radius >= 25:
                        score += 50
                    else:
                        score += 100
                    asteroid.split()
                    shot.kill()
            
            if asteroid.collide_with(player):
                print(f"Game over! Final Score: {score}") 
                return
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        await asyncio.sleep(0)  # Critical for web - yields control
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    asyncio.run(main())  # Changed to asyncio.run for web compatibility