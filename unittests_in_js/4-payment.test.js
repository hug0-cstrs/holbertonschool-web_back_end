const chai = require('chai'); // Importation de la bibliothèque Chai pour les assertions
const sinon = require('sinon'); // Importation de la bibliothèque Sinon pour les spies et les stubs
const Utils = require('./utils.js'); // Importation du module Utils depuis le fichier utils.js
const sendPaymentRequestToApi = require('./4-payment.js'); // Importation de la fonction sendPaymentRequestToApi depuis le fichier 4-payment.js

'use strict';


describe('sendPaymentRequestToApi function', () => {
  const spyConsole = sinon.spy(console, 'log'); // Création d'un spy pour espionner la fonction console.log

  it('validate the usage of the Utils function', () => {
    const stubUtils = sinon.stub(Utils, 'calculateNumber'); // Création d'un stub pour remplacer la fonction calculateNumber du module Utils

    stubUtils.withArgs('SUM', 100, 20).returns(10); // Définition du comportement du stub lorsque la fonction calculateNumber est appelée avec les arguments 'SUM', 100 et 20

    sendPaymentRequestToApi(100, 20); // Appel de la fonction sendPaymentRequestToApi avec les arguments 100 et 20

    chai.expect(spyConsole.calledOnce).to.be.true; // Vérification que la fonction console.log a été appelée une fois

    chai.expect(spyConsole.calledWith('The total is: 10')).to.be.true; // Vérification que la fonction console.log a été appelée avec l'argument 'The total is: 10'

    stubUtils.restore(); // Restauration de la fonction calculateNumber originale
    
    spyConsole.restore(); // Restauration de la fonction console.log originale
  });
});
