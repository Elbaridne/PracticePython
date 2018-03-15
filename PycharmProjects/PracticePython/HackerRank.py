def timeConversion(s):
    spl = s.split(':')
    ampm = spl[-1].rstrip('AMPM')
    am, pm = "AM", "PM"
    if am in s:
        if spl[0] == '12':
            spl[0] = '00'

    else:
        if spl[0] != '12':
            spl[0] = int(spl[0]) + 12
    return "{0}:{1}:{2}".format(spl[0], spl[1], ampm)


s = input().strip()
result = timeConversion(s)
print(result)