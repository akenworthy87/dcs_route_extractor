Feature: Waypoint conversions for Kola

  Scenario: Waypoint 1
    Given Map is Kola
    When Metric: X+00202542 Z+00332102
    Then Lat Long Precise: N 69°31'42.20"   E 31°09'17.99"
    And Lat Long Decimal Minutes: N 69°31.703'   E 31°09.299'
    And MGRS GRID: 36 W VC 27994 14368

  Scenario: Waypoint 2
    Given Map is Kola
    When Metric: X+00155326 Z+00443092
    Then Lat Long Precise: N 68°55'44.32"   E 33°40'59.19"
    And Lat Long Decimal Minutes: N 68°55.738'   E 33°40.986'
    And MGRS GRID: 36 W WB 27408 46595


  Scenario: Waypoint 3
    Given Map is Kola
    When Metric: X-00144544 Z+00323892
    Then Lat Long Precise: N 66°28'05.64"   E 29°42'00.06"
    And Lat Long Decimal Minutes: N 66°28.094'   E 29°42.001'
    And MGRS GRID: 35 W PP 20263 74701


  Scenario: Waypoint 4
    Given Map is Kola
    When Metric: X-00231814 Z-00333095
    Then Lat Long Precise: N 65°48'46.25"   E 15°04'43.44"
    And Lat Long Decimal Minutes: N 65°48.770'   E 15°04.724'
    And MGRS GRID: 33 W WN 03599 99052
