from fastapi import FastAPI, Request
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest
import uvicorn
from config import configs

app = FastAPI()
bot = Bot(token=configs.BOT_TOKEN)
dp = Dispatcher()

@app.post("/cart")
async def process_cart(request: Request):
    data = await request.json()
    
    telegram_id = data.get('telegram_id')
    cart = data.get('cart')
    username = data.get('username')
    admin_id = data.get('admin_id')

    if not admin_id:
        print("Admin ID не предоставлен")
        return {"error": "Admin ID не предоставлен"}, 400
    
    if not telegram_id:
        print("Admin ID не предоставлен")
        return {"error": "Telegram ID не предоставлен"}, 400
    
    cart_items = "\n\n".join(
        [f"№{item['product_id']} {item['name']}: \n  -- цена: {item['price']} ₽ \n  -- объем: {item['volume']}ml " for item in cart]
    )
    
    user_message = f"Ваши товары:\n{cart_items}.\n\n Благодарим за заказ! \n В ближайшее время наш оператор свяжется с Вами для уточнения деталей."
    admin_message = f"id:{telegram_id} @{username}:\n\n\n{cart_items}"
    
    try:
        await bot.send_message(admin_id, admin_message)
        
    except TelegramBadRequest as e:
        print(f"Ошибка Telegram: {str(e)} \n data: {data}")
        return {"error": f"Ошибка Telegram: {str(e)}"}, 400
    except Exception as e:
        print(f"Произошла ошибка: {str(e)} \n data: {data}")
        return {"error": f"Произошла ошибка: {str(e)}"}, 500
    
    try:
        await bot.send_message(telegram_id, user_message)
        
    except TelegramBadRequest as e:
        print(f"Ошибка Telegram: {str(e)} \n data: {data}")
        return {"error": f"Ошибка Telegram: {str(e)}"}, 400
    except Exception as e:
        print(f"Произошла ошибка: {str(e)} \n data: {data}")
        return {"error": f"Произошла ошибка: {str(e)}"}, 500


    return {"status": "Сообщение отправлено в Telegram"}, 200

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Здравствуйте! Рад приветствовать Вас в нашей галерее! Я L’ARIAN - виртуальный помощник и проводник по галерее Парфюма! Здесь Вы можете  выбрать и подобрать аромат для себя и близкого человека,  а также оформить заказ желаемого товара!" +
    "\n\nПереходите в галерею по синей кнопке 😏")

async def start_uvicorn():
    config = uvicorn.Config(app, host=configs.MAIN_HOST, port=int(configs.MAIN_PORT))
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    asyncio.create_task(start_uvicorn())
    
    await dp.start_polling(bot)
    print("start")

if __name__ == "__main__":
    asyncio.run(main())