from CSP_6_03_Writing_to_files import writeFile, sortNames, highScore


def test_writeFile():
    testList = ["Jerry", "Alex", "Ryan"]

    writeFile(testList, "test_names.txt")

    file = open("test_names.txt", "r")
    lines = file.readlines()
    file.close()

    assert lines == ["Jerry\n", "Alex\n", "Ryan\n"]


def test_sortNames():
    testList = ["Jerry", "Alex", "Ryan", "Bob"]

    writeFile(testList, "test_names.txt")

    sortNames("test_names.txt", "test_names_sorted.txt")

    file = open("test_names_sorted.txt", "r")
    lines = file.readlines()
    file.close()

    assert lines == ["Alex\n", "Bob\n", "Jerry\n", "Ryan\n"]


def test_highScore():
    testScores = [90, 80, 70]

    writeFile(testScores, "scores.txt")

    average = highScore(100)

    assert average == 85