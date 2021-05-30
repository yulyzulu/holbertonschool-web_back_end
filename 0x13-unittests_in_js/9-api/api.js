const express = require('express');

const app = express();

app.get('/', function(req, res) {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', function(req, res) {
  res.send(`Payment methods for cart ${req.params.id}`);
});

app.listen(7865, function() {
  console.log('API available on localhost port 7865');
});
