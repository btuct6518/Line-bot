from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('BN/bvou6Es2Bsrf1xWB5t2Cngg/2KUTReqxU8zhfFnr7ZkDuckqkedodgS4EqHIqudQExpJClvrHbkJYc5AmXlGyfHvop8VKSAbfyyzUeHIsXA9QDRISpzTxeDTVS323BSLQ5czTixgLd5gAqJYpgAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a43e021247e7f845b0126ab717b7f9f6')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
    line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
    return

    r = '很抱歉，我不懂你說甚麼'
    if msg in ['hi', 'Hi']:
        r = '嗨'
    elif msg == '玉婕是笨蛋':
        r = '您真是聰明'
    elif '瑋杰' in msg:
        r = '你是想說瑋杰非常有天分嗎?'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()