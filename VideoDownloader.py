import os
from pytube import YouTube

def Download():
    print('\n')
    #link do video

    link = input('Insira a url do vídeo: ')
    link = YouTube(link)

    print('===================================================')
    print('\n\n\n\n\n')
    print(link.title)

    stream = link.streams.first()

    stream.download('')
    print('\n\n\n\n\n')

    print('> Download realizado com sucesso! < ')

    os.system("pause")

def Intro():

    print('    ____                    ____  _            ___')
    print('   /  _/___ _____  _____   / __ \(_)________  / (_)')
    print('   / // __ `/ __ \/ ___/  / /_/ / / ___/ __ \/ / /')
    print(' _/ // /_/ / /_/ / /     / ____/ / /__/ /_/ / / /')
    print('/___/\__, /\____/_/     /_/   /_/\___/\____/_/_/')
    print('    /____/')

    print('        __   __          _         _          ')
    print('        \ \ / /         | |       | |         ')
    print('         \ V /___  _   _| |_ _   _| |__   ___ ')
    print('          \ // _ \| | | | __| | | | ''_  \ / _ \'')
    print('          | | (_) | |_| | |_| |_| | |_) |  __/')
    print('          \_/\___/ \__,_|\__|\__,_|_.__/ \___|')
    print('')

    print('    ____                      __                __')
    print('   / __ \____ _      ______  / /___  ____ _____/ /__  _____')
    print('  / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/')
    print(' / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /')
    print('/_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/')
    print('')

Intro()
Download()
