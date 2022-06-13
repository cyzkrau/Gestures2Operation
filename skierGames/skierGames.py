from ast import ImportFrom
from sre_constants import RANGE_UNI_IGNORE
from time import time
import pygame, sys, random

from sympy import li
import gesture
import cv2
import os

skier_images = [
    "./bg_img/skier_down.png", "./bg_img/skier_right1.png",
    "./bg_img/skier_right2.png", "./bg_img/skier_left2.png",
    "./bg_img/skier_left1.png"
]

obstacle_images = [
    "./bg_img/skier_tree.png",
    "./bg_img/skier_tree_nt.png",
    "./bg_img/skier_snowman.png",
]

flag_images = ["./bg_img/skier_flag_yellow.png", "./bg_img/skier_flag_red.png"]

yellow_ball_image = "./bg_img/skier_ball.png"
blue_ball_image = "./bg_img/skier_ball_blue.png"
coin_image = "./bg_img/skier_coin.png"
heart_image = "./bg_img/skier_heart.png"

people_images = ["./bg_img/skier_others1.png", "./bg_img/skier_others2.png"]

bonus_image = ["./bg_img/skier_go.png"]

monster_image = ["./bg_img/skier_monster.png"]

background_image = "./bg_img/skier_background.png"


class SkierClass(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./bg_img/skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -2: self.angle = -2
        if self.angle > 2: self.angle = 2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]
        return speed

    def move(self, speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20: self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620


class ObstacleClass(pygame.sprite.Sprite):

    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def scroll(self, terrainPos):
        self.rect.centery = self.location[1] - terrainPos


def create_map(start, end):
    obstacles = pygame.sprite.Group()
    locations = []
    gates = pygame.sprite.Group()
    for i in range(10):
        row = random.randint(start, end)
        col = random.randint(0, 9)
        location = [col * 64 + 20, row * 64 + 20]
        if not (location in locations):
            locations.append(location)
            type = random.choice([
                "obstacle", "obstacle", "obstacle", "obstacle", "obstacle",
                "people", "people", "people", "people", "flag", "yellow_ball",
                "coin", "heart", "go", "monster", "background"
            ])

            if type == "obstacle": img = random.choice(obstacle_images)
            elif type == "flag": img = random.choice(flag_images)
            elif type == "yellow_ball": img = yellow_ball_image
            elif type == "coin": img = coin_image
            elif type == "heart": img = heart_image
            elif type == "people": img = random.choice(people_images)
            elif type == "go": img = random.choice(bonus_image)
            elif type == "monster": img = random.choice(monster_image)
            elif type == "background": img = background_image
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)
    return obstacles


def animate():
    screen.fill([255, 255, 255])
    pygame.display.update(obstacles.draw(screen))
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    screen.blit(life_text, [10, 50])
    pygame.display.flip()


def updateObstacleGroup(map0, map1):
    obstacles = pygame.sprite.Group()
    for ob in map0:
        obstacles.add(ob)
    for ob in map1:
        obstacles.add(ob)
    return obstacles


def game_over():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("EXIT GAME")
                    exit()
                elif event.key == pygame.K_RIGHT:
                    print("PLAY AGIAIN")
                    os.system("python3 ./skierGames.py")

        game_over_text = font.render("Game Over!", 1, (0, 0, 0))
        hint_play_text = font.render("Press RIGHT to Play Again", 1, (0, 0, 0))
        hint_exit_text = font.render("Press LEFT to Exit", 1, (0, 0, 0))
        pygame.display.update(obstacles.draw(screen))
        screen.blit(game_over_text, [200, 250])
        screen.blit(hint_play_text, [100, 290])
        screen.blit(hint_exit_text, [175, 330])
        pygame.display.flip()


def game_win():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("EXIT GAME")
                    exit()
                elif event.key == pygame.K_RIGHT:
                    print("PLAY AGIAIN")
                    os.system("python3 ./skierGames.py")

        game_over_text = font.render("You Win!", 1, (0, 0, 0))
        hint_play_text = font.render("Press RIGHT to Play Again", 1, (0, 0, 0))
        hint_exit_text = font.render("Press LEFT to Exit", 1, (0, 0, 0))
        pygame.display.update(obstacles.draw(screen))
        screen.blit(game_over_text, [200, 250])
        screen.blit(hint_play_text, [100, 290])
        screen.blit(hint_exit_text, [175, 330])
        pygame.display.flip()


