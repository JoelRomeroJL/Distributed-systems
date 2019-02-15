from tkinter import *
import time
import threading


#--------------------------Clase del objeto reloj-----------------------------
class reloj():

	def __init__(self, horas, minutos, segundos, stop):
		super(reloj, self).__init__()
		self.horas = horas
		self.minutos = minutos
		self.segundos = segundos
		self.stop = stop

	#--------------------------Contador-------------------------------
	def contador(self):
		if self.stop == 1:
			time2 = str(self.horas)+":"+str(self.minutos)+":"+str(self.segundos)
		else:
			self.segundos +=1
			if self.segundos > 59:
				self.minutos +=1 
				self.segundos = 00
				if self.minutos > 59:
					self.horas += 1
					self.minutos = 00
					if self.horas > 23:
						self.horas = 00	
		time2 = str(self.horas)+":"+str(self.minutos)+":"+str(self.segundos)
		#time.sleep(1)
		#clock.config(text=time2)
		#clock.after(1000, contador)
		print(time2)
		return time2
	#-----------------------------------------------------------------

	#-----------------------------------------------------------------
	def modify(self, m, h):
		atc_time = time.strftime('%H:%M:%S').split(":")
		if m > 60:
			if h > 24:
				self.segundos = int(atc_time[2])
				self.minutos = 59
				self.horas = 0
				self.stop = 0
			else:
				self.segundos = int(atc_time[2])
				self.minutos = 59
				self.horas = h
				self.stop = 0
		else:
			self.horas =h
			self.minutos=m
			self.segundos=int(atc_time[2])
			self.stop = 0	
	#-----------------------------------------------------------------
	
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
r2 = reloj(h,m,s,0)
r3 = reloj(h,m,s,0)
r4 = reloj(h,m,s,0)
#-----------------------------------------------------

#--------------------Modificar Hora-------------------------
def modify1():
	global r
	m = int(masM.get())
	h = int(masH.get())
	r.modify(m,h)
def modify2():
	global r2
	m = int(masM2.get())
	h = int(masH2.get())
	r2.modify(m,h)
def modify3():
	global r3
	m = int(masM3.get())
	h = int(masH3.get())
	r3.modify(m,h)
def modify4():
	global r4
	m = int(masM4.get())
	h = int(masH4.get())
	r4.modify(m,h)
#----------------------------------------------------------

#---------Detener reloj-----------
def stop1():
	global r
	r.stop=1
def stop2():
	global r2
	r2.stop=1
def stop3():
	global r3
	r3.stop=1
def stop4():
	global r4
	r4.stop=1
#--------------------------------

#-----------------------------------------------Interfaz----------------------------------------------------------
root = Tk()
root.focus()
root.title("Practica 1")
root.geometry('945x250')
root.configure(background = "#0a0f0f")

#--------------------------------------------Labels------------------------------------------------------
clock = Label(root, font=('ubuntu', 35, 'bold'), bg='#527a7a', fg='white', bd=0, width=8)
clock.grid(column=0, row=2)

s = Label(root, text='              ', font=('ubuntu', 10, 'bold'), bg='#0a0f0f', fg='white', bd=0)
s.grid(column=5, row=2)
s2 = Label(root, text='              ', font=('ubuntu', 10, 'bold'), bg='#0a0f0f', fg='white', bd=0)
s2.grid(column=0, row=4)
s3 = Label(root, text='              ', font=('ubuntu', 10, 'bold'), bg='#0a0f0f', fg='white', bd=0)
s3.grid(column=0, row=5)


clock2 = Label(root, font=('ubuntu', 35, 'bold'), bg='#527a7a', fg='white', bd=0, width=8)
clock2.grid(column=6, row=2)

clock3 = Label(root, font=('ubuntu', 35, 'bold'), bg='#527a7a', fg='white', bd=0, width=8)
clock3.grid(column=0, row=6)

clock4 = Label(root, font=('ubuntu', 35, 'bold'), bg='#527a7a', fg='white', bd=0, width=8)
clock4.grid(column=6, row=6)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------Horas-------------------------------------------------------
masH = Entry(root, width=10)
masH.grid(column=2, row=2)
h = Label(root, text=' Horas ', font=('ubuntu', 10, 'bold'), bg='#3C3B37', fg='white', bd=0)
h.grid(column=2, row=3)

masH2 = Entry(root, width=10)
masH2.grid(column=7, row=2)
h2 = Label(root, text=' Horas ', font=('ubuntu', 10, 'bold'), bg='#3C3B37', fg='white', bd=0)
h2.grid(column=7, row=3)

