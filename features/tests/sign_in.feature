Feature: Sign in test cases

  Scenario: User can navigate to Sign In
    Given Open Target main page
    When Click on Account Button
    And Click Sign In from right side navigation menu
    Then Verify Sign In form opened

  Scenario: User can log in with valid credentials
    Given Open Target main page
    When Click on Account Button
    And Click Sign In from right side navigation menu
    And Input email and password on SignIn page
    Then Verify the verification code sent shown

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    And Store original window
    When Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window
