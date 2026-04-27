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

  Scenario: Verify each product has name and image on search results page
    Given Open Target main page
    When Search for rice
    Then Each product should have a product name and img
