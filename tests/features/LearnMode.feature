Feature: LearnMode

  @active
  Scenario Outline: Add two numbers and verify the number addition result
    Given I am on the "number addition" page
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

  @active
  Scenario Outline: Add two numbers and verify the number division result
    Given I am on the "number division" page
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

  @active
  Scenario Outline: Add one password and verify it
    Given I am on the "password restore" page
    When I enter "<newPassword>" into the input field
    Then I should see the result "<result>"

    Examples:
      | newPassword         | result           |
      | P@ssw0rD            | Valid Password   |
      | hElloW0rld          | Invalid Password |
      | Passw0rd!7          | Invalid Password |
      | null                | Invalid Password |
      | Mo7%                | Invalid Password |
      | asdfghjklpoiuytrewq | Invalid Password |
      | ONLYCAPITAL         | Invalid Password |
      | onlylower           | Invalid Password |
      | 001122              | Invalid Password |
      | @@@@@               | Invalid Password |
      | Κωδικός             | Invalid Password |

  @active
  Scenario Outline: Add three name and verify them
    Given I am on the "update nickname" page
    When I enter "<nickName>" and "<firstName>" and "<lastName>" into the input field
    Then I should see the result "<result>"

    Examples:
      | nickName   | firstName                      | lastName                        | result               |
      | skyline7   | Michael                        | Henderson                       | Your profile updated |
      | k_3        | J                              | Z                               | User input error     |
      | longnick9_ | MaximilianaElizabethMontgomery | AlexanderHamiltonJeffersonSmith | User input error     |
      | null       | null                           | null                            | User input error     |
      | 123-AA     | X Æ A-12                       | X Æ A-12                        | User input error     |
      | @@@@@      | Christopher                    | Williams                        | User input error     |

  @active1
  Scenario Outline: Add two numbers and verify the number multiplication result
    Given I am on the "number multiplication" page
    When I enter "<num1>" and "<num2>" into the input fields
    Then I should see the result "<result>"

    Examples:
      | num1        | num2 | result            |
      | null        | null | User input error  |
      | abc         | 1    | User input error  |
      | 5           | 7    | 35                |
      | 10000000000 | 8    | Application error |
      | 3.5         | 2.7  | 9.45              |
      | -8          | 4    | -32               |