# ==========================================
# Cubo de Rubik 2x2
# Versão 1
# Representação do estado, movimentos e
# visualização
# ==========================================

import tkinter as tk

# ==========================================
# Estado inicial do cubo
# Cada face é uma matriz 2x2
# ==========================================

E = {

    "U": [
        ["O","O"],
        ["O","O"]
    ],

    "D": [
        ["R","R"],
        ["R","R"]
    ],

    "L": [
        ["G","W"],
        ["G","W"]
    ],

    "F": [
        ["B","B"],
        ["B","B"]
    ],

    "R": [
        ["Y","G"],
        ["Y","G"]
    ],

    "B": [
        ["W","Y"],
        ["W","Y"]
    ]

}



# Função que gira a face
# Exemplo de uso: E["U"] = girar_face_horario(E["U"])
# face ∈ {U, D, L, F, R, B} , esses elementos são matrizes.


def girar_face_horario(face):

    return [

        [face[1][0], face[0][0]],
        [face[1][1], face[0][1]]

    ]


def girar_face_antihorario(face):

    return [

        [face[0][1], face[1][1]],
        [face[0][0], face[1][0]]

    ]


    # Guarda temporariamente a linha de A
    temp = A[linha][:]

    if sentido == 1:
        # Sentido horário
        # A -> B -> C -> D -> A

        A[linha] = B[linha][:]
        B[linha] = C[linha][:]
        C[linha] = D[linha][:]
        D[linha] = temp

    else:
        # Sentido anti-horário
        # A <- D <- C <- B <- A

        A[linha] = D[linha][:]
        D[linha] = C[linha][:]
        C[linha] = B[linha][:]
        B[linha] = temp

    return A, B, C, D



def girar(E, face, sentido):

    if sentido == 1:
        E[face] = girar_face_horario(E[face])
    else:
        E[face] = girar_face_antihorario(E[face])

    return E

def face_associada(movimento):

    match movimento:

        case "UP":
            return "U"

        case "DOWN":
            return "D"

        case "LEFT":
            return "L"

        case "RIGHT":
            return "R"

        case "FRONT":
            return "F"

        case "BACK":
            return "B"

def extrair_vetor(E, movimento):

    match movimento:

        case "UP":

            return [

                E["L"][0][1], E["L"][0][0],
                E["B"][0][1], E["B"][0][0],
                E["R"][0][1], E["R"][0][0],
                E["F"][0][1], E["F"][0][0]

            ]
        case "RIGHT":

            return [

                E["U"][1][1], E["U"][0][1],
                E["B"][0][0], E["B"][1][0],
                E["D"][1][1], E["D"][0][1],
                E["F"][1][1], E["F"][0][1]

            ]
        case "LEFT":

            return [

                E["F"][0][0], E["F"][1][0],
                E["D"][0][0], E["D"][1][0],
                E["B"][1][1], E["B"][0][1],
                E["U"][0][0], E["U"][1][0]

            ]
        
        case "DOWN":

            return [

                E["L"][1][0], E["L"][1][1],
                E["F"][1][0], E["F"][1][1],
                E["R"][1][0], E["R"][1][1],
                E["B"][1][0], E["B"][1][1]

            ]
        
        case "FRONT":

            return [

                E["U"][1][0], E["U"][1][1],
                E["R"][0][0], E["R"][1][0],
                E["D"][0][1], E["D"][0][0],
                E["L"][1][1], E["L"][0][1]

            ]
        
        case "BACK":

            return [

                E["R"][1][1], E["R"][0][1],
                E["U"][0][1], E["U"][0][0],
                E["L"][0][0], E["L"][1][0],
                E["D"][1][0], E["D"][1][1]

            ]
        