masH3 = Entry(root, width=10)
masH3.grid(column=2, row=6)
h3 = Label(root, text=' Horas ', font=('ubuntu', 10, 'bold'), bg='#3C3B37', fg='white', bd=0)
h3.grid(column=2, row=7)

masH4 = Entry(root, width=10)
masH4.grid(column=7, row=6)
h4 = Label(root, text=' Horas ', font=('ubuntu', 10, 'bold'), bg='#3C3B37', fg='white', bd=0)
h4.grid(column=7, row=7)
#--------------------------------------------------------------------------------------------------------

#------------------------------------------Minutos-------------------------------------------------------
masM = Entry(root, width=10)
masM.grid(column=3, row=2)
m = Label(root, text=' Minutos ', font=('ubuntu', 10, 'bold'), bg='#3C3B37', fg='white', bd=0)
m.grid(column=3, row=3)

masM2 = Entry(root, width=10)
masM2.grid(column=8, row=2)
m2 = Label(root, text=' Minutos ', font=('ubuntu', 10, 'bold'), bg='#3C3B37', fg='white', bd=0)
m2.grid(column=8, row=3)

masM3 = Entry(root, width=10)
masM3.grid(column=3, row=6)
m3 = Label(root, text=' Minutos ', font=('ubuntu', 10, 'bold'), bg='#3C3B37', fg='white', bd=0)
m3.grid(column=3, row=7)

masM4 = Entry(root, width=10)
masM4.grid(column=8, row=6)
m4 = Label(root, text=' Minutos ', font=('ubuntu', 10, 'bold'), bg='#3C3B37', fg='white', bd=0)
m4.grid(column=8, row=7)
#--------------------------------------------------------------------------------------------------------


#-------------------------------------------Acept--------------------------------------------------------
botonA = Button(root, text="Acept", font=('ubuntu', 13, 'bold'), bg='#3C3B37',fg='white', command=modify1)
botonA.grid(column=4, row=2)

botonA2 = Button(root, text="Acept", font=('ubuntu', 13, 'bold'), bg='#3C3B37',fg='white', command=modify2)
botonA2.grid(column=9, row=2)

botonA3 = Button(root, text="Acept", font=('ubuntu', 13, 'bold'), bg='#3C3B37',fg='white', command=modify3)
botonA3.grid(column=4, row=7)

botonA4 = Button(root, text="Acept", font=('ubuntu', 13, 'bold'), bg='#3C3B37',fg='white', command=modify4)
botonA4.grid(column=9, row=7)
#--------------------------------------------------------------------------------------------------------

#-------------------------------------------Modificar----------------------------------------------------
botonM = Button(root, text="Modify", font=('ubuntu', 15, 'bold'), bg='#3C3B37',fg='white', command=stop1)
botonM.grid(column=4, row=1)

botonM2 = Button(root, text="Modify", font=('ubuntu', 15, 'bold'), bg='#3C3B37',fg='white', command=stop2)
botonM2.grid(column=9, row=1)

botonM3 = Button(root, text="Modify", font=('ubuntu', 15, 'bold'), bg='#3C3B37',fg='white', command=stop3)
botonM3.grid(column=4, row=6)

botonM4 = Button(root, text="Modify", font=('ubuntu', 15, 'bold'), bg='#3C3B37',fg='white', command=stop4)
botonM4.grid(column=9, row=6)
#--------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------
def hilo1():
	#---------------------
	time2 = r.contador()
	clock.config(text=time2)
	clock.after(1000, hilo1)
	#---------------------
def hilo2():
	#---------------------
	time2 = r2.contador()
	clock2.config(text=time2)
	clock2.after(1000, hilo2)
	#---------------------
def hilo3():
	#---------------------
	time2 = r3.contador()
	clock3.config(text=time2)
	clock3.after(1000, hilo3)
	#---------------------
def hilo4():
	#---------------------
	time2 = r4.contador()
	clock4.config(text=time2)
	clock4.after(1000, hilo4)
	#---------------------
#---------------------------------------------------------

thread1 = threading.Thread(target=hilo1, name='Clock1')
thread2 = threading.Thread(target=hilo2, name='Clock2')
thread3 = threading.Thread(target=hilo3, name='Clock3')
thread4 = threading.Thread(target=hilo4, name='Clock4')

thread1.start()
thread2.start()
thread3.start()
thread4.start()

root.mainloop()
