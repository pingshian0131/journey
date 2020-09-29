from models import Sche

class json_carousel ():
    def __init__ (self, ):
        datas = Sche.query.all()
        day = []
        for data in datas:
            if data.day in day: continue
            day.append(data.day)
        days, date, time, title, dest, location, MoreInfo = [], [], [], [], [], [], []
        for i in range (max(day)):
            datas = Sche.query.filter(Sche.day==(i+1)).all()
            for data in datas:
                days.append(data.day)
                date.append(data.date)
                time.append(data.time)
                title.append(data.title)
                dest.append(data.dest)
                location.append(data.location)
                MoreInfo.append(data.MoreInfo)
        self.day = day
        self.date = date
        self.time = time
        self.title = title
        self.dest = dest
        self.location = location
        self.MoreInfo = MoreInfo

    def make_time_box (day):
        data = Sche.query.filter(Sche.day==day).first()
        ## data.uid
        json = ''
        for i in range (data.uid, data.uid+self.day.count(day)):
            tmp = '''{
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "''' + self.time[i] + '''",
            "size": "sm",
            "gravity": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "filler"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "corner_radius": "30px",
                "height": "12px",
                "width": "12px",
                "border_color": "#6486E3",
                "border_width": "2px"
              },
              {
                "type": "filler"
              }
            ],
            "flex": 0
          },
          {
            "type": "text",
            "text": "''' + self.dest[i] + '''",
            "gravity": "center",
            "flex": 4,
            "size": "sm",
            "action": {
              "type": "postback",
              "label": "action",
              "data": "date=''' + self.date[i] + '''&time=''' + self.time[i] + '''"
            }
          }
        ],
        "spacing": "lg",
        "corner_radius": "30px",
        "margin": "xl"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "filler"
              }
            ],
            "flex": 1
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "filler"
                      }
                    ],
                    "width": "2px",
                    "background_color": "#6486E3"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "flex": 1
              }
            ],
            "width": "12px"
          },
          {
            "type": "text",
            "text": "''' + self.location[i] + '''",
            "gravity": "center",
            "flex": 4,
            "size": "xs",
            "wrap": true,
            "color": "#b7b7b7"
          }
        ],
        "spacing": "lg",
        "height": "50px"
      },'''
            json += tmp
        return json

    def make_bubble ():
        for i in range (self.day):
            tmp = '''{
  "type": "bubble",
  "size": "giga",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Day''' + str(i+1) + '''",
            "color": "#FF0000",
            "size": "sm",
            "align": "start"
          },
          {
            "type": "text",
            "text": "''' + self.title[i] + '''",
            "color": "#FF0000",
            "size": "xl",
            "flex": 3,
            "wrap": true
          },
          {
            "type": "text",
            "text": "''' + self.date[i] + '''",
            "color": "#FF0000",
            "size": "sm",
            "align": "end",
            "gravity": "center",
            "flex": 1
          }
        ]
      }
    ],
    "padding_all": "20px",
    "spacing": "md",
    "padding_top": "22px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "Time",
            "size": "sm",
            "gravity": "center",
            "flex": 2
          },
          {
            "type": "filler",
            "flex": 1
          },
          {
            "type": "text",
            "text": "Schedule: Press and See More Info",
            "gravity": "center",
            "flex": 6,
            "size": "sm",
            "wrap": true
          }
        ],
        "spacing": "lg",
        "corner_radius": "30px",
        "margin": "xl"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "filler"
          }
        ],
        "height": "2px",
        "background_color": "#ACD6FF",
        "margin": "lg"
      },''' + self.make_time_box() + '''
      {
        "type": "text",
        "text": "Total: '''+ self.+''' hour",
        "color": "#b7b7b7",
        "size": "xs",
        "align": "end"
      }
    ]
  },
  "styles": {
    "header": {
      "background_color": "#ECF5FF"
    }
  }
}'''


    def make_json ():
        json = '''{
  "type": "carousel",
  "contents": [''' + self.make_bubble() + '''
  ]
}'''
        return json
