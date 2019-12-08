let cantidad = 30.00;
let nombre = 'Armando'



$('#btn_palomita').click(function(){
    swal({
        title: "¿Cobrar $" + cantidad + " a " + nombre +"?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
        closeOnClickOutside: false
      })
      .then((willDelete) => {
        if (willDelete) {
          swal( {
            title: "Se ha cobrado con exito a " + nombre,
            icon: "success",
            closeOnClickOutside: false,
          }).then(() => {
              //llamada de generacion a pdf
            swal('se genera el pdf... aqui va la accion');
        })         
          
        } else {
          swal({
              title: "No se ha cobrado a " + nombre,
              icon: "error",
              closeOnClickOutside: false

          });
        }
      });

})


