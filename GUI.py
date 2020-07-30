from tkinter import *
from tkinter import ttk
from scoring import scoreAbsouluteWordDifference as errorFun
import time
import textFilter
import printer


class inputWindow:

    def __init__(self, parent, corpus):
        self.parent = parent

        self.corpus = ttk.Label(parent, text=corpus)
        self.corpus.grid(columnspan=6, column=0, sticky=(W, E))

        self.input_feedback = ttk.Label(
            parent, text="Placeholder for feedback of typed text on <Return>")
        self.input_feedback.grid(columnspan=6, column=0, row=1, sticky=(W, E))

        self.input_label = ttk.Label(parent, text="colemak input")
        self.input_label.grid(row=2)

        self.main_input = ttk.Entry(parent)
        self.main_input.bind("<Return>", lambda e: self.handle_text_submission(e))
        self.main_input.grid(columnspan=6, column=1, row=2, sticky=(W, E))

        self.score_field = ttk.Label(parent, text="Score: 100%")
        self.score_field.grid(row=3)

        timerVar = StringVar()
        timerVar.set("Timer" + "0:00")
        self.timer_field = ttk.Label(parent, textvariable=timerVar)
        self.timer_field.grid(row=3, column=1)

        self.wpm_field = ttk.Label(parent, text="WPM: 100")
        self.wpm_field.grid(row=3, column=2)

        self.handle_time()

    def set_corpus(self, corpus_text):
        self.corpus['text'] = corpus_text

    def handle_text_submission(self, event):
        typed_text = self.main_input.get()
        self.input_feedback['text'] = typed_text
        t = time.time()
        print("Time Taken: " + str(t-self.start) + "s")
        printer.printCorrectIncorrect(self.corpus['text'], typed_text)
        # print("Uncorrected WPM: " + str(numWords/timeTaken*60))
        self.main_input.delete(0, 'end')
        wordsToType = textFilter.generateNWordsByLength(
            self.numWords, self.difficulty, self.homerow)
        displayText = " ".join(wordsToType)
        self.corpus['text'] = displayText

    def handle_time(self):
        self.start = time.time()

    def set_cmd_params(self, numWords, difficulty, homerow):
        self.numWords = numWords
        self.difficulty = difficulty
        self.homerow = homerow
