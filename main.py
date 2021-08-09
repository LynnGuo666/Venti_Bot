from khl import Cert, Bot, TextMsg
from constant import *
import requests

cert = Cert(client_id="svxTmFJ6en21w3u_", client_secret="l5qOdVMcPWMYRN8w", token="1/MTA0MjQ=/vPhQGaO6vosmVg7vtrtE9Q==")
bot = Bot(cmd_prefix=['='], cert=cert)


@bot.command("s")
async def search(msg: TextMsg, *args):
    r = requests.get("http://cloud-music.pl-fe.cn/search?keywords={}&limit=1&offset=0&type=1".format(''.join(args))).json()
    bot.logger.info("Searching: {}".format(''.join(args)))
    sid = r['result']['songs'][0]['id']
    title = r['result']['songs'][0]['name']
    artist_name = r['result']['songs'][0]['artists'][0]['name']
    pic = r['result']['songs'][0]['artists'][0]['img1v1Url']
    r_ = requests.get("http://cloud-music.pl-fe.cn/song/url?id={}".format(sid)).json()
    src = r_['data'][0]['url']
    bot.logger.info("Result: {}".format(title))
    await msg.reply_card(
        [
            {
                "type": "card",
                "theme": "secondary",
                "size": "lg",
                "modules": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain-text",
                            "content": title
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "plain-text",
                            "content": artist_name
                        }
                    },
                    {
                        "type": "audio",
                        "title": title,
                        "src": src,
                        "cover": pic
                    }
                ]
            }
        ]
    )


@bot.command("h")
async def help_txt(msg: TextMsg, *args):
    await msg.reply_card(HELP_CARD)


bot.run()
