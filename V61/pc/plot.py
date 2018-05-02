# # coding=utf-8
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit
# import uncertainties.unumpy as unp
# from uncertainties import ufloat
# import sympy
# from uncertainties import correlated_values, correlation_matrix
# import scipy.integrate as int
# from uncertainties.unumpy import nominal_values as noms
# from uncertainties.unumpy import std_devs as sdevs
# import scipy.constants as con
# from scipy.constants import physical_constants as pcon
# #Table Funktion
# dummy = ufloat(69,42)
# dummyarray = np.array([dummy,dummy*6.626])
# udummyarray = unp.uarray([4], [5*con.pi])
#
# #data1 = [a,b,c,d,e]
# #p1 = {'name':'tabelle1.tex','data':data1}
# #table(**p1)
# def table(name, data):
# 	j=0
# 	i=0
# 	f = [0,0,0,0,0,0,0,0,0,0,0,0,0]
# 	for i in range(len(data)):
# 		if(type(data[i][0]) == type(dummy) or type(data[i][0]) == type(dummyarray[1]) or type(data) == type(udummyarray)):
# 			f[i] = True
# 		else:
# 			f[i] = False
# 	print(f)
# 	output = open(name, 'w')
# 	output.write(r'\begin{table}[h]' + '\n' + r'\centering' + '\n' + r'\caption{CAPTION}' + '\n' +r'\sisetup{%uncertainty-seperator = {\,},'+'\n'+r'table-number-alignment = center,'+'\n'+'table-unit-alignment = center,'+'\n'+'%table-figures-integer = 1,'+'\n'+'%table-figures-decimal = 1,'+'\n'+'table-auto-round = true'+'\n'+'}'+'\n'+ r'\begin{tabular}{ ')
# 	for i in range(len(data)):
# 		if(f[i]):
# 			output.write(r'S[table-format= 3.1]'+'\n'+' @{\,$\pm{}$\,} '+'\n' + r' S[table-format= 3.1] ')
# 		else:
# 			output.write(r' S[table-format= 3.1] '+'\n')
# 	output.write(r'}' + '\n' + r'\toprule' + '\n')
#
# 	for i in range(len(data)):
# 		if(i < (len(data)-1)):
# 			if(f[i]):
# 				output.write(r'\multicolumn{2}{c}{TITLE}'+'\n'+'&')
# 			else:
# 				output.write(r'{$\text{Title}$}'+'\n'+'&')
# 		else:
# 			if(f[i]):
# 				output.write(r'\multicolumn{2}{c}{TITLE} \\'+'\n')
# 			else:
# 				output.write(r'{$\text{Title}$} \\'+'\n')
# 	output.write(r' \midrule' + '\n')
#
# 	#Tabelle
# 	for j in range(len(data[0])):
# 		i = 0
# 		while i <= len(data)-1:
# 				if(f[i]):
# 					if(i == len(data)-1):
# 						output.write(str(data[i][j].n) + '&' + str(data[i][j].s) + r'\\' + '\n')
# 					else:
# 						output.write(str(data[i][j].n)+ '&' + str(data[i][j].s) + '&')
# 					i = i+1
# 				else:
# 					if(i == len(data)-1):
# 						output.write(str(data[i][j]) + r'\\' + '\n')
# 					else:
# 						output.write(str(data[i][j]) + '&')
# 					i = i+1
# 	#Tabelle Ende
# 	output.write(r'\bottomrule' + '\n' + r'\end{tabular}' + '\n' + r'\label{tab:LABEL}' + '\n' + r'\end{table}')
# 	output.close()
#
#
# def g_1(x):
#     t = 1 - (x/r_1)
#     return t
#
# def g_2(x):
#     t = 1 - (x/r_2)
#     return t
#
# def g_3(x):
#     t = 1 - (x/r_3)
#     return t
#
# def g_4(x):
#     t = 1 - (x/r_4)
#     return t
#
# def g_5(x):
# 	t = 1 - (x/r_5)
# 	return t
#
# def g_6(x):
# 	t = 1
# 	return t
#
# Z = np.linspace(0, 2.5)
# r_1 = 1.4
# r_2 = 1.4
# r_3 = 1
# r_4 = 1.4
# r_5 = 1.4
#
# plt.plot(Z, g_1(Z) * g_2(Z), label= "Anordnung 1 ($r_1 = 1.4$ $r_2 = 1.4$)")
# plt.plot(Z, g_3(Z) * g_4(Z), label= "Anordnung 2 ($r_1 = 1$ $r_2 = 1.4$)")
# plt.plot(Z, g_5(Z) * g_6(Z), label= "Anordnung 3 ($r_1 = 1.4$ $r_2 = \infty$)")
# plt.xlabel("$L/m$")
# plt.ylabel('$g_1 g_2$')
# plt.legend()
# plt.grid()
# # plt.show()
# plt.savefig("Anordnungen_Theorie.pdf")
# plt.clf()
#
# data1 = [a,b,c,d,e]
# p1 = {'name':'tabelle1.tex','data':data1}
# table(**p1)
