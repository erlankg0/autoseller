let btnPrev = document.querySelector('.slider-prev')
let btnNext = document.querySelector('.slider-next')

let sliders = document.querySelectorAll('.slider-wrapper')

sliders.forEach(slider => {
    let offset = 0;

    btnNext.addEventListener('click', function () {
        offset += 477;
        if (offset > 2385) {
            offset = 0;
        }
        slider.style.left = -offset + 'px';
    })

    btnPrev.addEventListener('click', function () {
        offset -= 477;
        if (offset < 0) {
            offset = 2385;
        }
        slider.style.left = -offset + 'px';
    })
});

$(".js-range-slider").ionRangeSlider({
    type: "double",
    min: 0,
    max: 25000000,
    from: 250000,
    to: 5000000,
    grid: true
});


