import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

import pandas as pd
import warnings
import psycopg2
warnings.filterwarnings("ignore")

conn = psycopg2.connect(database="covid",
                        user='postgres', password='arnav1609', 
                        host='127.0.0.1', port='5432')
curr = conn.cursor()

curr.execute("SELECT state_name, COUNT (deaths) as dc from county_data group by state_name order by dc desc limit 3;")
data1 = curr.fetchall()
data1 = pd.DataFrame(data1)
data1
conn.close()

state1 = data1[0][0]
deaths1 = data1[1][0]
state2 = data1[0][1]
deaths2 = data1[1][1]
state3 = data1[0][2]
deaths3 = data1[1][2]

message = 'Top 3 states by the number of Covid deaths in US.' + ' ' + '1.'+ ' ' + str(state1) + ' ' + 'Deaths -' + ' ' + str(deaths1) + ' ' + '2.' + ' ' + str(state2) + ' ' + 'Deaths -' + ' ' + str(deaths2) + ' ' +'3.' + ' ' + str(state3) + ' '  + 'Deaths -' + ' ' + str(deaths3)

client.chat_postMessage(channel='#covid-data', text = message)