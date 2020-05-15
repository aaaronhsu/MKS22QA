from tkinter import Tk, simpledialog, messagebox

def extractData():
    # pulls data from file
    f = open('test.txt')
    data = f.readlines()
    for i in range(len(data) - 1):
        # removes the \n of each line
        data[i] = data[i][:-1]
    f.close()
    return data

def downloadKnowledge(data):
    # updates world dict with extracted data
    d = {}
    for i in range(len(data)):
        data[i] = data[i].split(',')
        d[data[i][0]] = data[i][1]
    return d

def uploadKnowledge():
    # updates CSV with data in world
    f = open('test.txt', 'w')
    for i in world:
        f.write(i + ',' + world[i] + '\n')
    f.close()



# pulls data from CSV and sets up windows
print('Ask the Expert - Capital Cities of the World')
root = Tk()
root.withdraw()
world = downloadKnowledge(extractData())

while True:
    inp = simpledialog.askstring('Country', 'Type the name of the country:')
    if inp.lower() in world:
        messagebox.showinfo('Answer', 'The capital city of ' + inp + ' is ' + world[inp.lower()])
    else:
        learn = simpledialog.askstring('Country', 'Not in database, type the name of the capital of ' + inp + ":")
        world[inp] = learn
        uploadKnowledge()

# format example of test.txt:
# a,b
# c,d
# potato,candy
# asdf,qwer