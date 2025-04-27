//  $(document).ready(function () {




// // document.addEventListener('DOMContentLoaded', function () {

// // // Inicializa el mapa y establece la vista inicial
// // var map = L.map('map');

// // Agrega el mapa base de OpenStreetMap
// // L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
// //     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// // }).addTo(map);

// //  // Solicita la ubicación actual del usuario
// //  map.on('locationfound', onLocationFound);
// //  map.on('locationerror', onLocationError);
// //  map.locate({ setView: true, maxZoom: 16 });

// //  // Función para manejar la geolocalización exitosa
// //  function onLocationFound(e) {
// //     var radius = e.accuracy / 2;
// //     var userLatLng = e.latlng;
// //     L.marker(userLatLng).addTo(map)
// //     .bindPopup('Tú ubicación')
// //     .openPopup();
// //     L.circle(userLatLng, radius).addTo(map);
// //     let coordinates = {
// //         lat: userLatLng.lat,
// //         lng: userLatLng.lng
// //     };
// //     enviarCoordenadas(coordinates);
// // }

// // function onLocationError(e) {
// //     alert(e.message);
// // }

// // });


// navigator.geolocation.getCurrentPosition(function(position) {
//     const coords = {
//         latitude: position.coords.latitude,
//         longitude: position.coords.longitude
//     };

//     // Enviar coordenadas a tu backend en Python
//     // fetch('/guardar_ubicacion', {
//     //     method: 'POST',
//     //     headers: {
//     //         'Content-Type': 'application/json'
//     //     },
//     //     body: JSON.stringify(coords)
//     // });
//     enviarCoordenadas(coords);
// });


//  // Función para enviar coordenadas al servidor a través de AJAX
//  function enviarCoordenadas(coordinates) {
//     $.ajax({
//         url: 'url_get_mapa',
//         data: {coordinates:coordinates},
//         type: 'POST',
//             success: function (response) {
//                 let data = JSON.parse(response);
//                 // let data = JSON.parse(JSON.stringify(response));
//                 if(data.status == 1){
//                     alert('Coordenadas registradas correctamente');
//                 }else{
//                     alert('Error al enviar las coordenadas. Por favor, inténtalo de nuevo.');
//                 }
//             },
//             error: function (error) {
//             console.log(error);
//         }
//     });
//   }
// });

// //   let dataOriginal = JSON.parse(jsonOriginal);
// //   // Función para transformar las coordenadas al formato deseado
// //   function transformarCoordenadas(data) {
// //       let coordenadas = data.data.map(coord => {
// //           // Convertimos las coordenadas de string a número
// //           return [parseFloat(coord[0]), parseFloat(coord[1])];
// //       });
      
// //       return { coordenadas: coordenadas };
// //   }
// //   // Transformamos las coordenadas
// //   let resultado = transformarCoordenadas(dataOriginal);
// //   // Imprimimos el resultado
// //   console.log(JSON.stringify(resultado, null, 2));






// // Función para visualizar las coordenadas en el mapa
// function visualizarCoordenadas(coordenadas) {
//     if (!coordenadas || coordenadas.length === 0) {
//         console.error("No hay coordenadas para mostrar.");
//         return;
//     }
//     coordenadas.forEach(coord => {
//         if (Array.isArray(coord) && coord.length === 2) {
//             let marker = L.marker(coord).addTo(map);
//             marker.bindPopup(`Coordenadas: ${coord[0]}, ${coord[1]}`).openPopup();
//         } else {
//             console.error("Formato de coordenadas inválido:", coord);
//         }
//     });
// }



// if ("geolocation" in navigator) {
//     navigator.geolocation.getCurrentPosition(
//         function(position) {
//             const coordinates = {
//                 lat: position.coords.latitude,
//                 lng: position.coords.longitude
//             };
//             // console.log("Coordenadas obtenidas:", coordinates);

//             // Enviar al servidor
//             // fetch('/guardar_ubicacion', {
//             //     method: 'POST',
//             //     headers: {
//             //         'Content-Type': 'application/json'
//             //     },
//             //     body: JSON.stringify(coords)
//             // });
//             $.ajax({
//                         url: 'url_get_mapa',
//                         data: {coordinates:coordinates},
//                         type: 'POST',
//                             success: function (response) {
//                                 let data = JSON.parse(response);
//                                 // let data = JSON.parse(JSON.stringify(response));
//                                 if(data.status == 1){
//                                     // alert('Coordenadas registradas correctamente');
//                                 }else{
//                                     alert('Error al enviar las coordenadas. Por favor, inténtalo de nuevo.');
//                                 }
//                             },
//                             error: function (error) {
//                             console.log(error);
//                         }
//                     });
//         },
//         function(error) {
//             switch(error.code) {
//                 case error.PERMISSION_DENIED:
//                     alert("Permiso de ubicación denegado por el usuario.");
//                     break;
//                 case error.POSITION_UNAVAILABLE:
//                     alert("Información de ubicación no disponible.");
//                     break;
//                 case error.TIMEOUT:
//                     alert("La solicitud de ubicación ha tardado demasiado.");
//                     break;
//                 case error.UNKNOWN_ERROR:
//                     alert("Error desconocido.");
//                     break;
//             }
//         }
//     );
// } else {
//     alert("La geolocalización no es compatible con este navegador.");
// }

// });