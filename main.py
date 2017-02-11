from variables import set
from variables import get
from os import rmdir


def initiate():
    data = []
    threads = []
    try:
        total = get.connections(data, threads)
        answers = get.answers()

        import time
        while any([x for x in threads if x.isAlive()]):
            time.sleep(1)

        rmdir('TemporaryFiles')

        set.data(answers, data)
        set.output(total, data)

        return answers

    except Exception as e: print(e)#print('No WIFI')


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
