from tkinter import *

ventana = Tk()
ventana.title("ChatBot")
ventana.geometry("600x600")
ventana.configure(bg='#E5DDD5')  

titulo = Label(height=2, width=14, bg='#128C7E', text='ChatBot', font=('Helvetica', 20), fg='white')  
titulo.place(x=200, y=5)

chat_ent = Frame(height=420, width=580, bg='#E5DDD5')  
chat_ent.place(x=10, y=80)

texto_ent = Frame(height=60, width=500, bg='#E5DDD5')  
texto_ent.place(x=10, y=520)

recuadro = Frame(height=60, width=65, bg='#E5DDD5')  
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

respuestas = {
    'hola': 'Hola, ¿en qué puedo ayudarte?',
    'que es una ecuacion diferencial': 'Si una ecuación contiene las derivadas diferenciales de una o más variables dependientes con respecto a una o más variables independientes, se dice que es una ecuación diferencial.',
    'como se clasifican las ecuaciones diferenciales': 'Se clasifican según el tipo, el orden y la linealidad.',
    'cual es su clasificacion segun el tipo': 'Se clasifican en ecuaciones diferenciales ordinarias y ecuaciones diferenciales parciales.',
    'cual es su clasificacion segun el orden': 'El orden es la derivada más alta de una ecuación diferencial.',
    'cual es su clasificacion segun la linealida': 'Ecuaciones diferenciales lineales o no lineales',
    'que es una ecuacion diferencial ordinaria': 'Es una ecuacion que involucra a una variable independiente x, una funcion y(x) y una o varias derivadas de y(x).',
    'dame un ejemplo de una ecuacion diferencial ordinaria': 'dy/dx-5y=1',
    'que es una ecuacion diferencial lineal': 'Una ecuacion diferencial lineal debe de cumplir dos propiedades: 1.-La variable dependiente junto con todas sus derivadas son de primer grado., 2.-Cada coeficiente depende solo de la variable independiente.',
    'dame un ejemplo de una ecuacion diferencial lineal': 'xdy + ydx = 0',
    'que es una ecuacion diferencial no lineal': 'Es una ecuacion que no cumple las dos propiedades de una ecuacion diferencial lineal, se dice que no es lineal.',
    'dame un ejemplo de una ecuacion diferencial no lineal': 'yy"-2y = x+1',
    'que es una ecuacion diferencial de primer orden': 'Es una ecuacion diferencial que el orden de su deriva maxima es uno',
    'dame un ejemplo de una ecuacion diferencial de primer orden': '(x+y)dx - 4ydy = 0',
    'por que metodos se resuelve una ecuacion diferencial de primer orden': 'Metodo de separacion de variables, homogeneidad, exactitud y linealidad',
    'en que consiste el metodo de separacion de variables': 'Para resolver una ecuacion diferencial por este metodo debemos ser capaces de llevarla a la forma f(y)dy=f(x)dx.',
    'dame un ejemplo del metodo de separacion de variables': 'dy/dx+xy^2=0',
    'que es una ecuacion diferencial homogenea': 'Se dice  que f(x,y) es una funcion homogenea de grado n, si para algun numero real n, f(tx,ty)=t^nf(x,y)',
    'dame un ejemplo de una ecuacion diferencial homogenea': 'f(x,y)=x^2+xy+y^2',
    'en que consiste el metodo de homogeneidad': 'Consiste en hacer una reduccion, de una ecuacion diferencial homogenea a una de variables separables, por medio de una apropiada sustitucion.',
    'dame un ejemplo del metodo de homogeneidad': 'dy/dx=-(x-y)/x',
    'en que consiste el metodo de exactitud': 'Es una ecuacion diferencial ordinaria que presenta la forma M(x,y)+N(x,y)=0, donde las derivadas parciales de las funciones M y N son iguales.',
    'dame un ejemplo del metodo de exactitud': '(3xy+y^2)dx+(x^2+xy)dy=0',
    'en que consiste el metodo de linealidad': 'Se puede resolver una ecuacion diferencial por este metodo si tiene la forma a(x)dy/dx+a(x)y=g(x), en la cual se busca un factor integrante para resolverla.',
    'dame un ejemplo del metodo de linealidad': 'dy/dx-3y=x^6',
    'que es una ecuacion diferencial de orden superior': 'Son ecuaciones diferenciales en las que estan involucradas segundas, terceras, etc, derivadas, o ecuaciones de orden mayor a uno.',
    'dame un ejemplo de una ecuacion diferencial de orden superior': 'y"-y=0',
    'por que metodos se resuelven las ecuaciones de orden superior': 'Existen diversos metodos por los cuales se resuelve una ecuacion diferencial de orden superior, pero en concreto hay dos principales, homogeneas por coeficientes constantes y no homogeneas.',
    'metodo de ecuacion homogenea por coeficientes constantes': 'Se saca la ecuacion caracteristica de la ecuacion diferencial, se encuentran sus raices y se escriben como una combinacion lineal.',
    'dame un ejemplo de una ecuacion homogenea de coeficentes constantes': 'y"-8y=0',
    'metodo de ecuacion no homogenea con coeficientes constantes': 'Se resuelve en dos partes, 1.-Resolvemos la ecuacion homogenea, 2.-Resolvemos la ecuacion asociada por variacion de parametros o coeficientes indeterminados.',
    'dame un ejemplo de una ecuacion no homogenea de coeficientes constantes': 'y"-4y=-10xe^x',
    '¿Qué es una ecuación diferencial?': 'Si una ecuación contiene las derivadas diferenciales de una o más variables dependientes con respecto a una o más variables independientes, se dice que es una ecuación diferencial.',
    '¿Cómo se clasifican las ecuaciones diferenciales?': 'Se clasifican según el tipo, el orden y la linealidad.',
    'Cuál es su clasificación según el tipo': 'Se clasifican en ecuaciones diferenciales ordinarias y ecuaciones diferenciales parciales.',
    'Cuál es su clasificación según el orden': 'El orden es la derivada más alta de una ecuación diferencial.',
    '¿Cuál es su clasificación según la linealidad?': 'Ecuaciones diferenciales lineales o no lineales',
    '¿Qué es una ecuación diferencial ordinaria?': 'Es una ecuacion que involucra a una variable independiente x, una funcion y(x) y una o varias derivadas de y(x).',
    'Dame un ejemplo de una ecuación diferencial ordinaria': 'dy/dx-5y=1',
    '¿Qué es una ecuación diferencial lineal?': 'Una ecuacion diferencial lineal debe de cumplir dos propiedades: 1.-La variable dependiente junto con todas sus derivadas son de primer grado., 2.-Cada coeficiente depende solo de la variable independiente.',
    'Dame un ejemplo de una ecuación diferencial lineal': 'xdy + ydx = 0',
    '¿Qué es una ecuación diferencial no lineal?': 'Es una ecuacion que no cumple las dos propiedades de una ecuacion diferencial lineal, se dice que no es lineal.',
    'Dame un ejemplo de una ecuación diferencial no lineal': 'yy"-2y = x+1',
    '¿Qué es una ecuación diferencial de primer orden?': 'Es una ecuacion diferencial que el orden de su deriva maxima es uno',
    'Dame un ejemplo de una ecuación diferencial de primer orden': '(x+y)dx - 4ydy = 0',
    '¿Por qué métodos se resuelve una ecuación diferencial de primer orden?': 'Metodo de separacion de variables, homogeneidad, exactitud y linealidad',
    '¿En qué consiste el método de separación de variables?': 'Para resolver una ecuacion diferencial por este metodo debemos ser capaces de llevarla a la forma f(y)dy=f(x)dx.',
    'Dame un ejemplo del método de separación de variables': 'dy/dx+xy^2=0',
    '¿Qué es una ecuación diferencial homogénea?': 'Se dice  que f(x,y) es una funcion homogenea de grado n, si para algun numero real n, f(tx,ty)=t^nf(x,y)',
    'Dame un ejemplo de una ecuación diferencial homogénea': 'f(x,y)=x^2+xy+y^2',
    '¿En qué consiste el método de homogeneidad?': 'Consiste en hacer una reduccion, de una ecuacion diferencial homogenea a una de variables separables, por medio de una apropiada sustitucion.',
    'Dame un ejemplo del método de homogeneidad': 'dy/dx=-(x-y)/x',
    '¿En qué consiste el método de exactitud?': 'Es una ecuacion diferencial ordinaria que presenta la forma M(x,y)+N(x,y)=0, donde las derivadas parciales de las funciones M y N son iguales.',
    'Dame un ejemplo del método de exactitud': '(3xy+y^2)dx+(x^2+xy)dy=0',
    '¿En qué consiste el método de linealidad?': 'Se puede resolver una ecuacion diferencial por este metodo si tiene la forma a(x)dy/dx+a(x)y=g(x), en la cual se busca un factor integrante para resolverla.',
    'Dame un ejemplo del método de linealidad': 'dy/dx-3y=x^6',
    '¿Qué es una ecuación diferencial de orden superior?': 'Son ecuaciones diferenciales en las que estan involucradas segundas, terceras, etc, derivadas, o ecuaciones de orden mayor a uno.',
    'Dame un ejemplo de una ecuación diferencial de orden superior': 'y"-y=0',
    '¿Por qué métodos se resuelven las ecuaciones de orden superior?': 'Existen diversos metodos por los cuales se resuelve una ecuacion diferencial de orden superior, pero en concreto hay dos principales, homogeneas por coeficientes constantes y no homogeneas.',
    '¿En qué consiste el método de ecuación homogénea por coeficientes constantes?': 'Se saca la ecuacion caracteristica de la ecuacion diferencial, se encuentran sus raices y se escriben como una combinacion lineal.',
    'Dame un ejemplo de una ecuación homogénea de coeficientes constantes': 'y"-8y=0',
    '¿En qué consiste el método de ecuación no homogénea con coeficientes constantes?': 'Se resuelve en dos partes, 1.-Resolvemos la ecuacion homogenea, 2.-Resolvemos la ecuacion asociada por variacion de parametros o coeficientes indeterminados.',
    'Dame un ejemplo de una ecuación no homogenea de coeficientes constantes': 'y"-4y=-10xe^x',
}

