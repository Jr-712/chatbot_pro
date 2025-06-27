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
    bot = Label(chat_ent, height=3, width=90, bg='#E5DDD5', fg='black', text=f'Bot: {respuesta}', font=('Helvetica', 12), anchor='w', wraplength=480)  # Ajuste del ancho y posición
    bot.place(x=xi, y=yi + 25)
    conversacion.append(respuesta)

    yi += 35  # Ajuste de la distancia entre mensajes

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
