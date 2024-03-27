const request = require('request'); // Import request module to make HTTP requests
const { expect } = require('chai'); // Import expect module to use BDD style assertions

describe('Integration Testing', () => { // Describe the test suite for the API
  describe('GET /', () => { // Describe the test suite for the main route
    it('Code: 200 | Body: Welcome to the payment system', (done) => { // Test case for the main route
      const options = { // Define the request options
        url: 'http://localhost:7865', // Define the URL
        method: 'GET', // Define the method
      };

      request(options, function (error, response, body) { // Make the request to the server and define the callback
        expect(response.statusCode).to.equal(200); // Assert the status code
        expect(body).to.equal('Welcome to the payment system'); // Assert the response body
        done(); // End the test
      });
    });
  });

  describe('GET /cart/12', () => { // Describe the test suite for the cart route
    it('Responds with 200 and id 12 in msg', (done) => { // Test case for the cart route
      const options = { // Define the request options
        url: 'http://localhost:7865/cart/12', // Define the URL
        method: 'GET', // Define the method
      };

      request(options, function (error, response, body) { // Make the request to the server and define the callback
        expect(response.statusCode).to.equal(200); // Assert the status code
        expect(body).to.equal('Payment methods for cart 12'); // Assert the response body
        done(); // End the test
      });
    });
  });

  describe('GET /cart/1', () => { // Describe the test suite for the cart route
    it('Responds with 200 and id 1 in msg', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/1',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 1');
        done();
      });
    });
  });

  describe('GET /cart/123', () => { // Describe the test suite for the cart route with 123
    it('Responds with 200 and id 12 in msg', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/123',
        method: 'GET',
      };

      request(options, function (error, response, body) { // Make the request to the server and define the callback
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 123');
        done();
      });
    });
  });

  describe('GET /cart/a12', () => { // Describe the test suite for the cart route with a12
    it('Responds with 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/a12',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('GET /cart/a12b', () => { // Describe the test suite for the cart route with a12b
    it('Responds with 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/a12b',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('GET /cart/12b', () => { // Describe the test suite for the cart route with 12b
    it('Responds with 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/12b',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('GET /cart/hello', () => { // Describe the test suite for the cart route with hello
    it('Responds with 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/hello',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('GET /cart/', () => { // Describe the test suite for the cart route with no id
    it('Responds with 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('GET /available_payments JSON string', () => { // Describe the test suite for the available_payments route
    it('Responds with 200 and correct JSON string', (done) => {
      const options = {
        url: 'http://localhost:7865/available_payments',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal(
          '{"payment_methods":{"credit_cards":true,"paypal":false}}'
        );
        done();
      });
    });
  });

  describe('GET /available_payments JSON parsed', () => { // Describe the test suite for the available_payments route
    it('Responds with 200 and correct JSON object when parsed', (done) => { // Test case for the available_payments route
      const options = { // Define the request options
        url: 'http://localhost:7865/available_payments', // Define the URL
        method: 'GET', // Define the method
      };

      request(options, function (error, response, body) { // Make the request to the server and define the callback
        expect(response.statusCode).to.equal(200); // Assert the status code
        const bodyParsed = JSON.parse(body); // Parse the response body

        const referenceBody = { // Define the reference object
          payment_methods: { // Define the payment_methods object
            credit_cards: true, // Define the credit_cards key
            paypal: false, // Define the paypal key
          },
        };

        expect(bodyParsed).to.deep.equal(referenceBody); // Assert the response body
        done(); // End the test
      });
    });
  });

  describe('POST /login with body', () => { // Describe the test suite for the login route with body
    it('Responds with 200 and correct name Betty', (done) => {
      const options = {
        url: 'http://localhost:7865/login',
        method: 'POST',
        json: {
          userName: 'Betty',
        },
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      });
    });
  });

  describe('POST /login with no body', () => { // Describe the test suite for the login route with no body
    it('Responds with 200 and correct name Undefined', (done) => {
      const options = {
        url: 'http://localhost:7865/login',
        method: 'POST',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome undefined');
        done();
      });
    });
  });
});