function deleteSomething(url_target, csrf, callback_error, callback_done){
  $.ajax({
    headers: {'X-CSRFToken': csrf},
    url: url_target,
    type: 'DELETE',
    dataType: 'json',
    processData: false,
    contentType: false,
  })
    .done(function(data){
      callback_done(data);
    })
    .fail(function(xhr, _status, _error){
      const respJson = xhr.responseJSON
      const errors   = respJson.errors
      callback_error(errors);
    })
    .always(function(_data){})
}