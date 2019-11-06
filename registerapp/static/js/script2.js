
 $(document).ready(function(){
  $("#app-show").click(function(){
    $(".blur").delay(200).fadeOut(400);
	$(".app-container").addClass("show");
	$("#app-show").hide();
	$("#app-hide").show()
  });
  $("#app-hide").click(function(){
	$(".app-container").removeClass("show");
	$("#app-show").show();
	$("#app-hide").hide();
	 $(".blur").delay( 500 ).fadeIn(400);
  });
});

 $(window).on('load', function () {
      $("#loader").delay( 1000 ).fadeOut(200, function(){ 
                  $(".animation").addClass('fadeInUp');
               });
	  $("body").delay( 1000 ).removeClass("no-scroll");
	  
 });
 
 //Cache reference to window and animation items
var $animation_elements = $('.animation-element');
var $window = $(window);
$window.on('scroll resize', check_if_in_view);

function check_if_in_view() {
  var window_height = $window.height();
  var window_top_position = $window.scrollTop();
  var window_bottom_position = (window_top_position + window_height);

  $.each($animation_elements, function() {
    var $element = $(this);
    var element_height = $element.outerHeight();
    var element_top_position = $element.offset().top;
    var element_bottom_position = (element_top_position + element_height);

    //check to see if this current container is within viewport
    if ((element_bottom_position >= window_top_position) &&
        (element_top_position <= window_bottom_position)) {
      $element.addClass('fadeInUp');
    } else {
      //$element.removeClass('fadeInUp');
	  	  $element.addClass('null');
    }
  });
  
}
  


