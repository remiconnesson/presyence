// https://docs.cypress.io/api/introduction/api.html
describe("The Detailed Views survive an hard refresh", () => {
  function rendersHighlightedCode() {
    /* Here we check that the input function contains as first span the `def` python keyworkd. If it's there it means that (1.) the app has injected an element where there was none before (span is not present in the template), (2.) that the highlighter is working as it is the one creating the span */
    cy.get(
      '[data-testid="test-detail-function"] > pre > code > div > span'
    ).contains("def");
  }

  function rendersAnHTMLTable() {
    /*
     * Here we are checking that the table has 4 rows and 2 columns, which is possible, if and only if, the app has (1.) got the .csv from the pinia store, then (2.) parsed the CSV into an iterable and then (3.) built a HTML table from this iterable.
     */
    cy.get('[data-testid="test-detail-input"] > table > tbody ')
      .children()
      .should("have.length", 4);
    cy.get('[data-testid="test-detail-input"] > table > tbody > :nth-child(3)')
      .children()
      .should("have.length", 2);
  }

  it("can go back to home after a hard refresh", () => {
    /*
     *  Check that the back link still works after a hard refresh.
     *
     */
    cy.visit("/test/4");
    cy.reload(true);
    cy.get("a").click();
    cy.get("[data-testid='search-bar']").should("be.visible");
  });

  function containsStuffTheyHaveInCommon() {
    cy.contains("h2", "The Expected Result");
    cy.contains("h2", "The Test Input");
    cy.contains("h2", "Tested Function");
    rendersHighlightedCode();
    rendersAnHTMLTable();
  }

  it("hard refresh on a `WrongResult` and it renders properly", () => {
    cy.visit("/test/0");
    cy.reload(true);
    containsStuffTheyHaveInCommon();
    cy.contains("h2", "Pandas Error Message");
    cy.contains("h2", "The Observed Result");
  });

  it("hard refresh on a `Crash` and it renders properly", () => {
    cy.visit("/test/3");
    cy.reload(true);
    containsStuffTheyHaveInCommon();
    cy.contains("h2", "Traceback");
  });

  it("hard refresh on a `Success` it renders properly", () => {
    cy.visit("/test/5");
    cy.reload(true);
    containsStuffTheyHaveInCommon();
  });
});
