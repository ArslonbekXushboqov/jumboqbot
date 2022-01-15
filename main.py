import telebot
import requests as r
import sqlite3 as sql
import time
from buttons import *
from strings import *

dbfile = "userdata.db"
admin=1883949853

logs_channel = "@jumlogs1"

with sql.connect(dbfile) as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXiSTS users(
        id INTEGER, 
        name TEXT, 
        javob TEXT, 
        urinishlar INTEGER, 
        topilganlar INTEGER,
        rasm TEXT)''')
        con.commit()

def insert(userid, name, javob, urinishlar, topilganlar,rasm):
    con= sql.connect(dbfile)
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?",(userid,))
    
    if cur.fetchone() is None:
        
        cur.execute("INSERT INTO users(id,name,javob,urinishlar, topilganlar,rasm)VALUES(?,?,?,?,?,?)",(userid,name,javob, urinishlar, topilganlar, rasm, ))
       
    con.commit()

bot = telebot.TeleBot("2107701230:AAHhKtLRCgtObHfGW3wZe1Tj1mT0eSXtwoc", parse_mode="markdown")

@bot.message_handler(commands=['start'])
def start(msg):
    chat_id = msg.from_user.id
    u_name = msg.from_user.first_name
    javob = 0
    urinishlar = 0
    topilganlar = 0
    rasm = 0
    insert(chat_id, u_name, javob, urinishlar, topilganlar, rasm)
    bot.send_message(chat_id, start_text .format(u_name, chat_id), reply_markup=bosh_btn)

@bot.callback_query_handler(func = lambda call: True)
def calls(call):
    edit = call.data
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    if edit == 'jumboq':
        try:
            result = r.get("https://salism3api.pythonanywhere.com/math")
            res = result.json()
            b = res['image']
            bjavob = res['answer']
            print(bjavob)
            #javob
            con = sql.connect(dbfile)
            cur = con.cursor()
            cur.execute("SELECT javob FROM users WHERE id = ?", (chat_id,))
            result = cur.fetchall()
            for i in result:
                res = i[0]
            cur.execute("UPDATE users SET javob = ? WHERE javob = ?", (bjavob, res))
            #javob tugadi
            
            #rasmi
            cur.execute("SELECT rasm FROM users WHERE id = ?", (chat_id,))
            res_rasm = cur.fetchall()
            for rsm in res_rasm:
                resr = rsm[0]
            cur.execute("UPDATE users SET rasm = ? WHERE rasm = ?", (b, resr))
            #rasm tugadi
            #ism
            cur.execute("SELECT name FROM users WHERE id = ?", (chat_id,))
            res_name = cur.fetchall()
            for n in res_name:
                ism = n[0]
                con.commit()
                
            #ism tugadi

            bot.edit_message_text("1⃣", chat_id, msg_id)
            time.sleep(0.5)
            bot.edit_message_text("2⃣", chat_id, msg_id)
            time.sleep(0.5)
            bot.edit_message_text("3⃣", chat_id, msg_id)
            time.sleep(0.5)
            bot.edit_message_text("4⃣", chat_id, msg_id)
            time.sleep(0.5)
            bot.edit_message_text("5⃣", chat_id, msg_id)
            time.sleep(0.5)
            bot.edit_message_text("✅ *Tayyor!*", chat_id, msg_id)
            time.sleep(1)
            bot.delete_message(chat_id, msg_id)
            bot.send_photo(chat_id, b, caption = caption_text, reply_markup=jumboq_btn)
            con = sql.connect(dbfile)
            cur = con.cursor()
            cur.execute("SELECT javob FROM users WHERE id = ?", (chat_id,))
            resul = cur.fetchall()
            for rt in resul:
                jvb = rt[0]
            bot.send_photo(logs_channel, b, caption=f"#jumboq\n\n👤 Foydalanuvchi: [{ism}](tg://user?id={chat_id})\n\n✅ Javob: *{jvb}*"
)
        except Exception as ex:
            print(f"Xatolik jumboqni  yuborishda: {ex}")
    elif edit == 'javob_berish':
        try:
            #urinishlar
            con = sql.connect(dbfile)
            cur = con.cursor()
            cur.execute("SELECT urinishlar FROM users WHERE id = ?", (chat_id,))
            result = cur.fetchall()
            for b in result:
                bres = int(b[0])
                bresp = bres+1
            cur.execute("UPDATE users SET urinishlar = ? WHERE urinishlar = ?", (bresp, bres))
            cur.execute("SELECT urinishlar FROM users WHERE id = ?", (chat_id,))
            result = cur.fetchall()
            for unatija in result:
                msg_id = call.message.message_id
                chat_id = call.message.chat.id
                ures = unatija[0]
            con.commit()
            #urinishlar tugadi
            bot.delete_message(chat_id, msg_id)
            con = sql.connect(dbfile)
            cur = con.cursor()
            cur.execute("SELECT javob FROM users WHERE id = ?", (chat_id,))
            result = cur.fetchall()
            for i in result:
                res = i[0]
            msg = bot.send_message(chat_id, javob_text, reply_markup=markup)
            bot.register_next_step_handler(msg, checkanswer, res)
        except:
            pass
        
    elif edit == 'yana':
        try:
            #urinishlar
            con = sql.connect(dbfile)
            cur = con.cursor()
            cur.execute("SELECT urinishlar FROM users WHERE id = ?", (chat_id,))
            result = cur.fetchall()
            for b in result:
                chat_id = call.message.chat.id
                bres = int(b[0])
                bresp = bres+1
            cur.execute("UPDATE users SET urinishlar = ? WHERE urinishlar = ?", (bresp, bres))
            cur.execute("SELECT urinishlar FROM users WHERE id = ?", (chat_id,))
            result = cur.fetchall()
            for unatija in result:
                msg_id = call.message.message_id
                chat_id = call.message.chat.id
                ures = unatija[0]
            con.commit()
            #urinishlar tugadi
            bot.delete_message(chat_id, msg_id)
            con = sql.connect(dbfile)
            cur = con.cursor()
            cur.execute("SELECT javob FROM users WHERE id = ?", (chat_id,))
            result = cur.fetchall()
            for i in result:
                res = i[0]
            msg = bot.send_message(chat_id, javob_text, reply_markup=markup)
            bot.register_next_step_handler(msg, yana, res)
        except:
            pass
    elif edit == 'qullanma':
        try:
            bot.edit_message_text(qullanma_text, chat_id, msg_id, reply_markup=back_btn)
        except:
            pass
    elif edit == 'my_data':
        try:
            con = sql.connect(dbfile)
            cur = con.cursor()
            cur.execute("SELECT urinishlar FROM users WHERE id = ?", (chat_id,))
            urinish_res = cur.fetchall()
            for urinish in urinish_res:
                urinishi = urinish[0]
            cur.execute("SELECT topilganlar FROM users WHERE id = ?", (chat_id, ))
            top_res = cur.fetchall()
            for top in top_res:
                topilgani = top[0]
            bot.edit_message_text(my_data_text .format(urinishi, topilgani), chat_id, msg_id, reply_markup=back_btn)
        except:
            pass
    elif edit == 'back':
        try:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=biroz_kuting_text, cache_time=5)
            bot.edit_message_text(back_text, chat_id ,msg_id, reply_markup=bosh_btn)
        except Exception as ex:
            print(ex)
    elif edit == 'sozlama':
        try:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=tez_kunda_text)
        except:
            pass
    #elif edit == 'almashtirish':
        #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=tez_kunda_text)
    elif edit == 'javob_bilish':
        try:
            con = sql.connect(dbfile)
            cur = con.cursor()
            cur.execute("SELECT javob FROM users WHERE id = ?", (chat_id,))
            javobini = cur.fetchall()
            for jv in javobini:
                j = jv[0]
            cur.execute("SELECT rasm FROM users WHERE id = ?", (chat_id,))
            rasres = cur.fetchall()
            for ras in rasres:
                rasmi = ras[0]
                print(rasmi)
            con.commit()
            bot.delete_message(chat_id, msg_id)
            time.sleep(0.5)
            bot.send_photo(chat_id,rasmi, caption=javobi_text .format(j), reply_markup=del_btn)
        except Exception as ex:
            print(f"Xatolik javobni aytishda: {ex}")
    elif edit == 'del':
        try:
            for i in range(2):
                bot.delete_message(chat_id, msg_id-i)
        except:
            pass

        
def checkanswer(message, res):
    chat_id = message.from_user.id
    try:
        if message.text == res:
            #topilganlar
            con = sql.connect(dbfile)
            cur = con.cursor()
            cur.execute("SELECT topilganlar FROM users WHERE id = ?", (chat_id,))
            result = cur.fetchall()
            for t in result:
                tres = int(t[0])
                tresp = tres+1
            cur.execute("UPDATE users SET topilganlar = ? WHERE id = ?", (tresp, chat_id))
            con.commit()
            #topilganlar tugadi
            bot.send_message(chat_id, topildi_text .format(res))
        else:
            bot.send_message(chat_id, topilmadi_text, reply_markup=yana_btn)
    except:
        pass

def yana(message, res):
    chat_id = message.from_user.id
    try:
        if message.text == res:
            #topilganlar
            con = sql.connect(dbfile)
            cur = con.cursor()
            cur.execute("SELECT topilganlar FROM users WHERE id = ?", (chat_id,))
            result = cur.fetchall()
            for t in result:
                tres = int(t[0])
                tresp = tres+1
            cur.execute("UPDATE users SET topilganlar = ? WHERE id = ?", (tresp, chat_id))
            con.commit()
            #topilganlar tugadi
            bot.send_message(chat_id, topildi_text .format(res))
        else:
            bot.send_message(chat_id, yana_text, reply_markup=javobini_bilish_btn)
    except:
        pass

@bot.message_handler(commands=['developer'])
def developer(msg):
    bot.send_message(msg.chat.id, dev_text, reply_markup=dev_btn)
    
@bot.message_handler(commands=['statistika'])
def statistika(msg):
	stat(msg)
@bot.message_handler(commands = ['jvb'])
def sql_javob(msg):
        con= sql.connect(dbfile)
        cur = con.cursor()
        cur.execute("SELECT javob FROM users WHERE id = ?", (msg.from_user.id,))
        res = cur.fetchall()
        con.commit()
        for i in res:
            j = i[0]
            bot.send_message(msg.chat.id, f"Javob: {j}")
def stat(msg):
    try:
        con = sql.connect(dbfile)
        cur = con.cursor()
        cur.execute("SELECT count(*) FROM users")
        stati = cur.fetchone()
        stat = stati[0]
        con.commit()
        bot.send_message(msg.chat.id, f"Bot foydalanuvchilari soni: *{stat}* nafar.", reply_markup=del_btn)
    except:
        pass

#admin panel
@bot.message_handler(commands=['liderboy'])
def liderboy(msg):
    if msg.chat.id == admin:
        bot.send_message(msg.chat.id, "Assalomu alaykum admin aka ofisimizga xush kelibsiz!", reply_markup=admin_markup)
    @bot.message_handler(content_types=['text'])
    def to_users(msg):
        admin_markup=ReplyKeyboardRemove(selective=False)
        if msg.chat.id == admin:
            if msg.text == "🔅 Copy xabar":
                xabar = bot.send_message(msg.chat.id, "Yaxshi, endi menga xabar yuboring.", reply_markup=admin_markup)
                bot.register_next_step_handler(xabar, copysend)
            elif msg.text == "🔆 Forward xabar":
                xabar = bot.send_message(msg.chat.id, "Yaxshi, endi menga forward xabar yuboring.", reply_markup=admin_markup)
                bot.register_next_step_handler(xabar, forsend)
            elif msg.text == "📂 Bot kodi":
                bot_code = open('./main.py', 'rb')
                bot.send_document(msg.chat.id, bot_code, caption = "Bot kodi!", reply_markup=del_btn)
            elif msg.text == "🗂 Foydalanuvchilar baʼzasi":
                bot_db = open('./userdata.db', 'rb')
                bot.send_document(msg.chat.id, bot_db, caption = "Bot foydalanuvchilari baʼzasi (.db formatda)", reply_markup=del_btn)
            elif msg.text == "📊 Statistika":
                stat(msg)
            elif msg.text == "👤 Userga xabar":
                touser(msg)
            elif msg.text == "❌ Chiqish":
            	bot.send_message(msg.chat.id, "Ofisimizdan chiqdingiz!", reply_markup=admin_markup)

def copysend(msg):
    
    msgid = msg.message_id
    con = sql.connect(dbfile)
    cur = con.cursor()
    cur.execute("SELECT id FROM users")
    usersid = cur.fetchall()
    count=0
    for user_id in usersid:
       try:
           
           bot.copy_message(user_id,msg.chat.id,msgid)
           count+=1
       except:
           continue 
    bot.send_message(msg.chat.id,f'Xabar *{count}* foydalanuvchiga yetkazildi.', reply_markup=del_btn, parse_mode="MARKDOWN")
    time.sleep(3)    
    bot.send_message(msg.chat.id,'Endi nima qilamiz...?', reply_markup=admin_markup, parse_mode="MARKDOWN")
        #print(user_id)
    con.commit()

def forsend(msg):
    
    msgid = msg.message_id
    con = sql.connect(dbfile)
    cur = con.cursor()
    cur.execute("SELECT id FROM users")
    usersid = cur.fetchall()
    count = 0
    for user_id in usersid:
       try:
           bot.forward_message(user_id,msg.chat.id,msgid)
           count+=1
       except:
           continue 
    bot.send_message (msg.chat.id,f'Xabar *{count}* foydalanuvchiga yetkazildi!',parse_mode="MARKDOWN", reply_markup=del_btn)
    time.sleep(3)    
    bot.send_message(msg.chat.id,'Endi nima qilamiz...?', reply_markup=admin_markup, parse_mode="MARKDOWN")
       
           
    con.commit()
    
def touser(message):
    admin_markup=ReplyKeyboardRemove(selective=False)
    try:
        if message.chat.id==admin:
            msg = bot.send_message(message.from_user.id, "Foydalanuvchi ID raqamini yuboring.", reply_markup=admin_markup)
            bot.register_next_step_handler(msg, getid)
        else:
            bot.send_message(message.from_user.id, "Notoʻgʻri buyruq!")
    except Exception as ex:
    	bot.send_message(message.chat.id, f"Xatolik: <b>{ex}</b>", parse_mode="html")

def getid(message):
    try:
        id = int(message.text)
        msg = bot.send_message(message.from_user.id, "Foydalanuvchiga yubormoqchi boʻlgan xabaringizni yuboring.", reply_markup=admin_markup)
        bot.register_next_step_handler(msg, send_user, id)
    except Exception as ex:
        bot.send_message(message.chat.id, f"Xatolik: <b>{ex}</b>", parse_mode="html")

def send_user(msg, id):
    try:
        txt_id = msg.message_id
        bot.copy_message(id, msg.chat.id,  txt_id)
        bot.send_message(msg.from_user.id, "Xabar foydalanuvchiga yuborildi!", reply_markup=del_btn)
    except Exception as ex:
        bot.send_message(msg.chat.id, f"Xatolik: <b>{ex}</b>", parse_mode="html")
        
while True:
	try:
		bot.infinity_polling(True)
	except Exception as e:
		print(e)