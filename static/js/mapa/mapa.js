document.addEventListener('DOMContentLoaded', function () {

// var map = L.map('map').setView([4.599860, -74.162560], 13);


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
    // .bindPopup('<b>Tu ubicación actual.</b><br><a href="#" id="panic-button" class="panic-button"><img src="https://cdn.iconfinder.com/data/icons/basic-ui-elements-coloricon/21/24-512.png" alt="Llamar">Tú ubicación</a>')
    .bindPopup('Tú ubicación')
    .openPopup();
    L.circle(userLatLng, radius).addTo(map);
    // document.querySelector('#panic-button').addEventListener('click', function (e) {
    //     e.preventDefault();
        // var coordinates = {
        //     lat: userLatLng.lat,
        //     lng: userLatLng.lng
        // };
        //enviarCoordenadas(coordinates);
    // });
}

function onLocationError(e) {
    alert(e.message);
}

});