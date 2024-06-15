from Transiciones import *

def realizar(cadena):
    Transiciones=[
        [Transicion(1,0,"B","R",0),Transicion(4,1,"B","R",0),Transicion(7,"B","B","R",0)],
        [Transicion(1,0,0,"R",1),Transicion(1,1,1,"R",1),Transicion(2,"B","B","L",1)],
        [Transicion(3,0,"B","L",2)],
        [Transicion(3,0,0,"L",3),Transicion(3,1,1,"L",3),Transicion(0,"B","B","R",3)],
        [Transicion(4,0,0,"R",4),Transicion(4,1,1,"R",4),Transicion(5,"B","B","L",4)],
        [Transicion(6,1,"B","L",5)],
        [Transicion(6,0,0,"L",6),Transicion(6,1,1,"L",6),Transicion(0,"B","B","R",6)],
    ]

    control=0
    estado=0
    empieza=True
    cinta=[]
    resultado="Rechazada"
    cadena=str(cadena)
    for i in cadena:
        cinta.append(i)

    impresion=[]

    while empieza:
        encontro=None
        if control<0:
            auxiliar='B'
        else:
            if control>=len(cinta):
                auxiliar='B'
            else:
                auxiliar=str(cinta[control])
        if estado !=7:
            for i in Transiciones[estado]: 
                x=str(i.entrada)        
                if auxiliar == x:
                    encontro=i
        else: 
            resultado="Aceptado" 
            empieza=False
        
        impresion.append([control, cinta.copy(), resultado,encontro])
        if encontro:
            if control>=0 and control<len(cinta):
                cinta[control]=encontro.remplazo
            estado=encontro.estado
            if encontro.movimiento == "L":
                control-=1
            else:
                control+=1
                
        else: empieza=False
    return impresion
    


        

