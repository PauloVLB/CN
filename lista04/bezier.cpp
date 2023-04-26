#include <GL/glut.h>
#include <GL/glu.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <vector>

using namespace std;

enum {BEZIER_RECURSIVA, BEZIER_NAORECURSIVA};

//vetor que contem as abscissas dos pontos
vector<float> vx = {-1, 1, 2, 1};
//vetor que contem as ordenadas dos pontos
vector<float> vy = {2, 5, 5, 2};

//implemente uma das duas funções abaixo, mude a variável metodo para alternar o uso de uma ou de outra
//em ambas as funções, o parâmetro v contém ou só as abscissas dos pontos ou só as ordenadas
// por exemplo, se os pontos são (0, 2), (3, 4) e (7, 5)
// bezier será chamada com as abscissas, ou seja, com o vetor 0, 3, 7
// e também será chamada com as ordenadas, ou seja, com o vetor 2, 4, 5

//mude essa variável para usar a função bezier (recursiva) ou bezier2 (não recursiva)
int metodo = BEZIER_RECURSIVA;

//implementacao recursiva (nao use memoization para comparar os tempos)
//retorna o ponto da curva bezier em t considerando os pontos Pa, ..., Pb
//essa função deve ficar consideravelmente lenta a partir de 8+ pontos
float bezier1(vector<float> v, int a, int b, float t) {
	return 0;
}

//implementacao nao recursiva
//retorna o ponto da curva bezier em t considerando os pontos P0, ..., Pv.size()-1
//essa implementação deve ser mais eficiente que a recursiva sem memoization
float bezier2(vector<float> v, float t) {
	return 0;
}

//################################################################
// /!\ DEIXE O CÓDIGO ABAIXO COMO ESTÁ /!\
//################################################################

float tAtual = 0.0; //um ponto é renderizado na reta
int delta = 1; //= 1 ou -1... variação positiva ou negativa de tAtual, quando animacao = 1
int animacao = 1;
float top = 6, bottom = -4, left = -4, right = 6;
int showGuideLines = true;

enum {ADICIONARREMOVER, ALTERAR};
int estado = ADICIONARREMOVER;
int pontoAtual = 0;

void inicializacao() {
	glClearColor(0.5, 0.5, 0.5, 0.0);
}

void funcaoDisplay() {

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(left, right, bottom, top);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	glClear(GL_COLOR_BUFFER_BIT);

	for(int i = 0; i < vx.size(); i++) {
		if(i == pontoAtual && estado == ALTERAR) {
			glColor3f(0, 0, 1);
			glPointSize(6.0);
		} else {
			glColor3f(1, 1, 1);
			glPointSize(3.0);
		}
		glBegin(GL_POINTS);
		glVertex2f(vx[i], vy[i]);
		glEnd();
	}

	//renderização de tAtual
	float px, py;
	if(metodo == BEZIER_NAORECURSIVA) {
		px = bezier2(vx, tAtual);
		py = bezier2(vy, tAtual);
	} else {
		px = bezier1(vx, 0, vx.size()-1, tAtual);
		py = bezier1(vy, 0, vy.size()-1, tAtual);
	}

	glColor3f(1, 1, 1);
	glPointSize(6.0);
	glBegin(GL_POINTS);
	glVertex2f(px, py);
	glEnd();

	if(vx.size() > 2 && showGuideLines) {
		for(int i = 0; i < vx.size()-1; i++) {
			glColor3f(0, 0, 1);
			glBegin(GL_LINES);
			glVertex2f(vx[i], vy[i]);
			glVertex2f(vx[i+1], vy[i+1]);
			glEnd();
		}
	}

	//renderizacao da curva de bezier
	//utiliza varios segmentos de reta para compor a curva
	
	int n = 10*vx.size();
	for(int i = 0; i < n-1; i++) {
		float t = ((float)i)/(n-1);
		float tnext = ((float)(i+1))/(n-1);
		glColor3f(1, 0, 0);
		glBegin(GL_LINES);
		if(metodo == BEZIER_NAORECURSIVA) {
			glVertex2f(bezier2(vx, t), bezier2(vy, t));
			glVertex2f(bezier2(vx, tnext), bezier2(vy, tnext));
		} else {
			glVertex2f(bezier1(vx, 0, vx.size()-1, t), bezier1(vy, 0, vy.size()-1, t));
			glVertex2f(bezier1(vx, 0, vx.size()-1, tnext), bezier1(vy, 0, vy.size()-1, tnext));
		}
		glEnd();
	}

	//escreve um texto na tela para acompanhar a coordenada para t = tAtual
	glRasterPos2f(px+0.1, py+0.1);
	char texto[60];
	sprintf(texto, "t = %.2f, (x, y) = (%.2f, %.2f)", tAtual, px, py);
	for(int i = 0; i < strlen(texto); i++)
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, texto[i]);

	glutSwapBuffers();
	glFlush();
}

