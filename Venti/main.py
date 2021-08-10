from khl import Cert, Bot, TextMsg
from Venti.constant import HELP_CARD, EMPTY_WARN
from Venti.utils.utils import get_error_card
from Venti.modules.netease import search_netease
from Venti.modules.kuwo import search_kuwo


cert = Cert(client_id="svxTmFJ6en21w3u_", client_secret="l5qOdVMcPWMYRN8w", token="1/MTA0MjQ=/vPhQGaO6vosmVg7vtrtE9Q==")
bot = Bot(cmd_prefix=['='], cert=cert)


@bot.command("s")
async def search(msg: TextMsg, *args):
    if len(args) == 0:
        await msg.reply_card(EMPTY_WARN)
    else:
        keyword = ' '.join(args)
        try:
            card = search_netease(keyword, bot.logger)
        except Exception as e:
            card = get_error_card(e)
        await msg.reply_card(card)

@bot.command("kws")
async def search(msg: TextMsg, *args):
    if len(args) == 0:
        await msg.reply_card(EMPTY_WARN)
    else:
        keyword = ' '.join(args)
        try:
            card = search_kuwo(keyword, bot.logger)
        except Exception as e:
            card = get_error_card(e)
        await msg.reply_card(card)

@bot.command("h")
async def help_txt(msg: TextMsg, *args):
    await msg.reply_card(HELP_CARD)


def main():
    bot.run()


if __name__ == '__main__':
    main()
