from Transiciones import *

def realizar(cadena):
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
        
        if encontro:
            if control>=0 and control<len(cinta):
                cinta[control]=encontro.remplazo
            estado=encontro.estado
            if encontro.movimiento == "L":
                control-=1
            else:
                control+=1
                
        else: empieza=False
        impresion.append([control, cinta.copy(), resultado])
    return impresion
    


        

