import requests
from logging import Logger
from venti.constant import NETEASE_API_URL


def search_netease(keyword: str, logger: Logger) -> list:
    logger.info(f"Searching {keyword}...")
    # 获取歌曲信息并取第一个结果
    r = requests.get(f"{NETEASE_API_URL}/search?keywords={keyword}&limit=1&offset=0&type=1").json()
    sid = r['result']['songs'][0]['id']
    title = r['result']['songs'][0]['name']
    artist_name = r['result']['songs'][0]['artists'][0]['name']
    # 获取图片Url
    r = requests.get(f"{NETEASE_API_URL}/song/detail?ids={sid}").json()
    pic = r['songs'][0]['al']['picUrl']
    # 获取播放Url
    r = requests.get(f"{NETEASE_API_URL}/song/url?id={sid}").json()
    src = r['data'][0]['url']
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
