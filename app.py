import logging
from vibora import Vibora, Request, Response
from vibora.responses import JsonResponse

from telegram.ext import Updater
import telegram

__version__ = "0.0.1"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#@upsmile_bot
# https://t.me/
app = Vibora()
bot = telegram.Bot(token=r'552921360:AAHPKp77QI6pn2RKaMLWmxrCsDeyDWfPzEE')
bot.send_message(chat_id='@upsmile', text="The bot-service successfully started.")

@app.route('/')
async def index():
    
    response =  JsonResponse({
        "name":"distributor.support.bot.host",
        "version": __version__})    
    bot.send_message(chat_id='@upsmile', text="distributor.support.bot.host")
    return response    


@app.route('/',methods=['POST'])
async def post(request: Request):                
    values = await request.stream.read()
    message = values.decode(encoding="utf8")
    logging.info(message)
    bot.send_message(chat_id='@upsmile', text=message)
    return Response(b'ok',status_code=200)   

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8083)