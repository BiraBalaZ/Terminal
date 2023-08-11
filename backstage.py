from os import system
from time import sleep
import colors as c

def loop():
    system('cls')
    title('Bira`s Terminal')
    sleep(2)

    # Pedindo nome de usuário ao usuário
    requestName()

# Função para escrever um título
def title(title):
    print('-' * 30)
    print(f"{title :^30}")
    print('-' * 30)

def fakeLoad(phrase, sec):
    c.color_set(c.st_none, c.c_blue, c.bg_gray)
    system('cls')
    print(f'{phrase} [ ▢▢▢▢▢▢▢▢▢▢ ]')
    sleep(sec)
    system('cls')
    print(f'{phrase} [ ▣▢▢▢▢▢▢▢▢▢ ]')
    sleep(sec)
    system('cls')
    print(f'{phrase} [ ▣▣▢▢▢▢▢▢▢▢ ]')
    sleep(sec)
    system('cls')
    print(f'{phrase} [ ▣▣▣▢▢▢▢▢▢▢ ]')
    sleep(sec)
    system('cls')
    print(f'{phrase} [ ▣▣▣▣▢▢▢▢▢▢ ]')
    sleep(sec)
    system('cls')
    print(f'{phrase} [ ▣▣▣▣▣▢▢▢▢▢ ]')
    sleep(sec)
    system('cls')
    print(f'{phrase} [ ▣▣▣▣▣▣▢▢▢▢ ]')
    sleep(sec)
    system('cls')
    print(f'{phrase} [ ▣▣▣▣▣▣▣▢▢▢ ]')
    sleep(sec)
    system('cls')
    print(f'{phrase} [ ▣▣▣▣▣▣▣▣▢▢ ]')
    sleep(sec)
    system('cls')
    print(f'{phrase} [ ▣▣▣▣▣▣▣▣▣▢ ]')
    sleep(sec)
    system('cls')
    print(f'{phrase} [ ▣▣▣▣▣▣▣▣▣▣ ]\033[m')
    sleep(sec)
    system('cls')

def welcomeMaster():
    system('cls')
    sleep(.4)
    print(f'\033[{c.st_none};{c.c_green};{c.bg_gray}m-' * 30)

    sleep(1.5)
    system('cls')
    print(f'-' * 30)
    print(f"{'Welcome       ' :^30}")
    
    sleep(1)
    system('cls')
    print(f'-' * 30)
    print(f"{'Welcome Master' :^30}")
    
    sleep(1.5)
    system('cls')
    print(f'-' * 30)
    print(f"{'Welcome Master' :^30}")
    print('-' * 30)
    print(f'\033[m')

def program():
    prompt = input(f'[\033[{c.st_none};{c.c_red};{c.bg_gray}mroot\033[m@\033[{c.st_none};{c.c_green};{c.bg_gray}mterminal\033[m ~]$ ')

    if (prompt == 'exit'):
        print('Você escolheu sair. Até logo!')
    elif (prompt == 'restart'):
        loop()
    elif (prompt == 'cls' or prompt == 'clear'):
        system('cls')
        program()
    elif (prompt ==  'cl' or prompt ==  'csl'):
        print('Você quis dizer "cls"? [Y/N]')
        res = input(f'[\033[{c.st_none};{c.c_red};{c.bg_gray}mroot\033[m@\033[{c.st_none};{c.c_green};{c.bg_gray}mterminal\033[m ~]$ ')

        # Se Sim ou Se Não
        if (res.upper() == 'Y'):
            system('cls')
            program()
        elif (res.upper() == 'N'):
            print('Certo, então vamos tentar novamente:')
            program()
        else:
            print(f'"{res}" não é um comando reconhecido pelo sistema.')
            program()
    else:
        print(f'"{prompt}" não é um comando reconhecido pelo sistema.')
        program()

def requestName():
    username = str(input(f'\nUsername: \033[{c.st_none};{c.c_green};{c.bg_gray}m'))
    print(f'\033[m')
    fakeLoad('Reading Credentials', .1)

    # se o nome de usuáio for igual à 'root' ele pede a senha, caso contrário o programa encerra
    if (username == 'root'):

        # Pedindo a senha do usuário root
        requestPassword()
        
    else:
        print('Username not found. Try again.')
        requestName()

def requestPassword():
    password = str(input(f'\033[mPassword: \033[{c.st_none};{c.c_red};{c.bg_gray}m'))
    print(f'\033[m')

    # Se a senha estiver correta ele segue o programa
    if (password == '123'):
        fakeLoad('Downloading Archives', .3)
        fakeLoad('Making Coffee', .2)

        welcomeMaster()
        sleep(1)
        program()
    else:
        print('Incorrect credentials.\n')
        requestPassword()

# Iniciando o programa de fato
loop()

#                                   /
# _____ _____ _____               / /  ____          _                ______
# |  _ \_   _|  __ \     /\      / /  |  _ \   /\   | |        /\    |___  /   
# | |_) || | | |__) |   /  \    / /__ | |_) | /  \  | |       /  \      / /    
# |  _ < | | |  _  /   / /\ \  |___  /|  _ < / /\ \ | |      / /\ \    / /     
# | |_) || |_| | \ \  / ____ \    / / | |_) / ____ \| |____ / ____ \  / /__    
# |____/_____|_|  \_\/_/    \_\  / /  \____/_/    \_\______/_/    \_\/_____|   
#                               / /     
#                               /