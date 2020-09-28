from flask import Blueprint, request, current_app, redirect, url_for, render_template
from datetime import datetime
from models import users, Sche
from sqlalchemy import func , or_
from main import db, app
from line_bot_api import *
from json_data import timeline as tl 
from libs import sche_post
import sqlite3
import json

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(FollowEvent)
def handle_follow(event):
    user_id = event.source.user_id
#    if user_id != 'U1967dc58bc86ac7a20849717ea7c1b69':
#        line_bot_api.reply_message (event.reply_token , TextSendMessage (text = "您沒有權限喔！"))
#        return 0
    profile = line_bot_api.get_profile(user_id) 
    print ("user_id = " + user_id) 
    print(profile.display_name)
    print("======")
    newcoming_text = profile.display_name + " 您好，\n歡迎使用芥菜種會專管小幫手，請使用手機操作下方服務選單說明。"
    newcoming_text2 = "如在操作上有問題或仍無法解決您的疑問，請直接私訊社工，感謝您的耐心。"
    text = [TextSendMessage (text = newcoming_text) , TextSendMessage (text = newcoming_text2)]
    insert_data = users(
            userid=user_id,
            display_name=profile.display_name)
    insert_data.new_user()
    line_bot_api.link_rich_menu_to_user (user_id , "richmenu-8190b65e54fd3261bbd9d33dc951d1fe") 

    line_bot_api.reply_message(event.reply_token, text )

@handler.add(PostbackEvent)
def handle_post_message(event):
    print ("event =" , event)
    date, time = event.postback.data.split('&')
    more_data = sche_post.main(date.split('=')[1], time.split('=')[1])

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=more_data))

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    profile = line_bot_api.get_profile(user_id) 
    insert_data = users(userid=user_id, display_name=profile.display_name)
    insert_data.new_user()
   
    if event.message.text == '社工專用':
        text = "✴️ 查詢教會信件：請輸入'信件查詢A'\n✴️ 查詢教會帳號密碼：請輸入'帳號密碼'\n✴️ 查詢北區服務中心地址：請輸入'交通資訊'。\n✴️ 物資登記相關說明：請輸入'物資相關說明'"
        line_bot_api.reply_message (event.reply_token , TextSendMessage (text = text))
    elif event.message.text == 'timeline':
#        flex = t.main()
        flex = tl.make_json()
        with open ('tmp.txt', 'w', encoding='utf-8') as f:
            f.write(flex)
        parsed_json = json.loads(flex)
        message = FlexSendMessage(
            alt_text='timeline_sample',
            contents=parsed_json,
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == 'cat':
        flex = cl_trans.main()
#        with open ('tmp.txt', 'w', encoding='utf-8') as f:
#            f.write(flex)
        parsed_json = json.loads(flex)
        message = FlexSendMessage(
            alt_text='cat',
            contents=parsed_json,
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == '搜尋類別':
        pass

    elif event.message.text == '搜尋任務':
        pass

    elif event.message.text == '個案管理p.1':
        line_bot_api.link_rich_menu_to_user (user_id , "richmenu-84d7f90887b1ece1eb2c2c7d6d7985b0")
    elif event.message.text == '個案管理p.2':
        line_bot_api.link_rich_menu_to_user (user_id , "richmenu-cc77b263b47bbdedf9076ec937ef13e2")
    elif event.message.text == '回到首頁':
        line_bot_api.link_rich_menu_to_user (user_id , "richmenu-8190b65e54fd3261bbd9d33dc951d1fe") 
    elif event.message.text == '信件通知推播':
        user = users.query.filter(users.Userid == user_id).first()
        if user.State == 2:
            user.State = 4
            db.session.commit()
            line_bot_api.reply_message (event.reply_token , TextSendMessage (text = '請輸入密碼： '))

