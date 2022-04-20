
import tkinter as tk
import time
import random


def selectPracticeText():
    """
    Selects the text for the user to key accurately
    """
    choice = random.randint(1,4)
    if choice == 1:
        sampleText = "The quick brown fox jumps over the big log."
    elif choice == 2:
        sampleText = "Denny Crane and Alan Shore in Boston Legal."
    elif choice == 3:
        sampleText = "Razor makes the best computer accessories."
    elif choice == 4:
        sampleText = "You win the top secret hidden bonus round!"
    
    return sampleText

def lengthComparison():
    """
    Compares the length of the sample text and user text. Then adds any difference to the returned int value for total length errors.
    """
    sampleTextSize = len(sampleText)
    userEntrySize = len(userEntry.get())
    if sampleTextSize > userEntrySize:
        smallest = userEntrySize
        largest = sampleTextSize
    elif userEntrySize > sampleTextSize:
        smallest = sampleTextSize
        largest = userEntrySize
    else:
        smallest = sampleTextSize
        largest = sampleTextSize
    return smallest, largest

def stringComparison(largest):
    """
    Compares the values of each character in the sample string and user input with a for loop. Any extra or omitted characters are added to the total errors as well.
    """
    finishedEntry = userEntry.get()
    totalErrors = 0
    for i in range(largest):
        try:
            if finishedEntry[i] != sampleText[i]:
                totalErrors += 1
        except:
            totalErrors +=1

    return totalErrors

def finishedClick(event=0):
    """
    Actions to be taken when finished button is clicked. 
    Calculates user typing efficency.
    """

    #Calculate elapsed time    
    totalTime = calculateTime()

    #Calculate length discrepancies
    smallest, largest = lengthComparison()

    #Calculate errors by string comparison
    letterDifference = stringComparison(largest)

    #Calculate percentages and generate strings for results output
    lengthAccuracy, characterAccuracy = stringGeneration(smallest, largest, letterDifference)

    #Generate results GUI items after finished
    resultsGUI(lengthAccuracy, characterAccuracy, totalTime, largest)

    #Set state for GUI objects
    finishedButton["state"] = tk.DISABLED
    startButton["state"] =  tk.NORMAL
    startButton.focus_set()

def resultsGUI(lengthAccuracy, characterAccuracy, totalTime, largest):
    lengthComparisonLabel = tk.Label(root, text = lengthAccuracy)
    characterComparisonLabel = tk.Label(root, text = characterAccuracy)
    timeElapsedLabel = tk.Label(root, text="Total Time: " + str('{0:.1f}'.format(totalTime)) + " seconds")
    wpmCalculated = wpmCalculation(largest, totalTime)
    wpmLabel = tk.Label(root, text = "Estimated WPM: " + str('{0:.1f}'.format(wpmCalculated)))

    #Place results items in GUI after finished
    lengthComparisonLabel.grid(row=4, column=0)
    characterComparisonLabel.grid(row=4,column=1)
    timeElapsedLabel.grid(row=5, column=0)
    wpmLabel.grid(row=5, column=1)

def stringGeneration(smallest, largest, letterDifference):
    """
    Equations for percentages and string formulation for final output
    """
    sampleTextSize = len(sampleText)
    finishedEntrySize = len(userEntry.get()) 
    lengthPercentage = '{0:.1f}'.format((smallest / largest)*100)
    characterPercentage = '{0:.1f}'.format(100 - ((letterDifference / largest)*100))

    lengthAccuracy = ("Expected Length: " + str(sampleTextSize) + "\nYour Length: " + str(finishedEntrySize) + "\nLength Accuracy: " + str(lengthPercentage) + "%")
    characterAccuracy = ("Total Characters: " + str(sampleTextSize) + "\nInaccurate Characters: " + str(letterDifference) + "\nCharacter Accuracy: " + str(characterPercentage) + "%")
    
    return lengthAccuracy, characterAccuracy

def startClick():
    """
    Action taken when the "start" button is clicked:
    Starts the timer.
    Clears, enables, and changes focus to the userEntry field. 
    Enables the "Finished" button
    """
    global startTime
    startTime = time.time()
    finishedButton["state"] = tk.NORMAL
    userEntry["state"] = tk.NORMAL  
    userEntry.delete(0, tk.END)
    userEntry.focus_set()
    startButton["state"] = tk.DISABLED

def calculateTime():
    """
    Calculates time betwen "start" and "finished" button presses
    """
    stopTime = time.time()
    timeElapsed = stopTime - startTime
    return timeElapsed

def wpmCalculation(largest, totalTime):
    """
    Formula for calculating words per minute
    """
    userCharacters = len(userEntry.get()) / 5
    timeCalculation = 60 / totalTime
    wpm = userCharacters * timeCalculation
    return wpm
       
if __name__ == "__main__":
    
    #Creates Tkinter framework and design
    root = tk.Tk()
    root.geometry('525x225')
    root.title("Brandon's Typing Test")
    root.iconbitmap('icon.ico')
    root.bind('<Return>', finishedClick)

    #Create global GUI objects
    instructionTextLabel = tk.Label(root, font=12, text="Please key the sentence below exactly as displayed.")
    sampleText = selectPracticeText()
    sampleTextLabel = tk.Label(root, text=sampleText)
    userEntry = tk.Entry(root, width=45, borderwidth=4, bg="Yellow")
    userEntry.insert(2, sampleText)
    userEntry["state"] = tk.DISABLED
    finishedButton = tk.Button(root, text = "Finished", command = finishedClick)
    finishedButton["state"] = tk.DISABLED
    startButton = tk.Button(root, text = "Start", command = startClick)

    #Place global GUI objects
    instructionTextLabel.grid(row=0, column=0, columnspan=2, pady=5, padx=25)
    sampleTextLabel.grid(row=1, column=0, columnspan=2, pady=5, padx=25)
    userEntry.grid(row=2, column=0, columnspan=2, pady=5, padx=25)
    finishedButton.grid(row=3, column=1, pady= 5)
    startButton.grid(row=3, column=0, pady=5)

    root.mainloop()