import matplotlib.pyplot as plt 
import numpy as np
import copy

def JeuVie(nLigne,nCol,nIterations):
	matA=np.random.randint(2,size=(nLigne,nCol))
	matB=copy.deepcopy(matA)
	plt.figure(1);plt.clf();
	
	for _ in range(nIterations):
		for i in range(1,nLigne-1):
			for j in range(1,nCol-1):
				somme=np.sum(matA[i-1:i+2,j-1:j+2])
				somme-=matA[i,j]
				if matA[i,j]==0 and somme==3:
					matB[i,j]=1
				elif matA[i,j]==1 and (somme==2 or somme==3):
					matB[i,j]=1
				else:
					matB[i,j]=0
		plt.subplot(111);plt.cla()
		plt.imshow(matB[25:nLigne-25,25:nCol-25])
		plt.draw()
		plt.pause(0.1)

		matA=copy.deepcopy(matB)
	plt.show()
 
 
JeuVie(200,200,2000)
