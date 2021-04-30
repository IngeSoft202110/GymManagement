$(document).ready(() => {


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    $(".comentar").on("click", e => {
        
        // console.log({ ...$(e.target).data(), ...{ comentario: $(e.target).closest(".rutina").find(".comentario").val() } });
        
        $.ajax({
            url: "/comentar/",
            headers: {'X-CSRFToken': csrftoken},
            data: {
                ...$(e.target).data(),
                ...{ comentario: $(e.target).closest(".rutina").find(".comentario").val() }
            },
            method: "POST",
            success: () => {
                
                comentario: $(e.target).closest(".rutina").find(".comentario").val("")
                
            }
        }
        );
        
    })
    // $("#sitio").change(e => {
    //     $("#form_clasificacion").submit()
    // })
})


