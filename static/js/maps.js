let map;

// Variables containing the locations for each of the three offices 

const shoreditch = [{
    location: { 
        lat: 51.5251173,
        lng: -0.0821662
}}];

const camden = [{
    location: {
        lat: 51.539128,
        lng: -0.1444557
}}];

const watford = [{
    location: {
        lat: 51.6551025,
        lng: -0.4060513
}}];

// Initialize and add the map
      function initMap(officeLocations) {
        // The location of London
        const mylatlng = { lat: 51.5285582, lng: -0.2416808 };
        // The map, centered at London
        const map = new google.maps.Map(document.getElementById("map"), {
          zoom: 10,
          center: mylatlng,
        });
    

    if (officeLocations) {
        for (let i = 0; i < officeLocations.length; i++) {
        const marker = new google.maps.Marker({
          position: officeLocations[i].location,
          animation: google.maps.Animation.DROP,
          map: map,
        });
        }
    }
}
document.getElementById("shoreditch").addEventListener("click", () => {
    initMap(shoreditch);
});

document.getElementById("watford").addEventListener("click", () => {
    initMap(watford);
});

document.getElementById("camden").addEventListener("click", () => {
    initMap(camden);
});