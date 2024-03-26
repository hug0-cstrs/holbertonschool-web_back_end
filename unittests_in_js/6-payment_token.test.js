const chai = require('chai'); // Importation de la bibliothèque Chai pour les assertions
const getPaymentTokenFromAPI = require('./6-payment_token'); // Importation de la fonction getPaymentTokenFromAPI depuis le fichier 6-payment_token.js

describe('getPaymentTokenFromAPI', () => { // Définition d'une suite de tests pour la fonction getPaymentTokenFromAPI
  it('should return a payment token when API call is successful', (done) => { // Définition d'un test qui vérifie si la fonction renvoie un jeton de paiement en cas d'appel API réussi
    getPaymentTokenFromAPI(true) // Appel de la fonction getPaymentTokenFromAPI avec un argument true
      .then((res) => { // Utilisation de la promesse renvoyée par la fonction
        chai.expect(res).to.have.property('data'); // Vérification si la réponse a une propriété 'data'
        chai.expect(res.data).to.equal('Successful response from the API'); // Vérification si la valeur de la propriété 'data' est égale à 'Successful response from the API'
        done(); // Appel de la fonction done pour indiquer que le test est terminé
      })
      .catch((err) => done(err)); // Gestion des erreurs en appelant la fonction done avec l'erreur en cas d'échec
  });
});
