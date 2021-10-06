
base_url = "http://127.0.0.1:8000"

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let csrftoken = getCookie('csrftoken');

var list_snapshot = []
buildList()

function buildList() {
    var wrapper = document.getElementById('list-wrapper')
    var url = `${base_url}/tracker/api/list-url/`
    fetch(url)
        .then((resp) => resp.json())
        .then(function (data) {
            // console.log('Data:', data)
            var list = data
            for (var i in list) {
                try {
                    document.getElementById(`data-row-${i}`).remove()
                } catch (err) {

                }
                var title = list[i].title
                var link = list[i].url
                var item = `
                    <div class="input-group py-1" id="data-row-${i}">                        
                        <div class="input-group">
                          <span type="text" class="form-control">${title}</span>
                          <a type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#deleteModal"><i class="bi bi-trash"></i></a>   
                          <a type="button" class="btn btn-primary shorten" href="${link}" target="_blank"><i class="bi bi-link-45deg"></i></a>                           
                        </div>                                                
                    </div>`
                wrapper.innerHTML += item
            }

            if (list_snapshot.length > list.length) {
                for (var i = list.length; i < list_snapshot.length; i++) {
                    document.getElementById(`data-row-${i}`).remove()
                }
            }

            list_snapshot = list

            for (var i in list) {
                var deleteBtn = document.getElementsByClassName('delete')[i]
                deleteBtn.addEventListener('click', (function (item) {
                    return function () {
                        deleteItem(item)
                    }
                })(list[i]))

                let copy_link = document.getElementsByClassName('copy')[i]
                copy_link.addEventListener('click', function (item) {
                    let href = document.getElementsByClassName('shorten')[i]
                    href = href.getAttribute("href");
                    // console.log(href)
                    navigator.clipboard.writeText(base_url + href);
                    alert("Copied the text: " + href);

                })
            }

        });
}

navigator
    .share({
        title: document.title,
        text: 'Hello World',
        url: window.location.href
    })
    .then(() => console.log('Successful share! 🎉'))
    .catch(err => console.error(err));
function deleteItem(item) {
    // console.log('Delete clicked')
    fetch(`${base_url}/tracker/api/detail-url/${item.id}/`, {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    }).then((response) => {
        buildList()
    })
}


let form = document.getElementById('form')
form.addEventListener('submit', function (e) {
    e.preventDefault()
    // // console.log('Form submitted')
    let url = `${base_url}/tracker/api/list-url/`
    let long_url = document.getElementById('url').value
    var Http = new XMLHttpRequest();
    Http.open("POST", url);
    Http.setRequestHeader("Accept", "application/json");
    Http.setRequestHeader("Content-Type", "application/json");
    Http.setRequestHeader("X-CSRFToken", csrftoken);

    Http.onreadystatechange = function () {
        if (Http.readyState === 4) {
            // // console.log(Http.status);
            response = JSON.parse(Http.responseText);
            // // console.log(response);
            if (Http.status !== 201) {
                alert(`Error: ${Http.status} \nMsg: ${response["detail"]}`)
            }
        }
        buildList()
        document.getElementById('form').reset()
    }
    data = JSON.stringify({ "url": long_url })
    Http.send(data);
});



let logout = document.getElementById('logout')
logout.addEventListener('click', function (e) {
    const Http = new XMLHttpRequest();
    const url = `${base_url}/accounts/api/logout/`
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        // console.log(Http.responseText)
        if (Http.status == 200) {
            location.reload();
        }
    }
})

