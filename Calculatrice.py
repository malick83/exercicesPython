#-*- coding:utf-8 -*-

import tkinter
import tkinter.font

 
calculat = tkinter.Tk()
calculat.title("calculat")
calculat.geometry("501x420+300+200")
calculat.resizable(width=False, height=False)

varLab = tkinter.StringVar()
varLab.set("0")

fontStyle = tkinter.font.Font(family="Lucida Grande", size=9)

labenom = tkinter.Label(calculat, text="CALCULARICE TKINTER DE MALICK", width=50, height=2, borderwidth=2, background="#C0C0C0", font=fontStyle)
labenom.place(x=45, y=20)


labe = tkinter.Label(calculat, textvariable=varLab, width=50, height=2, borderwidth=2, background="#C0C0C0", font=fontStyle)



nb1 = " "
global result

def ajout(nb):
	global nb1 
	nb1 += nb
	varLab.set(nb1)

def add():
	global nb1, op, nb2
	try:
		nb2 = float(nb1)
	except ValueError:
		varLab.set("il nous faut d'abord une opération d'addition")
		print("il faut d'abord Entrer un nombre avant d'additionner")
	else:
		nb1 = ""
		op = 1
		varLab.set("+")

def sous():
	global nb1, op, nb2
	try:
		nb2 = float(nb1)
	except ValueError:
		print("il nous faut d'abord une opération de soustraction")
		varLab.set("il nous faut d'abord une opération de soustraction")
	else:
		nb1 = ""
		op = 2
		varLab.set("-")

def mult():
	global nb1, op, nb2
	try:
		nb2 = float(nb1)
	except ValueError:
		varLab.set("il nous faut d'abord une opération de multiplication")
		print("il nous faut d'abord une opération de multiplication")
	else:
		nb1 = ""
		op = 3
		varLab.set("x")

def div():
	global nb1, op, nb2
	try:
		nb2 = float(nb1)
	except ValueError:
		varLab.set("il nous faut d'abord une opération de division")
		print("il nous faut d'abord une opération de division")
	else:
		nb1 = ""
		op = 4
		varLab.set("/")

def mod():
	global nb1, op, nb2
	try:
		nb2 = float(nb1)
	except ValueError:
		varLab.set("il nous faut d'abord une opération modulo")
		print("il nous faut d'abord une opération de modulo")
	else:
		nb1 = ""
		op = 5
		varLab.set("≡")

def egal():
	global nb1
	global nb3
	global result
	global nb2
	#global nb4 
	try:
		nb3 = float(nb1)

	except ValueError:
		varLab.set("il nous faut d'abord une opération avant de voir le resultat")
		print("il nous faut d'abord une opération avant de voir le resultat")
	else:
		nb3 = float(nb1)
		if op == 1:
			result = nb2 + nb3
			varLab.set(result)
			nb1 = str(result)

		elif op == 2:
			result = nb2 - nb3
			varLab.set(result)
			nb1 = str(result)

		elif op == 3:
			result = nb2 * nb3
			varLab.set(result)
			nb1 = str(result)

		elif op == 4:
			try:
				result = nb2 / nb3
			except ZeroDivisionError:
				varLab.set("On ne peut pas diviser par 0")
				print("On ne peut pas diviser par 0")
			else:
				varLab.set(result)
				nb1 = str(result)

		elif op == 5:
			try:
				result = nb2 % nb3
			except ZeroDivisionError:
				varLab.set("Congruence modulo 0 n'existe pas")
				print("Congruence modulo 0 n'existe pas")
			else:
				varLab.set(result)
				nb1 = str(result)



def clear():
	global nb1
	nb1 = " "
	varLab.set(nb1)


def masquer():

	global nb1
	global no
	no = nb1.replace(nb1[:], " ")
	varLab.set(no)

def montrer():
	varLab.set(nb1)
	
labe.place(x=45, y=75)





def num1():
	ajout("1")

def num2():
	ajout("2")

def num3():
	ajout("3")

def num4():
	ajout("4")

def num5():
	ajout("5")

def num6():
	ajout("6")

def num7():
	ajout("7")

def num8():
	ajout("8")

def num9():
	ajout("9")

def point():
	ajout(".")

def zero():
	ajout("0")


bouton1 = tkinter.Button(calculat, text=" 1 ", command=num1, border=3)
bouton1.place(x=10, y=140)
bouton2 = tkinter.Button(calculat, text=" 2 ", command=num2, border=3)
bouton2.place(x=70, y=140)
bouton3 = tkinter.Button(calculat, text=" 3 ", command=num3, border=3)
bouton3.place(x=130, y=140)

bouton4 = tkinter.Button(calculat, text=" 4 ", command=num4, border=3)
bouton4.place(x=10, y=180)
bouton5 = tkinter.Button(calculat, text=" 5 ", command=num5, border=3)
bouton5.place(x=70, y=180)
bouton6 = tkinter.Button(calculat, text=" 6 ", command=num6, border=3)
bouton6.place(x=130, y=180)

bouton7 = tkinter.Button(calculat, text=" 7 ", command=num7, border=3)
bouton7.place(x=10, y=220)
bouton8 = tkinter.Button(calculat, text=" 8 ", command=num8, border=3)
bouton8.place(x=70, y=220)
bouton9 = tkinter.Button(calculat, text=" 9 ", command=num9, border=3)
bouton9.place(x=130, y=220)

boutonPoint = tkinter.Button(calculat, text=" .  ", command=point, border=3)
boutonPoint.place(x=10, y=260)
boutonZero = tkinter.Button(calculat, text=" 0 ", command=zero, border=3)
boutonZero.place(x=70, y=260)
boutonSup = tkinter.Button(calculat, text=" c  ", command=clear, border=3)
boutonSup.place(x=130, y=260)

boutonAddition = tkinter.Button(calculat, text=" + ", command=add, border=3)
boutonAddition.place(x=10, y=300)
boutonSoustraction = tkinter.Button(calculat, text=" -  ", command=sous, border=3)
boutonSoustraction.place(x=70, y=300)
boutonMultiplication = tkinter.Button(calculat, text=" x ", command=mult, border=3)
boutonMultiplication.place(x=130, y=300)

boutonDivision = tkinter.Button(calculat, text=" /  ", command=div, border=3)
boutonDivision.place(x=10, y=340)
boutonModulo = tkinter.Button(calculat, text=" ≡ ", command=mod, border=3)
boutonModulo.place(x=70, y=340)
boutonEgal = tkinter.Button(calculat, text=" = ", command=egal, border=3)
boutonEgal.place(x=130, y=340)

boutonMasquer = tkinter.Button(calculat, text="masquer", command=masquer, border=3)
boutonMasquer.place(x=10, y=380)
boutonMontrer = tkinter.Button(calculat, text="montrer", command=montrer, border=3)
boutonMontrer.place(x=100, y=380)


calculat.config(bg="#49A")

calculat.mainloop()







