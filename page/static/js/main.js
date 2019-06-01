// Closes responsive menu when a scroll trigger link is clicked
$('.js-scroll-trigger').click(function() {
  $('.navbar-collapse').collapse('hide');
});

// Activate scrollspy to add active class to navbar items on scroll
$('body').scrollspy({
  target: '#mainNav',
  offset: 57
});

// Collapse Navbar
var navbarCollapse = function() {
  if ($("#mainNav").offset().top > 100) {
    $("#mainNav").addClass("navbar-shrink");
  } else {
    $("#mainNav").removeClass("navbar-shrink");
  }
};
// Collapse now if page is not at top
navbarCollapse();
// Collapse the navbar when page is scrolled
$(window).scroll(navbarCollapse);

// Display texts on main page
(function() {
  var textos = $(".textos");
  var textIndex = -1;
  function showNext() {
    ++textIndex;
    textos.eq(textIndex % textos.length)
    .fadeIn(2000)
    .delay(6000)
    .fadeOut(2000, showNext);
  }
  showNext();
})();

//Parallax on header
/*$(document).scroll(function() {
  var st = $(this).scrollTop();
  $("#header").css({
  "background-position-y": (-st/20)
  })
  $("#headerc").css({
  "top": (-st/5),
  "bottom": (st/5)
  })
});*/