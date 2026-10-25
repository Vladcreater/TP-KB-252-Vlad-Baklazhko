globalList = [
    {"name": "Bob",  "phone": "0631234567", "email": "bob@gmail.com",  "group": "KB-251"},
    {"name": "Emma", "phone": "0631234568", "email": "emma@gmail.com", "group": "KB-252"},
    {"name": "Jon",  "phone": "0631234569", "email": "jon@gmail.com",  "group": "KB-241"},
    {"name": "Zak",  "phone": "0631234570", "email": "zak@gmail.com",  "group": "KB-242"}
]

FIELDS = ["name", "phone", "email", "group"]


def printAllList(listForPrinting):
    for item in listForPrinting:
        line = ("Name = " + item["name"] +
                " Phone = " + item["phone"] +
                " Email = " + item["email"] +
                " Group = " + item["group"])
        print(line)


def findPosition(listForFinding, nameForFinding):
    index = 0
    for item in listForFinding:
        if item["name"] < nameForFinding:
            index += 1
        else:
            break
    return index


def addElemToSortedList(listForAdd, newElem):
    positionForInsert = findPosition(listForAdd, newElem["name"])
    listForAdd.insert(positionForInsert, newElem)
    return


def getElement():
    name = input("Please enter the name ")
    phone = input("Please enter the phone ")
    email = input("Please enter the email ")
    group = input("Please enter the group ")
    return {"name": name, "phone": phone, "email": email, "group": group}


def deleteElem(listForDel, name):
    indexForDel = findPosition(listForDel, name)
    if indexForDel < len(listForDel) and listForDel[indexForDel]["name"] == name:
        del listForDel[indexForDel]
        return True
    else:
        return False


def updateElement(listForUpdate):
    name = input("Please enter the name of the element for update ")
    index = findPosition(listForUpdate, name)
    if index >= len(listForUpdate) or listForUpdate[index]["name"] != name:
        print("Element hasn't been found")
        return False

    oldElem = listForUpdate[index]
    print("Current data: ", oldElem)
    print("Press Enter to keep the current value")

    newElem = {}
    for field in FIELDS:
        value = input("Please enter new " + field + " [" + oldElem[field] + "] ")
        newElem[field] = value if value != "" else oldElem[field]

    del listForUpdate[index]
    addElemToSortedList(listForUpdate, newElem)
    print("Element has been updated")
    return True


def main():
    while True:
        chouse = input("Please enter the command [C - add new elem, D - delete elem, P - print all List, U - update element, X - exit] ")
        match chouse:
            case "C" | "c":
                newElem = getElement()
                addElemToSortedList(globalList, newElem)
            case "D" | "d":
                nameElemForDel = input("Please enter the name for delete ")
                if deleteElem(globalList, nameElemForDel):
                    print("Element has been deleted")
                else:
                    print("Element hasn't been found")
            case "P" | "p":
                printAllList(globalList)
            case "U" | "u":
                updateElement(globalList)
            case "X" | "x":
                print("Exit")
                break
            case _:
                print("Wrong operation")


main()
