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

function Extend(id) {
    var i = id
    $.ajax({
        url: '/ajax/extend',
        data: {'i': i},
        dataType: 'json',
        success: function (data) {
            location.reload()
        }

    })

}

function Disapprove(id) {
    var i = id
    var reason = document.getElementById('floatingInput'.concat(id)).value
    $.ajax({
        url: '/ajax/disapprove',
        data: {'i': i, 'j' : reason},
        dataType: 'json',
        success: function (data) {
            location.reload()
        }

    })

    }


