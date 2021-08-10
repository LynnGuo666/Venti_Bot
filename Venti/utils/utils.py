from Venti.constant import ERROR_CARD


def get_error_card(e: BaseException) -> list:
    error_card = ERROR_CARD.copy()
    error_card[0]['modules'][1]['text']['content'] = '错误信息： ' + ' '.join(e.args)
    return error_card
