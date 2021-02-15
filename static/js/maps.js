let map;

// Variables containing the locations for each of the three offices 

const shoreditch = [{
    location: {
        lat: 51.5251173,
        lng: -0.0821662
    }
}];

const camden = [{
    location: {
        lat: 51.539128,
        lng: -0.1444557
    }
}];

const watford = [{
    location: {
        lat: 51.6551025,
        lng: -0.4060513
    }
}];

// Initialize and add the map
function initMap(officeLocations) {
    // The location of London
    const mylatlng = {
        lat: 51.5285582,
        lng: -0.2416808
    };
    // The map, centered at London
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: mylatlng,
    });

    // Initalize and render the map for medium screen sizes
    if (window.screen.width < 768) {
        // The location of London
        const mylatlng = {
            lat: 51.5285582,
            lng: -0.2416808
        };
        // The map, centered at London
        const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 9,
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

var officeData = [{
        "officeLocation": "Shoreditch",
        "officeAddress": "16 Charlotte Road, Shoreditch, London, EC2A 3PG",
        "telephoneHeading": "Telephone",
        "phoneNumber": "01284 403847",
        "emailHeading": "Email",
        "emailAddress": "explorelondon@gmail.com"
    },
    {
        "officeLocation": "Camden",
        "officeAddress": "174 Camden High St, Camden Town, London, NW1 0NE",
        "telephoneHeading": "Telephone",
        "phoneNumber": "01284 4583925",
        "emailHeading": "Email",
        "emailAddress": "explorelondon@gmail.com"
    },
    {
        "officeLocation": "Watford",
        "officeAddress": "156 High St, Watford, WD17 2EN",
        "telephoneHeading": "Telephone",
        "phoneNumber": "01284 0394736",
        "emailHeading": "Email",
        "emailAddress": "explorelondon@gmail.com"
    }
];

$(document).ready(function () {
    // This function occurs when the DOM has been loaded
    $(".maps-btn").on('click', function (event) {

        // get the ID of this
        let officeId = $(this).attr("id").replace("-", " ");

        // helper function search the 'officeData' array
        function searchData(key, officeArray) {
            for (var i = 0; i < officeArray.length; i++) {
                // compare the ID being clicked with the officeData value, both toLowerCase()
                if (officeArray[i].officeLocation.toLowerCase() == key.toLowerCase()) {
                    return officeArray[i];
                }
            }
        }
        var office = searchData(officeId, officeData);

        // call the 'getDetails' function, and pass the appropriate office details from 'officeData' array
        getDetails(office.officeLocation, office.officeAddress, office.telephoneHeading, office.phoneNumber, office.emailHeading, office.emailAddress);

    });
});

function getDetails(officeLocation, officeAddress, telephoneHeading, phoneNumber, emailHeading, emailAddress) {
    $("#office-location").text(officeLocation);
    $("#office-address").text(officeAddress);
    $("#telephone-heading").text(telephoneHeading);
    $("#phone-number").text(phoneNumber);
    $("#email-heading").text(emailHeading);
    $("#email-address").text(emailAddress);

};

// ** Sources of guidance used to create this code

// https://developers.google.com/maps/documentation/javascript/adding-a-google-map
// https://developers.google.com/maps/documentation/javascript/markers
// https://github.com/mkthewlis/Milestone-Project-2
// https://stackoverflow.com/questions/17746737/how-to-append-string-to-a-href-with-jquery-or-javascript
// https://stackoverflow.com/questions/32772363/how-does-this-hash-work/32772416#32772416