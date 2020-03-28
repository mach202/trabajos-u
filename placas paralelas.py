# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:55:25 2020

@author: tiago
"""

import numpy as np
from copy import deepcopy
from PIL import Image


h=1# la diferencia entre cada nodo en mm
tamuni=400 # tamaño en mm de la caja cuadrada en la que esta el capacitor
diamplac=260 # tamaño de el capacitor en mm
rad=diamplac/2 #radio de las placas
rad2=pow(rad,2)#radio elevado al cuadrado
dis=30#distancia entre placas en mm
it=500 #numero de iteraciones
"""
se halla el tamaño de la matriz a utilizar, se corrige si no es impar para que sea impar y halla un centro entero
"""
tammatriz=tamuni/h 
tam=int(tammatriz) #se toma el entero
if tam/2-int(tam/2)==0:
   tam=tam+1
h=tamuni/tam # se vuelve a obtener H basado en las correciones
#creamos la matriz del sistema
A=np.zeros((tam,tam)) #se crea la matriz del sistema 
centro= (tam/2)+0.5 # se halla el centro para y como para x de la matriz
discentroplacas=round((dis/2)/h, 0) # se halla el numero de nodos que hay entre el centro y la placa de arriba y la de abajo desde el centro
placarriba=(tam/2)-discentroplacas+0.5-1 #fila donde se halla la placa de arriba
placaabajo=(tam/2)+discentroplacas+0.5-1 #fila donde se halla la placa de abajo
lado=round((diamplac/2)/h,0) # numero de nodos en los cuales sus valores estan libres en los lados por la fila de las placas (despues de sus bordes)
n=1 
#se llena la matriz con los valores de voltaje deseados en las placas (en la de arriba 100 v)
for x in range(tam):
   for y in range(tam):
        if x==placarriba :# se corrobora que el for este en la fila de la placa de arriba
            if y>=(tam/2+0.5-lado-1) and y<=(tam/2+0.5+lado-1):# si los valores de y estan entre los nodos en los que se encuetra la placa, entoces se le pone el valor de 100v
                if n==0:
                    print(y)
                A[x,y]=100
H=1
s=1
p=1
f=0
#aqui se realiza el calculo de diferencias finitas
B=deepcopy(A)# se crea una copia desligada de la matriz original la cual servira para realizar la iteraccion 1
for c in range(it):# el for se repite con el numero de iteracciones antes elegido
    f=f+1
    if f>=2:
     A=deepcopy(B)# despues de la primera it se vuelve a crear una copia de la misma la cual servira para la it siguiente                
    for a in range(tam):
        for b in range(tam):            
         if b>=(tam/2+0.5-lado-1) and b<=(tam/2+0.5+lado-1) and (a==placarriba or a==placaabajo): # si entra en este if es por que el for esta en las placas y no se debe realizar ningun cambio
             p=0
         if a==0 or b==0 or b==tam-1 or a==tam-1:# si entra en este if es por que el for esta en los bordes y por sus condiciones de frontera debe permanecer en 0
             H=0
         if (H!=0 and s!=0 and p!=0):# entra en un nodo valido para aplicar el calculo
             B[a,b]=(A[a+1,b]+A[a-1,b]+A[a,b+1]+A[a,b-1])/4 # se calcula el voltaje en ese punto mediante diferencias finitas
         H=1
         s=1
         p=1
 #b es la matriz final del voltaje        
         
matx=np.zeros((tam,tam))# se crea la matriz donde estara el campo electrico en x
maty=np.zeros((tam,tam))# se crea la matriz donde estara el campo electrico en y          
for a in range(tam):
    for b in range(tam):
        if b>=(tam/2+0.5-lado-1) and b<=(tam/2+0.5+lado-1) and (a==placarriba or a==placaabajo):# esta en las placas el for
             p=0
        if a==0 or b==0 or b==tam-1 or a==tam-1:#esta en los bordes el for
             H=0
        if (H!=0 and p!=0):# es un nodo valida
             matx[a,b]=(B[a+1,b]-B[a-1,b])/(2*h)# se realiza el calculo aproximado de la derivada del voltaje, con el nodo de atra y el de adelante (centrada)
             maty[a,b]=(B[a,b+1]-B[a,b-1])/(2*h)             
        H=1
        p=1
img = Image.fromarray(B)


#calculo de la capacitancia
#para ello tomamos el campo electrico en el centro de las placas
valorcampE=matx[int(centro),int(centro)]*pow(10,3)# se multiplica por 10¨¨3 ya que anteriormente sus unidades eran de V/mm
area=3.141592*(rad2/pow(1000,2))#area usada en el capacitor de comsol
cap=(area*valorcampE*8.8541878176*pow(10,-12))/100
img.show()









      
     
    
 
      
      
       
      
             
   
             
             
          
                
            
           
            
        
         
        
        
             
             
         
         
            
            
   
                
           
            
        
        
    
        
    
    









    