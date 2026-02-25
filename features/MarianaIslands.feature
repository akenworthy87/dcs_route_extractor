Feature: Waypoint conversions for MarianaIslands

  Scenario: Waypoint 0
    Given Map is MarianaIslands
    When Metric: X+0.0 Z+0.0
    Then Lat Long Precise: N 13°29'05.99"   E 144°47'51.14"
    And Lat Long Decimal Minutes: N 13°29.099'   E 144°47.852'
    And MGRS GRID: 55P BQ 61582 91839

  Scenario: Waypoint 1
    Given Map is MarianaIslands
    When Metric: X-186900.046875 Z-105762.8984375
    Then Lat Long Precise: N 11°47'13.21"   E 143°50'32.00"
    And Lat Long Decimal Minutes: N 11°47.220'   E 143°50.533'
    And MGRS GRID: 54P ZU 09760 04571

  Scenario: Waypoint 2
    Given Map is MarianaIslands
    When Metric: X-156148.296875 Z+469141.09375
    Then Lat Long Precise: N 12°04'28.42"   E 149°07'10.58"
    And Lat Long Decimal Minutes: N 12°04.473'   E 149°07.176'
    And MGRS GRID: 55P GP 30723 35691

  Scenario: Waypoint 3
    Given Map is MarianaIslands
    When Metric: X+592779.8125 Z+372040.96875
    Then Lat Long Precise: N 18°50'57.12"   E 148°16'06.08"
    And Lat Long Decimal Minutes: N 18°50.952'   E 148°16.101'
    And MGRS GRID: 55Q FA 33622 84619

  Scenario: Waypoint 4
    Given Map is MarianaIslands
    When Metric: X+500175 Z-532525.75
    Then Lat Long Precise: N 17°52'49.56"   E 139°44'17.95"
    And Lat Long Decimal Minutes: N 17°52.826'   E 139°44.299'
    And MGRS GRID: 54Q UE 66336 77409

