# *************************************************************************
# Desc: Changing the data type for data read from a file
# Change Log: When,Who,What
# 2020-05-15,RRoot,Created Function
# 2020-05-24, Emilija DImikj, expanded boolean Y/N
# *************************************************************************

from datetime import datetime as dt


def string_to_type_or_none(data, target_type):
    if data == '':
        data = None
    elif target_type.lower() == 'date':
        data = dt.strptime(data, '%Y-%m-%d')
    elif target_type.lower() == 'int':
        data = int(data)
    elif target_type.lower() == 'float':
        data = float(data)
    elif target_type.lower() == 'boolean' and data.upper() == 'Y':
        data = True
    elif target_type.lower() == 'boolean' and data.upper() == 'N':
        data = False
    return data


