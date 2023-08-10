import pyautogui
from game import Radar as r
from time import sleep

from utils import centerClick as c
from config import config

game_br_config = config.read_config('BrowseField')
eixoBrX = game_br_config.get('pos1')[0]
eixoBrY = game_br_config.get('pos1')[1]
section_br_height = game_br_config.get('larg')
section_br_width = game_br_config.get('alt')

game_bag_config = config.read_config('Bag')
eixoBagX = game_bag_config.get('pos2')[0]
eixoBagY = game_bag_config.get('pos2')[1]
eixoBgX = game_bag_config.get('pos1')[0]
eixoBgY = game_bag_config.get('pos1')[1]
section_bag_height = game_bag_config.get('larg')
section_bag_width = game_bag_config.get('alt')


chat_config = config.read_config('msgUser')
xhat = chat_config.get('pos1')[0]
yhat = chat_config.get('pos1')[1]

def cPosition():
    current_position = pyautogui.position()
    x = current_position.x
    y = current_position.y
    print(f"Coordenadas do mouse: x={x}, y={y}")


def ctrlClick():
    pyautogui.keyDown('ctrl')
    pyautogui.click()
    pyautogui.keyUp('ctrl')

def moveToBag():
    x1 = eixoBrX + section_br_width // 2
    y1 = eixoBrY + section_br_height // 6
    x2 = eixoBagX
    y2 = eixoBagY
    pyautogui.mouseDown(x1,y1)
    sleep(1)
    pyautogui.mouseUp(x2,y2)

def moveBagToTable(item):
    item =pyautogui.locateCenterOnScreen(item, region=(eixoBgX, eixoBgY, section_bag_width, section_bag_height), confidence=0.8)
    pyautogui.mouseDown(item)
    sleep(1)
    r.radarPos(5,8)
    pyautogui.mouseUp()

def moveTableToBag(sec1,sec2):
    x1 = eixoBgX
    y1 = eixoBgY
    r.radarPos(sec1,sec2)
    pyautogui.mouseDown()
    sleep(1)
    pyautogui.mouseUp(x1,y1)

def moveToTheSide(a,b,c,d):
    r.radarPos(a,b)
    pyautogui.mouseDown()
    sleep(1)

    r.radarPos(c,d)
    pyautogui.mouseUp()


def openBrowseField():
    pyautogui.rightClick()
    b= pyautogui.locateOnScreen('game/img/browse.png', confidence=0.7)
    while b is None:
        b = pyautogui.locateOnScreen('game/img/browse.png', confidence=0.7)
    c.centerClick(b)

def find_coin(img_number):
    img = pyautogui.locateOnScreen(f'game/img/gold/gold_{img_number}.png', confidence=0.971,
                                   region=(eixoBrX, eixoBrY, section_br_height, section_br_width))
    print(img_number)

    return img_number if img is not None else None


def coinValue():
    for i in range(1, 101):
        img_number = find_coin(i)
        if img_number is not None:
            print(i)
            print(f'encontrado {img_number}')
            return img_number
    return 0

def printCoinPerCoin():
    x=100
    while x > 0: 
            sleep(0.5)
            screenshot = pyautogui.screenshot(region=(eixoBgX-2, eixoBgY-2, section_bag_width+4, section_bag_height+4))#area da bag
            filename = f'gold_{x}.png'
            screenshot.save(filename)
            
            pyautogui.moveTo(1724,600)
            pyautogui.keyDown('ctrl')
            pyautogui.mouseDown()
            pyautogui.moveTo(1781,600)
            pyautogui.mouseUp()
            pyautogui.keyUp('ctrl')
            sleep(0.5)
            pyautogui.moveTo(1382, 534)
            pyautogui.mouseDown()
            pyautogui.moveTo(1215, 534)
            pyautogui.mouseUp()
            pyautogui.click(1317,581)
            sleep(0.5)
            x=x-1

def sendMessage(message):
    pyautogui.hotkey('enter')
    pyautogui.typewrite(message)
    pyautogui.hotkey('enter')
def pause(t):
    sleep(t)

