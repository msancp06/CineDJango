$(document).ready(function(){
  $('select.selectPelicula').change(function () {

    var pelicula = $(this).find("option:selected");
    var opcionPelicula  = pelicula.val();
    var idPelicula = parseInt(opcionPelicula, 10);

    //url en django?
    $.ajax({
      url: "getSesionesAjax",
      cache:'false',
      data: {'idPelicula' : idPelicula },
      type:"GET",
      success: function(data){
        $(".selectSesion option.sesion").remove();
        for (var i = data.length - 1; i >= 0; i--) {
          $(".selectSesion").append('<option class="sesion" sala=" '+ data[i].sala +' " id="' + data[i].idVisualizacion + '"> Sesion: '+ data[i].sesion +'</option>');
        }
      }


  });

  $('select.selectSesion').change(function (){
    var sala = $('option:selected', this).attr('sala');
    $(".salaDePelicula").html("Sala: " + sala);
  });

  });
});

function verSesiones(visualizaciones) {
  var idPelicula;
  var select;
  select = document.getElementsByClassName("selectPelicula");
  idPelicula = select.options[select.selectedIndex].value;

  for(var i = 0; i<visualizaciones.length; i++){
    alert(visualizaciones[i].pelicula);
  }

}
