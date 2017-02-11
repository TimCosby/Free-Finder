import urllib
from urllib.request import urlopen
from os import remove
from os import mkdir
from os.path import exists

URL = 'http://maps.wireless.utoronto.ca/stg/popUp.php?name='
DIRECTORY = 'TemporaryFiles\\temp'
PAGES = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008',
         '0009', '0010', '0011', '0012', '0013', '0014', '0016', '0019',
         '0020', '0021', '0022', '0023', '0024', '0025', '0026', '0027',
         '0028', '0029', '0030', '0032', '0033', '0034', '0036', '0038',
         '0039', '0040', '0041', '0042', '0043', '0047', '0049', '0050',
         '0051', '0052', '0053', '0054', '0056', '0057', '0061', '0062',
         '0064', '0065', '0066', '0067', '0068', '0070', '0071', '0072',
         '0073', '0075', '0077', '0078', '0079', '0080', '0082', '0083',
         '0088', '0089', '0090', '0091', '0097', '0098', '0101', '0103',
         '0104', '0105', '0106', '0110', '0111', '0115', '0120', '0123',
         '0125', '0127', '0128', '0129', '0130', '0131', '0132', '0133',
         '0134', '0138', '0142', '0143', '0145', '0146', '0152', '0153',
         '0154', '0155', '0156', '0158', '0160', '0161', '0171', '0172',
         '0192', '0193', '0194', '0401', '0405', '0407', '0411', '0415',
         '0416', '0417', '0418', '0419', '0420', '0421', '0423', '0426',
         '0429', '0430', '0434', '0435', '0443', '0453', '0455', '0501',
         '0502', '0503', '0504', '0506', '0507', '0508', '0509', '0514',
         '0515', '0518', '0528', '0530', '0575', '0600', '0602', '0603',
         '0608', '0675', '0930', '097A', 'A005', 'A006', 'A008', 'A010',
         'A030', 'A032', 'A061', 'A068', 'A098', 'B006', 'B010', 'B012',
         'X033', 'X073', 'XESC', 'XINN', 'XLAW', 'XMSB', 'XMUS', 'XNEW',
         'XROB', 'XSMC', 'XVAR', 'XVIC', 'XWDW', 'XXBC', 'XXFC', 'XXSU']
