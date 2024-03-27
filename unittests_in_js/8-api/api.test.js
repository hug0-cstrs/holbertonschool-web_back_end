// Importation du module 'assert' pour les assertions
const request = require("request"); // Importation du module 'request' pour effectuer des requêtes HTTP

const url = "http://127.0.0.1:7865"; // L'URL de l'API à tester

describe("Index page", () => {
  // Suite de tests pour la page d'accueil
  it("Good Status", (done) => {
    // Cas de test pour vérifier le code de statut
    request(url, (err, res, body) => {
      // Faire une requête GET à l'URL
      assert.equal(res.statusCode, 200); // Vérifier que le code de statut est 200 (OK)
      done(); // Appeler le rappel 'done' pour indiquer que le test est terminé
    });
  });

  it("Correct output", (done) => {
    // Cas de test pour vérifier le corps de la réponse
    request(url, (err, res, body) => {
      // Faire une requête GET à l'URL
      assert.equal(body, "Welcome to the payment system"); // Vérifier que le corps de la réponse est 'Welcome to the payment system
      done(); // Appeler le rappel 'done' pour indiquer que le test est terminé
    });
  });

  it("No error response", (done) => {
    // Cas de test pour vérifier s'il y a des erreurs
    request(url, (err, res, body) => {
      // Faire une requête GET à l'URL
      assert.equal(err, null); // Vérifier qu'il n'y a pas d'erreurs (err est null)
      done(); // Appeler le rappel 'done' pour indiquer que le test est terminé
    });
  });
});
