// function for hide None value tags in Lessons.html
var count_click = 0
var count = 0

function hide_tags(){
    tag_0 = document.getElementsByClassName('tag')
    for (el = 0; el <= tag_0.length; el ++){
        if(tag_0[el].innerHTML == 'None'){
            tag_0[el].style.display = 'none';
        }
    }
}
hide_tags()

// block for opening comments block
function comments(){
    count_click += 1
    if(count_click % 2 == 0){
        var arrow_down = document.getElementById('arrow_down').style.display = "block";
        var arrow_up = document.getElementById('arrow_up').style.display = "none";
        var comments_block_down = document.getElementById('comments_container').style.display = "none";
    } else {
        var arrow_up = document.getElementById('arrow_up').style.display = "block";
        var arrow_down = document.getElementById('arrow_down').style.display = "none";
        var comments_block_up = document.getElementById('comments_container').style.display = "block";
    }
}


// funct for show response block on comment
function message_response(){
    count += 1
    if (count % 2 == 0){
        document.getElementById('response_div_id').style.display = 'block';
    } else {
        document.getElementById('response_div_id').style.display = 'none';
    }

}