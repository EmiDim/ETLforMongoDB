# *************************************************************************
# Desc: Transformation of data exctracted with ExtractScript.py
# Change Log: When,Who,What
# 2020-05-24, Emilija Dimikj, Created file and functions
# *************************************************************************

import ExtractScript
import CommonFuncScript
import re


def TransformCustomers():
    CustomersTable = []
    RegexStr = '^[0-9]{5}(?:-[0-9]{4})?$'
    CT = ExtractScript.CustomersXLSFile()
    for c in CT:
        FullName = c['FirstName'].strip()
        if c['MiddleName'].strip() != '':
            FullName += ' ' + c['MiddleName'].strip()
        FullName += ' ' + c['LastName'].strip()

        PostalCode = ''
        if c['ResidenceCountry'] == 'US':
            if re.match(RegexStr, str(c['ResidencePostalCode'])):
                PostalCode = c['ResidencePostalCode']
            else:
                PostalCode = None
        dicData = {'CustomerId': CommonFuncScript.string_to_type_or_none(c['CustomerId'], 'int'),
                   'CustomerFullName': FullName,
                   'EmailAddress': c['EmailAddress'].strip(),
                   'ResidenceCity': c['ResidenceCity'],
                   'ResidenceState': c['ResidenceState'].strip(),
                   'ResidencePostalCode': PostalCode,
                   'ResidenceCountry': c['ResidenceCountry'].strip()}
        CustomersTable.append(dicData)
    return CustomersTable


def TransformAccountBalances():
    BalancesTable = []
    ABT = ExtractScript.AccountBalancesFile()
    for ab in ABT:
        dicData = {'CustomerId': CommonFuncScript.string_to_type_or_none(ab['CustomerId'], 'int'),
                   'AccountId': CommonFuncScript.string_to_type_or_none(ab['AccountId'], 'int'),
                   'AccountNumber': ab['AccountNumber'],
                   'AccountType': ab['AccountType'],
                   'AccountBalance': CommonFuncScript.string_to_type_or_none(ab['AccountBalance'][0:13] + '.' + ab['AccountBalance'][13:15], 'float'),
                   'EffectiveDate': CommonFuncScript.string_to_type_or_none(ab['EffectiveDate'][0:10], 'date'),
                   'IsPrimary': CommonFuncScript.string_to_type_or_none(ab['IsPrimary'],'boolean'),
                   'PrimaryCustomerId': CommonFuncScript.string_to_type_or_none(ab['PrimaryCustomerId'], 'int')}
        BalancesTable.append(dicData)
    return BalancesTable


def JoinCustomerAndAccount():
    CustomersTable = TransformCustomers()
    AccountTable = TransformAccountBalances()
    FinalDataTable = []
    for ab in AccountTable:
        for c in CustomersTable:
            if c['CustomerId'] == ab['CustomerId']:
                dicData = {'CustomerId': ab['CustomerId'],
                           'CustomerFullName': c['CustomerFullName'],
                           'EmailAddress': c['EmailAddress'],
                           'ResidenceCity': c['ResidenceCity'],
                           'ResidenceState': c['ResidenceState'],
                           'ResidencePostalCode': c['ResidencePostalCode'],
                           'ResidenceCountry': c['ResidenceCountry'],
                           'AccountNumber': ab['AccountNumber'],
                           'AccountType': ab['AccountType'],
                           'AccountBalance': ab['AccountBalance'],
                           'EffectiveDate': ab['EffectiveDate']}
                FinalDataTable.append(dicData)
    return FinalDataTable



