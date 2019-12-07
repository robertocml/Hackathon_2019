let cantidad = '30.00'


$('#btn_palomita').click(function(){
    swal({
        title: "Cobrar $ " + cantidad + " ?",
        text: "Once deleted, you will not be able to recover this imaginary file!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
        closeOnClickOutside: false
      })
      .then((willDelete) => {
        if (willDelete) {
          swal("Poof! Your imaginary file has been deleted!", {
            icon: "success",
          });
        } else {
          swal("Your imaginary file is safe!");
        }
      });

})


