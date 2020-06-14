from tkinter import *
from tkinter import ttk


class inputWindow:

    def __init__(self, parent):
        self.parent = parent

        self.corpus = ttk.Label(parent, text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit..
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit.. Lorem ipsum dolor sit amet, consectetur adipiscing elit.""")
        self.corpus.grid(columnspan=6, column=0, sticky=(W, E))

        self.input_feedback = ttk.Label(
            parent, text="Placeholder for feedback of typed text on <Enter>")
        self.input_feedback.grid(columnspan=6, column=0, row=1, sticky=(W, E))

        self.input_label = ttk.Label(parent, text="colemak input")
        self.input_label.grid(row=2)

        self.main_input = ttk.Entry(parent)
        self.main_input.bind("<Enter>", lambda e: None)
        self.main_input.grid(columnspan=6, column=1, row=2, sticky=(W, E))

        self.score_field = ttk.Label(parent, text="Score: 100%")
        self.score_field.grid(row=3)

        self.timer_field = ttk.Label(parent, text="Timer: 0:00")
        self.timer_field.grid(row=3, column=1)

        self.wpm_field = ttk.Label(parent, text="WPM: 100")
        self.wpm_field.grid(row=3, column=2)
