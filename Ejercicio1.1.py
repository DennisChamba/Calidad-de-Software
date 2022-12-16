class Month:
    def __init__(self, name:str, days:int):
        self.name = name
        self.days = days

def showday ( daynumber:int, isleapyear:bool):

    """
    Muestra el mes y día dentro del mes del número de día del año.
    daynumber: número de día del año.
    isleapyear: Verdadero si el año es bisiesto.
    """
    months = [ "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" ]
    days = [ 31 for x in months ]
    thirtylist = ( "Abril", "Junio","Septiembre", "Noviembre" )
    for j in [ months.index(k) for k in thirtylist]:
        days[j] = 30
    # Considerar año bisiesto days[months.index("Febrero")] = \28 + ((isleapyear and 1) or 0)
    days[months.index("Febrero")] = 29 if isleapyear else 28

    """
    daymap contiene 12 objetos Month, cada uno de los cuales tiene un part nombre/días.
    """
    daymap = [ ]

    for i in range(len(months)):
        newMonth = Month(months[i], days[i])
        daymap.append(newMonth)

    if daynumber > 0 and daynumber <= 366:
        for el in daymap:
            if daynumber <= el.days:
                print (el.name, daynumber)
                return
            daynumber = daynumber - el.days
    else:
        raise ValueError("daynumber")

print("showday(1,False) ->",end="")
showday(1,False)
print("showday(32,False) ->",end="")
showday(32,False)
print("showday(60,True) ->",end="")
showday(60,True)
print("showday(366,True) ->",end="")
showday(366,True)
print("showday(369,True) ->",end="")
showday(369,True) 