def obtener_respuesta(pregunta):
    pregunta = pregunta.lower()
    return respuestas.get(pregunta, 'No te entiendo, vuelve a escribir tu pregunta')

def mensaje():
    global yi
    u = entrada_text.get()

    usuario = Label(chat_ent, height=1, width=45, bg='#E5DDD5', fg='black', text=f'Tu: {u}', font=('Helvetica', 12), anchor='w')
    usuario.place(x=xi, y=yi)
    conversacion.append(u)

    respuesta = obtener_respuesta(u)
    bot = Label(chat_ent, height=3, width=70, bg='#E5DDD5', fg='black', text=f'Bot: {respuesta}', font=('Helvetica', 12), anchor='w', wraplength=480)
    bot.place(x=xi, y=yi + 25)
    conversacion.append(respuesta)

    yi += 75

entrada_text = Entry(texto_ent, width=32, bg='#E5DDD5', font=('Helvetica', 14), relief=FLAT, border=0)
entrada_text.place(x=10, y=13)
entrada_text.insert(0, 'Mensaje...')
entrada_text.config(fg='black')
entrada_text.bind("<FocusIn>", enter)
entrada_text.bind("<FocusOut>", leave)

boton = Button(recuadro, height=1, width=3, bg='#128C7E', text='>', font=('Helvetica', 20),
               activeforeground='white', fg='white', relief=FLAT, border=0,
               activebackground='#25D366', command=mensaje)
boton.place(x=5, y=4)

ventana.mainloop()
