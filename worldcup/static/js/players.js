ADD_PLAYER_URL = '/players/insert';
GET_PLAYER_URL = '/players/get_players';

var addPlayer = function () {
    var data = {
        'name': $('#name').val(),
        'teamName': $('#team-name').val(),
        'runs': $('#runs').val(),
        'wickets': $('#wickets').val(),
        'rank': $('#rank').val()

    };

    $.ajax({
        type: "POST",
        url: ADD_PLAYER_URL,
        dataType: 'json',
        data: data,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))
        },
        success: function (data) {
            console.log("success")
            window.location = '/players/'
        },
        error: function (err) {
            console.log("An error occurred")
        }

    })
}

var showPlayerDetails = function (filter) {
    var url = GET_PLAYER_URL;
    if (filter) {
        url = GET_PLAYER_URL + '?country=' + filter
    }

    $.ajax({
        type: 'GET',
        dataType: 'json',
        async: false,
        url: url,
        contentType: 'application/json',
        success: function (data) {
            generateTable(data.data, 'players-table')
        },
        error: function (err) {
            console.log("An error occurred " + err)
        }
    })

};


function generateTable(data, parentDivId) {
    //Create a HTML Table element.
    var table = document.createElement("table");
    table.border = "1";

    //Get the count of columns.
    var columnCount = data[0].length;

    //Add the header row.
    var row = table.insertRow(-1);
    for (var i = 0; i < columnCount; i++) {
        var headerCell = document.createElement("th");
        headerCell.innerHTML = data[0][i];
        row.appendChild(headerCell);
    }

    //Add the data rows.
    for (var i = 1; i < data.length; i++) {
        row = table.insertRow(-1);
        for (var j = 0; j < columnCount; j++) {
            var cell = row.insertCell(-1);
            cell.innerHTML = data[i][j];
        }
    }

    var dvTable = document.getElementById(parentDivId);
    dvTable.innerHTML = "";
    dvTable.appendChild(table);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function goToAddPlayerPage() {
    window.location = '/players/addPlayerPage'
}
