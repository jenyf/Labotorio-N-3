#Informacion_de_dividendos_por_cpo
#DECLARACION
dividendos_por_cpo_2005 =0.0
dividendos_por_cpo_2006=0.0
dividendos_por_cpo_2007=0.0
total=0

#INPUT
dividendos_por_cpo_2005 =0.06
dividendos_por_cpo_2006=0.09
dividendos_por_cpo_2007=0.08

#PROCESSING
total=(dividendos_por_cpo_2005+dividendos_por_cpo_2006+dividendos_por_cpo_2007)

#OUTPUT
print("############################")
print("    dividendos por cpo      ")
print("############################")
print("dividendos por cpo 2005:", dividendos_por_cpo_2005)
print("dividendos por cpo 2006:", dividendos_por_cpo_2006)
print("dividendos por cpo 2007:", dividendos_por_cpo_2007)
print("total:", total)
print("############################")
