# [PIE CHARTS]

from matplotlib import pyplot as plt

plt.style.use('ggplot')


slices = [200,50,30,10,23]   # non deve essere uguale a 100, la proporzione viene fatta da MPL

# etichette

labels = ['si', 'no', 'forse', 'non so', 'preferisco non dire']

# colors

colors = ['red', 'brown', 'orange', 'green', 'blue']


# explode : far risaltare una o più fette  --> nulla ci vieta di fare un explode su tutte 
explode = [0,0,0,0,0.3]



#   wedgeprops = cambia il bordo dei colori
#   startangle = da dove inizia la creazione del grafico
#   autopct = inserisce le percetuali automaticamente
plt.pie(slices, labels=labels, colors = colors, wedgeprops={'edgecolor': '000000'}, startangle=70, explode=explode, autopct='%1.1f%%')








plt.title('Nome del grafico')

plt.show()