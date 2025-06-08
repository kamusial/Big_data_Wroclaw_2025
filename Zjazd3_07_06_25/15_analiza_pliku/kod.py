from clasy import File

moj_plik = File('diabetes.csv')

moj_plik.open()
moj_plik.show_details('kamil', 'col')
moj_plik.describe()
moj_plik.correlation()
moj_plik.plots()
moj_plik.save()