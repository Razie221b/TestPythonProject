Feature: LearnMode

  Scenario Outline: Add two numbers and verify the number addition result
    Given I am on the adder page
    When I enter "<num1>" and "<num2>" into the input fields
    Then I should see the result "<result>"

    Examples:
      | num1        | num2 | result            |
      | 1           | 2    | 3                 |
      | -2          | 4    | 2                 |
      | 1.5         | 2.5  | 4.0               |
      | abc         | 1    | User input error  |
      | null        | null | User input error  |
      | 10000000000 | 1    | Application Error |

  Scenario Outline: Add two numbers and verify the number division result
    Given I am on the divider page
    When I enter "<num1>" and "<num2>" into the input fields
    Then I should see the result "<result>"

    Examples:
      | num1 | num2 | result            |
      | 4    | 2    | 2                 |
      | -10  | 2    | -5                |
      | 5    | 2    | 2.5               |
      | abc  | 1    | User input error  |
      | null | null | User input error  |
      | 10   | 0    | Application Error |

  Scenario Outline: Add one password and verify it
    Given I am on the password Restore page
    When I enter "<newPassword>" into the input field
    Then I should see the result "<result>"

    Examples:
      | newPassword | result            |
      | P@ssw0rD    | Valid Password    |
#      | -10         | -5                |
#      | 5           | 2.5               |
#      | abc         | User input error  |
#      | null        | User input error  |
#      | 10          | Application Error |