const radios = document.querySelectorAll('input[name="slider"]');
let currentSlide = 0;
const totalSlides = radios.length;

function showNextSlide() {
    // Определяем текущий слайд
    radios.forEach((radio, index) => {
        if (radio.checked) {
            currentSlide = index;
        }
    });

    // Переход на следующий слайд (циклический переход)
    currentSlide = (currentSlide + 1) % totalSlides;
    radios[currentSlide].checked = true;
}

function showPrevSlide() {
    // Определяем текущий слайд
    radios.forEach((radio, index) => {
        if (radio.checked) {
            currentSlide = index;
        }
    });

    // Переход на предыдущий слайд (циклический переход)
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    radios[currentSlide].checked = true;
}

// Привязываем обработчики событий к кнопкам
document.getElementById('next_button').addEventListener('click', showNextSlide);
document.getElementById('prev_button').addEventListener('click', showPrevSlide);

