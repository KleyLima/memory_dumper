# -*- coding: utf-8 -*-

entrada_diretorio = [[deslocamento for deslocamento in input("Dump 16bytes").split()] for _ in range(2)]

entrada_diretorio[0].extend(entrada_diretorio[1])
entrada_diretorio = entrada_diretorio[0]

FILENAME = '[:8]'
EXT = '[8:11]'
ATRIB = '[11]'
HORA = '[22:24]'
DATA = '[24:26]'
GRANULO_INIT = '[26:28]'

file_name = eval('{}{}'.format(entrada_diretorio, FILENAME))
extension = eval('{}{}'.format(entrada_diretorio, EXT))
atrib = eval('{}{}'.format(entrada_diretorio, ATRIB))
hora = eval('{}{}'.format(entrada_diretorio, HORA))
data = eval('{}{}'.format(entrada_diretorio, DATA))
granulo_init = eval('{}{}'.format(entrada_diretorio, GRANULO_INIT))
