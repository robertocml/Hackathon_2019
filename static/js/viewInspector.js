let cantidad = 30.00;
let nombre = 'Armando'



$('#btn_palomita').click(function () {
  swal({
    title: 'Buscando usuario...',
    timer: 1000,
    buttons: false
  }).then(() => {
    $('#form_view').submit(() => {

      //hacer el submit y no se hace reload de la pagina
      return false;

    })
  }).then(() => (

    swal({
      title: "¿Cobrar $" + cantidad + " a " + $("#oferente").val() + $("#id_oferente").val() + "?",
      icon: "warning",
      buttons: true,
      dangerMode: true,
      closeOnClickOutside: false
    })
      .then((willDelete) => {
        if (willDelete) {
          swal({
            title: "Se ha cobrado con exito a " + $("#oferente").val() + $("#id_oferente").val(),
            icon: "success",
            closeOnClickOutside: false,
          }).then(() => {
            //llamada de generacion a pdf
            swal('se genera el pdf... aqui va la accion');

          })

        } else {
          swal({
            title: "No se ha cobrado a " + $("#oferente").val(),
            icon: "error",
            closeOnClickOutside: false

          });
        }
      })));

})

$('#btn_edita').click(() => {
  window.location.assign("edita");
})

$('#btn_add').click(() => {
  window.location.assign("agrega");
})


