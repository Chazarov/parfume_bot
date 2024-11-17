function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}



function update_cart_counter(counterElement){

    const action_url = counterElement.getAttribute('data-action_url');
    

    fetch(action_url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
    })
    .then(response => response.json())
    .then(data => {
        var counter = data.counter
        if(counter == 0){
            counterElement.style.display = 'none';
        }else{
            counterElement.innerText = counter;
        }
    })
    .catch(error => { 
        alert("Не удалось выполнить запрос");
    });



}



document.addEventListener('DOMContentLoaded', () => {
    const cart_counter = document.querySelector('#cart_counter');

    update_cart_counter(cart_counter);
});
