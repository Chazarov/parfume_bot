function update_price(priceElement){
    const selectedOption = document.querySelector('input[name="volume"]:checked');
    volume_item_id = selectedOption.value;

    
    const action_url = priceElement.getAttribute('data-action_url');

    fetch(action_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({
            volume_item_id: volume_item_id,
        })
    })
    .then(response => response.json())
    .then(data => {
        var price = data.price
        priceElement.innerText = price
    })
    .catch(error => { 
        alert("Не удалось выполнить запрос" + error);
    });
}



document.addEventListener('DOMContentLoaded', () => {
    const price_display = document.querySelector('#price');
    const inputs = document.querySelectorAll('input[name="volume"]');

    inputs.forEach((radio) => {
        radio.addEventListener('change', () => {
                update_price(price_display);
        });
    });
    update_price(price_display);
});
