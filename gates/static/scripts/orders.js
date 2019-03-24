$('document').ready(function() {
	$('.welcome').hide();
	$('.guide-text').hide();
	$('.welcome').fadeIn(2000);
	$('.guide-text').fadeIn(2000);
});

$(function() {
	$('.order-title').on('click', function() {
		$('#' + $(this).attr('panel-id')).slideToggle(300);
		var symbol = $(this).find('.expand-symbol').html();
		$(this).find('.expand-symbol').html(symbol == '-' ? '+' : '-');
	});	
});
