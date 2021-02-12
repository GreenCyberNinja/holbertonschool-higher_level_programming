$(document).ready(function () {
    $('DIV#update_header').bind("click", function(){
        $('HEADER').replaceWith('New Header!!!');
    });
});
