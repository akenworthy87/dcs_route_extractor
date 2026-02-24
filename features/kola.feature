Feature: Waypoint conversions for Kola

  Scenario: Waypoint 1
    Given Map is Kola
    When Metric: X+00202542 Z+00332102
    Then Lat Long Precise: N 69°31'42.20"   E 31°09'17.99"
    And Lat Long Decimal Minutes: N 69°31.703'   E 31°09.299'
    And MGRS GRID: 36 W VC 27994 14368
