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
        return {"error": "Admin ID не предоставлен"}, 400
    
    if not telegram_id:
        return {"error": "Telegram ID не предоставлен"}, 400
    
    cart_items = "\n\n".join(
        [f"№{item['product_id']} {item['name']}: \n {item['price']} X volume: {item['volume']}ml Р" for item in cart]
    )
    
    user_message = f"Ваши товары:\n{cart_items}.\n\n Благодарим за заказ! В ближайшее время с вами свяжется наш оператор, для дальнейшего согласования"
    admin_message = f"id:{telegram_id} @{username}:\n\n\n{cart_items}"
    
    try:
        await bot.send_message(admin_id, admin_message)
        
    except TelegramBadRequest as e:
        return {"error": f"Ошибка Telegram: {str(e)}"}, 400
    except Exception as e:
        return {"error": f"Произошла ошибка: {str(e)}"}, 500
    
    try:
        await bot.send_message(telegram_id, user_message)
        
    except TelegramBadRequest as e:
        return {"error": f"Ошибка Telegram: {str(e)}"}, 400
    except Exception as e:
        return {"error": f"Произошла ошибка: {str(e)}"}, 500


    return {"status": "Сообщение отправлено в Telegram"}, 200

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет!")

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