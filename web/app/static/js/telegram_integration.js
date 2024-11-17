const tg = window.Telegram.WebApp;
tg.expand();

console.log("Connect")

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}


// const BOT_LOCATION = "https://t.me/C000lBot"


function sendCartToServer() {
    if (window.Telegram.WebApp) {

        

        const userId = tg.initDataUnsafe.user.id;
        const username = tg.initDataUnsafe.user.username
        const actionUrl = buttonElement.getAttribute('data-action_url');
        const redirect_to = buttonElement.getAttribute('data-redirect_url')

        const params = new URLSearchParams({
            tgUserId: userId,
            username: username,
        });

        fetch(`${actionUrl}?${params.toString()}`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {

                alert('Благодарим за заказ! В ближайшее время с вами свяжется наш оператор.');
                window.location.href=redirect_to
            } else {
                console.error('Ошибка при отправке данных:', data.details);
            }
        })
        .catch(error => {
            alert('Ошибка сети:', error);
        });

        
    } else {
        alert('Telegram не доступен');
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