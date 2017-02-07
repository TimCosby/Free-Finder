from variables import set
from variables import get


def initiate():
    data = []
    try:
        total = get.connections(data)
        answers = get.answers()
        set.data(answers, data)
        set.output(total, data)
    except: print('No WIFI')
    return answers


def refresh(answers):
    ### KEEPS CHOICES FROM LAST SESSION BUT UPDATES NUMBERS
    data = []
    try:
        total = get.connections(data)
        set.data(answers, data)
        set.output(total, data)
    except: print('No WIFI')


if __name__ == '__main__':
    # First Run
    answers = []
    Uinput = ''
    while Uinput.lower() != 'exit':

        if Uinput.lower() == 'refresh':
            refresh(answers)  # Refreshes previous answers
        else:  # Redoes the program
            answers = initiate()

        Uinput = ''
        while Uinput.lower() != 'refresh' and Uinput.lower() != 'exit' and Uinput.lower() != 'redo':
            Uinput = input('Redo/Refresh/Exit\n')