def escrever_vetor(E, movimento, V):

    match movimento:

        case "UP":

            E["L"][0][1], E["L"][0][0] = V[0], V[1]
            E["B"][0][1], E["B"][0][0] = V[2], V[3]
            E["R"][0][1], E["R"][0][0] = V[4], V[5]
            E["F"][0][1], E["F"][0][0] = V[6], V[7]

    

        case "RIGHT":

            
            E["U"][1][1], E["U"][0][1] = V[0], V[1]
            E["B"][0][0], E["B"][1][0] = V[2], V[3]
            E["D"][1][1], E["D"][0][1] = V[4], V[5]
            E["F"][1][1], E["F"][0][1] = V[6], V[7]
            
        case "LEFT":

            E["F"][0][0], E["F"][1][0] = V[0], V[1]
            E["D"][0][0], E["D"][1][0] = V[2], V[3]
            E["B"][1][1], E["B"][0][1] = V[4], V[5] 
            E["U"][0][0], E["U"][1][0] = V[6], V[7]

        case "DOWN":

            E["L"][1][0], E["L"][1][1] = V[0], V[1]
            E["F"][1][0], E["F"][1][1] = V[2], V[3]
            E["R"][1][0], E["R"][1][1] = V[4], V[5]
            E["B"][1][0], E["B"][1][1] = V[6], V[7]

        case "FRONT":

            E["U"][1][0], E["U"][1][1] = V[0], V[1]
            E["R"][0][0], E["R"][1][0] = V[2], V[3]
            E["D"][0][1], E["D"][0][0] = V[4], V[5]
            E["L"][1][1], E["L"][0][1] = V[6], V[7]

        case "BACK":

            E["R"][1][1], E["R"][0][1] = V[0], V[1]
            E["U"][0][1], E["U"][0][0] = V[2], V[3]
            E["L"][0][0], E["L"][1][0] = V[4], V[5]
            E["D"][1][0], E["D"][1][1] = V[6], V[7]

            


            
    return E



def SLIDE(V, n):

    N = len(V)

    n = n % N

    return V[-n:] + V[:-n]

# Função Movimento
# Exemplo de uso: E = movimento(E, "UP", 1)

def movimento(E, movimento, sentido):

    
    # Determina qual face deve girar
    face = face_associada(movimento)

    # Gira a face
    E = girar(E, face, sentido)

    # Extrai o vetor ativo
    V = extrair_vetor(E, movimento)

    # Desloca o vetor
    if sentido == 1:
        V = SLIDE(V, +2)
    else:
        V = SLIDE(V, -2)

    # Reescreve o vetor no estado
    E = escrever_vetor(E, movimento, V)

    return E





# Vamos testar um primeiro movimento 
E = movimento(E, "BACK", 1)


# ==========================================
# Conversão letra -> cor
# ==========================================

cores = {

    "W": "white",
    "Y": "yellow",
    "R": "red",
    "O": "orange",
    "G": "green",
    "B": "blue"

}

# ==========================================
# Configuração da janela
# ==========================================

LADO = 60
ESP = 2

janela = tk.Tk()
janela.title("Cubo de Rubik 2x2")



canvas = tk.Canvas(
    janela,
    width=900,
    height=650,
    bg="gray80"
)

canvas.pack()

# ==========================================
# Desenha uma face
# ==========================================

def desenhar_face(face, x, y):

    for linha in range(2):

        for coluna in range(2):

            x1 = x + coluna*(LADO+ESP)
            y1 = y + linha*(LADO+ESP)

            x2 = x1 + LADO
            y2 = y1 + LADO

            cor = cores[E[face][linha][coluna]]

            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill=cor,
                outline="black",
                width=2
            )

    # Contorno da face

    canvas.create_rectangle(
        x-2,
        y-2,
        x + 2*LADO + ESP + 2,
        y + 2*LADO + ESP + 2,
        outline="black",
        width=3
    )

    # Nome da face

    canvas.create_text(
        x + LADO,
        y - 12,
        text=face,
        font=("Arial",12,"bold")
    )

# ==========================================
# Desenha o cubo aberto
# ==========================================

def mostrar():

    canvas.delete("all")

    PASSO = 170

    XF = 220
    YF = 220

    desenhar_face("U", XF, YF-PASSO)

    desenhar_face("L", XF-PASSO, YF)
    desenhar_face("F", XF, YF)
    desenhar_face("R", XF+PASSO, YF)
    desenhar_face("B", XF+2*PASSO, YF)

    desenhar_face("D", XF, YF+PASSO)

# ==========================================
# Programa principal
# ==========================================

mostrar()

janela.mainloop()
