#!/usr/bin/env python3

import random
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN

from contants import SCREEN_WIDTH, SCREEN_HEIGHT

from agents import Plant, Predator, Prey


def main():
    print("Запущено")

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Alien vs Predator")

    if_active = True

    plants = [Plant() for i in range(150)]
    predators = [Predator() for i in range(20)]
    preys = [Prey() for i in range(50)]

    while if_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if_active = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if_active = False
        screen.fill((11, 11, 11))
        [p.update(screen, food=predators) for p in plants]
        [p.update(screen, food=preys) for p in predators]
        [p.update(screen, food=plants) for p in preys]

        plants = [p for p in plants if p.is_alive is True]
        plants = plants + [Plant() for i in range(2)]

        preys = [p for p in preys if p.is_alive is True]

        for p in preys[:]:
            if p.energy > 5:
                p.energy = 0
                preys.append(
                    Prey(
                        x=p.x + random.randint(-20, 20), y=p.y + random.randint(-20, 20)
                    )
                )

        predators = [p for p in predators if p.age < 2000]

        for p in predators[:]:
            if p.energy > 10:
                p.energy = 0
                predators.append(
                    Predator(
                        x=p.x + random.randint(-20, 20), y=p.y + random.randint(-20, 20)
                    )
                )

        pygame.display.flip()
        clock.tick(24)

    pygame.quit()


if __name__ == "__main__":
    main()
