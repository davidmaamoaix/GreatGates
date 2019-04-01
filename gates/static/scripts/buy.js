(function($) {
	$.fn.inputFilter = function(inputFilter) {
		return this.on("input keydown keyup mousedown mouseup select contextmenu drop", function() {
			if (inputFilter(this.value)) {
				this.oldValue = this.value;
				this.oldSelectionStart = this.selectionStart;
				this.oldSelectionEnd = this.selectionEnd;
			} else if (this.hasOwnProperty("oldValue")) {
				this.value = this.oldValue;
				this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
			}
		});
	};
}(jQuery));

function subtract(value) {
	if (value && isNum(value) && value > 0) {
		return value - 1;
	} else {
		return 0;
	}
}

function add(value) {
	if (value && isNum(value) && value < 20) {
		return parseInt(value) + 1;
	} else if (parseInt(value) >= 20) {
		return 20;
	} else {
		return 1;
	}
}

function isNum(num) {
	return /^\d*$/.test(num);
}

function updateTotal() {
	var total = 0;
	$('.amount-box').each(function() {
		total += parseInt($(this).val());
	});
	$('#total').text('¥' + total);
}

$('.amount-box').inputFilter(function(value) {
	return isNum(value);
});

$('.amount-box').focusout(function() {
	var value = $(this).val();
	if (value > 20) $(this).val(20);
	updateTotal();
});

$('.minus').on('click', function() {
	$(this).siblings('.amount-box').val(subtract($(this).siblings('.amount-box').val()));
	updateTotal();
});

$('.add').on('click', function() {
	$(this).siblings('.amount-box').val(add($(this).siblings('.amount-box').val()));
	updateTotal();
});