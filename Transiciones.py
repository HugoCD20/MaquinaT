#----------------q0--------------------
class Transicion1:
    def __init__(self):
        self.estado=1
        self.entrada=0
        self.remplazo="B"
        self.movimiento="R"

class Transicion2:
    def __init__(self):
        self.estado=4
        self.entrada=1
        self.remplazo="B"
        self.movimiento="R"

class Transicion3:
    def __init__(self):
        self.estado=7
        self.entrada="B"
        self.remplazo="B"
        self.movimiento="R"
#----------------q1--------------------
class Transicion4:
    def __init__(self):
        self.estado=1
        self.entrada=0
        self.remplazo=0
        self.movimiento="R"

class Transicion5:
    def __init__(self):
        self.estado=1
        self.entrada=1
        self.remplazo=1
        self.movimiento="R"

class Transicion6:
    def __init__(self):
        self.estado=2
        self.entrada="B"
        self.remplazo="B"
        self.movimiento="L"
#----------------q2--------------------
class Transicion7:
    def __init__(self):
        self.estado=3
        self.entrada=0
        self.remplazo="B"
        self.movimiento="L"
#----------------q3--------------------
class Transicion8:
    def __init__(self):
        self.estado=3
        self.entrada=0
        self.remplazo=0
        self.movimiento="L"

class Transicion9:
    def __init__(self):
        self.estado=3
        self.entrada=1
        self.remplazo=1
        self.movimiento="L"

class Transicion10:
    def __init__(self):
        self.estado=0
        self.entrada="B"
        self.remplazo="B"
        self.movimiento="R"
#----------------q4--------------------
class Transicion11:
    def __init__(self):
        self.estado=4
        self.entrada=0
        self.remplazo=0
        self.movimiento="R"

class Transicion12:
    def __init__(self):
        self.estado=4
        self.entrada=1
        self.remplazo=1
        self.movimiento="R"

class Transicion13:
    def __init__(self):
        self.estado=5
        self.entrada="B"
        self.remplazo="B"
        self.movimiento="L"
#----------------q5--------------------
class Transicion14:
    def __init__(self):
        self.estado=6
        self.entrada=1
        self.remplazo="B"
        self.movimiento="L"
#----------------q6--------------------
class Transicion15:
    def __init__(self):
        self.estado=6
        self.entrada=0
        self.remplazo=0
        self.movimiento="L"

class Transicion16:
    def __init__(self):
        self.estado=6
        self.entrada=1
        self.remplazo=1
        self.movimiento="L"

class Transicion17:
    def __init__(self):
        self.estado=0
        self.entrada="B"
        self.remplazo="B"
        self.movimiento="R"



