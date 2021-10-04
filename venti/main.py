from venti.modules.kuwo.mvsearch import mvsearch_kuwo
from khl import Cert, Bot, TextMsg
from venti.constant import HELP_CARD, EMPTY_WARN
from venti.utils.utils import get_error_card
from venti.modules.netease.search import search_netease
from venti.modules.kuwo.search import search_kuwo
from venti.modules.kuwo.play import play_kuwo

cert = Cert(client_id="", client_secret="", token="")
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


@bot.command("h")
async def help_txt(msg: TextMsg, *args):
    await msg.reply_card(HELP_CARD)


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


@bot.command("kwp")
async def search(msg: TextMsg, *args):
    if len(args) == 0:
        await msg.reply_card(EMPTY_WARN)
    else:
        keyword = ' '.join(args)
        try:
            card = play_kuwo(keyword, bot.logger)
        except Exception as e:
            card = get_error_card(e)
        await msg.reply_card(card)


@bot.command("kwmv")
async def mvsearch(msg: TextMsg, *args):
    if len(args) == 0:
        await msg.reply_card(EMPTY_WARN)
    else:
        keyword = ' '.join(args)
        try:
            card = mvsearch_kuwo(keyword, bot.logger)
        except Exception as e:
            card = get_error_card(e)
        await msg.reply_card(card)


def main():
    bot.run()


if __name__ == '__main__':
    main()
