const express = require('express');
const {Sequelize} = require('sequelize');
const { Json } = require('sequelize/types/lib/utils');

const app = express();
const sequelize = new Sequelize({
    dialect : 'sqlite',
    storage : './test.db'
});

var json_t = require('./Public/testingjson.json');

/*app.get('/', function(req,res){
    URL = req.url;
    res.send(URL);
})
*/

app.use('/index', function(req, res) {
    res.send('Welcome to index');
    res.send(JSON.stringify(json_t));
});

app.set('view engine', 'ejs');

app.get('/', function(req, res) {
    res.render('index.ejs');
});

app.use('/asset', express.static(__dirname + '/public'));

app.listen(3000,'127.0.0.1');