import urllib2

listOfStocks = ["AAPL", "MSFT", "GOOG", "FB", "AMZN"]

urls = []

for company in listOfStocks:
    urls.append(
        'http://real-chart.finance.yahoo.com/table.csv?s=' + company + '&d=6&e=28&f=2015&g=m&a=11&b=12&c=1980&ignore=.csv')

Output_File = open('C:/your_path_here/Data.csv', 'w')

New_Format_Data = ''

for counter in range(0, len(urls)):

    Original_Data = urllib2.urlopen(urls[counter]).read()

    if counter == 0:
        New_Format_Data = "Company," + urllib2.urlopen(urls[counter]).readline()

    rows = Original_Data.splitlines(1)

    for row in range(1, len(rows)):
        New_Format_Data = New_Format_Data + listOfStocks[counter] + ',' + rows[row]

Output_File.write(New_Format_Data)

Output_File.close()