import json
from flask import Flask, request, abort 
from linebot import ( 
    LineBotApi, WebhookHandler
)
from linebot.exceptions import ( 
    InvalidSignatureError
)
from linebot.models import * 


app = Flask(__name__)
# LINE BOT info
line_bot_api = LineBotApi('K11XiWgF5NBZv0USayva/YIKBb113lmSKhN+OerY4kaMAxZESuEN7KMBeH3G/BYeKoQHau93HTYA+N273YMXjpGl61v/zqeSgkjTGvxEV0snBZnVqt8Jj/bwKCsa5/TpPQFmPM0s4kGrf/WHT7qA+gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8424b9ebd908ee4e06d274494d2cd0b8')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# Message event
@handler.add(MessageEvent) 
def handle_message(event):
    message_type = event.message.type
    user_id = event.source.user_id
    reply_token = event.reply_token
    message = event.message.text
    if(message == '常見問題'):
        FlexMessage = json.load(open('pa.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('常見問題',FlexMessage))
    if(message == '清潔保養'):
        FlexMessage = json.load(open('card.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('清潔保養',FlexMessage))
    if(message == '工序常見問題'):
        FlexMessage = json.load(open('fix.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('工序常見問題',FlexMessage))
    if(message == '浮動感/空心聲'):
        FlexMessage = json.load(open('sound.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('浮動感/空心聲',FlexMessage))
    if(message == '我要報修'):
        FlexMessage = json.load(open('report.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('我要報修',FlexMessage))
    if(message == '預約客服人員服務'):
        FlexMessage = json.load(open('cust.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('預約客服人員服務',FlexMessage))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)