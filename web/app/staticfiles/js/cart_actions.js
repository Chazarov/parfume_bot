
 

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}



function add_to_cart_or_delete(buttonElement) {
    const selectedOption = document.querySelector('input[name="volume"]:checked');
    var volume_item_id = null;
    if (selectedOption) {
        volume_item_id = selectedOption.value;
    }

    
    const action_url = buttonElement.getAttribute('data-add_action_url');
    const product_id = buttonElement.getAttribute('data-product_id');
    const not_in_cart_content = buttonElement.getAttribute('data-not_in_cart_content');
    const in_cart_content = buttonElement.getAttribute('data-in_cart_content');

    fetch(action_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({
            product_id: product_id,
            volume_item_id: volume_item_id,
        })
    })
    .then(response => response.json())
    .then(data => {
        var in_cart = data.in_cart
        console.log(in_cart)
        if(in_cart){
            buttonElement.innerHTML = in_cart_content
        }else{
            buttonElement.innerHTML = not_in_cart_content
        }
    })
    .catch(error => { 
        alert("Не удалось выполнить запрос" + error);
    });
}


function update_indicator(buttonElement){
    const selectedOption = document.querySelector('input[name="volume"]:checked');
    var volume_item_id = null
    if (selectedOption) {
        volume_item_id = selectedOption.value;
    }

    const not_in_cart_content = buttonElement.getAttribute('data-not_in_cart_content');
    const in_cart_content = buttonElement.getAttribute('data-in_cart_content');
    const product_id = buttonElement.getAttribute('data-product_id');
    const action_url = buttonElement.getAttribute('data-check_action_url');



    fetch(action_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({
            product_id: product_id,
            volume_item_id: volume_item_id
        })
    })
    .then(response => response.json())
    .then(data => {
        var in_cart = data.in_cart

        console.log(in_cart)
        if(in_cart){
            buttonElement.innerHTML = in_cart_content
        }else{
            buttonElement.innerHTML = not_in_cart_content
        }
    })
    .catch(error => { 
        alert("Не удалось выполнить запрос");
    });

}






document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('[id^="cart_button"]');
    const inputs = document.querySelectorAll('input[name="volume"]');

    buttons.forEach(button => {
        update_indicator(button);
        button.addEventListener('click', () => {
            add_to_cart_or_delete(button);
        });
    });

    inputs.forEach((radio) => {
        radio.addEventListener('change', () => {
            buttons.forEach(button => {
                update_indicator(button);
            });
        });
    });
});

