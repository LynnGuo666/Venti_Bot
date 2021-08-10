VERSION = 'Thyme 0.1.0.2'
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