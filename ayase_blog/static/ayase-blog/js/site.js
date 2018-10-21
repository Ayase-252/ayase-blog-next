$(document).ready(function (){
    $(".nav-toggle").click(function(event){
        $(".nav-mobile-menu-bg").slideToggle(400);
        $(".nav-menu").fadeToggle(400);
    });
    hljs.initHighlightingOnLoad();
});
