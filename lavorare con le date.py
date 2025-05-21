# lavorare con le date

##  formato  aaaa/mm/gg
## creare grafico di base
## aggiungere linestyle
## cambiare formato


from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates


plt.style.use('ggplot')


x = [
    datetime(2025,1,10),
    datetime(2025,1,15),
    datetime(2025,1,17),
    datetime(2025,1,20),
    datetime(2025,1,27),
    datetime(2025,1,30)
]

y = [3,6,2,8,5,9]


#all'inizio abbiamo un grafico dispersivo: possiamo andare a creare una linea con LINESTYLE

plt.plot_date(x,y, linestyle='solid')


# prendi la finestra attuale e fai un autoformatt
# date ruotate e più leggibili   = GCF

plt.gcf().autofmt_xdate()



# formattiamo  'magari ci serve il mese scritto..
# d = giorno / b = mese / y = anno

date_formattate = mpl_dates.DateFormatter('%d %b %y')

plt.gca().xaxis.set_major_formatter(date_formattate)



plt.title('Nome del grafico')

plt.show()