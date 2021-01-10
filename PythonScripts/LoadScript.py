# *************************************************************************
# Desc: Load to MongoDB Script transformed data with TransformScript.py
# Change Log: When,Who,What
# 2020-05-24, Emilija Dimikj, Created file and functions
# *************************************************************************


import TransformScript
import ReportScript
import pymongo


def getMongoConnectionStr():
    # strConn = 'mongodb://localhost:27017'
    strConn="mongodb+srv://admin:Bothell2018@cluster0-yogcb.azure.mongodb.net/test?retryWrites=true&w=majority"
    try:
        objCon = pymongo.MongoClient(strConn)
        return strConn
    except Exception as ex:
        print(ex)
        return str(ex)


def Load2Mongo():
    strConn = getMongoConnectionStr()
    try:
        objConn = pymongo.MongoClient(strConn)

        db = objConn['ClientAccountBalances']
        if db['ClientBalancesData'].drop():
            print('Collection ClientBalancesData dropped')
        objColl = db['ClientBalancesData']

        ClientBalancesTable = TransformScript.JoinCustomerAndAccount()
        objColl.insert_many(ClientBalancesTable)
        print('Inserted ' + str(len(ClientBalancesTable)) + ' docs.')
        return len(ClientBalancesTable)
    except Exception as ex:
        print(ex)
        return str(ex)


def startETLprocess():
    retVal = Load2Mongo()
    print(type(retVal) == int)
    if type(retVal) == int:
        ReportScript.CreateReport()
    else:
        ReportScript.CreateErrorReport(retVal)
    print('ETL report was created!')


startETLprocess()