use_hand = True

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("./bg_music/bg_music_jp.flac")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode([640, 640])
    clock = pygame.time.Clock()
    skier = SkierClass()
    speed = [0, 6]
    map_position = 0
    points = 0
    life = 3
    map0 = create_map(20, 29)
    map1 = create_map(10, 19)
    print(map0)
    activeMap = 0

    obstacles = updateObstacleGroup(map0, map1)

    font = pygame.font.Font(None, 50)
    if use_hand:
        hand_detector = gesture.GestureMonitor(width=600, height=300)

    while True:
        clock.tick(30)
        if use_hand:
            hand_detector.update()
            hand_detector.show()
            if cv2.waitKey(1) & 0xFF == 27:
                break
            if hand_detector.is_left():
                speed = skier.turn(-1)
            elif hand_detector.is_right():
                speed = skier.turn(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speed = skier.turn(-1)
                elif event.key == pygame.K_RIGHT:
                    speed = skier.turn(1)

        skier.move(speed)
        map_position += speed[1]

        if map_position >= 640 and activeMap == 0:
            activeMap = 1
            map0 = create_map(20, 29)
            obstacles = updateObstacleGroup(map0, map1)
        if map_position >= 1280 and activeMap == 1:
            activeMap = 0
            for ob in map0:
                ob.location[1] = ob.location[1] - 1280
            map_position = map_position - 1280
            map1 = create_map(10, 19)
            obstacles = updateObstacleGroup(map0, map1)

        for obstacle in obstacles:
            obstacle.scroll(map_position)

        hit = pygame.sprite.spritecollide(skier, obstacles, False)
        if hit:
            if hit[0].type == "obstacle" and not hit[0].passed:
                life -= 1
                skier.image = pygame.image.load("./bg_img/skier_crash.png")
                animate()
                pygame.time.delay(1000)
                skier.image = pygame.image.load("./bg_img/skier_down.png")
                skier.angle = 0
                speed = [0, 6]
                hit[0].passed = True

            if hit[0].type == "people" and not hit[0].passed:
                points -= 50
                skier.image = pygame.image.load("./bg_img/skier_crash.png")
                animate()
                pygame.time.delay(1000)
                skier.image = pygame.image.load("./bg_img/skier_down.png")
                skier.angle = 0
                speed = [0, 6]
                hit[0].passed = True

            if hit[0].type == "monster" and not hit[0].passed:
                skier.image = pygame.image.load("./bg_img/skier_crash.png")
                animate()
                life = 0

            elif hit[0].type == "flag" and not hit[0].passed:
                points += 10
                obstacles.remove(hit[0])

            elif hit[0].type == "coin" and not hit[0].passed:
                points += 20
                obstacles.remove(hit[0])

            elif hit[0].type == "yellow_ball" and not hit[0].passed:
                points += 40
                obstacles.remove(hit[0])

            elif hit[0].type == "heart" and not hit[0].passed:
                life += 1
                obstacles.remove(hit[0])

            elif hit[0].type == "go" and not hit[0].passed:
                points += 5
                skier.image = pygame.image.load("./bg_img/skier_down.png")
                animate()
                skier.angle = 0
                speed = [0, 16]
                hit[0].passed = True
                for i in range(10):
                    skier.move(speed)
                    map_position += speed[1]
                    if map_position >= 640 and activeMap == 0:
                        activeMap = 1
                    map0 = create_map(20, 29)
                    obstacles = updateObstacleGroup(map0, map1)
                    if map_position >= 1280 and activeMap == 1:
                        activeMap = 0
                        for ob in map0:
                            ob.location[1] = ob.location[1] - 1280
                        map_position = map_position - 1280
                        map1 = create_map(10, 19)
                        obstacles = updateObstacleGroup(map0, map1)
                    pygame.time.delay(50)
                    animate()
                speed = [0, 6]

        score_text = font.render("Score: " + str(points), 1, (0, 0, 0))
        life_text = font.render("Life: " + str(life), 1, (0, 0, 0))

        if life == 0 or points < -200:
            game_over()
            break
        if points >= 500:
            game_win()
        if life > 20:
            life = 20

        animate()

    pygame.mixer.music.set_volume(0)
