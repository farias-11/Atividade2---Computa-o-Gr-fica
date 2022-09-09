import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

glBegin(GL_TRIANGLES);
glVertex2f(0, 1);
glVertex2f(-1, 0);
glVertex2f(1, 0);
glEnd();

def Triangulo():
    glBegin(GL_TRIANGLES)
    glEnd()
def main():
    pygame.init() #Inicialize todos os módulos pygame importados
    display = (700, 700) #Define o tamanho da tela (Plano)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #insere o código do pygame dentro do display de demonstração
    gluPerspective(80, #quantos graus o objeto será posicinado
                   (display[0]/display[1]), #tamanho da dela, no caso 700x700,
                   1, #o qual distante o objeto será renderizado
                   20 #Distância a ser desenhado.
    )

glTranslatef(-2,-2, 0);
glBegin(GL_TRIANGLES);
glVertex2f(-2, -1);
glVertex2f(1, -1);
glVertex2f(0, 2);
glEnd();

glRotatef(90, 0, 0, 1);
glBegin(GL_TRIANGLES);
glVertex2f(-2, -1);
glVertex2f(1, -1);
glVertex2f(0, 2);
glEnd();

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Triangulo()
        pygame.display.flip()

main()
