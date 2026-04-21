Feature: Cart test cases

  Scenario: User can see cart empty msg
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

