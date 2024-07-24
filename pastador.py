from time import sleep
import os
import shutil
from random import randint
 
def isextensao(dir):
    print('Checando se ha arquivos com extensao...')
    sleep(0.3)
    for c in dir:
        if '.' in c:
            return True
        else:
            return False

def takeext(dir):
    l = list()
    for c in dir:
        if '.' in c and c != 'pastador.py':
            l.append(c)
    return l

def splitter(arq):
    l = list()
    for c in arq:
        if c[0] != '.' and c[-1] != '.':
            o = c.split('.')
            l.append(o[-1])
    return l
        

def criadir(splited):
    for arq in range(0, len(splited)):
        aq = splited[arq].upper()
        if os.path.exists(aq) == False:
            os.mkdir(f'{splited[arq]}')
            print(f'Pasta {splited[arq]} foi criada')
            sleep(0.2)
            
def coladir(arq):
    s = []
    for c in range(0,len(arq)):
        s.clear
        s = arq[c].split('.')
        pastedir = f'./{s[-1].upper()}'
        totpath = f'{pastedir}/{arq[c]}'
        if os.path.exists(totpath) == False:
            try:
                print(f'Arquivo {arq[c]} foi copiado para {pastedir}')
                shutil.move(f'{arq[c]}', pastedir)
            except:
                print(f'{arq[c]} nao pode ser movido para {pastedir}')
            sleep(0.2)   
        
        
dir = os.listdir('./')
while True:
    numConfirmacao = randint(100,999)
    resp = str(input(f'Este programa vai organizar seus arquivos por pastas. \nDidite [{numConfirmacao}] para continuar'))
    if resp.isnumeric() == False:
        break
    else:
        resp = int(resp)
    if resp == numConfirmacao:
        if isextensao:
            arq = takeext(dir)
            print(f'Preparando para mover {len(arq)} arquivos')
            sleep(4)
            splited = splitter(arq)
            print('Criando As Pastas....')
            sleep(3)
            criadir(splited)
            print('Copiando e colando arquivos')
            sleep(3)
            coladir(arq)
            break
        else:
            print('Nao encontrei arquivos com extensao :(')
            break
    else:
        print(f'{Fore.GREEN}Stopped')
        break
print('Obrigado volte sempre!')
   
    
