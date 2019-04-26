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

	$('.delete').on('click', function() {
		if (confirm('Are you sure you want to delete this order?')) {
			var url = '/remove';
			var param = 'entryId=' + $(this).attr('entry');
			var xhr = new XMLHttpRequest();
			xhr.open("POST", url, true);
			xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
			xhr.send(param);

			$(this).parent().parent().slideUp(400, function() {
				$(this).remove();

				if ($('#pending-panel').children().length == 0) {
					$('#pending-panel').html('<p class="secondary nothing">Nothing to show here</p>');
				} else {
					$('#pending-panel').children().last().children('hr').remove();
				}
			});
		}
	});
});