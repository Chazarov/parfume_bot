const radios = document.querySelectorAll('input[name="slider"]');
let currentSlide = 0;
const totalSlides = radios.length;

function showNextSlide() {
    radios.forEach((radio, index) => {
        if (radio.checked) {
          currentSlide = index; // Получаем индекс активного слайда
        }
      });
    
      // Переключаемся на следующий слайд
      currentSlide = (currentSlide + 1) % totalSlides; // Цикличный переход
      radios[currentSlide].checked = true; // Активируем следующий слайд
}

// Меняем слайды каждые 3 секунды
setInterval(showNextSlide, 3000);