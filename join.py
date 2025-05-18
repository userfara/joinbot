import os
import telebot
from telebot.types import Message

API_TOKEN = '7956116848:AAHsg8yg1EZOc7ZUGZkb2FXX5_lMa37Dxn4'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['new_chat_members', 'left_chat_member'])
def handle_new_left_members(message: Message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        if message.reply_to_message:
            bot.delete_message(message.chat.id, message.reply_to_message.message_id)
    except Exception as e:
        print(f"Error: {e}")

# Portni belgilash
PORT = int(os.environ.get("PORT", 5000))

# Botni ishga tushirish
if __name__ == "__main__":
    bot.polling()
