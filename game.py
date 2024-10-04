import pgzrun
import random
import keyboard

WIDTH = 960
HEIGHT = 520

bg = Actor("草.png")
fbullet = Actor('绿钉子.png')
fupbullet = Actor('上绿钉子.png')
fdownbullet = Actor('下绿钉子.png')
fleftbullet = Actor('左绿钉子.png')
bList = []
bupList = []
bleftList = []
bdownList = []
HP = 191981
wm = Actor('红心.png',[200,400])
boss = Actor('黄心.png', [200,200])
bossHP = 114514
bosszt = 'free'
bossbList = []
bossbupList = []
bossbdownList = []
bossbleftList = []
dbullet = Actor('红钉子.png')
dupbullet = Actor('上红钉子.png')
ddownbullet = Actor('下红钉子.png')
dleftbullet = Actor('左红钉子.png')
fbCD = True
bossmove = None
wq = random.randint(1,2)
state = '运行'
def draw():
    global state
    bg.draw()
    wm.draw()
    boss.draw()
    for b in bList:
        b.draw()
    for bup1 in bupList:
        bup1.draw()
    for bdown1 in bdownList:
        bdown1.draw()
    for bleft1 in bleftList:
        bleft1.draw()
    for bossb in bossbList:
        bossb.draw()
    for bossbdown1 in bossbdownList:
        bossbdown1.draw()
    for bossbup1 in bossbupList:
        bossbup1.draw()
    for bossbleft1 in bossbleftList:
        bossbleft1.draw()
    screen.draw.text(str(bossHP) + '/114514', center=[boss.x,boss.y-60],fontsize=35,color='yellow')
    screen.draw.text(str(HP) + '/191981', center=[wm.x, wm.y - 40], fontsize=30, color='red')
    if wq == 1:
        screen.draw.text('weapon:' + 'One nail snag',center=[850,70],fontsize=25,color='green')
    elif wq == 2:
        screen.draw.text('weapon:' + 'Four nail snag', center=[850, 70], fontsize=25, color='purple')
    if state == '成功':
        screen.draw.text('You win!',center=[480,260],fontsize=60,color='yellow')
    elif state == '失败':
        screen.draw.text('Game Over...',center=[480,260],fontsize=60,color='black')
def on_mouse_down(pos):
    if wq == 1:
        fbullet = Actor('绿钉子.png', [pos[0]+100,pos[1]])
        bList.append(fbullet)
    elif wq == 2:
        fdownbullet = Actor('下绿钉子.png', [pos[0],pos[1]+80])
        fupbullet = Actor('上绿钉子.png', [pos[0], pos[1]-80])
        fleftbullet = Actor('左绿钉子.png', [pos[0]-80, pos[1]])
        fbullet = Actor('绿钉子.png', [pos[0]+80,pos[1]])
        bList.append(fbullet)
        bupList.append(fupbullet)
        bleftList.append(fleftbullet)
        bdownList.append(fdownbullet)
def jc():
    for l in bList:
        if l.x >= 1000 or l.x <= -10:
            bList.remove(l)
        if o.y >= 700 or o.y <= -10:
            bupList.remove(o)
    for o1 in bdownList:ssa
        if o1.y >= 700 or o1.y <= -10:
            bdownList.remove(o1)
    for o2 in bossbList:
        if o2.x >= 1000 or o2.x <= -10:
            bossbList.remove(o2)
    for o3 in bossbleftList:
        if o3.x >= 1000 or o2.x <= -10:
            bossbleftList.remove(o3)
    for l1 in bupList:
        if l1.y >= 700 or l1.y <= -10:
            bupList.remove(l1)
    for l2 in bdownList:
        if l2.y >= 700 or l2.y <= -10:
            bdownList.remove(l2)
    for l3 in bleftList:
        if l3.x >= 1000 or l3.x <= -10:
            bleftList.remove(l3)
def exit1():
    exit()
def update():
    global fbCD
    global bossmove
    global bossHP
    global state
    if state != '成功' and state != '失败':
        if keyboard.is_pressed('W') == True:
            wm.y -= 5
        if keyboard.is_pressed('S') == True:
            wm.y +=5
        if keyboard.is_pressed('A') == True:
            wm.x -= 5
        if keyboard.is_pressed('D') == True:
            wm.x += 5
        if wm.x < 0:
            wm.x += 5
        if wm.x > 960:
            wm.x -= 5
        if wm.y > 520:
            wm.y -= 5
        if wm.y < 0:
            wm.y += 5
        if boss.x >960:
            boss.x-=10
        elif boss.x<0:
            if bossHP < 10000:
                boss.x += 20
            else:
                boss.x += 10
        if bossmove == 1:
            if bossHP < 10000:
                boss.x += 20
            else:
                boss.x -= 10
        elif bossmove == 2:
            if bossHP < 10000:
                boss.x += 20
            else:
                boss.x += 10
        else:
            if bossHP < 10000:
                boss.x += 20
            else:
                boss.x += 10
        if bossHP <= 0:
            state = '成功'
        elif HP <= 0:
            state = '失败'
        move()
        collide()
    else:
        clock.schedule_interval(exit1,5)
    jc()
def fbCD1():
    global fbCD
    if fbCD == False:
        fbCD == True
