import os
os.system('pip install telebot')
os.system('pip install requests')
import telebot
import re
import requests

API_TOKEN = '6711097028:AAH9ivfM3MjeW2f-rCA7qCNfUwFnZGxVJbM'
bot = telebot.TeleBot(API_TOKEN)

admin = 6565529894

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "مرحبا بك عزيزي في بوت رشق المشاهدات المجاني\n"
                             "ارسل الرابط التيليكرام لطلب 1000 مشاهده مجانيه", parse_mode="Markdown")

@bot.message_handler(func=lambda message: re.search(r't\.me', message.text))
def send_views(message):
    chat_id = message.chat.id
    link = message.text
    response = send_request(link)
    
    if response:
        bot.send_message(chat_id, f"تم الارسال المشاهدات للرابط: {link}", )
    else:
        bot.send_message(chat_id, "فشل الارسال، حاول مجددا بعد قليل", parse_mode="Markdown")
        bot.send_message(admin, "عزيزي ادمن البوت:\nهنالك مشاكل في الاتصالات والطلبات تتم رفضها.\n"
                                       "اغلب الاسباب:\n- تم حظر حسابك في الموقع بسبب انتهاكيات الاستخدام\n"
                                       "- ان API_KEY_SITE غلط",)

@bot.message_handler(func=lambda message: not re.search(r't\.me', message.text))
def invalid_link(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "يرجى إرسال الرابط بشكل صحيح!\n\nمثال:\n[https://t.me/Sero_Bots/6665]",)

def send_request(link):
    response = requests.get(f"https://smm-speed.com/api/v2?action=add&service=2666&link={link}&quantity=1000&key=539b55dc24467105b4085c1d58aaeafe")
    data = response.json()
    return data.get('order', False)

if __name__ == '__main__':
    bot.polling(none_stop=True)
