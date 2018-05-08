

def date_to_string(date):
    """
    :param date: xxxx-xx-xx xx:xx:xx
    :return:
    """
    run_month = ['1','3','5','7','8','10','12']

    date=date.split(' ')
    date_time = date[0]
    date_hosurs = date[1]
    day = date_time.split('-')[2]
    month = date_time.split('-')[1]
    year = date_time.split('-')[0]
    hour =date_hosurs.split(':')[0]
    minute = date_hosurs.split(':')[1]
    secounds = date_hosurs.split(':')[2]
    if int(hour)+8 < 24:
        hour = str(int(hour)+8)
    else:
        hour = str(int(hour)+8-24)
        day = str(int(day)+1)

        if month in run_month:
            if day > '31':
                day = '1'
                if month == '12':
                    year = str(int(year)+1)
                    month = '1'
                else:
                    month = str(int(month)+1)

        elif month == '2':
            if day >'28':
                month  = str(int(month)+1)
                day = '1'
        else:
            if day >'30':
                day ='1'
                if month == '12':
                    year = str(int(year)+1)
                    month = '1'
                else:
                    month =str(int(month)+1)

    return "%s-%s-%s %s:%s:%s" % (year,month,day,hour,minute,secounds)