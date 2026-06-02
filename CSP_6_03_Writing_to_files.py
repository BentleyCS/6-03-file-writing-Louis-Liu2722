def writeFile(inputList, fileName):
    # Creates a file with the given name.
    # Each item from the list is written on its own line.
    file = open(fileName, "w")

    for item in inputList:
        file.write(str(item) + "\n")

    file.close()


def sortNames(fileName, targetFile):
    # Reads names from the source file.
    file = open(fileName, "r")
    names = file.readlines()
    file.close()

    # Removes the extra new line characters.
    for i in range(len(names)):
        names[i] = names[i].strip()

    # Sorts the names alphabetically.
    names.sort()

    # Writes the sorted names into the target file.
    writeFile(names, targetFile)


def highScore(newScore: int):
    # Adds the new score to scores.txt.
    file = open("scores.txt", "a")
    file.write(str(newScore) + "\n")
    file.close()

    # Reads all scores from scores.txt.
    file = open("scores.txt", "r")
    scores = file.readlines()
    file.close()

    total = 0

    # Adds all scores together.
    for score in scores:
        total += int(score.strip())

    # Calculates and returns the average.
    average = total / len(scores)

    return average