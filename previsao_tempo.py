import pandas as pd

from sklearn.naive_bayes import GaussianNB

dados=pd.read_excel(r"E:\Users\vnune\Desktop\Vinícius\UFU\IA\Naive Bayes\Project\tempo uberlandia.xlsx")


x_dados=dados.iloc[:,0:3].values
y_chuva=dados.iloc[:,7].values
y_tmin=dados.iloc[:,6].values
y_tmax=dados.iloc[:,5].values
y_umidade=dados.iloc[:,3].values


naive_chuva=GaussianNB()
naive_tmin=GaussianNB()
naive_tmax=GaussianNB()
naive_umidade=GaussianNB()

naive_chuva.fit(x_dados,y_chuva)
naive_tmin.fit(x_dados,y_tmin)
naive_tmax.fit(x_dados,y_tmax)
naive_umidade.fit(x_dados,y_umidade)


data=input("Informe a data de hoje no formato dd/mm: ")
temp=input("Informe a temperatura do dia: ")
dia = int(data[0:2])
mes=int(data[3:5])

x=0
for dado in x_dados[:,1]:
    if dado==mes:
        break
    x+=1

for dado in x_dados[x:,0]:
    if dado==dia:
        break
    x+=1
x+=1
if dia==31 and mes==12:
    dia_am=1
    mes_am=1
else:
    dia_am=x_dados[x,0]
    mes_am=x_dados[x,1]
amanha=str(dia_am)+"/"+str(mes_am)

chuva=naive_chuva.predict([[dia_am,mes_am,int(temp)]])
tmin=naive_tmin.predict([[dia_am,mes_am,int(temp)]])
tmax=naive_tmax.predict([[dia_am,mes_am,int(temp)]])
umidade=naive_umidade.predict([[dia_am,mes_am,int(temp)]])

if chuva <=25:
      tempo="Sem chuva"
elif chuva<=75:
      tempo="chuva moderada"
else:
      tempo="chuva forte"


print("A previsão do tempo do dia",amanha,"será de:","\n"
      " Temp Máxima:",tmax[0],"\n Temp Mínima:",tmin[0],"\n"
        " Chuva:",tempo,"("+ str(chuva[0]/10)+" mm)\n"
      " Umidade:",umidade[0],"%")
