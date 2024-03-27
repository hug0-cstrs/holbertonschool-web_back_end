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
      const options = {
        url: 'http://localhost:7865/cart/12',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 12');
        done();
      });
    });
  });

  describe('GET /cart/8', () => {
    it('Responds with 200 and id 1 in msg', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/1',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 8');
        done();
      });
    });
  });

  describe('GET /cart/111', () => {
    it('Responds with 200 and id 12 in msg', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/123',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 111');
        done();
      });
    });
  });

  describe('GET /cart/k47', () => {
    it('Responds with 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/k47',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('GET /cart/s56z', () => {
    it('Responds with 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/s56z',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('GET /cart/96a', () => {
    it('Responds with 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/96a',
        method: 'GET',
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('GET /cart/hello', () => {
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

  describe('GET /cart/', () => {
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
});
