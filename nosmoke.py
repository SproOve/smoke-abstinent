from datetime import datetime, timedelta, date
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv
import subprocess as sp

os.system('mode con: cols=75 lines=2')

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

startDate = datetime.fromisoformat(os.getenv('startDate'))
weekendSmoking = os.getenv('weekendSmoking')

dayCigs = float(os.getenv('dayCigs'))
boxCost = int(os.getenv('boxCost'))
boxCount = int(os.getenv('boxCount'))


dayRate = dayCigs / boxCount * boxCost

hourRate = dayRate/24

def calculate():
    sp.call('cls', shell=True)
    today = datetime.today()
    delta = today - startDate
    nosmokingHours = delta.total_seconds()/3600
    if weekendSmoking == 'False':
        nosmokingHours = round(nosmokingHours/7 * 5)
    stringValue = "{:8.2f}".format(nosmokingHours*hourRate)
    print('Seit dem ' + str(startDate.date()) + ' gespartes Geld:' +  stringValue + ' €' )
    time.sleep(60)
    calculate()

calculate()
