var init_point_factory = function(point) {
    return function(map, options) {
        var latlng = [point.coordinates[1],
                      point.coordinates[0]];
        L.marker(latlng).addTo(map);
        map.setView(latlng, 16);

        //var div = $(map.getContainer()).closest('.same-y');
        //var resize = function() {
        //    div.height(div.width());
        //    map.invalidateSize(false);
        //};
        //$(window).resize(function() {
        //    resize();
        //});
        //resize();
    }
}