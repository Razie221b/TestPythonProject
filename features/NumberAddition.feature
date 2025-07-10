Feature: Login functionality

  @active
  Scenario: Enter "1" and "2" into the input fields, then click on the "Calculate" button. Expected Result: "3"
    Given open base URL
    When enter "1" and "2" into the input fields
    Then verify expected result: "3"

#  @active
#  Scenario: Input "-2" and "4" into the input fields where one number is negative, then click on the "Calculate" button. Expected Result: "2"
#    Given open base URL
#    When enter "1" and "2" into the input fields
#    Then verify expected result: "3"