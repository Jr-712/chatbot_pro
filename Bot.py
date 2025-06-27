from tkinter import *

ventana = Tk()
ventana.title("ChatBot")
ventana.geometry("600x600")
ventana.configure(bg='#E5DDD5')  # Color de fondo similar al de WhatsApp

titulo = Label(height=2, width=14, bg='#128C7E', text='ChatBot', font=('Helvetica', 20), fg='white')  # Cambio de color de fondo y texto
titulo.place(x=200, y=5)

chat_ent = Frame(height=420, width=580, bg='#E5DDD5')  # Cambio de color de fondo
chat_ent.place(x=10, y=80)

texto_ent = Frame(height=60, width=500, bg='#E5DDD5')  # Cambio de color de fondo
texto_ent.place(x=10, y=520)

recuadro = Frame(height=60, width=65, bg='#E5DDD5')  # Cambio de color de fondo
recuadro.place(x=525, y=520)

conversacion = []

def enter(e):
    entrada_text.delete(0, 'end')
    entrada_text.config(fg='black')

def leave(e):
    n = entrada_text.get()
    entrada_text.config(fg='black')

    if n == '' or n == ' ':
        entrada_text.insert(0, 'Mensaje...')
        entrada_text.config(fg='black')

xi = 0
yi = 0

def mensaje():
    global yi
    u = entrada_text.get()

    usuario = Label(chat_ent, height=1, width=45, bg='#E5DDD5', fg='black', text=f'Tu: {u}', font=('Helvetica', 12), anchor='w')  # Ajuste del ancho y posición
    usuario.place(x=xi, y=yi)
    conversacion.append(u)

    respuesta = obtener_respuesta(u)
    bot = Label(chat_ent, height=3, width=70, bg='#E5DDD5', fg='black', text=f'Bot: {respuesta}', font=('Helvetica', 12), anchor='w', wraplength=480)  # Ajuste del ancho y posición
    bot.place(x=xi, y=yi + 25)
    conversacion.append(respuesta)

    yi += 75  # Ajuste de la distancia entre mensajes

