VERSION = 'Thyme Pre-Release 1.1'
NETEASE_API_URL = 'http://cloud-music.pl-fe.cn'
HELP_CARD = [
  {
    "type": "card",
    "theme": "secondary",
    "size": "lg",
    "modules": [
      {
        "type": "header",
        "text": {
          "type": "plain-text",
          "content": "Venti Bot - 帮助"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": "全天下最好的吟游诗人来啦~"
        }
      },
      {
        "type": "divider"
      },
      {
        "type": "section",
        "text": {
          "type": "kmarkdown",
          "content": "**指令列表：**"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "paragraph",
          "cols": 2,
          "fields": [
            {
              "type": "kmarkdown",
              "content": "获得帮助:\n点歌:"
            },
            {
              "type": "kmarkdown",
              "content": "=h\n=s `歌曲名称/歌曲ID`"
            }
          ]
        }
      },
      {
        "type": "divider"
      },
      {
        "type": "section",
        "text": {
          "type": "kmarkdown",
          "content": "**开发人员：**"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": "Guang_Chen_#8351\nBaobob_Lynn#3266"
        }
      },
      {
        "type": "divider"
      },
      {
        "type": "context",
        "elements": [
          {
            "type": "plain-text",
            "content": "歌曲版权归网易云所有，因使用该软件所导致的法律问题，开发人员概不负责\n当前版本号：{}".format(VERSION)
          }
        ]
      }
    ]
  }
]
ERROR_CARD = [
  {
    "type": "card",
    "theme": "secondary",
    "size": "lg",
    "modules": [
      {
        "type": "header",
        "text": {
          "type": "plain-text",
          "content": "出现异常，请联系开发者处理"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "kmarkdown",
          "content": "STR"
        }
      }
    ]
  }
]
EMPTY_WARN = [
  {
    "type": "card",
    "theme": "secondary",
    "size": "lg",
    "modules": [
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": "搜索关键词不能为空哦~"
        }
      }
    ]
  }
]
