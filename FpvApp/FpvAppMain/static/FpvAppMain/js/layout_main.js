function show_article(){
    var url = window.location.href
    if (url == 'http://127.0.0.1:8000/lessons_page'){
        document.getElementById('article_configurator').style.display = 'block';
    } else {
        document.getElementById('article_configurator').style.display = 'none';
    }
}
show_article()

function show_photo(num){
    console.log(num)
    if(num == 'photo_1'){
        document.getElementById('pic_block').style.display = 'block';
        document.getElementById('pic_block_2').style.display = 'none';
        document.getElementById('pic_block_3').style.display = 'none';
        document.getElementById('pic_block_4').style.display = 'none';
        document.getElementById('pic_block_5').style.display = 'none';
        document.getElementById('block_photo_2').style.display = 'none';
        document.getElementById('block_photo_3').style.display = 'none';
        document.getElementById('block_photo_4').style.display = 'none';
        document.getElementById('block_photo_5').style.display = 'none';

    } else if(num == 'photo_2'){
        document.getElementById('pic_block').style.display = 'block';
        document.getElementById('pic_block_2').style.display = 'block';
        document.getElementById('pic_block_3').style.display = 'none';
        document.getElementById('pic_block_4').style.display = 'none';
        document.getElementById('pic_block_5').style.display = 'none';
        document.getElementById('block_photo_1').style.display = 'none';
        document.getElementById('block_photo_3').style.display = 'none';
        document.getElementById('block_photo_4').style.display = 'none';
        document.getElementById('block_photo_5').style.display = 'none';
    } else if(num == 'photo_3'){
        document.getElementById('pic_block').style.display = 'block';
        document.getElementById('pic_block_2').style.display = 'block';
        document.getElementById('pic_block_3').style.display = 'block';
        document.getElementById('pic_block_4').style.display = 'none';
        document.getElementById('pic_block_5').style.display = 'none';
        document.getElementById('block_photo_1').style.display = 'none';
        document.getElementById('block_photo_2').style.display = 'none';
        document.getElementById('block_photo_4').style.display = 'none';
        document.getElementById('block_photo_5').style.display = 'none';
    } else if(num == 'photo_4'){
        document.getElementById('pic_block').style.display = 'block';
        document.getElementById('pic_block_2').style.display = 'block';
        document.getElementById('pic_block_3').style.display = 'block';
        document.getElementById('pic_block_4').style.display = 'block';
        document.getElementById('pic_block_5').style.display = 'none';
        document.getElementById('block_photo_1').style.display = 'none';
        document.getElementById('block_photo_2').style.display = 'none';
        document.getElementById('block_photo_3').style.display = 'none';
        document.getElementById('block_photo_5').style.display = 'none';
    } else if(num == 'photo_5'){
        document.getElementById('pic_block').style.display = 'block';
        document.getElementById('pic_block_2').style.display = 'block';
        document.getElementById('pic_block_3').style.display = 'block';
        document.getElementById('pic_block_4').style.display = 'block';
        document.getElementById('pic_block_5').style.display = 'block';
        document.getElementById('block_photo_1').style.display = 'none';
        document.getElementById('block_photo_2').style.display = 'none';
        document.getElementById('block_photo_3').style.display = 'none';
        document.getElementById('block_photo_4').style.display = 'none';
    }
}


function first_slide() {
        var text = document.getElementById('second_text')
        document.body.style.backgroundImage = "url('http://127.0.0.1:8000/static/FpvAppMain/img/bg.avif')"
        text.style.display = "none"

}

function first_cube() {
   var text = document.getElementById('second_text')
   document.body.style.backgroundImage = "url('http://127.0.0.1:8000/static/FpvAppMain/img/DeepSixDrone_1.jpeg')"
   document.body.style.backgroundPosition = "center"
   document.body.style.backgroundSize = "100% 100%"
   text.style.display = "block"
   text.style.color = "#ebb81e"
   text.style.fontSize = "40px"
   text.innerHTML = 'Open new world'
   text.style.width = "100%"
   text.style.height = "40vh"
   text.style.display = "flex"
   text.style.justifyContent = "center"
   text.style.position = "relative"
   text.style.animationName = "show_text_first"
   text.style.animationDuration = "2s"
   text.style.animationTimingFunction = "linear"


}


function second_cube(){
        var text = document.getElementById('second_text')
        document.body.style.backgroundImage = "url('http://127.0.0.1:8000/static/FpvAppMain/img/Mavic.webp')"
        document.body.style.backgroundPosition = "center"
        document.body.style.backgroundSize = "100% 100%"
        text.style.display = "block"
        text.style.color = "#ebb81e"
        text.style.fontSize = "40px"
        text.innerHTML = 'Build your own drone'
        text.style.width = "100%"
        text.style.height = "30vh"
        text.style.display = "flex"
        text.style.justifyContent = "start"
        text.style.padding = "2%"
        text.style.position = "relative"
        text.style.animationName = "show_text_second"
        text.style.animationDuration = "2s"
        text.style.animationTimingFunction = "linear"
}

function third_cube() {
    var text = document.getElementById('second_text')
    var photos = document.getElementById('second_slide')
    document.body.style.backgroundImage = "url('http://127.0.0.1:8000/static/FpvAppMain/img/war_drone.webp')"
    document.body.style.backgroundPosition = "center"
    document.body.style.backgroundSize = "100% 100%"
    text.style.display = "block"
    text.style.color = "#ebb81e"
    text.style.fontSize = "40px"
    text.innerHTML = 'Your way is freedom'
    text.style.width = "100%"
    text.style.height = "20vh"
    text.style.display = "flex"
    text.style.justifyContent = "end"
    text.style.padding = "2%"
    text.style.position = "relative"
    text.style.animationName = "show_text_third"
    text.style.animationDuration = "2s"
    text.style.animationTimingFunction = "linear"

}

function four_cube() {
    var text = document.getElementById('second_text')
    document.body.style.backgroundImage = "url('http://127.0.0.1:8000/static/FpvAppMain/img/war_drone_2.webp')"
    document.body.style.backgroundPosition = "center"
    document.body.style.backgroundSize = "100% 100%"
    text.style.display = "block"
    text.style.color = "#ebb81e"
    text.style.fontSize = "40px"
    text.innerHTML = 'Bomb for your enemies'
    text.style.width = "100%"
    text.style.height = "20vh"
    text.style.display = "flex"
    text.style.justifyContent = "end"
    text.style.padding = "2%"
}


function fifth_cube() {
    var text = document.getElementById('second_text')
    document.body.style.backgroundImage = "url('http://127.0.0.1:8000/static/FpvAppMain/img/war_drone_3.jpeg')"
    document.body.style.backgroundPosition = "center"
    document.body.style.backgroundSize = "100% 100%"
    text.style.display = "block"
    text.style.color = "#ebb81e"
    text.style.fontSize = "40px"
    text.innerHTML = 'Rest after work'
    text.style.width = "100%"
    text.style.height = "20vh"
    text.style.display = "flex"
    text.style.justifyContent = "end"
    text.style.padding = "2%"
}
