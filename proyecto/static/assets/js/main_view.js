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

$(document).ready(() => {
    const csrftoken = getCookie('csrftoken');
    $(".comentar").on("click", e => {
        $.ajax({
            url: "/comentar/",
            headers: { 'X-CSRFToken': csrftoken },
            data: {
                ...$(e.target).data(),
                ...{ comentario: $(e.target).closest(".rutina").find(".comentario").val() }
            },
            method: "POST",
            success: () => {
                $(e.target).closest(".rutina").find(".comentario").val("")
            }
        });
    });

    $(".seguir").on("click", e => {
        console.log($(e.target).data());
        $.ajax({
            url: "/seguirRutina/",
            headers: { 'X-CSRFToken': csrftoken },
            data: $(e.target).data(),
            method: "POST",
            success: () => {
                console.log("segui la rutina");
            }
        });
    });
})


