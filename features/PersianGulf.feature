Feature: Waypoint conversions for PersianGulf

  Scenario: Waypoint 0
    Given Map is PersianGulf
    When Metric: X+00000000 Z+00000000
    Then Lat Long Precise: N 26°10'18.54"   E 56°14'30.96"
    And Lat Long Decimal Minutes: N 26°10.309'   E 56°14.516'
    And MGRS GRID: 40R DP 24244 94932

  Scenario: Waypoint 1
    Given Map is PersianGulf
    When Metric: X-249918.109375 Z+237165.671875
    Then Lat Long Precise: N 23°54'31.03"   E 58°35'08.47"
    And Lat Long Decimal Minutes: N 23°54.517'   E 58°35.141'
    And MGRS GRID: 40Q FM 61409 45014

  Scenario: Waypoint 2
    Given Map is PersianGulf
    When Metric: X-238522.4375 Z-375984.65625
    Then Lat Long Precise: N 23°57'19.77"   E 52°33'47.19"
    And Lat Long Decimal Minutes: N 23°57.329'   E 52°33.786'
    And MGRS GRID: 39Q XG 59053 50180

  Scenario: Waypoint 3
    Given Map is PersianGulf
    When Metric: X+373045.0625 Z-333250.90625
    Then Lat Long Precise: N 29°28'28.39"   E 52°46'59.92"
    And Lat Long Decimal Minutes: N 29°28.473'   E 52°46.998'
    And MGRS GRID: 39R XN 72909 61888

  Scenario: Waypoint 4
    Given Map is PersianGulf
    When Metric: X+292009.34375 Z+283698.000
    Then Lat Long Precise: N 28°47'35.69"   E 59°07'49.57"
    And Lat Long Decimal Minutes: N 28°47.594'   E 59°07.826'
    And MGRS GRID: 40R GS 07941 86942
