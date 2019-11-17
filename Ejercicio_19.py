#Informacion_de_otros_gastos_neto
#DECLARACION
otros_gastos_neto_2006=0
otros_gastos_neto_2007=0
otros_gastos_neto_2008=0.0
total=0

#INPUT
otros_gastos_neto_2006=49
otros_gastos_neto_2007=273
otros_gastos_neto_2008=1.909

#PROCESSING
total=(otros_gastos_neto_2006+otros_gastos_neto_2007+otros_gastos_neto_2008)

#OUTPUT
print("############################")
print("      otros gastos neto     ")
print("############################")
print("otros gastos neto 2006:", otros_gastos_neto_2006)
print("otros gastos neto 2007:", otros_gastos_neto_2007)
print("otros gastos neto 2008:", otros_gastos_neto_2008)
print("total:", total)
print("############################")
