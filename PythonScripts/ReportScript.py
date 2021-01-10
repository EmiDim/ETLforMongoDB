# *************************************************************************
# Desc: Functions for HTML Report generaton
# Change Log: When,Who,What
# 2020-05-25, Emilija Dimikj, Created file and functions
# *************************************************************************

from datetime import datetime as dt
import TransformScript


def createHTMLtable(tableList, caption, color):
    table: str = "<table style='border:1px solid black; background-color:" + color + "'>\n"
    table += "<caption style='font-weight: bold; font-size: 20px;' >" + caption + "</caption>\n"
    table += '<tr>\n'
    for k in tableList[0].keys():
        table += '<th>' + k + '</th>'
    table += '</tr>\n'

    table += "  <tr>\n"
    for row in tableList:
        for k in row.keys():
            table += '<td>' + str(row[k]) + '</td>\n'
        table += '</tr>\n'

    table += '\t</table>\n'
    return table



def CreateReport():
    strTitle = "ETL Process Page"
    # Start the page
    strContent = '''
      <html>
        <head>
          <title>''' + strTitle + '''</title> 
        </head>  
        <body>\n'''

    # Add content to the body
    strContent += createHTMLtable(TransformScript.TransformCustomers(), 'Customers Data', '#D4E6F1')
    strContent += '<hr>'

    strContent += createHTMLtable(TransformScript.TransformAccountBalances(), 'Account Balances Data', '#FADBD8')
    strContent += '<hr>'

    strContent += createHTMLtable(TransformScript.JoinCustomerAndAccount(), "Customer's Account Balances data", '#E7E1E5')
    strContent += '<hr>'

    strContent += "\t<table style='border:1px solid black; background-color:#E5E7E9;'>\n"
    strContent += "\t\t<tr><th>ETL Process</th><th>DateTime</th><th>Status</th></tr>\n"
    strContent += '\t\t<tr><td>Convert To HTML</td><td>' + str(dt.now()) + '</td><td>Success</td></tr>\n'
    strContent += '\t</table>\n'

    # Close the body and end the file
    strContent += '''    </body>
      </html>
      '''

    # Save the HTML code
    objFile = open('../Reports/ETLReport.html', 'w')
    objFile.write(strContent)
    objFile.close()


def CreateErrorReport(error):
    strTitle = "ETL Process Page"
    # Start the page
    strContent = '''
          <html>
            <head>
              <title>''' + strTitle + '''</title> 
            </head>  
            <body>\n'''
    strContent += "<p style='color:red;font-weight: bold; font-size: 20px;'>ERROR: " + str(error) + "</p>\n"
    strContent += '<hr>'

    strContent += "<table style='border:1px solid black; background-color:#E5E7E9;'>\n"
    strContent += "<tr><th>ETL Process</th><th>DateTime</th><th>Status</th></tr>\n"
    strContent += "<tr><td>Customer's Account Balances</td><td>" + str(dt.now()) + '</td><td>Failure</td></tr>\n'
    strContent += '</table>\n'

    # Close the body and end the file
    strContent += '''    </body>
          </html>
          '''

    # Save the HTML code
    objFile = open('../Reports/ETLReport.html', 'w')
    objFile.write(strContent)
    objFile.close()

