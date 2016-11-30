$(document).ready(function() {
    $('#elections').DataTable( {
        "ajax": {
            "url": "/json",
            "dataSrc": "data"
        }
    });
});