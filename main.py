import pandas as pd
import requests
import datetime

import time




while True:
    sheet_id = "1pCRRJhPY5xqBzY5esdhUrx8QQ4Ay0Mydwr5Wcn955pQ"
    
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

    df = pd.read_csv(url)
    df["Date"] = pd.to_datetime(df["Date"])
    df
    current_time = pd.datetime.now()
    
    print(pd.datetime.now().strftime('%H:%M:%S'))
    print(datetime.date.today())
    print(df["Date"].dt.date)
    
    
   
    
    
    df = df[(df["Date"].dt.strftime("%d-%m")==current_time.strftime("%d-%m"))&(pd.datetime.now().strftime('%H:%M')=='00:00')]
    
    


    def send_message(row):
        
        bot_id = "5427350839:AAGXCxTPWbstCKowANMfLa0vch4dB_qB5_A"
        chat_id = "2005025161"
        
        message="Its "+(row[0]+" Birthday")+" Send them the Best Wishes!!!"+"\n"+row[2]
        url = f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={message}"

        return requests.get(url).json()

    if not df.empty:
        df['status'] = df.apply(send_message, axis=1)

    time.sleep(60)
    
