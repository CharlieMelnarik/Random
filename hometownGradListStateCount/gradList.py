###########################################
# Just messing around                     #
###########################################
import data
import csv

def SearchName():
    name = str(input("Who are you searching for?: "))
    with open('gradlist.txt') as f:
        for line in f:
            if line.__contains__(name):
                town = line.partition(":")[0]
                if not line.__contains__(":"):
                    pass
                else:
                    print(town)


#SearchName()

def gradPerState():
    #Creates a list of the states that actually exist in the txt file
    stateList = []
    count = 0
    with open('gradlist.txt') as f:
        for line in f:
            for i in data.states:
                if line.__contains__(i + "\n"):
                    state = line.strip("\n")
                    stateList.append(state)

    with open('gradlist.txt') as f:
        stateCount = []
        count = 0
        for line in f:
            #checks each line for the state and resets the count of people per state
            for i in stateList:
                if line.strip("\n") == i:
                    stateCount.append(count)
                    # print(count)
                    # print(i)
                    count = 0
            # checks for lines not containing a city and counts the people still
            if not line.__contains__(":") and line.__contains__(","):
                count = count + line.count(",")
                count = count + line.count("/n")
                # print(line)
            # counts the rest of the lines of people that have citys in those lines
            if line.__contains__(":"):
                noTown = line.partition(":")[2]
                count = count + noTown.count(",")
                count = count + noTown.count("\n")
                # print(noTown)
    #adds the last count of the last state. removes the first count since its 0
    stateCount.append(count)
    stateCount = stateCount[1:]
    print(stateCount)
    print(stateList)
    #use the two arrays to write to csv to make a map. array positions line up
    with open('count.csv', 'w', newline='') as csvfile:
        CSV = csv.writer(csvfile)
        for i in range(len(stateCount)):
            CSV.writerow([stateList[i], stateCount[i]])
gradPerState()
