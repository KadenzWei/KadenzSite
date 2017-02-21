$(function() {
    $('#sidebar div,#sidebar img').mouseover(function() {
        $(this).siblings().animate({ opacity: 0.5 }, 300);
        $(this).animate({ opacity: 0.5 }, 300);
    });
    $('#sidebar div,#sidebar img').mouseleave(function() {
        $(this).siblings().animate({ opacity: 1 }, 300);
        $(this).animate({ opacity: 1 }, 300);
    });
});
