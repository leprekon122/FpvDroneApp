// function for hide None value tags in Lessons.html


function hide_tags(){
    tag_0 = document.getElementsByClassName('tag')
    for (el = 0; el <= tag_0.length; el ++){
        if(tag_0[el].innerHTML == 'None'){
            tag_0[el].style.display = 'none';
        }
    }
}
hide_tags()