void funcaoKeyboard(unsigned char key, int x, int y) {

	if(key == 'q') {
		exit(-1);
	}
	if(!animacao) {
		if(key == 'a') {
			tAtual -= 0.01;
			if(tAtual < 0)
				tAtual = 0;
		}
		if(key == 'd') {
			tAtual += 0.01;
			if(tAtual > 1)
				tAtual = 1;
		}
	}
	if(key == 's')
		animacao = 1 - animacao;
	if(key == 'g')
		showGuideLines = !showGuideLines;
	glutPostRedisplay();
}

void temporizador() {
	glutPostRedisplay();
	if(animacao) {
		tAtual += 0.003*delta;
		if(tAtual > 1) {
			tAtual = 1;
			delta = -1;
		}
		if(tAtual < 0) {
			tAtual = 0;
			delta = 1;
		}
	}
}

void funcaoMouseMotion(int x, int y) {

	GLint viewport[4];
	GLdouble modelview[16];
	GLdouble projection[16];
	GLfloat winX, winY, winZ;
	GLdouble worldX, worldY, worldZ;

	glGetDoublev(GL_MODELVIEW_MATRIX, modelview);
	glGetDoublev(GL_PROJECTION_MATRIX, projection);
	glGetIntegerv(GL_VIEWPORT, viewport);

	winX = (float)x;
	winY = (float)viewport[3] - (float)y;
	winZ = 0;

	gluUnProject(winX, winY, winZ, modelview, projection, viewport, &worldX, &worldY, &worldZ);

	if(estado == ALTERAR) {
		vx[pontoAtual] = worldX;
		vy[pontoAtual] = worldY;
	}
}

void funcaoMouse(int button, int state, int x, int y) {

	GLint viewport[4];
	GLdouble modelview[16];
	GLdouble projection[16];
	GLfloat winX, winY, winZ;
	GLdouble worldX, worldY, worldZ;

	glGetDoublev(GL_MODELVIEW_MATRIX, modelview);
	glGetDoublev(GL_PROJECTION_MATRIX, projection);
	glGetIntegerv(GL_VIEWPORT, viewport);

	winX = (float)x;
	winY = (float)viewport[3] - (float)y;
	winZ = 0;

	gluUnProject(winX, winY, winZ, modelview, projection, viewport, &worldX, &worldY, &worldZ);

	if(state == GLUT_UP) {
		if(estado == ADICIONARREMOVER) {
			if(button == GLUT_LEFT_BUTTON) {
				vx.push_back(worldX);
				vy.push_back(worldY);
			}
			if(button == GLUT_RIGHT_BUTTON) {
				vx.pop_back();
				vy.pop_back();
			}
		} else {
			if(button == GLUT_LEFT_BUTTON) {
				vx[pontoAtual] = worldX;
				vy[pontoAtual] = worldY;
				estado = ADICIONARREMOVER;
			}
		}
	} if(state == GLUT_DOWN) {
		float menorDistancia;
		int pontoMaisProximo = 0;
		for(int i = 0; i < vx.size(); i++) {
			float distancia1 = fabs(vx[i] - worldX) + fabs(vy[i] - worldY);
			if(i == 0 || distancia1 < menorDistancia) {
				menorDistancia = distancia1;
				pontoMaisProximo = i;
			}
		}
		if(menorDistancia < 0.2 && vx.size() > 0 && estado == ADICIONARREMOVER) {
			estado = ALTERAR;
			pontoAtual = pontoMaisProximo;
		}
	}
	glutPostRedisplay();
}


int main(int argc, char **argv) {

	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(800, 800);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("Curvas de Bezier");
	glutKeyboardFunc(funcaoKeyboard);
	glutMouseFunc(funcaoMouse);
	glutMotionFunc(funcaoMouseMotion);
	glutDisplayFunc(funcaoDisplay);
	glutIdleFunc(temporizador);
	inicializacao();

	glutMainLoop();

	return 0;
}
