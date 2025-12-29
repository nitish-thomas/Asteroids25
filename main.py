import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()

    score = 0
    font = pygame.font.Font(None, 36)

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
    dt = 0




    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        
        updatable.update(dt)
        


        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide_with(shot):
                    log_event("asteroid_shot")
                    # Award points based on asteroid size
                    # Large asteroids: 20 points
                    # Medium asteroids: 50 points  
                    # Small asteroids: 100 points
                    if asteroid.radius >= 40:
                        score += 20
                    elif asteroid.radius >= 25:
                        score += 50
                    else:
                        score += 100
                    

                    asteroid.split()
                    shot.kill()
           
            if asteroid.collide_with(player):
                log_event("player_hit")
                print("Game over!") 
                sys.exit()  
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
