Feature: Waypoint conversions for Kola

  Scenario: Waypoint 1
    Given Map is Kola
    When Metric: X+00202541.640625 Z+00332102.0625
    Then Lat Long Precise: N 69°31'42.20"   E 31°09'17.99"
    And Lat Long Decimal Minutes: N 69°31.703'   E 31°09.299'
    And MGRS GRID: 36W VC 27994 14368

  Scenario: Waypoint 2
    Given Map is Kola
    When Metric: X+00155326.359375 Z+00443092.1875
    Then Lat Long Precise: N 68°55'44.32"   E 33°40'59.19"
    And Lat Long Decimal Minutes: N 68°55.738'   E 33°40.986'
    And MGRS GRID: 36W WB 27408 46595


  Scenario: Waypoint 3
    Given Map is Kola
    When Metric: X-00144544.109375 Z+00323891.90625
    Then Lat Long Precise: N 66°28'05.64"   E 29°42'00.06"
    And Lat Long Decimal Minutes: N 66°28.094'   E 29°42.001'
    And MGRS GRID: 35W PP 20263 74701


  Scenario: Waypoint 4
    Given Map is Kola
    When Metric: X-00231814.000000 Z-00333095.00000
    Then Lat Long Precise: N 65°48'46.27"   E 15°04'43.47"
    And Lat Long Decimal Minutes: N 65°48.771'   E 15°04.724'
    And MGRS GRID: 33W WN 03600 99052
