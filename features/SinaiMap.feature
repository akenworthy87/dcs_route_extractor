Feature: Waypoint conversions for SinaiMap

  Scenario: Waypoint 0
    Given Map is SinaiMap
    When Metric: X+00000000 Z+00000000
    Then Lat Long Precise: N 30°02'49.89"   E 31°14'41.13"
    And Lat Long Decimal Minutes: N 30°02.831'   E 31°14.685'
    And MGRS GRID: 36 R UU 30777 25313

  Scenario: Waypoint 1
    Given Map is SinaiMap
    When Metric: X+155034.609375 Z-178363.421875
    Then Lat Long Precise: N 31°24'20.51"   E 29°20'40.69"
    And Lat Long Decimal Minutes: N 31°24.341'   E 29°20.678'
    And MGRS GRID: 35 R QQ 22908 76942

  Scenario: Waypoint 2
    Given Map is SinaiMap
    When Metric: X+142099.046875 Z+327047.625
    Then Lat Long Precise: N 31°19'49.58"   E 34°39'31.86"
    And Lat Long Decimal Minutes: N 31°19.826'   E 34°39.531'
    And MGRS GRID: 36 R XV 57825 67412

  Scenario: Waypoint 3
    Given Map is SinaiMap
    When Metric: X-330973.125 Z+456823.46875
    Then Lat Long Precise: N 27°02'29.34"   E 35°53'56.75"
    And Lat Long Decimal Minutes: N 27°02.489'   E 35°53.945'
    And MGRS GRID: 36 R YQ 87601 94339

  Scenario: Waypoint 4
    Given Map is SinaiMap
    When Metric: X-358076.21875 Z-53823.4609375
    Then Lat Long Precise: N 26°48'31.93"   E 30°45'21.69"
    And Lat Long Decimal Minutes: N 26°48.532'   E 30°45.361'
    And MGRS GRID: 36 R TQ 76954 67236
