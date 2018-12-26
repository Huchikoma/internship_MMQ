var leftPos, newWidth;
var updateUnderlinePosition = function(elem) {
	leftPos = elem.position().left;
	newWidth = elem.width();
	$(".navbar-underline").css("left", leftPos).css("width", newWidth);
}

// mark active element on page load
// $el = $(".nav.navbar-nav:has(div.navbar-underline) > li.active");
// updateUnderlinePosition($el);

//update position on hover

$(".nav.navbar-nav:has(div.navbar-underline) > li").hover(function() {
	$el = $(this);
	updateUnderlinePosition($el);
}, function() {
	$(".navbar-underline").css("left", leftPos).css("width", 0);
});