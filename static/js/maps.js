// Initialize and add the map
      function initMap() {
        // The location of office1
        const office1 = { lat: 51.5259342, lng: -0.0833539 };
        // The map, centered at office1
        const map = new google.maps.Map(document.getElementById("map"), {
          zoom: 10,
          center: office1,
        });
        // The marker, positioned at Uluru
        const marker = new google.maps.Marker({
          position: office1,
          map: map,
        });
      }