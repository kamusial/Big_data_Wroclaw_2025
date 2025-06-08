import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class File:
    def __init__(self, path):
        self.path = path
        self.content = None
        self.figure_counter = 0
        self.operation_counter = 5

    def open(self):
        if self.operation_counter > 0:
            self.content = pd.read_csv(self.path)
            print(f'Otwarto plik {self.path}')
            print(self.content.head(3))
            self.operation_counter -= 1

    def show_details(self, *details):
        if self.operation_counter > 0:
            self.operation_counter -= 1
            print(f'------Szczegóły---------:')
            if 'col' in details:
                print(f'Kolumny:\n{self.content.columns}')
            if 'shape' in details:
                print(f'Kształt: {self.content.shape[0]} wierszy, {self.content.shape[1]} kolumn')

    def describe(self):
        if self.operation_counter > 0:
            self.operation_counter -= 1
            print('Opis')
            print(self.content.describe(percentiles=[.1, 0.2, 0.5, 0.9]
    ).T.round().to_string())

    def correlation(self):
        if self.operation_counter > 0:
            self.operation_counter -= 1
            print('Koleracja:')
            sns.heatmap(self.content.corr(), annot=True)
            self.figure_counter += 1
            plt.savefig('corr'+str(self.figure_counter)+'.png')
            plt.show()

    def plots(self):
        if self.operation_counter > 0:
            self.operation_counter -= 1
            print('Wykresy:')
            sns.pairplot(self.content)
            self.figure_counter += 1
            plt.savefig('pair' + str(self.figure_counter) + '.png')
            plt.show()

    def save(self):
        if self.operation_counter > 0:
            self.operation_counter -= 1
            self.content.to_csv(self.path[:-3]+'_saved.'+self.path[-3:])