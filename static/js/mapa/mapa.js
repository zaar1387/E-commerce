document.addEventListener('DOMContentLoaded', function () {

// Inicializa el mapa y establece la vista inicial
var map = L.map('map');

// Agrega el mapa base de OpenStreetMap
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

 // Solicita la ubicación actual del usuario
 map.on('locationfound', onLocationFound);
 map.on('locationerror', onLocationError);
 map.locate({ setView: true, maxZoom: 16 });

 // Función para manejar la geolocalización exitosa
 function onLocationFound(e) {
    var radius = e.accuracy / 2;
    var userLatLng = e.latlng;
    L.marker(userLatLng).addTo(map)
    .bindPopup('Tú ubicación')
    .openPopup();
    L.circle(userLatLng, radius).addTo(map);
    let coordinates = {
        lat: userLatLng.lat,
        lng: userLatLng.lng
    };
    enviarCoordenadas(coordinates);
}

function onLocationError(e) {
    alert(e.message);
}

});


 // Función para enviar coordenadas al servidor a través de AJAX y realizar la llamada telefónica
 function enviarCoordenadas(coordinates) {
   
    // $.ajax({
    //     url: 'url_get_mapa', 
    //     method: 'POST',
    //     data: JSON.stringify({ coordinates: coordinates }),
    //     contentType: 'application/json',
    //     success: function (response) {
        
    //       alert('Coordenadas registradas correctamente');
         
    //   },
    //     error: function (xhr, status, error) {
    //         console.error('Error al enviar las coordenadas:', error);
    //         alert('Error al enviar las coordenadas. Por favor, inténtalo de nuevo.');
    //     }
    // });





    $.ajax({
        url: 'url_get_mapa',
        data: {coordinates:coordinates},
        type: 'POST',
            success: function (response) {
                let data = JSON.parse(response);
                if(data.status == 1){
                    alert('Coordenadas registradas correctamente');
                }else{
                    alert('Error al enviar las coordenadas. Por favor, inténtalo de nuevo.');
                }
            },
            error: function (error) {
            console.log(error);
        }
    });
  }