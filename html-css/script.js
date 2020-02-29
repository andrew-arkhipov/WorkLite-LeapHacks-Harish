$(document).ready(function () {

    var firebaseConfig = {
        apiKey: "AIzaSyDofv8FSUNrBM7mQ-on5oMQRO3IpGaEKq4",
        authDomain: "worklite-1ab69.firebaseapp.com",
        databaseURL: "https://worklite-1ab69.firebaseio.com",
        storageBucket: "worklite-1ab69.appspot.com",
    };
    firebase.initializeApp(firebaseConfig);

    var database = firebase.database();

    // get customer from firebase database
    $("#login").click(function () {
        var ref = database.ref("Firms/" + $("#firm").val());
        ref.once("value", gotData, errData);
    });

    // if customer exists, cache ffn and relocate to booker view
    function gotData(data) {
        console.log(data.val());
        if(!(data.val() == null))
        {
            localStorage.setItem("firm", $("#firm").val());
            $(location).attr("href", "home.html");
        }
    }

    function errData(data) {
        console.log("Error!");
    }

});