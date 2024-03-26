const sendPaymentRequestToApi = require('./5-payment.js'); // Importe la fonction sendPaymentRequestToApi depuis le fichier 5-payment.js
const sinon = require('sinon'); // Importe la bibliothèque sinon
const { expect } = require('chai'); // Importe la fonction expect depuis la bibliothèque chai

describe('sendPaymentRequestToApi', () => { // Définit une suite de tests pour la fonction sendPaymentRequestToApi
  let consoleSpy;

  beforeEach(() => { // Avant chaque test
    consoleSpy = sinon.spy(console, 'log'); // Crée un espion sur la fonction console.log
  });

  afterEach(() => { // Après chaque test
    consoleSpy.restore(); // Restaure la fonction console.log
  });

  it('should log "The total is: 120" and be called once when called with 100 and 20', () => { // Définit un test qui vérifie si la fonction log affiche "The total is: 120" et est appelée une fois lorsque la fonction sendPaymentRequestToApi est appelée avec les arguments 100 et 20
    sendPaymentRequestToApi(100, 20); // Appelle la fonction sendPaymentRequestToApi avec les arguments 100 et 20
    expect(consoleSpy.calledOnce).to.be.true; // Vérifie si la fonction console.log a été appelée une fois
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true; // Vérifie si la fonction console.log a été appelée avec l'argument 'The total is: 120'
  });

  it('should log "The total is: 20" and be called once when called with 10 and 10', () => { // Définit un test qui vérifie si la fonction log affiche "The total is: 20" et est appelée une fois lorsque la fonction sendPaymentRequestToApi est appelée avec les arguments 10 et 10
    sendPaymentRequestToApi(10, 10); // Appelle la fonction sendPaymentRequestToApi avec les arguments 10 et 10
    expect(consoleSpy.calledOnce).to.be.true; // Vérifie si la fonction console.log a été appelée une fois
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true; // Vérifie si la fonction console.log a été appelée avec l'argument 'The total is: 20'
  });
});
