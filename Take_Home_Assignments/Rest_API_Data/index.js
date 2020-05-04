const PORT = 8000;
const http = require('http');
const projects = require('./data-store');

// Note: this is a requirement by Hackerrank that this is written in http module and not express. The recommended way to approach this is to utilize more modern and convenience library that abstract much of the necessary logic and clear divide of responsibility.

// I wrote this just to pass the written test case. One of the test case was to expect "application/json" while the more modern way would expect "application/json; charset=utf-8"

const get_id = (url) => {
    return url.substring(10)
}

const routes = (req, res) => {
    if (!req.url.startsWith('/projects') || req.method !== "GET") {
        res.writeHead(404)
        res.end()
    } else {
        const id = get_id(req.url)
        const filtered = projects.filter(x => `${x.id}` === id)
        if (!id) {
            res.writeHead(400, {"content-type": "application/json"})
            res.write(JSON.stringify({"message" : "BAD REQUEST"}))
            res.end()
        } else if (!parseInt(id, 10) || filtered.length < 1) {
            console.log("404 here")
            res.writeHead(404)
            res.end()
        } else if (filtered.length === 1) {
            res.writeHead(200, {"content-type": "application/json"})
            res.write(JSON.stringify(filtered[0]))
            res.end()
        }
    }
}

const server = http.createServer(routes).listen(PORT)
console.log('Server is running on 8000')

module.exports = server;




