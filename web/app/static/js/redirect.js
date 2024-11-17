function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}




function redirect(buttonElement){
    const redirect_url = buttonElement.getAttribute('data-redirect_url');
    window.location.href=redirect_url
}

document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('[data-action="redirect"]');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            redirect(button);
        });
    });

});



