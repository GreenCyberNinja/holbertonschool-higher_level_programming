$(document).ready(function () {
    $('DIV#add_item').bind("click", function(){
        $('UL.my_list').append('<li>Item</li>');
    });
});
