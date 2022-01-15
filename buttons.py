from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton, ForceReply

bosh_btn = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('🔢 Matematik jumboq', callback_data = 'jumboq')
    ],[
        InlineKeyboardButton('⚠️ Qoʻllanma', callback_data = 'qullanma'),
        InlineKeyboardButton('⚙ Sozlamalar', callback_data='sozlama')
    ],[
        InlineKeyboardButton('👤 Mening maʻlumotlarim', callback_data='my_data')
        
    ]]
    )
jumboq_btn = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('💡 Javob berish', callback_data = 'javob_berish'),
        #InlineKeyboardButton('♻️ Almashtirish', callback_data = 'almashtirish')
    ]]
    )
back_btn = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('Orqaga', callback_data = 'back')
    ]]
    )

yana_btn = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('🔄 Yana urinish', callback_data = 'yana')
    ]]
    )
    
    
javobini_bilish_btn = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('✅ Javobini bilish', callback_data = 'javob_bilish')
    ]]
    )

dev_btn = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('📞 Bogʻlanish', url = 'https://t.me/LiderBoy')
    
    ],[
        InlineKeyboardButton('🗑', callback_data='del')
    ]]
    )
del_btn = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('🗑', callback_data='del')
    ]]
    )
    
admin_markup = ReplyKeyboardMarkup(True)
admin_markup.row("🔅 Copy xabar", "🔆 Forward xabar")
admin_markup.row("📂 Bot kodi", "🗂 Foydalanuvchilar baʼzasi")
admin_markup.row("📊 Statistika", "👤 Userga xabar")
admin_markup.row("❌ Chiqish")

markup = ForceReply(selective=False)