let btnCatalog = document.querySelector('.catalog-auto-h');
let catalog = document.querySelector('.katalog-auto__list');

btnCatalog.addEventListener('click', function () {
    catalog.classList.toggle('item-show');
    btnCatalog.classList.toggle('link-active');
})

let btnCredit = document.querySelector('.credit-h');
let credit = document.querySelector('.header-kredit');

btnCredit.addEventListener('click', function () {
    credit.classList.toggle('item-show');
    btnCredit.classList.toggle('link-active');
})

let btnSpec = document.querySelector('.special-h');
let spec = document.querySelector('.header-spec');

btnSpec.addEventListener('click', function () {
    spec.classList.toggle('item-show');
    btnSpec.classList.toggle('link-active');
})

// Pop-up callback
let btnCall = document.querySelector('.header-bottom__callback-btn');
let popup = document.querySelector('.popup-callback');
let btnClose = document.querySelector('.popup-callback__close');
let parentPopup = document.querySelector('.parent-popup-div');

btnCall.addEventListener('click', function() {
    popup.classList.add('popup-callback-open');
    parentPopup.classList.add('parent-popup');
})

btnClose.addEventListener('click', function() {
    popup.classList.remove('popup-callback-open');
    parentPopup.classList.remove('parent-popup');
})


// Burger
let burgerBtn = document.querySelector('.header__burger');
let burger = document.querySelector('.burger');

burgerBtn.addEventListener('click', function(){
    burger.classList.toggle('burger-show');
    burgerBtn.classList.toggle('burger-btn-open');
})