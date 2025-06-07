import tkinter as tk
from tkinter import ttk, messagebox
import random


class HoroskopeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikacja Horoskop")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Słownik ze znakami zodiaku i ich miesiącami
        self.znaki_zodiaku = {
            "Baran": "21 marca - 19 kwietnia",
            "Byk": "20 kwietnia - 20 maja",
            "Bliźnięta": "21 maja - 20 czerwca",
            "Rak": "21 czerwca - 22 lipca",
            "Lew": "23 lipca - 22 sierpnia",
            "Panna": "23 sierpnia - 22 września",
            "Waga": "23 września - 22 października",
            "Skorpion": "23 października - 21 listopada",
            "Strzelec": "22 listopada - 21 grudnia",
            "Koziorożec": "22 grudnia - 19 stycznia",
            "Wodnik": "20 stycznia - 18 lutego",
            "Ryby": "19 lutego - 20 marca"
        }

        # Przykładowe horoskopy
        self.horoskopy = [
            "Dziś czeka Cię wyjątkowy dzień pełen niespodzianek!",
            "Twoja energia będzie dziś na najwyższym poziomie.",
            "Dobry dzień na podejmowanie ważnych decyzji.",
            "Uważaj na swoich przyjaciół - ktoś może Cię zaskoczyć.",
            "Miłość będzie dziś w powietrzu!",
            "Koncentruj się na pracy - przyniesie to świetne rezultaty.",
            "Czas na relaks i odpoczynek od codziennych spraw.",
            "Nowe możliwości pojawią się w najbliższym czasie.",
            "Twoja intuicja będzie dziś bardzo silna - słuchaj jej.",
            "Dzień pełen pozytywnej energii i dobrych wiadomości!"
        ]

        self.setup_ui()

    def setup_ui(self):
        # Główna ramka
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Tytuł
        title_label = ttk.Label(main_frame, text="🌟 HOROSKOP 🌟",
                                font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Etykieta dla listy wyboru
        znak_label = ttk.Label(main_frame, text="Wybierz swój znak zodiaku:")
        znak_label.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)

        # Lista wybieralna ze znakami zodiaku
        self.znak_var = tk.StringVar()
        self.znak_combobox = ttk.Combobox(main_frame, textvariable=self.znak_var,
                                          values=list(self.znaki_zodiaku.keys()),
                                          state="readonly", width=20)
        self.znak_combobox.grid(row=2, column=0, columnspan=2, pady=(0, 20))
        self.znak_combobox.set("Wybierz znak...")

        # Ramka dla przycisków
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        # Przyciski
        horoskop_btn = ttk.Button(button_frame, text="Horoskop",
                                  command=self.pokaz_horoskop, width=12)
        horoskop_btn.grid(row=0, column=0, padx=5)

        miesiac_btn = ttk.Button(button_frame, text="Miesiąc",
                                 command=self.pokaz_miesiac, width=12)
        miesiac_btn.grid(row=0, column=1, padx=5)

        wyjscie_btn = ttk.Button(button_frame, text="Wyjście",
                                 command=self.wyjscie, width=12)
        wyjscie_btn.grid(row=0, column=2, padx=5)

        # Pole tekstowe do wyświetlania wyników
        self.result_text = tk.Text(main_frame, height=8, width=45,
                                   font=("Arial", 10), wrap=tk.WORD)
        self.result_text.grid(row=4, column=0, columnspan=2, pady=(20, 0))

        # Scrollbar dla pola tekstowego
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical",
                                  command=self.result_text.yview)
        scrollbar.grid(row=4, column=2, sticky=(tk.N, tk.S))
        self.result_text.configure(yscrollcommand=scrollbar.set)

    def pokaz_horoskop(self):
        """Wyświetla losowy horoskop dla wybranego znaku"""
        wybrany_znak = self.znak_var.get()

        if wybrany_znak == "Wybierz znak..." or not wybrany_znak:
            messagebox.showwarning("Uwaga", "Proszę wybrać znak zodiaku!")
            return

        # Losowy horoskop
        horoskop = random.choice(self.horoskopy)

        # Wyświetlenie w polu tekstowym
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"🔮 HOROSKOP DLA ZNAKU {wybrany_znak.upper()} 🔮\n\n")
        self.result_text.insert(tk.END, horoskop)
        self.result_text.insert(tk.END, f"\n\n✨ Miłego dnia! ✨")

    def pokaz_miesiac(self):
        """Wyświetla okres dla wybranego znaku zodiaku"""
        wybrany_znak = self.znak_var.get()

        if wybrany_znak == "Wybierz znak..." or not wybrany_znak:
            messagebox.showwarning("Uwaga", "Proszę wybrać znak zodiaku!")
            return

        # Pobranie okresu dla znaku
        okres = self.znaki_zodiaku[wybrany_znak]

        # Wyświetlenie w polu tekstowym
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"📅 OKRES DLA ZNAKU {wybrany_znak.upper()} 📅\n\n")
        self.result_text.insert(tk.END, f"Twój znak zodiaku {wybrany_znak} obejmuje okres:\n\n")
        self.result_text.insert(tk.END, f"🗓️ {okres}")

    def wyjscie(self):
        """Zamyka aplikację po potwierdzeniu"""
        odpowiedz = messagebox.askyesno("Wyjście", "Czy na pewno chcesz zamknąć aplikację?")
        if odpowiedz:
            self.root.quit()


def main():
    root = tk.Tk()
    app = HoroskopeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()