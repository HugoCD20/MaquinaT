from Transiciones import *

Transiciones=[
    [Transicion1(),Transicion2(),Transicion3()],
    [Transicion4(),Transicion5(),Transicion6()],
    [Transicion7()],
    [Transicion8(),Transicion9(),Transicion10()],
    [Transicion11(),Transicion12(),Transicion13()],
    [Transicion14()],
    [Transicion15(),Transicion16(),Transicion17()],
]

control=0
estado=0
empieza=True
cinta=[]
resultado="Rechazada"
cadena=input("Ingresa la cadena palindroma de 0 y 1:")
cadena=str(cadena)
for i in cadena:
    cinta.append(int(i))


while empieza:
    encontro=None
    if control<0:
        auxiliar=-1
    else:
        if control>=len(cinta):
            auxiliar=7
        else:
            auxiliar=cinta[control]
    if estado !=7:
        for i in Transiciones[estado]:            
            if auxiliar == i.entrada:
                encontro=i
    else: 
        resultado="Aceptado" 
        empieza=False
    
    if encontro:
        if control>=0 and control<len(cinta):
            if encontro.remplazo == 'B':
                cinta.pop(control)
            else:
                cinta[control]=encontro.remplazo
        estado=encontro.estado
        if encontro.movimiento == "L":
            control-=1
        else:
            control+=1
    else: empieza=False

print(resultado)

        

