from variables import specify


def data(answers, data):
    if answers[0] != '':
        specify.show(answers[0], data)  # Determines if only libraries or not

    if answers[1] != '' and answers[2] != '':
        specify.range(answers[1] + '-' + answers[2], data)  # Buildings with N to M people in

    if answers[3] != '':
        specify.search(answers[3], data)  # Buildings with search terms in

    specify.asort(answers[4], data)  # Determines sort method


def output(total, data):
    if len(data) == 0:
        print('None')
    else:
        for things in range(len(data)):
            print('Building:', data[things][0], '\nPersons:', data[things][1], '\nPercentage of Persons on campus here:', (str(((data[things][1]/total)*100)) + '    ')[:4] + '%', end='\n\n')
        print('Total Persons on campus: ~' + str(total))

        print('Total results:', len(data))