import time
import shutil
import requests
import os


def get_data(name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get('https://query1.finance.yahoo.com/v7/finance/download/' + name
                     + '?period1=1581609627&period2=1613232027&interval=1mo&events=history&includeAdjustedClose=true',
                     headers=headers)
    with open(str(name)+'.csv', 'wb') as f:
        f.write(r.content)
    f.close()
    download_folder = os.getcwd()
    print(download_folder)
    # download_folder = str('C:\\Users\\ASUS\\Downloads\\' + name + '.csv')
    source = str(download_folder)+'/'+str(name)+'.csv'
    destination = str(download_folder) + '/data/' + str(name) + '.csv'
    time.sleep(1)
    shutil.move(source, destination)


if __name__ == '__main__':
    name = 'DOGE-USD'
    get_data(name)
