$(document).ready(function() {
    $('#elections').DataTable( {
        "ajax": {
            "url": "/api/us_elections",
            "dataSrc": "data"
        }
    });
});