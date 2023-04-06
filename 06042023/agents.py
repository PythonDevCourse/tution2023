#!/usr/bin/env python3

from contants import SCREEN_HEIGHT, SCREEN_WIDTH

import random
import pygame
import math


class Agent(pygame.sprite.Sprite):
    def __init__(self, size, color, x=None, y=None):
        super().__init__()

        self.surf = pygame.Surface((2 * size, 2 * size), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.surf, color, (size, size), size)
        self.rect = self.surf.get_rect()

        self.vmax = 2.0

        self.x = x if x else random.randint(0, SCREEN_WIDTH)
        self.y = y if y else random.randint(0, SCREEN_HEIGHT)

        self.dx = 0
        self.dy = 0

        self.is_alive = True
        self.target = None
        self.age = 0
        self.energy = 0

        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

    def update(self, screen, food=()):
        self.age = self.age + 1

        if self.vmax == 0:
            screen.blit(self.surf, self.rect)
            return

        if self.target and not self.target.is_alive:
            self.target = None

        if self.target:
            squared_dist = (self.x - self.target.x) ** 2 + (self.y - self.target.y) ** 2
            if squared_dist < 400:
                self.target.is_alive = False
                self.energy = self.energy + 1

        if not self.target:
            min_dist = 9999999
            min_agent = None
            for a in food:
                if a is not self and a.is_alive:
                    sq_dist = (self.x - a.x) ** 2 + (self.y - a.y) ** 2
                    if sq_dist < min_dist:
                        min_dist = sq_dist
                        min_agent = a
            if min_dist < 100000:
                self.target = min_agent

        fx = 0
        fy = 0

        if self.target:
            fx += 0.1 * (self.target.x - self.x)
            fy += 0.1 * (self.target.y - self.y)

        self.dx = self.dx + 0.05 * fx
        self.dy = self.dy + 0.05 * fy

        velocity = math.sqrt(self.dx**2 + self.dy**2)
        if velocity > self.vmax:
            self.dx = (self.dx / velocity) * (self.vmax)
            self.dy = (self.dy / velocity) * (self.vmax)

        # update position based on delta x/y
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        # ensure it stays within the screen window
        self.x = max(self.x, 0)
        self.x = min(self.x, SCREEN_WIDTH)
        self.y = max(self.y, 0)
        self.y = min(self.y, SCREEN_HEIGHT)

        # update graphics
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)
        screen.blit(self.surf, self.rect)


class Predator(Agent):
    def __init__(self, x=None, y=None):
        size = 4
        color = (255, 0, 0)
        super().__init__(size, color)
        self.vmax = 2.5


class Prey(Agent):
    def __init__(self, x=None, y=None):
        size = 3
        color = (255, 255, 255)
        super().__init__(size, color)
        self.vmax = 2.0


class Plant(Agent):
    def __init__(self, x=None, y=None):
        size = 2
        color = (0, 128, 0)
        super().__init__(size, color)
        self.vmax = 0
