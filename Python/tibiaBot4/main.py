from game import Radar as r
from game import userEvents as user
import pyautogui as p


r.Altenador

row =5
col =9
col1 = col-1
awaitGuest = 1
r.radarPersona(row,col)
r.radarPersona(row,col1)

def initBet():
    user.sendMessage('Para apostar voce precisa adicionar no mínimo 25cc na minha frente.')
    user.sendMessage('Valor maximo de aposta é de 100cc.')
    awaitBet = 1
    while True:
        if awaitBet == 1:
            awaitBet = r.Guest(row,col1)
        else:
            user.sendMessage('Abra um chat no meu privado para apostar.')
            user.pause(1)
            break

 
r.Altenador
while True: 

    if awaitGuest == 1:
        awaitGuest = r.Guest(row,col)
        #Verificar se a tela do Tibia está ativa, caso não esteja desativar.

    else: #Um Visitante chegou!
        while True:            
            messageTo =  None
            subMenu2 = None
            r.radarPos(row, col)
            p.rightClick()
            subMenu2 =  p.locateOnScreen('game/img/subMenu2.png', confidence=0.6)
            menuGuest = p.locateOnScreen('game/img/subMenuGuest.png', confidence=0.5)
            if menuGuest is not None:
                messageTo = p.locateOnScreen('game/img/messageTo.png', confidence=0.7)
                if messageTo is not None:
                    p.moveTo(messageTo)
                    p.click()
                    menuGuest = None
                    break
            elif subMenu2 is not None:
                p.hotkey('esc')
                awaitGuest = 1
                break
            
        if awaitGuest == 0:
            awaitBet = 1
            initBet()
            bet = 0
            check = 0
            while True:#Aposta!
                if awaitBet == 1:
                    awaitBet = r.Guest(row,col1)
                    '''if check == 5:
                        user.guestClose()
                        print('teste9')
                        break'''
                else: #Usuario inseriu algo no campo de aposta!
                    check = 0
                    r.radarPos(row, col1)
                    bet1 = user.coinValue()
                    bet = bet + bet1
                    if bet1 == 0:
                        user.sendMessage('...')
                        awaitGuest = r.Guest(row,col)
                        if awaitGuest == 1:
                            user.guestClose()
                            break
                    if bet < 25:
                        user.sendMessage(f'Valor apostado: {bet}')
                        user.sendMessage('Tu precisa adicionar no min 25cc para apostar.')
                        user.moveToTheSide(5,8,4,8)
                        awaitBet = 1
                        check = check + 1
                        if check > 5:
                            user.guestClose()
                            user.sendMessage('Estou reiniciando o jogo, pois o valor inserido nao confere com o min para aposta.')
                            awaitGuest = 0
                            #Aqui devolver o valor apostado.
                            user.sleep(3)
                            break
                    elif bet >= 25:#usuario decide qual será a aposta que ele irá fazer
                        user.moveToBag()
                        user.guestCls()
                        user.sendMessage('Para apostar em 1,2,3 escreva baixo, para 4, 5 ou 6 digite alto.')
                        user.guestCls()
                        choice = None
                        flag = 0
                        user.sleep(2)
                        while True:
                            if choice == None:
                                choice = p.locateOnScreen('game/img/alto.png', confidence= 0.85)
                                flag = 1 
                            if choice == None:
                                choice = p.locateOnScreen('game/img/baixo.png', confidence= 0.85)
                                flag = 2
                            if choice != None:
                                break
                        if flag == 1:
                            dice = user.trowDice()
                            if dice > 3:
                                user.sendMessage('Voce ganhou!')
                                user.payDebit(bet)
                                user.guestClose()
                                user.sleep(3)
                            else:
                                user.sendMessage('Voce perdeu!')
                                user.guestClose()
                                user.sleep(3)
                            break
                        elif flag == 2:
                            dice = user.trowDice()
                            if dice <= 3:
                                user.sendMessage('Voce ganhou!')
                                user.payDebit(bet)
                                user.guestClose()
                                user.sleep(3)
                            else:
                                user.sendMessage('Voce perdeu!')
                                user.guestClose()
                                user.sleep(3)
                            break
                #check = check + 1
                


        #break


