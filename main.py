import customtkinter as ctk
import random

class SortingVisualiser:

    def __init__(self):

        #initilising variables
        self.boxes = []
        self.arr = [64, 34, 25, 12, 22, 11, 90]
        self.animationSpeed = 5
        self.animationSpeedLabel = None
        self.boxHeight = 100
        self.swapAnimationValue = 150
        self.opt1 = "Bubble Sort"
        self.opt2 = "Selection Sort"

        self.complexities = {
            self.opt1: {
                "Best Case": "O(n)",
                "Average Case": "O(n^2)",
                "Worst Case": "O(n^2)"
            },
            self.opt2: {
                "Best Case": "O(n^2)",
                "Average Case": "O(n^2)",
                "Worst Case": "O(n^2)"
            }
        }

        self.setupUI()

    def setupUI(self):
        ctk.set_appearance_mode("system")  
        ctk.set_default_color_theme("dark-blue") 

        self.app = ctk.CTk()  
        self.app.geometry("800x800")
        self.app.resizable(False, False)
        self.app.title(self.opt1)

        self.menuFrame = ctk.CTkFrame(self.app, fg_color="transparent")
        self.menuFrame.pack(side="top", pady=50)

        self.buttonFrame = ctk.CTkFrame(self.app, fg_color="transparent")
        self.buttonFrame.pack(side="bottom")

        self.sliderFrame = ctk.CTkFrame(self.app, fg_color="transparent")
        self.sliderFrame.pack(side="bottom")

        self.boxFrame = ctk.CTkFrame(self.app, fg_color="transparent")
        self.boxFrame.place(x=0, y=300, relwidth=1)

        self.optionMenu()

        self.titleLabel = ctk.CTkLabel(self.menuFrame, 
                                      font=("Helvetica", 16, "bold"),  
                                      text_color=("white", "gray25"), 
                                      text=f"Sorting Algorithm: {self.opt1}\n\nBest Case: O(n)\nAverage Case: O(n^2)\nWorst Case: O(n^2)",
                                      width=250,
                                      height=150,  
                                      corner_radius=20,
                                      fg_color=("gray15", "gray75"))   
        self.titleLabel.pack(side="top", pady=30, padx=20)  


        self.createBoxes()
        self.createSlider()
        self.createButtons()

        self.app.mainloop()
    
    def updateUI(self, choice):
        self.app.title(choice)

        self.arr = [64, 34, 25, 12, 22, 11, 90]

        for box in self.boxes:
            box.destroy()
        self.boxes = []

        self.createBoxes()

        self.titleLabel.configure(
            text=f"Sorting Algorithm: {choice}\n\n"
                 f"Best Case: {self.complexities[choice]['Best Case']}\n"
                 f"Average Case: {self.complexities[choice]['Average Case']}\n"
                 f"Worst Case: {self.complexities[choice]['Worst Case']}"
        )

        if choice == self.opt1:
            self.sortButton.configure(command= lambda: self.bubbleSort(0, 0))
        elif choice == self.opt2:
            self.sortButton.configure(command= lambda: self.selectionSort(0, 0, 0))

    def createButtons(self):
        self.sortButton = ctk.CTkButton(self.buttonFrame,
                       text="SORT",
                       corner_radius=15,
                       width=80,
                       height=50,
                       font=("Helvetica", 14, "bold"),
                       fg_color="SlateBlue3",
                       text_color="gray75",
                       hover_color="SlateBlue4",
                       command=self.differentSorting)

        self.shuffleButton = ctk.CTkButton(self.buttonFrame,
                       text="SHUFFLE",
                       corner_radius=15,
                       width=80,
                       height=50,
                       font=("Helvetica", 14, "bold"),
                       fg_color="SlateBlue3",
                       text_color="gray75",
                       hover_color=("SlateBlue4"),
                       command=self.shuffleArray)

        self.sortButton.pack(side="left", padx=10, pady=40)
        self.shuffleButton.pack(side="left", padx=10, pady=40)

    def differentSorting(self):
        if self.optionmenu.get() == self.opt1:
            self.bubbleSort(0, 0)
        elif self.optionmenu.get() == self.opt2:
            self.selectionSort(0, 0, 0)

    def optionMenu(self):
        self.optionmenu = ctk.CTkOptionMenu(self.menuFrame,
                                            height=40,
                                            width=100, 
                                            font=("Helvetica", 18, "bold"),
                                            text_color=("gray75"),
                                            fg_color=("SlateBlue3"),
                                            button_color=("SlateBlue3"),
                                            button_hover_color="SlateBlue4",
                                            values=[self.opt1, self.opt2],
                                            command=self.updateUI)
        self.optionmenu.set(self.opt1)
        self.optionmenu.pack(pady=10)

    def bubbleSort(self, i=0, j=0):
        self.sortButton.configure(state="disabled")
        self.shuffleButton.configure(state="disabled")
        self.optionmenu.configure(state="disabled")
        n = len(self.arr)
        if i >= n-1:
            self.sortButton.configure(state="normal")
            self.shuffleButton.configure(state="normal")
            self.optionmenu.configure(state="normal")
            return

        if j < n-i-1:
            if self.arr[j] > self.arr[j+1]:
                self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                self.swapBoxes(j, j+1, lambda: self.boxFrame.after(int(1000/self.animationSpeed), lambda: self.bubbleSort(i, j+1)))
            else:
                self.boxFrame.after(int(1000/self.animationSpeed), self.bubbleSort(i, j+1))
        else:
            self.boxFrame.after(int(1000/self.animationSpeed), lambda: self.bubbleSort(i+1, 0))
    
    def selectionSort(self, i=0, min_idx=0, j=0):
        self.sortButton.configure(state="disabled")
        self.shuffleButton.configure(state="disabled")
        self.optionmenu.configure(state="disabled")
        n = len(self.arr)

        if i >= n - 1: 
            self.sortButton.configure(state="normal")
            self.shuffleButton.configure(state="normal")
            self.optionmenu.configure(state="normal")
            return

        if j == i: 
            min_idx = i  

        if j >= n:
            if min_idx != i:
                self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
                self.swapBoxes(i, min_idx, lambda: self.boxFrame.after(int(1000 / self.animationSpeed), lambda: self.selectionSort(i + 1, i, i + 1)))
            else:
                self.boxFrame.after(int(1000 / self.animationSpeed), lambda: self.selectionSort(i + 1, i, i + 1))
            return

        self.searchAnimation(j)

        if self.arr[j] < self.arr[min_idx]:  
            min_idx = j

        self.boxFrame.after(
            int(1000 / self.animationSpeed), 
            lambda: self.selectionSort(i, min_idx, j + 1))


    def shuffleArray(self):
        random.shuffle(self.arr)
        for i in range(len(self.arr)):
            self.boxes[i].configure(text=str(self.arr[i]))

    def createBoxes(self):
        for i in range(len(self.arr)):
            posX = 50 + i * 100
            box = ctk.CTkLabel(master=self.boxFrame, 
                               text=str(self.arr[i]),
                               width=80,
                               height=80,
                               fg_color=("gray15", "gray75"),
                               text_color=("gray75", "gray15"),
                               font=("Helvatica", 18, "bold"),
                               corner_radius=8)
            box.place(x=posX, y=int(self.boxHeight))
            self.boxes.append(box)

    def flashColorAnimation(self, swap1, swap2, count=0, maxFlashes=5):
        if count >= maxFlashes:
            self.boxes[swap1].configure(fg_color="purple2")
            self.boxes[swap2].configure(fg_color="purple2")
            return 
        flashColor = "purple2" if count % 2 == 0 else ("gray15", "gray75")
        self.boxes[swap1].configure(fg_color=flashColor)
        self.boxes[swap2].configure(fg_color=flashColor)

        self.boxFrame.after(int(1000/self.animationSpeed), lambda: self.flashColorAnimation(swap1, swap2, count+1, maxFlashes))

    def resetColor(self, swap1, swap2):
        self.boxes[swap1].configure(fg_color=("gray15", "gray75"))
        self.boxes[swap2].configure(fg_color=("gray15", "gray75"))

    def swapBoxesAnimation(self, swap1, swap2, callback, steps=5, animation="up"):
        if self.optionmenu.get() == self.opt1:  
            self.swapAnimationValue = 150
        elif self.optionmenu.get() == self.opt2:  
           self.swapAnimationValue = 50

        x1, y1 = self.boxes[swap1].winfo_x(), self.boxes[swap1].winfo_y()
        x2, y2 = self.boxes[swap2].winfo_x(), self.boxes[swap2].winfo_y()

        targetx1 = 50 + swap2 * 100
        targetx2 = 50 + swap1 * 100
        targetY = self.boxHeight - 85

        if animation == "up":
            if y1 > targetY :
                if self.optionmenu.get() == self.opt1:  # Bubble Sort
                    self.boxes[swap1].place(x=x1, y=y1 - steps)

                elif self.optionmenu.get() == self.opt2:  # Selection Sort
                    self.boxes[swap1].place(x=x1, y=y1 - steps)
                    self.boxes[swap2].place(x=x2, y=y2 - steps)
                self.boxFrame.after(int(self.swapAnimationValue / self.animationSpeed),
                                        lambda: self.swapBoxesAnimation(swap1, swap2, callback, steps, "up"))
            else:
                self.swapBoxesAnimation(swap1, swap2, callback, steps, "swap")

        elif animation == "swap":
            if x1 < targetx1 or x2 > targetx2:
                if x1 < targetx1:
                    self.boxes[swap1].place(x=x1 + steps, y=y1)
                if x2 > targetx2:
                    self.boxes[swap2].place(x=x2 - steps, y=y2)
                self.boxFrame.after(int(self.swapAnimationValue / self.animationSpeed),
                                    lambda: self.swapBoxesAnimation(swap1, swap2, callback, steps, "swap"))
                               
            else:
                self.swapBoxesAnimation(swap1, swap2, callback, steps, "down")

        elif animation == "down":
            if y1 < self.boxHeight :
                if self.optionmenu.get() == self.opt1:  # Bubble Sort
                    self.boxes[swap1].place(x=x1, y=y1 + steps)

                elif self.optionmenu.get() == self.opt2:  # Selection Sort
                    self.boxes[swap1].place(x=x1, y=y1 + steps)
                    self.boxes[swap2].place(x=x2, y=y2 + steps)
                self.boxFrame.after(int(self.swapAnimationValue / self.animationSpeed),
                                        lambda: self.swapBoxesAnimation(swap1, swap2, callback, steps, "down"))
            else:
                self.boxes[swap1].place(x=targetx1, y=self.boxHeight)
                self.boxes[swap2].place(x=targetx2, y=self.boxHeight)
                self.boxes[swap1], self.boxes[swap2] = self.boxes[swap2], self.boxes[swap1]
                self.resetColor(swap1, swap2)
                callback()
        
    def swapBoxes(self, swap1, swap2, callback, steps=5):
        self.flashColorAnimation(swap1, swap2, count=0, maxFlashes=5)
        self.boxFrame.after(int(5000/self.animationSpeed), lambda: self.swapBoxesAnimation(swap1, swap2, callback, steps, "up"))

    def searchAnimation(self, index):
        if index >= len(self.arr):  
            return 

        self.boxes[index].configure(fg_color="khaki")  
            
        self.boxFrame.after(
            int(1000 / self.animationSpeed), 
            lambda idx=index: (self.boxes[idx].configure(fg_color=("gray15", "gray75")), 
            self.searchAnimation(idx + 1))
        )


#slider functions
    def sliderCallback(self, value):
        self.animationSpeed = int(value)
        self.animationSpeedLabel.configure(text=f"Speed: {self.animationSpeed}")

    def createSlider(self):
        animationSlider = ctk.CTkSlider(self.sliderFrame, 
                                        from_=1, 
                                        to=10, 
                                        number_of_steps=9,
                                        progress_color="green",
                                        button_color="SlateBlue3",
                                        button_hover_color="SlateBlue4",
                                        command=self.sliderCallback)
        animationSlider.pack(pady=10)

        self.animationSpeedLabel = ctk.CTkLabel(self.sliderFrame, 
                                                font=("Helvetica", 18, "bold"),
                                                text_color=("gray15","gray75"),
                                                text=f"Speed: {self.animationSpeed}")
        self.animationSpeedLabel.pack(pady=10)
    
if __name__ == "__main__":
    SortingVisualiser()