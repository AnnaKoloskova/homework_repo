#Задача 1
#https://www.codewars.com/kata/568dc014440f03b13900001d


def get_drink_by_profession(param):

    newparam = param.lower()
    
    if newparam == 'jabroni':
        return 'Patron Tequila'
    elif newparam == 'school counselor':
        return 'Anything with Alcohol'
    elif newparam == 'programmer':
        return 'Hipster Craft Beer'
    elif newparam == 'bike gang member':
        return "Moonshine"
    elif newparam == 'politician':
        return "Your tax dollars"
    elif newparam == "rapper":
        return "Cristal"
    else:
        return "Beer"

#  Забавная задача)
