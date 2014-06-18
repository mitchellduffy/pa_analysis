
### a set of methods to deal with Spanish language and translation issues

import datetime

def makedatetime(fecha):
    if len(fecha) != 7:
        sys.exit('Wrong number of items in fecha/date')


    month = 0
    mes = fecha[3]

    if mes == 'enero':
        month = 1
    elif mes == 'febrero':
        month = 2
    elif mes == 'marzo':
        month = 3
    elif mes == 'abril':
        month = 4
    elif mes == 'mayo':
        month = 5
    elif mes == 'junio':
        month = 6
    elif mes == 'julio':
        month = 7
    elif mes == 'agosto':
        month = 8
    elif mes == 'septiembre':
        month = 9
    elif mes == 'octubre':
        month = 10
    elif mes == 'noviembre':
        month = 11
    elif mes == 'diciembre':
        month = 12

    if month == 0:
        sys.exit('Incorrect spanish month spelling. No datetime could be produced. There is something wrong here!')

    t = fecha[6].split(':')

    dt = datetime.datetime(int(fecha[5]), month, int(fecha[1]), int(t[0]), int(t[1]), int(t[2]))

    return dt


