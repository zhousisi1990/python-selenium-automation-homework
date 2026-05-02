Feature: Cart test cases

  Scenario: User can see cart empty msg
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for Toothpaste
    And Click on the first Add to cart button
    And Click on Add to cart button from side menu
    And Close side menu
    And Click on Cart icon
    Then Verify cart has 1 item(s)

