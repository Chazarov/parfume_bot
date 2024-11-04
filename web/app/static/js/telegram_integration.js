


function sendCartToServer() {
    // Проверяем, что Telegram Web Apps API доступен
    if (window.Telegram.WebApp) {
        const tg = window.Telegram.WebApp;

        // Получаем информацию о пользователе
        const userId = tg.initDataUnsafe.user.id;

        // URL для отправки данных
        const serverUrl = 'api/cart'; // Замените на нужный URL

        // Формируем параметры для GET-запроса
        const params = new URLSearchParams({
            tgUserId: userId
        });

        // Отправляем GET-запрос на сервер
        fetch(`${serverUrl}?${params.toString()}`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log('Данные успешно отправлены');
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