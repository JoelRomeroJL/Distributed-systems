from tkinter import *
import time

#--------------------------Clase del objeto reloj-----------------------------
class reloj():

	def __init__(self, horas, minutos, segundos, stop):
		super(reloj, self).__init__()
		self.horas = horas
		self.minutos = minutos
		self.segundos = segundos
		self.stop = stop

	def imprimir(self):
		print(str(self.horas)+":"+str(self.minutos)+":"+str(self.segundos))
#-----------------------------------------------------------------------------

#---------------------Hora Actual------------------------
def timer():
	atc_time = time.strftime('%H:%M:%S').split(":")
	s = int(atc_time[2])
	m = int(atc_time[1])
	h = int(atc_time[0])
	return h, m, s
#--------------------------------------------------------

#----------Declaracion del objeto global--------------
h, m, s = timer()
r = reloj(h,m,s,0)
#-----------------------------------------------------

#--------------------Modificar Hora-------------------------
def modify():
	global r
	atc_time = time.strftime('%H:%M:%S').split(":")
	s = int(atc_time[2])
	m = int(masM.get())
	h = int(masH.get())

	r.horas =h
	r.minutos=m
	r.segundos=s
	r.stop = 0
#----------------------------------------------------------

#---------Dtener reloj-----------
def stop():
	global r
	r.stop=1
#--------------------------------

#-----------------------------------------------Interfaz----------------------------------------------------------
root = Tk()
root.focus()
root.title("Practica 1")
root.geometry('500x200')
root.configure(background = "#0a0f0f")

clock = Label(root, font=('ubuntu', 35, 'bold'), bg='#527a7a', fg='white', bd=0)
clock.grid(column=0, row=2)
#clock.pack(fill=BOTH, expand=1)

#--------------------------------------------Horas-------------------------------------------------------
masH = Entry(root, width=10)
masH.grid(column=2, row=2)
h = Label(root, text=' Horas ', font=('ubuntu', 10, 'bold'), bg='#3C3B37', fg='white', bd=0)
h.grid(column=2, row=3)
#--------------------------------------------------------------------------------------------------------

#------------------------------------------Minutos-------------------------------------------------------
masM = Entry(root, width=10)
masM.grid(column=3, row=2)
m = Label(root, text=' Minutos ', font=('ubuntu', 10, 'bold'), bg='#3C3B37', fg='white', bd=0)
m.grid(column=3, row=3)
#--------------------------------------------------------------------------------------------------------


#-------------------------------------------Acept--------------------------------------------------------
boton = Button(root, text="Acept", font=('ubuntu', 13, 'bold'), bg='#3C3B37',fg='white', command=modify)
boton.grid(column=4, row=2)
#--------------------------------------------------------------------------------------------------------

#-------------------------------------------Modificar----------------------------------------------------
boton2 = Button(root, text="Modify", font=('ubuntu', 15, 'bold'), bg='#3C3B37',fg='white', command=stop)
boton2.grid(column=4, row=1)
#--------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

#--------------------------Contador-------------------------------
def contador():
	global r
	if r.stop == 1:
		time2 = str(r.horas)+":"+str(r.minutos)+":"+str(r.segundos)
	else:
		r.segundos +=1
		if r.segundos > 59:
			r.minutos +=1 
			r.segundos = 00
		elif r.minutos > 59:
			r.horas += 1
			r.minutos = 00
		time2 = str(r.horas)+":"+str(r.minutos)+":"+str(r.segundos)
		#time.sleep(1)
	clock.config(text=time2)
	clock.after(1000, contador)
	print(time2)
#-----------------------------------------------------------------

#---------------------
contador()
root.mainloop()
#---------------------

