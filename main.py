from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("800x700")
ventana.title("Metodo Gauss Jordan")
ventana.resizable(False,False)
ventana.config(background = "#A7A7A7")
main_title = Label(text = "GAUSS JORDAN", font = ("Cambria", 14), bg = "#A7A7A7", fg = "black", width = "500", height = "2")
main_title.pack()

#funcion que muestra el manual de usuario
def manual():
    raiz2=Toplevel()
    raiz2.geometry("980x800")
    raiz2.config(bg="#A7A7A7")
    raiz2.title("Manual usuario")
    titulo2=Label(raiz2,text="Manual usuario", font=(14), bg = "#A7A7A7", fg = "black", width = "500", height = "2")
    titulo2.pack()

    explicacion1 = Label(raiz2, text="COMO USAR EL PROGRAMA:", font=("Franklin Gothic Demi", 14, "bold"), fg="white",bg="#A7A7A7")
    explicacion1.place(x=40, y=65)
    explicacion2 = Label(raiz2, text="INGRESAR MATRICES", font=("Georgia", 14, "bold"), fg="white", bg="#A7A7A7")
    explicacion2.place(x=60, y=100)
    explicacion3 = Label(raiz2,text="ASD",font=("Georgia", 14, "bold"), fg="white", bg="#A7A7A7")
    explicacion3.place(x=80, y=130)
    explicacion4 = Label(raiz2, text="ASD ",font=("Georgia", 14, "bold"), fg="white", bg="#A7A7A7")
    explicacion4.place(x=80, y=190)
    explicacion5 = Label(raiz2, text="ASD",font=("Georgia", 14, "bold"), fg="white", bg="#A7A7A7")
    explicacion5.place(x=80, y=220)
    explicacion6 = Label(raiz2,text="ASD",font=("Georgia", 14, "bold"), fg="white", bg="#A7A7A7")
    explicacion6.place(x=80, y=250)
    explicacion7 = Label(raiz2, text="ASD",font=("Georgia", 14, "bold"), fg="white", bg="#A7A7A7")
    explicacion7.place(x=80, y=280)

#Obtener y almacenar datos de la matrices
a = StringVar()
b = StringVar()
c = StringVar()
d = StringVar()
e = StringVar()
f = StringVar()
g = StringVar()
h = StringVar()
i = StringVar()
j = StringVar()
k = StringVar()
l = StringVar()

#campos de texto
a_label= Label(text="Ingrese (0 - 0)",bg="white")
a_label.place(x=200,y=200)

a_entrada = Entry(textvariable =a, width="20")
a_entrada.place(x = 210,y= 225, width ="50", height="30")

b_label= Label(text="Ingrese (0 - 1)",bg="white")
b_label.place(x=300,y=200)

b_entrada = Entry(textvariable =b, width="20")
b_entrada.place(x = 310,y= 225, width ="50", height="30")

c_label= Label(text="Ingrese (0 - 2)",bg="white")
c_label.place(x=400,y=200)

c_entrada = Entry(textvariable =c, width="20")
c_entrada.place(x = 410,y= 225, width ="50", height="30")

d_label= Label(text="Ingrese (0 - 3)",bg="white")
d_label.place(x=500,y=200)

d_entrada = Entry(textvariable =d, width="20")
d_entrada.place(x = 510,y= 225, width ="50", height="30")




e_label= Label(text="Ingrese (1 - 0)",bg="white")
e_label.place(x=200,y=300)

e_entrada = Entry(textvariable =e, width="20")
e_entrada.place(x = 210,y= 325, width ="50", height="30")

f_label= Label(text="Ingrese (1 - 1)",bg="white")
f_label.place(x=300,y=300)

f_entrada = Entry(textvariable =f, width="20")
f_entrada.place(x = 310,y= 325, width ="50", height="30")

g_label= Label(text="Ingrese (1 - 2)",bg="white")
g_label.place(x=400,y=300)

g_entrada = Entry(textvariable =g, width="20")
g_entrada.place(x = 410,y= 325, width ="50", height="30")

h_label= Label(text="Ingrese (1 - 3)",bg="white")
h_label.place(x=500,y=300)

h_entrada = Entry(textvariable =h, width="20")
h_entrada.place(x = 510,y= 325, width ="50", height="30")




i_label= Label(text="Ingrese (2 - 0)",bg="white")
i_label.place(x=200,y=400)

i_entrada = Entry(textvariable =i, width="20")
i_entrada.place(x = 210,y= 425, width ="50", height="30")

j_label= Label(text="Ingrese (2 - 1)",bg="white")
j_label.place(x=300,y=400)

j_entrada = Entry(textvariable =j, width="20")
j_entrada.place(x = 310,y= 425, width ="50", height="30")

k_label= Label(text="Ingrese (2 - 2)",bg="white")
k_label.place(x=400,y=400)

k_entrada = Entry(textvariable =k, width="20")
k_entrada.place(x = 410,y= 425, width ="50", height="30")

l_label= Label(text="Ingrese (2 - 2)",bg="white")
l_label.place(x=500,y=400)

l_entrada = Entry(textvariable =l, width="20")
l_entrada.place(x = 510,y= 425, width ="50", height="30")


#BOTON PARA ENVIAR LOS 12 CUADRITOS
submit_btn_matriz=Button(ventana, text="Procesar matriz",font=(11),width="20",height="2", relief="flat",bg="#8C8C8C", fg="white")
submit_btn_matriz.place(x=300, y=500)


#Boton para manual de usuario
submit_btn=Button(ventana, text="Manual usuario",font=(11),width="20",height="2", command=manual,relief="flat",bg="#8C8C8C", fg="white")
submit_btn.place(x=600, y=10)

#Borrar campos
def borrar_limpiar():
    a.set("")


ventana.mainloop()

# Variables
matriz = []
res = []


# Funciones
def mat(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz


def llenar(n):
    matriz = mat(n)
    for x in range(n):
        for y in range(n):
            matriz[x][y] = float(input('Valor de [' + str(x) + '][' + str(y) + '] = '))
        res.append(float(input('Valor del resultado de la matriz [' + str(x) + '] = ')))


def gauss(n):
    for z in range(n - 1):
        for x in range(1, n - z):
            if (matriz[z][z] != 0):
                p = matriz[x + z][z] / matriz[z][z]
                for y in range(n):
                    matriz[x + z][y] = matriz[x + z][y] - (matriz[z][y] * p)
                res[x + z] = res[x + z] - (res[z] * p)


def gjordan(n):
    for z in range(n - 1, 0, -1):
        for x in range(z):
            if (matriz[z][z] != 0):
                p = matriz[x][z] / matriz[z][z]
                matriz[x][z] = matriz[x][z] - (matriz[z][z] * p)
                res[x] = res[x] - (res[z] * p)


def sol(n):
    print("\n")
    for i in range(n):
        if (matriz[i][i] != 0):
            ms = True
        else:
            ms = False
            break
    if (ms == True):
        for i in range(n):
            print("El valor de x" + str(i) + ' es = ' + str(res[i] / matriz[i][i]))
    else:
        print('La matriz no tiene solucion')


def det(n):
    deter = 1
    for x in range(n):
        deter = matriz[x][x] * deter
    print('\nEl determinante de la matriz es = ', deter)


def im(n):
    print("\nMatriz resultante:")
    for i in range(n):
        print(matriz[i][:])


# Programa
# n = int(input ('Tamano de la matriz : '))
n = 3
llenar(n)
gauss(n)
gjordan(n)
sol(n)
det(n)
im(n)

