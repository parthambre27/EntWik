//Cache reference to window and animation items
var $animation_elements1 = $('#showcase');
var $window1 = $(window);
$window1.on('scroll', check_if_in_view1);
$window1.on('load scroll resize', check_if_in_view1);
$window1.trigger('scroll');

function check_if_in_view1() {
  var window_height1 = $window1.height();
  var window_top_position1 = $window1.scrollTop();
  var window_bottom_position1 = (window_top_position1 + window_height1);

  $.each($animation_elements1, function() {
    var $element1 = $(this);
    var element_height1 = $element1.outerHeight();
    var element_top_position1 = $element1.offset().top;
    var element_bottom_position1 = (element_top_position1 + element_height1);

    //check to see if this current container is within viewport
    if ((element_bottom_position1 >= window_top_position1) &&
        (element_top_position1 <= window_bottom_position1)) {
      $("#logo1").hide();
	   $("#logo2").show();
	   $("header").removeClass("header-hidden");
    } else {
     $("#logo1").show();
	 $("#logo2").hide();
	 $("header").addClass("header-hidden");
    }
  });
  
}