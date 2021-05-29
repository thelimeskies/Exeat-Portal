function Approve(exeat_id) {
    var i = exeat_id
    console.log(exeat_id)
    $.ajax({
        url: '/ajax/approve',
        data: {'i': i},
        dataType: 'json',
        success: function (data) {
            location.reload()
        }

    })

}

function Accept(exeat_id) {
    var i = exeat_id
    $.ajax({
        url: '/ajax/accept',
        data: {'i': i},
        dataType: 'json',
        success: function (data) {
            location.reload()
        }

    })

}

function ClockIn(id) {
    var i = id
    $.ajax({
        url: '/ajax/clock_in',
        data: {'i': i},
        dataType: 'json',
        success: function (data) {
            location.reload()
        }

    })

}

function ClockOut(id) {
    var i = id
    $.ajax({
        url: '/ajax/clock_out',
        data: {'i': i},
        dataType: 'json',
        success: function (data) {
            location.reload()
        }

    })

}


