import requests
from logging import Logger
from venti.constant import KUWO_API_URL


def mvsearch_kuwo(keyword: str, logger: Logger) -> list:
    logger.info(f"Searching {keyword}...")
    # 获取歌曲信息并取第一个结果
    r = requests.get(f"{KUWO_API_URL}/kuwo/search/searchMusicBykeyWord?key={keyword}").json()
    rid = r['data']['list'][0]['rid']
    title = r['data']['list'][0]['name']
    artist_name = r['data']['list'][0]['artist']
    pic = r['data']['list'][0]['pic']
    # 获取MV播放Url
    r = requests.get(f"{KUWO_API_URL}/kuwo/mv_url?rid={rid}").json()
    src = r['url']
    logger.info(f'Result {title}')
    return [{
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
    }]
