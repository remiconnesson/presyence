// https://docs.cypress.io/api/introduction/api.html
describe("The Detailed Views survive an hard refresh", () => {
  function rendersHighlightedCode() {
    /* Here we check that the input function contains as first span the `def` python keyworkd. If it's there it means that (1.) the app has injected an element where there was none before (span is not present in the template), (2.) that the highlighter is working as it is the one creating the span */
    cy.get(
      '[data-testid="test-detail-function"] > pre > code > div > span'
    ).contains("def");
  }

  function containsStuffTheyHaveInCommon() {
    cy.contains("h2", "The Expected Result");
    cy.contains("h2", "The Test Input");
    cy.contains("h2", "Tested Function");
    rendersHighlightedCode();
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
