import json
import urllib.request
import os
import datetime as dt
import locale
import random
def omikuzi():
    luck = random.randint(1,100)
    if luck <= 5: ret = """
    超スーパーウルトラアルティメットをさらに超越した大々々々々々・・・\n・\n・\n\n
    （女神の声）・・・なんと・・・ついにこの運命を受け入れるものが現れましたか，
    良いですか，人の子よ．よく聞きなさい．そなたは・・・\n・\n・\n\n
    """+omikuzi()
    elif luck <= 40: ret = "凶"
    elif luck <= 80: ret = "吉"
    elif luck <= 94: ret = "中吉"
    elif luck <= 97: ret = "大吉"
    else: ret = "大凶"
    return ret

region = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
def lambda_handler(event, context):
    for message_event in json.loads(event['body'])['events']:
        url = 'https://api.line.me/v2/bot/message/reply'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + region
                  }
        if "こんにちは" in message_event['message']['text'] :
            body = {
                'replyToken': message_event['replyToken'],
                'messages': [
                    {
                        "type": "text",
                        "text": "Test OK",
                    }
                ]
            }
        elif "今日" in message_event['message']['text'] and "曜日" in message_event['message']['text'] :
            locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
            date_today =  dt.date.today()
            # date_today = date_today.replace("-", ",")
            # ans = str(date_today)
            ans = date_today.strftime('%A')
            # ans = dt.date(int(date_today)).strftime('%A')
            body = {
                'replyToken': message_event['replyToken'],
                'messages': [
                    {
                        "type": "text",
                        "text": "今日は" + ans + "です！",
                    }
                ]
            }
        elif "ごみ" in message_event['message']['text'] :
            today = dt.date.today() 
            tomorrow_date = today.weekday() + 1
            if tomorrow_date == 7:
                body = {
                'replyToken': message_event['replyToken'],
                'messages': [
                    {
                        "type": "text",
                        "text": "明日は月曜日です．\
                        燃やすごみの日なので，生ごみ，木くず，紙くず，製品プラスチック，ゴム，皮革製品などが捨てられます．",
                    }
                ]
            }
            elif tomorrow_date == 1:
                body = {
                'replyToken': message_event['replyToken'],
                'messages': [
                    {
                        "type": "text",
                        "text": "明日は火曜日です．\
                        資源ごみの日なので，ビン，かん，ペットボトル，発泡トレイ・スチロールが捨てられます．",
                    }
                ]
            }
            elif tomorrow_date == 2:
                body = {
                'replyToken': message_event['replyToken'],
                'messages': [
                    {
                        "type": "text",
                        "text": "明日は水曜日です．\
                        隔週で燃やさないごみの日なので，金属，ガラス，陶器などが捨てられます．",
                    }
                ]
            }
            elif tomorrow_date == 3:
                body = {
                'replyToken': message_event['replyToken'],
                'messages': [
                    {
                        "type": "text",
                        "text": "明日は木曜日です．\
                        燃やすごみの日なので，生ごみ，木くず，紙くず，製品プラスチック，ゴム，皮革製品などが捨てられます．",
                    }
                ]
            }
            elif tomorrow_date == 4:
                body = {
                'replyToken': message_event['replyToken'],
                'messages': [
                    {
                        "type": "text",
                        "text": "明日は金曜日です．\
                        ごみの収集はありません．",
                    }
                ]
            }
            elif tomorrow_date == 5:
                body = {
                'replyToken': message_event['replyToken'],
                'messages': [
                    {
                        "type": "text",
                        "text": "明日は土曜日です．\
                        容器包装プラスチックの日なのでプラマークのついたプラスチック製の容器包装が捨てられます．",
                    }
                ]
            }
            elif tomorrow_date == 6:
                body = {
                'replyToken': message_event['replyToken'],
                'messages': [
                    {
                        "type": "text",
                        "text": "明日は日曜日です．\
                        ごみの収集はありません．",
                    }
                ]
            }
                
            else:
                tomorrow_date = tomorrow_date
                ans = tomorrow_date
                body = {
                    'replyToken': message_event['replyToken'],
                    'messages': [
                        {
                            "type": "text",
                            "text": ans,
                        }
                    ]
                }
        
        elif "さとし" in message_event['message']['text']:
            if len(message_event['message']['text'].split())>1 and all('0'<=c<="9" for c in message_event['message']['text'].split()[1]):
                stringsatoshi = "さとし"*min(int(message_event['message']['text'].split()[1]), 100)
                ret = ""
                while stringsatoshi:
                    ret += stringsatoshi[:19]+'\n'
                    stringsatoshi = stringsatoshi[19:]
                
                body = {
                    'replyToken': message_event['replyToken'],
                    'messages': [{
                        "type": "text",
                        "text": ret,
                    }]
                }
            else:
                body = {
                    'replyToken': message_event['replyToken'],
                    'messages': [{
                        "type": "text",
                        "text": "さとしの後には空白スペースを開けて数字を入力してください．",
                    }]
                }
        elif "おみくじ" in message_event['message']['text']:
            body = {
                    'replyToken': message_event['replyToken'],
                    'messages': [{
                        "type": "text",
                        "text": omikuzi()+"じゃ！！",
                    }]
                }
            
                
            
        else:          
            body = {
                'replyToken': message_event['replyToken'],
                'messages': [
                    {
                        "type": "text",
                        "text": message_event['message']['text'],
                    }
                ]
            }

        req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), method='POST', headers=headers)
        with urllib.request.urlopen(req) as res:
            logger.info(res.read().decode("utf-8"))


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }



