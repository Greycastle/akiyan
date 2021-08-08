let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), { zoom: 8});


  const infoWindow = new google.maps.InfoWindow();
  const markers = []
  for (let place of nagano) {
    const marker = new google.maps.Marker({
        position: { lat: place['latitude'], lng: place['longitude'] },
        map,
        title: place['locationRaw'],
        customInfo: place
    });
    markers.push(marker.position)
    title = place['locationRaw']
    
    price = parseInt(place['price']) / 10000
    price = `${price}万円`
    const content = `<div class="info"><h3>${title}</h3><div class="price">${price}</div><div class="pics"><img src="${place['image1']}"/><img src="${place['image2']}"/><img src="${place['image3']}"/></div><div><a target="_blank" href="${place['url']}">Open link</a></div></div>`
    marker.addListener("click", () => {
        infoWindow.close();
        infoWindow.setContent(content);
        infoWindow.open(marker.getMap(), marker);
    });
  }

    var bounds = new google.maps.LatLngBounds();
    for (var i = 0; i < markers.length; i++) {
        bounds.extend(markers[i]);
    }

    map.fitBounds(bounds);
}