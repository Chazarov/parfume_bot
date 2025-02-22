function history_back(){
    window.history.back()
}

document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('[data-action="history_back"]');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            history_back();
        });
    });

});