def collide():
    global bossHP
    global HP
    for b in bList:
        if b.colliderect(boss) and wq == 2:
            bossHP -= random.randint(1,10)
        elif b.colliderect(boss) and wq == 1:
            bossHP -= random.randint(6,25)
    for bup2 in bupList:
        if bup2.colliderect(boss):
            bossHP -= random.randint(1,10)
    for bdown2 in bdownList:
        if bdown2.colliderect(boss):
            bossHP -= random.randint(1,10)
    for bleft2 in bleftList:
        if bleft2.colliderect(boss):
            bossHP -= random.randint(1,10)
    for a1 in bossbList:
        if wm.colliderect(a1):
            HP -= random.randint(30,150)
    for a2 in bossbdownList:
        if wm.colliderect(a2):
            HP -= random.randint(30, 150)
    for a3 in bossbupList:
        if wm.colliderect(a3):
            HP -= random.randint(30, 150)
    for a4 in bossbleftList:
        if wm.colliderect(a4):
            HP -= random.randint(30, 150)
    if boss.colliderect(wm):
        HP -= random.randint(80,600)
def move():
    for b in bList:
        b.x -= 8
    for bdown in bdownList:
        bdown.y -= 8
    for bup in bupList:
        bup.y += 8
    for bleft in bleftList:
        bleft.x += 8
    for bossb in bossbList:
        if bossHP < 50000:
            bossb.x-= 7
        else:
            bossb.x -= 4
    for bossbdown1 in bossbdownList:
        if bossHP <50000:
            bossbdown1.y -= 7
        else:
            bossbdown1.y -= 4
    for bossbup1 in bossbupList:
        if bossHP < 50000:
            bossbup1.y += 7
        else:
            bossbup1.y += 4
    for bossbleft1 in bossbleftList:
        if bossHP < 50000:
            bossbleft1.x += 7
        else:
            bossbleft1.x += 4
def bossgj():
    xd = random.randint(1,4)
    if xd == 1 and bossHP >= 70000:
        for op1 in range(3):
            dbullet = Actor('红钉子.png', [wm.x+50, wm.y])
            bossbList.append(dbullet)
            clock.unschedule(bossgj)
        clock.schedule_interval(bossgj,1)
    elif xd == 1 and bossHP < 70000:
        for op2 in range(10):
            dbullet = Actor('红钉子.png',[wm.x+250,wm.y])
            ddownbullet = Actor('下红钉子.png', [wm.x, wm.y+250])
            bossbList.append(dbullet)
            bossbdownList.append(ddownbullet)
            clock.unschedule(bossgj)
        clock.schedule_interval(bossgj,1)
    if xd == 2 and bossHP >= 80000:
        for op3 in range(2):
            dbullet = Actor('红钉子.png',[wm.x+300,wm.y])
            dleftbullet = Actor('左红钉子.png', [wm.x-300, wm.y])
            bossbList.append(dbullet)
            bossbleftList.append(dleftbullet)
            clock.unschedule(bossgj)
        clock.schedule_interval(bossgj,1)
    elif xd == 2 and bossHP < 80000:
        for op4 in range(3):
            dbullet = Actor('红钉子.png', [wm.x + 300, wm.y])
            dleftbullet = Actor('左红钉子.png', [wm.x - 300, wm.y])
            ddownbullet = Actor('下红钉子.png',[wm.x,wm.y+300])
            dupbullet = Actor('上红钉子.png',[wm.x,wm.y-300])
            bossbList.append(dbullet)
            bossbleftList.append(dleftbullet)
            bossbdownList.append(ddownbullet)
            bossbupList.append(dupbullet)
            clock.unschedule(bossgj)
        clock.schedule_interval(bossgj, 1)
    if xd == 3:
        for op5 in range(1):
            dbullet = Actor('红钉子.png', [wm.x + 300, wm.y])
            dleftbullet = Actor('左红钉子.png', [wm.x - 300, wm.y])
            ddownbullet = Actor('下红钉子.png', [wm.x, wm.y + 300])
            dupbullet = Actor('上红钉子.png', [wm.x, wm.y - 300])
            dbullet1 = Actor('红钉子.png', [wm.x + 400, wm.y])
            dleftbullet1 = Actor('左红钉子.png', [wm.x - 400, wm.y])
            ddownbullet1 = Actor('下红钉子.png', [wm.x, wm.y + 400])
            dupbullet1 = Actor('上红钉子.png', [wm.x, wm.y - 400])
            bossbList.append(dbullet)
            bossbleftList.append(dleftbullet)
            bossbdownList.append(ddownbullet)
            bossbupList.append(dupbullet)
            bossbList.append(dbullet1)
            bossbleftList.append(dleftbullet1)
            bossbdownList.append(ddownbullet1)
            bossbupList.append(dupbullet1)
            clock.unschedule(bossgj)
        clock.schedule_interval(bossgj, 1)
def move1():
    global bossmove
    if wm.x>0 and wm.x <480:
        boss.pos = [wm.x + 350,wm.y]
        bossmove = 1
    elif wm.x>480 and wm.x <960:
        boss.pos = [wm.x - 350,wm.y]
        bossmove = 2
def move2():
    global bossmove
    if wm.x>480 and wm.x <960 and boss.x <= 10:
        boss.pos = [wm.x - 350,wm.y]
        bossmove = 2
    if wm.x>0 and wm.x <480 and boss.x >= 950:
        boss.pos = [wm.x + 350,wm.y]
        bossmove = 1
    if wm.x>480 and wm.x <960 and boss.x >= 950:
        boss.pos = [wm.x - 350,wm.y]
        bossmove = 2
    if wm.x>0 and wm.x <480 and boss.x <= 10:
        boss.pos = [wm.x + 350,wm.y]
        bossmove = 1
clock.schedule_interval(move2,1)
clock.schedule_interval(move1,5)
clock.schedule_interval(bossgj,1)
pgzrun.go()
