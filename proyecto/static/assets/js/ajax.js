

function llamarAjax(pagina, parametros, fretorna) {
    if (parametros instanceof FormData) {
        $.ajaxSetup({ cache: false, contentType: false, processData: false });
    } else {
        $.ajaxSetup({ cache: true, contentType: 'application/x-www-form-urlencoded; charset=UTF-8', processData: true });
    }
    $.ajax({
        type: 'POST',
        url: pagina,
        data: parametros,
        dataType: "json",
        success: function (data) {
            if ($.isFunction(fretorna))
                fretorna(data);
        },
        error: function (xhr, textStatus, error) {
            console.log("Status:" + xhr.statusText);
            console.log("Tipo: " + textStatus);
            console.log(error);
        }
    });
}


