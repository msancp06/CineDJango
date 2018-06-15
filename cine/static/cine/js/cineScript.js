$(document).ready(function(){
  $('select.selectPelicula').change(function () {

    //Si cambia la peli, ponemos a 0 la sesion
    var select = $('select.selectSesion');
    select.val($('option:first', select).val());

    var pelicula = $(this).find("option:selected");
    var opcionPelicula  = pelicula.val();
    var idPelicula = parseInt(opcionPelicula, 10);

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
  });

  $('select.selectSesion').change(function (){
    var idSala = $('option:selected', this).attr('sala');
    $(".salaDePelicula").html("Sala: " + idSala);

    $.ajax({
      url: "getSalasAjax",
      cache:'false',
      data: {'idSala' : idSala },
      type:"GET",
      success: function(data){
        //alert("Filas: " + data[0].filas + " Asiento/Fila: " + data[0].asientosPorFila + " UltimaFila: " + data[0].asientosUltimaFila);
        crearSala(parseInt(data[0].filas, 10), parseInt(data[0].asientosPorFila, 10), parseInt(data[0].asientosUltimaFila, 10));
      }
    });


  });

});

function crearSala(filas, asientosPorFila, asientosUltimafila){
  $("div.sala").html("");
  for(var i = 0; i<filas; i++){
		for(var j = 0; j<asientosPorFila; j++){
			if(j == 0){
				$("div.sala").append($('<div class="celda fila"></div>'));
			}else{
				$("div.sala").append($('<div class="celda"></div>'));
			}
      if(j+1 == (asientosPorFila/2)){
        $("div.sala").append($('<div class="celdaPasillo"></div>'));
      }
		}
	}
  for(var j = 0; j<asientosUltimafila; j++){
    if(j == 0){
      $("div.sala").append($('<div class="celda fila"></div>'));
    }else{
      $("div.sala").append($('<div class="celda"></div>'));
    }
  }

}

/*
function quitarOverlay(){
  $("#overlay").css('display', 'none');
}

function cargarOverlay(){
  $("#overlay").css('display', 'block');
}
*/

function verSesiones(visualizaciones) {
  var idPelicula;
  var select;
  select = document.getElementsByClassName("selectPelicula");
  idPelicula = select.options[select.selectedIndex].value;

  for(var i = 0; i<visualizaciones.length; i++){
    alert(visualizaciones[i].pelicula);
  }

}
