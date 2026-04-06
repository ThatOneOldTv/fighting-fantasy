$(document).ready( function () {
    console.log('page loaded')
});

function display_main_menu() {
    document.getElementById('main_menu').classList.remove('d-none')
    document.getElementById('play_menu').classList.add('d-none')
}

function display_play_menu() {
    console.log('display play menu')
    document.getElementById('main_menu').classList.add('d-none')
    document.getElementById('play_menu').classList.remove('d-none')
}