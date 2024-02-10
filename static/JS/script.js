$(document).ready(function(){
    $("button").on("click", function(){
        $("button").html("MERCI!")
    })
    $("button").bind("contextmenu", function(e){
        e.preventDefault();
        alert("Votre message a bien été envoyé.");
    })
})