import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")

        self.questions = [
            {"question": "What is the capital of France?",
             "options": ["Paris", "London", "Berlin", "Madrid"],
             "answer": "Paris"},
            {"question": "Who wrote 'Romeo and Juliet'?",
             "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
             "answer": "William Shakespeare"},
            {"question": "What is the chemical symbol for water?",
             "options": ["W", "H2O", "O2", "CO2"],
             "answer": "H2O"}
        ]

        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(master, text="")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", command=lambda idx=i: self.check_answer(idx))
            button.pack(fill=tk.X, padx=10, pady=5)
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
            self.current_question_index += 1
        else:
            self.display_score()

    def check_answer(self, option_index):
        selected_option = self.option_buttons[option_index].cget("text")
        correct_answer = self.questions[self.current_question_index - 1]["answer"]
        if selected_option == correct_answer:
            self.score += 1
        self.next_question()

    def display_score(self):
        messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/{len(self.questions)}")
        self.master.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
