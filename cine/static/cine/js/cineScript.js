var entradasReservadas = new Array();

$(document).ready(function(){
  $('.noRef').on('click', function(e){
    e.preventDefault();
  });
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

  $('select.navPeliculas').change( function() {
    var opcion = $(this).find("option:selected");
    var url = opcion.attr('url');
    if(url){
      window.location = url;
    }
    return false;
  });
});





function cargarSala(filas, asientosPorFila, asientosUltimafila, idVisualizacion){

  //Buscamos las entradas correspondientes a
  $.ajax({
    url: "getEntradasAjax",
    cache:'false',
    data: {'idVisualizacion' : idVisualizacion },
    type:"GET",
    success: function(data){
      expandirSala(filas, asientosPorFila, asientosUltimafila, data, idVisualizacion);
    }
  });
}
function expandirSala(filas, asientosPorFila, asientosUltimafila, entradas, idVisualizacion){

  var claseVisualizacion = ".vis" + idVisualizacion + "Sala";

  $(claseVisualizacion).html("");
  for(var i = 0; i<filas-1; i++){
		for(var j = 0; j<asientosPorFila; j++){
			if(j == 0){
				$(claseVisualizacion).append($('<div fila="'+(i+1)+'" asiento="'+(j+1)+'" class="celda fila">'+(j+1)+'<input type="checkbox" name="checks[]" value="' + idVisualizacion + ',' + (i+1) + ',' + (j+1) + '"/>' +'</div>'));
			}else{
				$(claseVisualizacion).append($('<div fila="'+(i+1)+'" asiento="'+(j+1)+'" class="celda ">'+(j+1)+ '<input type="checkbox" name="checks[]" value="' + idVisualizacion + ',' + (i+1) + ',' + (j+1) + '"/>' +'</div>'));
			}
      if(j+1 == (asientosPorFila/2)){
        $(claseVisualizacion).append($('<div fila="'+(i+1)+'" class="celdaPasillo"></div>'));
      }
		}
	}
  for(var j = 0; j<asientosUltimafila; j++){
    if(j == 0){
      $(claseVisualizacion).append($('<div fila="'+(i+1)+'" asiento="'+(j+1)+'" class="celda fila">'+(j+1)+'<input type="checkbox" name="checks[]" value="' + idVisualizacion + ',' + (i+1) + ',' + (j+1) + '"/>' +'</div>'));
    }else{
      $(claseVisualizacion).append($('<div fila="'+(i+1)+'" asiento="'+(j+1)+'" class="celda">'+(j+1)+'<input type="checkbox" name="checks[]" value="' + idVisualizacion + ',' + (i+1) + ',' + (j+1) + '"/>' +'</div>'));
    }
  }

  for(var i = 0; i<entradas.length; i++){
    $(claseVisualizacion + ' [fila = "' + entradas[i].fila + '"][asiento = "' + entradas[i].asiento + '"]').removeClass("celda").addClass("celdaOcupada").children('input').prop('disabled', true);
  }

  $(claseVisualizacion).toggle("slow");

  $(":checkbox").on("click", function(){
    $(this).parent.toggleClass('celdaSeleccionada');
    /*
    var sesionPeli = $(this).parent().attr('class').replace('vis','').replace('Sala','');
    var filaPeli = $(this).attr('fila');
    var asientoPeli = $(this).attr('asiento');

    var entrada = sesionPeli + "." + filaPeli + "." + asientoPeli;

    var entrada = new Object();
    entrada.sesion = sesionPeli;
    entrada.fila = filaPeli;
    entrada.asiento = asientoPeli;

    entradasReservadas.push(entrada);
*/
  });
}

function reservar(){

  $.ajax({
    url: "saveEntradasAjax",
    cache:'false',
    data: {'arrayEntradas[]' : entradasReservadas },
    type:"GET",
    success: function(data){
      setTimeout("location.reload(true);", 1500);
    }
  });
}

function filtar(){
  var opcion = $(this).find("option:selected");
  var url = opcion.attr('filtrar');
  if(url){
    window.location = url;
  }
  return false;
}


function verSesiones(visualizaciones) {
  var idPelicula;
  var select;
  select = document.getElementsByClassName("selectPelicula");
  idPelicula = select.options[select.selectedIndex].value;

  for(var i = 0; i<visualizaciones.length; i++){
    alert(visualizaciones[i].pelicula);
  }

}
