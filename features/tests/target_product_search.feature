# Created by lana at 4/16/26
Feature: Test cases for Product Search on Target

  Scenario: User can search for a product "tea" on Target
    Given Open Target main page
    When Search for tea
    Then Verify search results for tea shown

  Scenario: User can search for a product "coffee" on Target
    Given Open Target main page
    When Search for coffee
    Then Verify search results for coffee shown

  Scenario: User can see cart empty msg
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: User can navigate to Sign In
    Given Open Target main page
    When Click on Sign In Button
    And Click Sign In from right side navigation menu
    Then Verify Sign In form opened