const tg = window.Telegram.WebApp;
tg.expand();


const BOT_LOCATION = "https://t.me/C000lBot"


function sendCartToServer() {
    // Проверяем, что Telegram Web Apps API доступен
    if (window.Telegram.WebApp) {

        

        // Получаем информацию о пользователе
        const userId = tg.initDataUnsafe.user.id;
        const username = tg.initDataUnsafe.user.username


        // URL для отправки данных
        const serverUrl = '/api/cart'; // Замените на нужный URL

        // Формируем параметры для GET-запроса
        const params = new URLSearchParams({
            tgUserId: userId,
            username: username,
        });

        // Отправляем GET-запрос на сервер
        fetch(`${serverUrl}?${params.toString()}`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {

                console.log('Данные успешно отправлены');
                window.location.href=BOT_LOCATION
            } else {
                console.error('Ошибка при отправке данных:', data.details);
            }
        })
        .catch(error => {
            console.error('Ошибка сети:', error);
        });

        
    } else {
        console.error('Telegram WebApp API не доступен');
    }
}



document.addEventListener('DOMContentLoaded', () => {
    const cartButton = document.getElementById('cart');
    if (cartButton) {
        cartButton.addEventListener('click', () => {
            sendCartToServer();
        });
    }
});