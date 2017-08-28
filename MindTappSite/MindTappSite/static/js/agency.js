// Agency Theme JavaScript

$(window).on("load", function () {
    if($(window).scrollTop() === 0) {
        setTimeout(function(){
            $('body').addClass('loaded');
            $("#mainNav").addClass('animate-header');
            $(".intro-text").addClass('animate-intro');
        }, 1000);
    } else {
        $('body').addClass('loaded');
    }
});

(function($) {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 51
    });

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function(){ 
            $('.navbar-toggle:visible').click();
    });

    // Offset for Main Navigation
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    })


    window.sr = ScrollReveal();
    sr.reveal(".sr-timeline", {
        duration: 1000
    });
    sr.reveal(".sr-services", {
        duration: 1000
    }, 300);
    sr.reveal(".sr-portfolio", {
        duration: 1000
    }, 600);
    sr.reveal(".sr-team", {
        duration: 1000
    }, 600);

})(jQuery); // End of use strict
