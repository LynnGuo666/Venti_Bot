from Venti.constant import ERROR_CARD


def get_error_card(e: BaseException) -> list:
    error_card = ERROR_CARD.copy()
    error_card[0]['modules'][1]['text']['content'] = f'**{e.__class__.__name__}**: ' + \
                                                     f'{" ".join(e.args)} | ' + \
                                                     f'{e.__doc__}'

    return error_card
