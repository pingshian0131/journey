

def make_json():
    json = '''{
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
            "text": "Day1",
            "color": "#FF0000",
            "size": "sm",
            "align": "start"
          },
          {
            "type": "text",
            "text": "桃園機場→關西機場→Millennials",
            "color": "#FF0000",
            "size": "xl",
            "flex": 3,
            "wrap": true
          },
          {
            "type": "text",
            "text": "09/22",
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
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "1100",
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
            "text": "交通",
            "gravity": "center",
            "flex": 4,
            "size": "sm",
            "action": {
              "type": "postback",
              "label": "action",
              "data": "date=1206&time=1100"
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
            "text": "桃園捷運：台北→桃園國際機場第二航廈",
            "gravity": "center",
            "flex": 4,
            "size": "xs",
            "wrap": true,
            "color": "#b7b7b7"
          }
        ],
        "spacing": "lg",
        "height": "50px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "1220",
                "gravity": "center",
                "size": "sm"
              }
            ],
            "flex": 1
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
                "width": "12px",
                "height": "12px",
                "border_width": "2px",
                "border_color": "#6486E3"
              },
              {
                "type": "filler"
              }
            ],
            "flex": 0
          },
          {
            "type": "text",
            "text": "報到",
            "gravity": "center",
            "flex": 4,
            "size": "sm",
            "action": {
              "type": "postback",
              "label": "action",
              "data": "date=1206&time=1220"
            }
          }
        ],
        "spacing": "lg",
        "corner_radius": "30px"
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
            "text": "桃園國際機場第二航廈",
            "gravity": "center",
            "flex": 4,
            "size": "xs",
            "wrap": true,
            "color": "#b7b7b7"
          }
        ],
        "spacing": "lg",
        "height": "50px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "1420",
            "gravity": "center",
            "size": "sm",
            "color": "#BE77FF"
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
                "width": "12px",
                "height": "12px",
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
            "text": "交通 180min",
            "gravity": "center",
            "flex": 4,
            "size": "sm",
            "color": "#BE77FF",
            "action": {
              "type": "postback",
              "label": "action",
              "data": "date=1206&time=1420"
            }
          }
        ],
        "spacing": "lg",
        "corner_radius": "30px"
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
            "text": "中華航空-C0123",
            "gravity": "center",
            "flex": 4,
            "size": "xs",
            "wrap": true,
            "color": "#b7b7b7"
          }
        ],
        "spacing": "lg",
        "height": "50px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "1750",
            "gravity": "center",
            "size": "sm"
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
                "width": "12px",
                "height": "12px",
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
            "text": "入境",
            "gravity": "center",
            "flex": 4,
            "size": "sm",
            "action": {
              "type": "postback",
              "label": "action",
              "data": "date=1206&time=1750"
            }
          }
        ],
        "spacing": "lg",
        "corner_radius": "30px"
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
            "text": "日本關西國際機場T1",
            "gravity": "center",
            "flex": 4,
            "size": "xs",
            "wrap": true,
            "color": "#b7b7b7"
          }
        ],
        "spacing": "lg",
        "height": "50px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "1900",
            "gravity": "center",
            "size": "sm",
            "color": "#BE77FF"
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
                "width": "12px",
                "height": "12px",
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
            "text": "交通 120min",
            "gravity": "center",
            "flex": 4,
            "size": "sm",
            "color": "#BE77FF",
            "action": {
              "type": "postback",
              "label": "action",
              "data": "date=1206&time=1900"
            }
          }
        ],
        "spacing": "lg",
        "corner_radius": "30px"
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
            "text": "京都市區利木津巴士車票：三條京阪or京都市役所前",
            "gravity": "center",
            "flex": 4,
            "size": "xs",
            "wrap": true,
            "color": "#b7b7b7"
          }
        ],
        "spacing": "lg",
        "height": "50px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "2200",
            "gravity": "center",
            "size": "sm"
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
                "width": "12px",
                "height": "12px",
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
            "text": "抵達民宿",
            "gravity": "center",
            "flex": 4,
            "size": "sm",
            "action": {
              "type": "postback",
              "label": "action",
              "data": "date=1206&time=2200"
            }
          }
        ],
        "spacing": "lg",
        "corner_radius": "30px"
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
            "text": "京都Millennials旅館 (The Millennials Kyoto)",
            "gravity": "center",
            "flex": 4,
            "size": "xs",
            "wrap": true,
            "color": "#b7b7b7"
          }
        ],
        "spacing": "lg",
        "height": "50px"
      },
      {
        "type": "text",
        "text": "Total: 11 hour",
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
    return json
