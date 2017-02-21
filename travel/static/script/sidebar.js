$(function () {
    // if ($(window).width() <= 7iconRate6) {
    //     $("#navbar").addClass("navbar-fixed-top");
    // }
    // else {
    //     $("#navbar").addClass("navbar-fixed-top");
    // }
    sidebar();

    $(window).resize(function () {
        sidebar();
    });
});

function sidebar(){
    var sideRate = 10;
    var iconRate = 4;
    var height = $(window).height();
    var width = $(window).width();
    $("#sidebar").height(height);
    $("#sidebar").css("width",width/sideRate);
    $("#content").css("margin-left",width/sideRate);

    $("#sidebar img").css("width",width/sideRate/iconRate).css("height","auto");
    $("#sidebar img").css("margin-left",width/sideRate/iconRate/2*3);
    $("#sidebar img").css("margin-right",width/sideRate/iconRate/2*3);
    var margin_top=(height-200-width/sideRate/iconRate*6)/12;
    $("#sidebar img").css("margin-top",margin_top);
    $("#sidebar img").css("margin-bottom",margin_top);
}


