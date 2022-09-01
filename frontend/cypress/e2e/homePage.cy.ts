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

  function theHomePageIsAlright() {
    // it should load 8 tests
    cy.get("[data-testid='home-all-tests-list']")
      .children()
      .should("have.length", 8);

    // should have 5 success, 1 crash and 2 wrong results and apply the correct status tag
    const statusInOrderOfAppearance = [
      "WrongResult",
      "WrongResult",
      "Success",
      "Crash",
      "Success",
      "Success",
      "Success",
      "Success",
    ];

    cy.get("[data-testid='home-status-tag']").each(($el, i) => {
      const correctStatus = statusInOrderOfAppearance[i];
      const correctClass =
        correctStatus === "Success" ? "is-success" : "is-danger";

      expect($el).to.contain(correctStatus);
      expect($el).to.have.class(correctClass);
    });

    // it should filter based on the search term
    const expectNumberOfTestsToBe = (n) => {
      cy.get("[data-testid='home-all-tests-list']")
        .children()
        .should("have.length", n);
    };

    cy.get('[data-testid="search-bar"]').type("drop");
    expectNumberOfTestsToBe(6);

    cy.get('[data-testid="search-bar"]').clear();
    expectNumberOfTestsToBe(8);

    // it should filter based on which checkboxes are checked
    cy.get('[data-testid="filter-checkbox"]').first().click();
    expectNumberOfTestsToBe(7);
    cy.get('[data-testid="filter-checkbox"]').first().click();
    expectNumberOfTestsToBe(8);
    // it should apply both filtering options
    cy.get('[data-testid="filter-checkbox"]').first().click();
    cy.get('[data-testid="search-bar"]').type("drop");
    expectNumberOfTestsToBe(5);
  }

  it("should work well on the happy path", () => {
    /* The happy path is , get on the home page, fiddle with the filter, click on one element, inspect the test result, then go back and do it again */
    cy.visit("/");
    theHomePageIsAlright();
    // navigate to a test detail view
    cy.get(
      '[data-testid="home-all-tests-list"] > :nth-child(2) > .panel-block'
    ).click();

    /* it should be able to navigate to TestDetail, to render it, then to comeback */
    cy.contains("h2", "The Expected Result");
    cy.contains("h2", "The Test Input");
    cy.contains("h2", "Tested Function");
    rendersHighlightedCode();
    rendersAnHTMLTable();
    // comeback
    cy.get("a").click();
    // the home page must still function the same
    theHomePageIsAlright();
  });
});
