import pygame
import sys
import random
import time


pygame.init()


# Цвета
first_color = (200, 200, 200)
second_color = (25, 25, 25)
third_color = (100, 100, 100)

# Окно
displayX = 1280
displayY = 720

screen = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("ProCaster by Ahmed, MoroZ & Govor Games (feet. Шакальное качество corporation & Shalimich.inc)")
pygame.display.set_icon(pygame.image.load("logo_icon.ico"))

screen.fill(first_color)

# ФПС
clock = pygame.time.Clock()
tick = 60

# Шрифты
f1 = pygame.font.Font(None, displayY//10)

# Классы и функции
# Класс сфер
class Sphere:
    def __init__(self, n=None, i=None):
        self.name = n
        self.image = pygame.image.load(i).convert_alpha()

    def getName(self):
        return self.name

    def getImage(self):
        return self.image

    def getImagetobar(self):
        return pygame.transform.scale(self.image, (displayX / 10, displayY / 5.6))


# Класс способностей
class Skill:
    def __init__(self, n=None, i=None, c=None):
        self.name = n
        self.image = pygame.image.load(i).convert_alpha()
        self.cast = c

    def getName(self):
        return self.name

    def getImage(self):
        return self.image

    def getImagetobar(self):
        return pygame.transform.scale(self.image, (displayX / 10, displayY / 5.6))

    def getImagetodesk(self):
        return pygame.transform.scale(self.image, (displayX / 3, displayY / 1.86))

    def getCast(self):
        return self.cast


# Отрисовка активных сфер
def PrintSpheres(active_spheres):
    for j in range(len(active_spheres)):
        screen.blit(active_spheres[j].getImagetobar(), (displayX / 9 + displayX / 9 * j + displayX / 9, displayY - displayY / 4))

# Отрисовка активных способностей
def PrintSkills(active_skills):
    for j in range(len(active_skills)):
        screen.blit(active_skills[j].getImagetobar(), (displayX / 9 + displayX / 9 * (3 + j) + displayX / 9, displayY - displayY / 4))

# Отрисовка способности, которую нужно создать
def PrintGlobalSkill(skill):
    screen.blit(skill.getImagetodesk(), ((displayX - displayX / 9) / 3 + displayX / 9, displayY / 20))

# Отрисовка Invoke
def PrintInvoke():
    screen.blit(invoke, (displayX / 9 + displayX / 9 * 5 + displayX / 9, displayY - displayY / 4))

# Закрасить места под активные сферы
def UnprintSpheres(color):
    for j in range(3):
        pygame.draw.rect(screen, color, (displayX / 9 + displayX / 9 * j + displayX / 9, displayY - displayY / 4, displayX / 10, displayY / 5.6), width=0)

# Закрасить места под активные способности
def UnprintSkills(color):
    for j in range(2):
        pygame.draw.rect(screen, color, (displayX / 9 + displayX / 9 * (3 + j) + displayX / 9, displayY - displayY / 4, displayX / 10, displayY / 5.6), width=0)

# Закрасить место  способности, которую нужно создать
def UnprintGlobalSkill(color):
    pygame.draw.rect(screen, color, ((displayX - displayX / 9) / 3 + displayX / 9, displayY / 20, displayX / 3, displayY / 1.86), width=0)

# Закрасить Invoke
def UnprintInvoke(color):
    pygame.draw.rect(screen, color, (displayX / 9 + displayX / 9 * 5 + displayX / 9, displayY - displayY / 4, displayX / 10, displayY / 5.6), width=0)

# Закрасить всё
def UnprintAll(color):
    UnprintSpheres(color)
    UnprintSkills(color)
    UnprintGlobalSkill(color)
    UnprintInvoke(color)

# Менюшка слева
left_menu = pygame.Surface((displayX/9, displayY))
left_menu.fill(second_color)
left_menu.set_alpha(230)
screen.blit(left_menu, (0, 0))

# Картинки
quas = Sphere("Quas", "pictures\invoker-quas.jpg")
wex = Sphere("Wex", "pictures\invoker-wex.jpg")
exort = Sphere("Exort", "pictures\invoker-exort.jpg")

invoke = pygame.image.load("pictures\invoker-invoke.jpg").convert_alpha()
invoke = pygame.transform.scale(invoke, (displayX/10, displayY/5.6))

cold_snap = Skill("Cold Snap", "pictures\invoker-cold-snap.jpg", [quas, quas, quas])
ghost_walk = Skill("Ghost Walk", "pictures\invoker-ghost-walk.jpg", [quas, quas, wex])
tornado = Skill("Tornado", "pictures\invoker-tornado.jpg", [quas, wex, wex])
e_m_p = Skill("E.M.P", "pictures\invoker-emp.jpg", [wex, wex, wex])
alacrity = Skill("Alacrity", "pictures\invoker-alacrity.jpg", [wex, wex, exort])
chaos_meteor = Skill("Chaos Meteor", "pictures\invoker-chaos-meteor.jpg", [wex, exort, exort])
sun_strike = Skill("Sun Strike", "pictures\invoker-sun-strike.jpg", [exort, exort, exort])
forge_spirit = Skill("Forge Spirit", "pictures\invoker-forge-spirit.jpg", [quas, exort, exort])
ice_wall = Skill("Ice Wall", "pictures\invoker-ice-wall.jpg", [quas, quas, exort])
deafening_blast = Skill("Deafening Blast", "pictures\invoker-deafening-blast.jpg", [quas, wex, exort])

# Список всех сфер
spheres = [quas, wex, exort]
# Список всех способностей
skills = [cold_snap, ghost_walk, tornado, e_m_p, alacrity, chaos_meteor, sun_strike, forge_spirit, ice_wall, deafening_blast]


# Игры
# Игра 1
def Game_1():
    name = "Classic"

    # Список активных сфер
    active_spheres = []
    # Список активных способностей
    active_skills = []

    # Заполнение списка способностей
    skill_list = [skills[random.randint(0, 9)]]
    for i in range(9):
        skill_list.append(skills[random.randint(0, 9)])
        while skill_list[i] == skill_list[i-1]:
            skill_list[i] = skills[random.randint(0, 9)]

    num = 0

    time1 = time.time()

    run = True
    while run:

        # Отрисовка способности, которую нужно создать
        PrintGlobalSkill(skill_list[num])

        for event in pygame.event.get():

            # Нажатие Q
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                if len(active_spheres) < 3:
                    active_spheres.append(quas)
                else:
                    active_spheres.pop(0)
                    active_spheres.append(quas)

            # Нажатие W
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                if len(active_spheres) < 3:
                    active_spheres.append(wex)
                else:
                    active_spheres.pop(0)
                    active_spheres.append(wex)

            # Нажатие E
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if len(active_spheres) < 3:
                    active_spheres.append(exort)
                else:
                    active_spheres.pop(0)
                    active_spheres.append(exort)

            # Нажатие R
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                for jz in skills:
                    if active_spheres.count(quas) == jz.getCast().count(quas)\
                            and active_spheres.count(wex) == jz.getCast().count(wex)\
                            and active_spheres.count(exort) == jz.getCast().count(exort):
                        if len(active_skills) == 0:
                            active_skills.append(jz)
                        elif len(active_skills) == 1 and active_skills[0] != jz:
                            active_skills.append(None)
                            active_skills[1] = active_skills[0]
                            active_skills[0] = jz
                        elif active_skills[0] != jz:
                            active_skills[1] = active_skills[0]
                            active_skills[0] = jz

            # Если способность создана правильно
            if len(active_skills) > 0 and active_skills[0] == skill_list[num]:
                num += 1
                # Выход из режима
                if num == 10:
                    time1 = time.time() - time1
                    UnprintAll(first_color)
                    UnprintGlobalSkill(third_color)
                    text1 = f1.render(str(round(time1, 2)) + "сек", True, second_color)
                    screen.blit(text1, ((displayX - displayX/9)/2, displayY/2))
                    run = False
                    break

            # Выход из режима
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                UnprintAll(first_color)
                run = False
                break

            # Выход
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Отрисовка активных сфер
        PrintSpheres(active_spheres)

        # Отрисовка активных способностей
        PrintSkills(active_skills)

        # Отрисовка Invoke
        PrintInvoke()

        # Обновление экрана
        pygame.display.update()
        clock.tick(60)


# Игра 2
def Game_2():
    name = "Infinity"

    # Список активных сфер
    active_spheres = []
    # Список активных способностей
    active_skills = []

    old_skill = None
    new_skill = skills[random.randint(0, 9)]

    run = True
    while run:

        # Отрисовка способности, которую нужно создать
        PrintGlobalSkill(new_skill)

        for event in pygame.event.get():

            # Нажатие Q
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                if len(active_spheres) < 3:
                    active_spheres.append(quas)
                else:
                    active_spheres.pop(0)
                    active_spheres.append(quas)

            # Нажатие W
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                if len(active_spheres) < 3:
                    active_spheres.append(wex)
                else:
                    active_spheres.pop(0)
                    active_spheres.append(wex)

            # Нажатие E
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if len(active_spheres) < 3:
                    active_spheres.append(exort)
                else:
                    active_spheres.pop(0)
                    active_spheres.append(exort)

            # Нажатие R
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                for jz in skills:
                    if active_spheres.count(quas) == jz.getCast().count(quas)\
                            and active_spheres.count(wex) == jz.getCast().count(wex)\
                            and active_spheres.count(exort) == jz.getCast().count(exort):
                        if len(active_skills) == 0:
                            active_skills.append(jz)
                        elif len(active_skills) == 1 and active_skills[0] != jz:
                            active_skills.append(None)
                            active_skills[1] = active_skills[0]
                            active_skills[0] = jz
                        elif active_skills[0] != jz:
                            active_skills[1] = active_skills[0]
                            active_skills[0] = jz

            # Если способность создана правильно
            if len(active_skills) > 0 and active_skills[0] == new_skill:
                old_skill = new_skill
                while old_skill == new_skill:
                    new_skill = skills[random.randint(0, 9)]

            # Выход из режима
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
                break

            # Выход
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Отрисовка активных сфер
        PrintSpheres(active_spheres)

        # Отрисовка активных способностей
        PrintSkills(active_skills)

        # Отрисовка Invoke
        PrintInvoke()

        # Обновление экрана
        pygame.display.update()
        clock.tick(60)


while True:
    for event in pygame.event.get():

        # Нажатие 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            Game_1()

        # Нажатие 2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            Game_2()

        # Выход
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Обновление экрана
    pygame.display.update()
    clock.tick(60)