def obtener_respuesta(pregunta):
    if 'hola' in pregunta:
        return 'Hola, ¿en qué puedo ayudarte?'
    elif 'que es una ecuacion diferencial' in pregunta:
        return 'Si una ecuación contiene las derivadas diferenciales de una o más variables dependientes con respecto a una o más variables independientes, se dice que es una ecuación diferencial.'
    elif 'como se clasifican las ecuaciones diferenciales' in pregunta:
        return 'Se clasifican según el tipo, el orden y la linealidad.'
    elif 'cual es su clasificacion segun el tipo' in pregunta:
        return 'Se clasifican en ecuaciones diferenciales ordinarias y ecuaciones diferenciales parciales.'
    elif 'cual es su clasificacion segun el orden' in pregunta:
        return 'El orden es la derivada más alta de una ecuación diferencial.'
    elif 'cual es su clasificacion segun la linealida' in pregunta:
        return 'Ecuaciones diferenciales lineales o no lineales'
    elif 'que es una ecuacion diferencial ordinaria' in pregunta:
        return 'Es una ecuacion que involucra a una variable independiente x, una funcion y(x) y una o varias derivadas de y(x).'
    elif 'dame un ejemplo de una ecuacion diferencial ordinaria' in pregunta:
        return 'dy/dx-5y=1'
    elif 'que es una ecuacion diferencial lineal' in pregunta:
        return 'Una ecuacion diferencial lineal debe de cumplir dos propiedades: 1.-La variable dependiente junto con todas sus derivadas son de primer grado., 2.-Cada coeficiente depende solo de la variable independiente.'
    elif 'dame un ejemplo de una ecuacion diferencial lineal' in pregunta:
        return 'xdy + ydx = 0'
    elif 'que es una ecuacion diferencial no lineal' in pregunta:
        return 'Es una ecuacion que no cumple las dos propiedades de una ecuacion diferencial lineal, se dice que no es lineal.'
    elif 'dame un ejemplo de una ecuacion diferencial no lineal' in pregunta:
        return 'yy"-2y = x+1'
    elif 'que es una ecuacion de primer orden' in pregunta:
        return 'Es una ecuacion diferencial que el orden de su deriva maxima es uno'
    elif 'dame un ejemplo de una ecuacion de primer orden' in pregunta:
        return '(x+y)dx - 4ydy = 0'
    elif 'por que metodos se resuelve una ecuacion de primer orden' in pregunta:
        return 'Metodo de separacion de variables, homogeneidad, exactitud y linealidad'
    elif 'en que consiste el metodo de separacion de variables' in pregunta:
        return 'Para resolver una ecuacion diferencial por este metodo debemos ser capaces de llevarla a la forma f(y)dy=f(x)dx.'
    elif 'dame un ejemplo del metodo de variables separables' in pregunta:
        return 'dy/dx+xy^2=0'
    elif 'que es una ecuacion diferencial homogenea' in pregunta:
        return 'Se dice  que f(x,y) es una funcion homogenea de grado n, si para algun numero real n, f(tx,ty)=t^nf(x,y)'
    elif 'dame un ejemplo de una ecuacion diferencial homogenea' in pregunta:
        return 'f(x,y)=x^2+xy+y^2'
    elif 'en que consiste el metodo de homogeneidad' in pregunta:
        return 'Consiste en hacer una reduccion, de una ecuacion diferencial homogenea a una de variables separables, por medio de una apropiada sustitucion.'
    elif 'dame un ejemplo del metodo de homogeneidad' in pregunta:
        return 'dy/dx=-(x-y)/x'
    elif 'en que consiste el metodo de exactitud' in pregunta:
        return 'Es una ecuacion diferencial ordinaria que presenta la forma M(x,y)+N(x,y)=0, donde las derivadas parciales de las funciones M y N son iguales.'
    elif 'dame un ejemplo del metodo de exactitud' in pregunta:
        return '(3xy+y^2)dx+(x^2+xy)dy=0'
    elif 'en que consiste el metodo de linealidad' in pregunta:
        return 'Se puede resolver una ecuacion diferencial por este metodo si tiene la forma a(x)dy/dx+a(x)y=g(x), en la cual se busca un factor integrante para resolverla.'
    elif 'dame un ejemplo del metodo de linealidad' in pregunta:
        return 'dy/dx-3y=x^6'
    elif 'que es una ecuacion diferencial de orden superior' in pregunta:
        return 'Son ecuaciones diferenciales en las que estan involucradas segundas, terceras, etc, derivadas, o ecuaciones de orden mayor a uno.'
    elif 'dame un ejemplo de una ecuacion diferencial de orden superior' in pregunta:
        return 'y"-y=0'
    elif 'por que metodos se resuelven las ecuaciones de orden superior' in pregunta:
        return 'Existen diversos metodos por los cuales se resuelve una ecuacion de diferencial de orden superior, pero en concreto hay dos principales, homogeneas por coeficientes constantes y no homogeneas.'
    elif 'metodo de ecuacion homegenea por coeficientes constantes' in pregunta:
        return 'Se saca la ecuacion caracteristica de la ecuacion diferencial, se encuentran sus raices y se escriben como una combinacion lineal.'
    elif 'dame un ejemplo de una ecuacion homegenea de coeficentes constantes' in pregunta:
        return 'y"-8y=0'
    elif 'metodo de ecuacion no homegenea con coeficientes constantes' in pregunta:
        return 'Se resuelve en dos partes, 1.-Resolvemos la ecuacion homogenea, 2.-Resolvemos la ecuacion asociada por variacion de parametros o coeficientes indeterminados.'
    elif 'dame un ejemplo de una ecuacion no homegenea de coeficentes constantes' in pregunta:
        return 'y"-4y=-10xe^x'
    else:
        return 'No te entiendo.'

entrada_text = Entry(texto_ent, width=32, bg='#E5DDD5', font=('Helvetica', 14), relief=FLAT, border=0)  # Ajuste del tamaño de la fuente
entrada_text.place(x=10, y=13)
entrada_text.insert(0, 'Mensaje...')
entrada_text.config(fg='black')
entrada_text.bind("<FocusIn>", enter)
entrada_text.bind("<FocusOut>", leave)

boton = Button(recuadro, height=1, width=3, bg='#128C7E', text='>', font=('Helvetica', 20),
               activeforeground='white', fg='white', relief=FLAT, border=0,
               activebackground='#25D366', command=mensaje)  # Cambio de colores
boton.place(x=5, y=4)

ventana.mainloop()
