from tkinter import Frame, Label, Button, Entry


class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Program to check roullete")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.create_random_wheels_btn = Button(self, text="Create random wheels")
        self.create_random_wheels_btn.grid(row=2, column=0, padx=10, pady=10)

        self.make_tests_for_my_wheels = Button(self, text="Make tests for my wheels")
        self.make_tests_for_my_wheels.grid(row=3, column=0, padx=10, pady=10)

        self.make_score_stats = Button(self, text="Show Score for my wheels")
        self.make_score_stats.grid(row=4, column=0, padx=10, pady=10)

        self.show_score_among_wheels = Button(self, text="show_score_stats_among_random_wheels")
        self.show_score_among_wheels.grid(row=5, column=0, padx=10, pady=10)

        self.make_sektors_stats_btn = Button(self, text="Make sektors stats for my wheels")
        self.make_sektors_stats_btn.grid(row=6, column=0, padx=10, pady=10)

        self.winners_in_sektors_stats_btn = Button(self, text="Calculate winners in sektors")
        self.winners_in_sektors_stats_btn.grid(row=7, column=0, padx=10, pady=10)

        self.entry_sektor_finder = Entry(self)
        self.entry_sektor_finder.insert(0, 'afar4010.xlsx 16')
        self.entry_sektor_finder.grid(row=8, column=1, padx=10, pady=10)

        self.find_sektor_for_wheel_btn = Button(self, text="Find sektor for wheel")
        self.find_sektor_for_wheel_btn.grid(row=8, column=0, padx=10, pady=10)


