var http = require('http');

http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('Hello Node user');
    res.end();
}).listen(3000);
console.log('Listening on 3000');