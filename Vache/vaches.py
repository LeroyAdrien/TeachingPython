import matplotlib.pyplot as plt
import numpy as np 
import copy

def Vache(nLigne,nCol,nIterations):
	matA=np.random.randint(2,size=(nLigne,nCol))*2-1
	matB=copy.deepcopy(matA)
	plt.figure(1);plt.clf();
	plt.imshow(matA)
	plt.draw()
	plt.pause(8)
	for _ in range(nIterations):
		for i in range(1,nLigne-1):
			for j in range(1,nCol-1):
				somme=np.sum(matA[i-1:i+2,j-1:j+2])
				if somme<0:
					matB[i,j]=-1
				else:
					matB[i,j]=1
		plt.subplot(111);plt.cla()
		plt.imshow(matB)#[25:nLigne-25,25:nCol-25])
		plt.draw()
		plt.pause(2)

		matA=copy.deepcopy(matB)
	plt.show()
	
Vache(100,100,9)
 
