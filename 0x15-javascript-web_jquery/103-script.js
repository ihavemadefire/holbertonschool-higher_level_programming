#!/usr/bin/node
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val();
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
  /// /
  $('#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val();
        $.get(url, function (data) {
          $('#hello').text(data.hello);
        });
      }
    });
  });

/// /
});
