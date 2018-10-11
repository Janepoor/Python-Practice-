
# “Jan 1st 2019” -》“2019-01-01”

# YYYY-MM-DD

def ref(s):

    month_map = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
                 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

    if s == None or len(s) ==0:
        return -1

    day, month, year = s.split(' ')

    day_number = "".join([i for i in day if i.isdigit()])
    day_number = '0' + day_number if len(day_number) == 1 else day_number
    month_number = month_map.get(month)
    res = year + '-' + month_number + '-' + day_number
    print(res)
    return res


ref('1st Mar 1984')
ref('31st Feb 1984')