def trowDice():
    print('Jogando dado.')
    dice = None
    flag = 0
    cof = 1
    a = eixoBgX
    b = eixoBgY
    c = section_bag_width
    d = section_bag_height
    diceClick = pyautogui.locateOnScreen('game/img/dice/dice_1.png',region= (a,b,c,d), confidence= 0.6)
    if diceClick is None:
        diceClick = pyautogui.locateOnScreen('game/img/dice/dice_3.png',region= (a,b,c,d), confidence= 0.6)


    pyautogui.click(diceClick)
    sleep(1)
    while True:
        if dice == None:
            dice = pyautogui.locateOnScreen('game/img/dice/dice_1.png',region= (a,b,c,d), confidence= cof)
            flag = 1
            if dice is not None:
                break
            
        if dice == None:
            dice = pyautogui.locateOnScreen('game/img/dice/dice_2.png',region= (a,b,c,d), confidence= cof)
            flag = 2
            if dice is not None:
                break
            
        if dice == None:
            dice = pyautogui.locateOnScreen('game/img/dice/dice_3.png',region= (a,b,c,d), confidence= cof)
            flag = 3
            if dice is not None:
                break
            
        if dice == None:
            dice = pyautogui.locateOnScreen('game/img/dice/dice_4.png',region= (a,b,c,d), confidence= cof)
            flag = 4
            if dice is not None:
                break
            
        if dice == None:
            dice = pyautogui.locateOnScreen('game/img/dice/dice_5.png',region= (a,b,c,d), confidence= cof)
            flag = 5
            if dice is not None:
                break
            
        if dice == None:
            dice = pyautogui.locateOnScreen('game/img/dice/dice_6.png',region= (a,b,c,d), confidence= cof)
            flag = 6
            if dice is not None:
                break

        if dice == None:
            cof = cof-0.001
            print(cof)
            print(flag)
            if cof < 0.94: 
                flag = 3
                break
    print(flag)
    
    sleep(1)
    return flag

def guestClose():
    pyautogui.moveTo(xhat, yhat)
    pyautogui.rightClick()
    subMenu3 = None
    close = None
    while subMenu3 is None:
        subMenu3 = pyautogui.locateOnScreen('game/img/subMenu3.png', confidence=0.8)
        close = pyautogui.locateOnScreen('game/img/close.png', confidence=0.7)
        if subMenu3 is not None:
            while close is None:
                close = pyautogui.locateOnScreen('game/img/close.png', confidence=0.9)
                
            if close is not None:
                pyautogui.moveTo(close)
                pyautogui.click()
                sleep(1)
                break
            break

def guestCls():
    pyautogui.moveTo(xhat, yhat)
    pyautogui.rightClick()
    subMenu3 = None
    cls = None
    while subMenu3 is None:
        subMenu3 = pyautogui.locateOnScreen('game/img/subMenu3.png', confidence=0.8)
        cls = pyautogui.locateOnScreen('game/img/clearWindow.png', confidence=0.7)
        if subMenu3 is not None:
            while cls is None:
                cls = pyautogui.locateOnScreen('game/img/clearWindow.png', confidence=0.9)
                
            if cls is not None:
                pyautogui.moveTo(cls)
                pyautogui.click()
                sleep(1)
                break
            break
     
def moveItems(position, x,y,dif):
    cont=0
    pyautogui.moveTo(position)
    #pyautogui.keyDown('ctrl')
    pyautogui.mouseDown()
    r.radarPos(x,y)
    pyautogui.mouseUp()
    #pyautogui.keyUp('ctrl')
    ''''''
    sleep(1)
    move=pyautogui.locateOnScreen('game/img/moveItem.png', confidence=0.8)
    while move is None:
        move=pyautogui.locateOnScreen('game/img/moveItem.png', confidence=0.8)
    p = pyautogui.locateOnScreen('game/img/leftButton.png', region=move, confidence=0.8)
    while p is None:
        p=pyautogui.locateCenterOnScreen('game/img/leftButton.png', confidence=0.8)
    pyautogui.moveTo(p)
    while cont<dif:
        pyautogui.click()
        cont=cont+1
    pyautogui.hotkey('enter')

     
def moveItems2(position, x,y,dif):
    cont=0
    pyautogui.moveTo(position)
    pyautogui.keyDown('ctrl')
    pyautogui.mouseDown()
    r.radarPos(x,y)
    pyautogui.mouseUp()
    pyautogui.keyUp('ctrl')
    ''''''
    sleep(1)
    move=pyautogui.locateOnScreen('game/img/moveItem.png', confidence=0.8)
    while move is None:
        move=pyautogui.locateOnScreen('game/img/moveItem.png', confidence=0.8)
    p = pyautogui.locateOnScreen('game/img/leftButton.png', region=move, confidence=0.8)
    while p is None:
        p=pyautogui.locateCenterOnScreen('game/img/leftButton.png', confidence=0.8)
    pyautogui.moveTo(p)
    while cont<dif:
        pyautogui.click()
        cont=cont+1
    pyautogui.hotkey('enter')


def giveBack(bet):
    cof = 0.995
    while cof > 0.96:
        x = bet
        while x < 101:
            betPosition= r.find_all_images2(f'game/img/gold/gold_{x}.png', cof)
            #print(cof)
            if betPosition !=[]:
                break
            x=x+1
            #print(x)
        if betPosition !=[]:
            break
        cof = cof - 0.005
        
    if x >= bet:
        retorno = abs(x-bet)
        #print(x)
        print(betPosition)
        moveItems2(betPosition[0], 5, 8, retorno)

    

def payDebit(bet):
    debit = int(bet * 0.8)

    sendMessage(f'Valor a ser pago: {int(debit + bet)}')

    sendMessage(f'Devolvendo valor da aposta')
    giveBack(bet)
    sendMessage(f'Pagando vitoria')
    giveBack(debit)
