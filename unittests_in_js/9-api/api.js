const express = require('express'); // Import express module to create the server

const app = express(); // Create the server
const port = 7865; // Define the port

app.get('/', (req, res) => { // Define the main route
  res.end('Welcome to the payment system'); // Send the response
});

app.get('/cart/:id([0-9]+)', (req, res) => { // Define the cart route
  res.end(`Payment methods for cart ${req.params.id}`); // Send the response
});

app.listen(port, () => { // Start the server
  console.log('API available on localhost port 7865'); // Display the message
});