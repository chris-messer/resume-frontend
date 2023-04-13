

function getCount() {
    let c = fetch("https://r65f0mds6j.execute-api.us-east-1.amazonaws.com/Prod/read_count")
                .then(res => {
                    return res.json();
                })
                .then(data => {
                    const markup = `<p>Visitor Count: ${data.count}</p>`;
                    document.querySelector('dt').insertAdjacentHTML('beforeend', markup)
                });
    return c
}

getCount()

