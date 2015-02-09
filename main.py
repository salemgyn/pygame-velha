#coding: utf-8
#! /usr/bin/env python
#
#Autor: Melky-Salém <msalem@globo.com>
#Descrição: Jogo da Velha com AI Minimax

import pygame,sys
from pygame.locals import *

class JogoVelha(object):
	ESQUERDO = 1

	BRANCO 		  = (255, 255, 255)
	PRETO 		  = (  0,   0,   0)
	CINZA 		  = (128, 128, 128)
	PRATA 		  = (192, 192, 192)
	VERMELHO 	  = (255,   0,   0)
	VERDE 		  = (  0, 128,   0)
	LIMA 		  = (  0, 255,   0)
	AZUL 		  = (  0,   0, 255)
	AZUL_ESCURO   = (  0,   0, 128)
	AMARELO 	  = (255, 255,   0)
	AQUA 		  = (  0, 255, 255)
	MAGENTA 	  = (255,   0, 255)
	MARROM 		  = (128,   0,   0)
	AZUl_PETROLEO = (  0, 128, 128)
	ROXO 		  = (128,   0, 128)
	OLIVA 		  = (128, 128,   0)

	ESPACO_O_1 = ( 10,  10, 110, 110)
	ESPACO_O_2 = (145,  10, 110, 110)
	ESPACO_O_3 = (290,  10, 110, 110)

	ESPACO_O_4 = ( 10, 145, 110, 110)
	ESPACO_O_5 = (145, 145, 110, 110)
	ESPACO_O_6 = (290, 145, 110, 110)

	ESPACO_O_7 = ( 10, 290, 110, 110)
	ESPACO_O_8 = (145, 290, 110, 110)
	ESPACO_O_9 = (290, 290, 110, 110)

	ESPACO_X_1_INI = ( 10,  10),(110, 110)
	ESPACO_X_1_FIN = (110,  10),( 10, 110)
	ESPACO_X_2_INI = (145,  10),(245, 110)
	ESPACO_X_2_FIN = (145, 110),(245,  10)
	ESPACO_X_3_INI = (290,  10),(390, 110)
	ESPACO_X_3_FIN = (290, 110),(390,  10)

	ESPACO_X_4_INI = ( 10, 145),(110, 245)
	ESPACO_X_4_FIN = ( 10, 245),(110, 145)
	ESPACO_X_5_INI = (145, 145),(245, 245)
	ESPACO_X_5_FIN = (145, 245),(245, 145)
	ESPACO_X_6_INI = (290, 145),(390, 245)
	ESPACO_X_6_FIN = (290, 245),(390, 145)

	ESPACO_X_7_INI = ( 10, 290),(110, 390)
	ESPACO_X_7_FIN = ( 10, 390),(110, 290)
	ESPACO_X_8_INI = (145, 290),(245, 390)
	ESPACO_X_8_FIN = (145, 390),(245, 290)
	ESPACO_X_9_INI = (290, 290),(390, 390)
	ESPACO_X_9_FIN = (290, 390),(390, 290)

	pygame.init()
	pygame.display.set_caption('Jogo da Velha com AI')

	TELA = pygame.display.set_mode((420,420))
	BACKGROUND = pygame.Surface(TELA.get_size())

	BACKGROUND = BACKGROUND.convert()

	ESPESSURA = 5

	# CRIAÇÃO DAS LINHAS DE DIVISÃO (POPULAR #)
	def cria_linhas(self):
		pygame.draw.line(self.BACKGROUND, self.PRETO, (  0, 125), (420, 125), self.ESPESSURA)
		pygame.draw.line(self.BACKGROUND, self.PRETO, (  0, 275), (420, 275), self.ESPESSURA)
		pygame.draw.line(self.BACKGROUND, self.PRETO, (125,   0), (125, 420), self.ESPESSURA)
		pygame.draw.line(self.BACKGROUND, self.PRETO, (275,   0), (275, 420), self.ESPESSURA)

	# PARA O
	# pygame.draw.ellipse(BACKGROUND, AZUL, ESPACO_O_1, ESPESSURA)

	# PARA X
	# pygame.draw.line(BACKGROUND, VERDE, ESPACO_X_1_INI[0], ESPACO_X_1_INI[1], ESPESSURA)
	# pygame.draw.line(BACKGROUND, VERDE, ESPACO_X_1_FIN[0], ESPACO_X_1_FIN[1], ESPESSURA)

	def marque_em(self,mouse_pos):
		x,y = mouse_pos

		if x <= 125 and y <= 125:
			pygame.draw.line(self.BACKGROUND, self.VERDE, self.ESPACO_X_1_INI[0], self.ESPACO_X_1_INI[1], self.ESPESSURA)
			pygame.draw.line(self.BACKGROUND, self.VERDE, self.ESPACO_X_1_FIN[0], self.ESPACO_X_1_FIN[1], self.ESPESSURA)
		elif x <= 275 and y <= 125:
			pygame.draw.line(self.BACKGROUND, self.VERDE, self.ESPACO_X_2_INI[0], self.ESPACO_X_2_INI[1], self.ESPESSURA)
			pygame.draw.line(self.BACKGROUND, self.VERDE, self.ESPACO_X_2_FIN[0], self.ESPACO_X_2_FIN[1], self.ESPESSURA)
		elif x > 275 and y <= 125:
			pygame.draw.line(self.BACKGROUND, self.VERDE, self.ESPACO_X_3_INI[0], self.ESPACO_X_3_INI[1], self.ESPESSURA)
			pygame.draw.line(self.BACKGROUND, self.VERDE, self.ESPACO_X_3_FIN[0], self.ESPACO_X_3_FIN[1], self.ESPESSURA)

	def main(self):
		self.BACKGROUND.fill(self.BRANCO)
		self.cria_linhas()
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONUP and event.button == self.ESQUERDO:
					self.marque_em(event.pos)
			self.TELA.blit(self.BACKGROUND,(0,0))
			pygame.display.update()

jogoVelha = JogoVelha()
jogoVelha.main()