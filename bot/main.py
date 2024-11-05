from fastapi import FastAPI, Request
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import uvicorn
from config import configs
from kbds import main_menu_buttons

app = FastAPI()
bot = Bot(token=configs.BOT_TOKEN)
dp = Dispatcher()

@app.post("/cart")
async def process_cart(request: Request):
    data = await request.json()
    
    telegram_id = data.get('telegram_id')
    cart = data.get('cart')
    username = data.get('username')
    
    if not telegram_id:
        return {"error": "Telegram ID не предоставлен"}, 400
    
    cart_items = "\n".join(
        [f"{item['name']} x {item['price']} Р" for item in cart]
    )
    
    user_message = f"Ваши товары:\n{cart_items}"
    admin_message = f"id:{telegram_id} @{username}:\n{cart_items}"
    
    await bot.send_message(telegram_id, user_message) 
    await bot.send_message(configs.ADMIN_ID, admin_message)

    return {"status": "Сообщение отправлено в Telegram"}

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет!")

async def start_uvicorn():
    config = uvicorn.Config(app, host="0.0.0.0", port=8080)
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    # Запускаем сервер FastAPI в отдельной задаче
    asyncio.create_task(start_uvicorn())
    
    # Запуск бота
    await dp.start_polling(bot)
    print("start")

if __name__ == "__main__":
    asyncio.run(main())