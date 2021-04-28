$(document).ready(() => {
    $(".comentar").on("click", e => {
        
        // console.log({ ...$(e.target).data(), ...{ comentario: $(e.target).closest(".rutina").find(".comentario").val() } });
        
        $.ajax({
            url: "/comentar/",
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                ...$(e.target).data(),
                ...{ comentario: $(e.target).closest(".rutina").find(".comentario").val() },
                
            },
            method: "POST",
            success: e => {
                alert(e)
            }
        }
        );
        // $("#form_clasificacion").submit()
    })
    $("#sitio").change(e => {
        $("#form_clasificacion").submit()
    })
})