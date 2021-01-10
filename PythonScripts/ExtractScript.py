# *************************************************************************
# Desc: Extracting data from Excel and Txt file
# Change Log: When,Who,What
# 2020-05-24, Emilija Dimikj, Created file and functions
# *************************************************************************


import pyexcel as pe


def CustomersFile():
    CustomerTable = []
    with open("..SourceData/Customer.txt", 'r') as cf:
        header_line = [next(cf) for x in range(1)]
        line = cf.readline()
        while line != '':
            spLine = line.split('\t')
            dicData = {'CustomerId': spLine[0],
                       'CustomerTag': spLine[1],
                       'FirstName': spLine[2],
                       'MiddleName': spLine[3],
                       'LastName': spLine[4],
                       'EmailAddress': spLine[24],
                       'ResidenceCity': spLine[36],
                       'ResidenceState': spLine[37],
                       'ResidencePostalCode': spLine[38],
                       'ResidenceCountry': spLine[39]}
            CustomerTable.append(dicData)
            line = cf.readline()
    print('CustomersFile returned ' + str(len(CustomerTable)) + ' rows')
    return CustomerTable


def AccountBalancesFile():
    AccountBalancesTable = []
    with open("../SourceData/AccountBalances.txt", 'r') as abf:
        header_line = [next(abf) for x in range(1)]
        effectiveDate = header_line[0][95:129].strip()
        # ab = {}
        line = abf.readline()
        while line != '':
            dicData = {'CustomerId': line[0:10],
                       'AccountId': line[60:70],
                       'AccountNumber': line[170:220].strip(),
                       'AccountType': line[220:270].strip(),
                       'AccountBalance': line[320:335],
                       'EffectiveDate': effectiveDate,
                       'IsPrimary': line[575:576],
                       'PrimaryCustomerId': line[576:586]}
            AccountBalancesTable.append(dicData)
            line = abf.readline()
    print('AccountBalancesFile returned ' + str(len(AccountBalancesTable)) + ' rows')
    return AccountBalancesTable


def CustomersXLSFile():
    CustomerTable = []
    xlsFileName = "../SourceData/Customer.xlsx"
    CustomerRecords = pe.get_records(file_name=xlsFileName)
    pe.free_resources()

    for c in CustomerRecords:
        dicData = {'CustomerId': c['CustomerId'],
                   'CustomerTag': c['CustomerTag'],
                   'FirstName': c['FirstName'],
                   'MiddleName': c['MiddleName'],
                   'LastName': c['LastName'],
                   'EmailAddress': c['EmailAddress'],
                   'ResidenceCity': c['ResidenceCity'],
                   'ResidenceState': c['ResidenceState'],
                   'ResidencePostalCode': c['ResidencePostalCode'],
                   'ResidenceCountry': c['ResidenceCountry']}
        CustomerTable.append(dicData)
    print('CustomersXLSFile returned ' + str(len(CustomerTable)) + ' rows')
    return CustomerTable
