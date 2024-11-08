const tg = window.Telegram.WebApp;
tg.expand();

console.log("Connect")


const BOT_LOCATION = "https://t.me/C000lBot"


function sendCartToServer() {
    if (window.Telegram.WebApp) {

        

        const userId = tg.initDataUnsafe.user.id;
        const username = tg.initDataUnsafe.user.username


        const serverUrl = '/api/process_order'; 

        const params = new URLSearchParams({
            tgUserId: userId,
            username: username,
        });

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
    const cartButton = document.getElementById('process_order');
    if (cartButton) {
        cartButton.addEventListener('click', () => {
            sendCartToServer();
        });
    }
});