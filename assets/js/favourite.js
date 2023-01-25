let newCars = document.querySelector('.main-cont')
let probeg = document.querySelector('.probeg-cont')
let taxi = document.querySelector('.taxi-cont')

let btnNew = document.querySelector('.main__btns-new')
let btnProbeg = document.querySelector('.main__btns-probeg')
let btnTaxi = document.querySelector('.main__btns-taxi')

btnProbeg.addEventListener('click', function(){
    probeg.style.display = 'block'
    btnProbeg.classList.add('fav-btn-active')
    btnNew.classList.remove('fav-btn-active')
    btnTaxi.classList.remove('fav-btn-active')
    newCars.style.display = 'none'
    taxi.style.display = 'none'
})

btnTaxi.addEventListener('click', function(){
    taxi.style.display = 'block'
    newCars.style.display = 'none'
    probeg.style.display = 'none'
    btnProbeg.classList.remove('fav-btn-active')
    btnNew.classList.remove('fav-btn-active')
    btnTaxi.classList.add('fav-btn-active')
})

btnNew.addEventListener('click', function(){
    newCars.style.display = 'block'
    taxi.style.display = 'none'
    probeg.style.display = 'none'
    btnProbeg.classList.remove('fav-btn-active')
    btnNew.classList.add('fav-btn-active')
    btnTaxi.classList.remove('fav-btn-active')
})