BUILDINGS = ['University College', 'Hart House',
             'Gerstein Science Information Centre', 'McMurrich Bldg.',
             'Medical Sciences Bldg.', 'Robarts Research Library',
             'Lassonde Mining Bldg.', 'Wallberg Bldg.', 'Sandford Fleming',
             'Simcoe Hall', 'Tanz Neuroscience Bldg', 'Munk Centre',
             'Whitney Hall', 'UTS', 'Banting Institute',
             'J. Robert S. Prichard Alumni House', 'Rosebrugh Bldg.',
             'Engineering Annex', 'Mechanical Engineering Bldg.',
             'University College Union', 'Haultain Bldg.', 'Fitzgerald Bldg.',
             'Cumberland House', 'Physical Geography Building',
             'Architecture Bldg.', 'Sir Daniel Wilson Residence',
             'Varsity Stadium', 'Wetmore Hall-New College', 'Sidney Smith Hall',
             'Massey College', 'Astronomy & Astrophysics Building',
             'Woodsworth College', '49 St. George St. ( Old TYP )',
             'Flavelle House', 'Varsity Pavilion', 'Goldring Centre',
             'School of Graduate Studies', 'Canadiana Gallery',
             'Aerospace Building', 'Falconer Hall', 'Edward Johnson Bldg.',
             'Best Building', 'Inst. of Child Study', '1 Spadina Crescent',
             'Graduate Student Union', 'Bancroft Hall', 'South Borden Bldg.',
             'Earth Science Centre', 'Graduate House', 'Dentistry Bldg.',
             '665 Spadina Ave', '215 Huron St.', 'Benson Bldg.',
             'Galbraith Bldg.', '92 College St.',
             'Ramsay Wright Zoological Labs', 'Lash Miller Chemistry Labs',
             'Faculty Club', 'Sussex Court', 'McLennan Physical Labs',
             'Anthropology Building', 'Bahen Centre for Information Technology',
             'Gage Research Bldg', '254-256 McCaul St.', '123 St George St',
             'Munk School', '88 College St.',
             'Glen Morris Theatre ( 4 Glen Morris )', 'Medieval Studies Centre',
             '90 Wellesley', 'Morrison Residence',
             'School of Continuing Studies', 'Max Gluskin House',
             'Fields Institute', '162 St George St', '121 St George St',
             '246 Bloor St. W.', 'Rotman School of Management - South', 'UTSU',
             'Ontario Inst. For Studies In Education', '703 Spadina Ave.',
             '172 St George St', 'Jackman Humanities Building',
             'Early Learning Centre', 'Woodsworth College Residence',
             'New College Residence', 'Innis College', 'Innis Residence',
             'Rotman School of Management',
             'Campus Co-op Day Care 370 Huron St.', '713 Spadina Ave.',
             'Koffler Student Services Centre', 'Koffler House',
             '40 Sussex Ave', '500 University', '56 Spadina Rd.',
             'Health Sciences Bldg', 'Examination Centre - 255 McCaul',
             '263 McCaul Street', 'Chestnut Residence',
             'Donnelly Centre Cellular & Biomolecular Research',
             'Leslie L. Dan Pharmacy Bldg', '455 Spadina Ave.',
             'MacDonald-Mowat House', 'Stewart Bulding', 'MaRS Centre',
             '481 University Ave', 'Loretto College', 'Elmsley Hall',
             'Alumni Hall', 'Brennan Hall', 'Odette Hall', 'Windle House',
             'Phelan House', 'Pontifical Inst.', 'More Hall', 'Fisher Hall',
             'Teefy Hall', 'Maritain House', 'Carr Hall', 'Kelly Library',
             'Cardinal Flahiff Building', 'Toronto School of Theology',
             'Sobara Residence', '39 Queens Park Cres. E.', '3 Elmsley Place',
             '5 Elmsley Place', 'Victoria College', 'Emmanuel College',
             'Birge-Carnegie', 'Burwash Hall', 'Annesley Hall',
             'Goldring Student Centre', 'Margaret Addison Hall',
             'Isabel Bader Theatre', 'E.J. Pratt Library', 'Northrop Frye Hall',
             'Rowell Jackman Hall', 'Lillian Massey Bldg.',
             '63 65 Charles St W', 'Knox College', 'Trinity College',
             'Gerald Larkin Bldg.', 'George Ignatieff Theatre',
             'St. Hildas College', 'Wycliffe College', 'CAMH ( 250 College )',
             'McLuhan Program', 'Macleod Auditorium (MSB)', 'Bissell Bldg.',
             'D.L. Pratt', 'Convocation Hall', 'Varsity Arena',
             'Wilson Hall-New College', 'North Borden Bldg.',
             'Warren Stevens Bldg.', 'Regis College - 100 Wellesley',
             'T. Fisher Rare Books Library', 'Convocation Tent',
             'Graham Library', 'Sid Smith Outside', 'Lash Miller Outside',
             'ESC Outside', 'Innis Outside', 'Near Law Library', 'MSB Outside',
             'Near Music', 'New College Outside', 'Robarts Outside',
             'SMC Outside', 'Varsity', 'Victoria Outside', 'Woodsworth Outside',
             'Back Campus', 'Front Campus', 'Outside Student Union']
QUESTIONS = ['Show all or only buildings with Libraries?', 'Range lowest:', 'Range highest:',
             'Search terms:', 'What sort? Alphabetic/Persons ' + \
             'Count(least/most)/Best Wifi/Relative to search?']


def pages(data, page):
    urllib.request.urlretrieve(URL + PAGES[page], 'TemporaryFiles\\temp' + str(page) + '.txt')

    # Give a progress bar
    #print('Page: ' + str(page + 1) + '/' + str(len(PAGES)))

    file = open(DIRECTORY + str(page) + '.txt', 'r')
    for lines in file:
        if lines[:13] != '<BODY BGCOLOR': pass
        else:
            start = lines.find('<BQ>') + 4  # GETS TOTAL CONNECTIONS
            connections = int(lines[start:lines.find('<P>',start)])

            avg = lines.find('P>A', start)  # Finds avg connections

            if avg != -1:
                avg = float(lines[lines.find(':', avg) + 2:lines.find('<P>',avg)])
            else: avg = 0

            data.append([BUILDINGS[page], connections, avg])  # Puts stuff into list

    file.close()
    remove(DIRECTORY + str(page) + '.txt')


def connections(data, threads):  ### IN FINAL VERSION MAKE THIS PUSH FROM MAIN SERVER ONLY NEEDED DATA
    import threading

    if not exists('TemporaryFiles'):
        mkdir('TemporaryFiles')

    for page in range(len(PAGES)):
        # Makes threads galore
        t = threading.Thread(target=pages, args=(data, page))
        t.daemon = True
        t.start()
        threads.append(t)


    urllib.request.urlretrieve('http://maps.wireless.utoronto.ca/stg/index.php', 'TemporaryFiles\\temp.txt')
    file = open(DIRECTORY + '.txt', 'r')
    total = 0

    for lines in file:  # Get total
        if lines.find('Current Connections ') != -1:
            total = int(lines[lines.find('Current Connections ')+20:lines.find('</font>')])
    file.close()

    remove(DIRECTORY + '.txt')

    return total


def answers():
    answers = []
    for question in QUESTIONS:
        answers.append(input(question + ' \n'))  # Gets all the answers to each question
        ### IMPLEMENT NEAREST TO ME
    return answers
