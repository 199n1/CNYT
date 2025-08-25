Libreria de operaciones con numeros complejos en python
No se utiliza el archivo de datos complex nativo de python, sino que los numeros complejos se modelan con tuplas.

Representacion de los numeros complejos:
forma cartesiana (a,b) donde a es la parte real y b la imaginaria
forma polar: (r,θ) donde r esel modulo(magnitud) y θ es la fase( radianes)

Funciones implementadas:
la libreria incluye 9 operaciones
1. Suma → suma(z1, z2) 
2. Resta → resta(z1, z2)  
3. Producto → producto(z1, z2)  
4. División → division(z1, z2)  
5. Módulo → modulo(z)  
6. Conjugado → conjugado(z)  
7. Conversión cartesiano → polar → cartesiano_a_polar(z)  
8. Conversión polar → cartesiano → polar_a_cartesiano(p)  
9. Fase → fase(z)
    
Pruebas unitarias
Las pruebas fueron desarrolladas con el framework unittest de Python.  
Cada función cuenta con 2 casos de prueba
