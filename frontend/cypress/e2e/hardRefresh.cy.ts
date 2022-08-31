// https://docs.cypress.io/api/introduction/api.html

describe("The Detailed Views survive an hard refresh", () => {

  function containsStuffTheyHaveInCommon() {
    cy.contains("h2", "The Expected Result");
    cy.contains("h2", "The Test Input");
    cy.contains("h2", "Tested Function");
  }

  it("hard refresh on a `WrongResult` and it renders properly", () => {
    cy.visit("/test/0");
    containsStuffTheyHaveInCommon();
  });

  it("hard refresh on a `Crash` and it renders properly", () => {
    cy.visit("/test/2");
    containsStuffTheyHaveInCommon();
  });

  it("hard refresh on a `Success` it renders properly", () => {
    cy.visit("/test/5");
    containsStuffTheyHaveInCommon();
  });
});
