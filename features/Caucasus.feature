Feature: Waypoint conversions for Caucasus

  Scenario: Waypoint 0
    Given Map is Caucasus
    When Metric: X-0.0 Z-0.0    
    Then Lat Long Precise: N 45°07'46.18"   E 34°15'55.85"
    And Lat Long Decimal Minutes: N 45°07.769'   E 34°15.930'
    And MGRS GRID: 36T WQ 99517 98114

  Scenario: Waypoint 1
    Given Map is Caucasus
    When Metric: X+200023.640625 Z-168025.390625
    Then Lat Long Precise: N 46°55'59.66"   E 32°05'59.98"
    And Lat Long Decimal Minutes: N 46°55.994'   E 32°05.999'
    And MGRS GRID: 36T VS 31491 98138

  Scenario: Waypoint 2
    Given Map is Caucasus
    When Metric: X+234591.609375 Z+556411.5
    Then Lat Long Precise: N 46°55'20.74"   E 41°37'03.07"
    And Lat Long Decimal Minutes: N 46°55.345'   E 41°37.051'
    And MGRS GRID: 37T FM 99281 99870

  Scenario: Waypoint 3
    Given Map is Caucasus
    When Metric: X-288780.03125 Z+622080.375
    Then Lat Long Precise: N 42°12'07.78"   E 41°44'15.18"
    And Lat Long Decimal Minutes: N 42°12.129'   E 41°44.253'
    And MGRS GRID: 37T GG 26006 75850

  Scenario: Waypoint 4
    Given Map is Caucasus
    When Metric: X-403850.0625 Z-194444.34375
    Then Lat Long Precise: N 41°29'39.78"   E 31°51'45.88"
    And Lat Long Decimal Minutes: N 41°29.663'   E 31°51.764'
    And MGRS GRID: 36T VL 05072 94264
