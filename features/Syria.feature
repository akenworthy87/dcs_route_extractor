Feature: Waypoint conversions for Syria

Scenario: Waypoint 0
  Given Map is Syria
  When Metric: X+00000000 Z+00000000
  Then Lat Long Precise: N 35°01'18.90"   E 35°54'02.00"
  And Lat Long Decimal Minutes: N 35°01.315'   E 35°54.033'
  And MGRS GRID: 36S YD 64649 79320

Scenario: Waypoint 1
  Given Map is Syria
  When Metric: X+116002.8203125 Z-240300.59375
  Then Lat Long Precise: N 35°58'01.30"   E 33°12'05.36"
  And Lat Long Decimal Minutes: N 35°58.021'   E 33°12.089'
  And MGRS GRID: 36S WE 18167 80310

Scenario: Waypoint 2
  Given Map is Syria
  When Metric: X+147761.734375 Z+297687.65625
  Then Lat Long Precise: N 36°23'37.25"   E 39°09'57.59"
  And Lat Long Decimal Minutes: N 36°23.620'   E 39°09.959'
  And MGRS GRID: 37S EA 14886 27627

Scenario: Waypoint 3
  Given Map is Syria
  When Metric: X-198525.15625 Z+285825.875
  Then Lat Long Precise: N 33°16'15.91"   E 39°01'56.92"
  And Lat Long Decimal Minutes: N 33°16.265'   E 39°01.948'
  And MGRS GRID: 37S ES 03024 81340

Scenario: Waypoint 4
  Given Map is Syria
  When Metric: X-182837.015625 Z-291574
  Then Lat Long Precise: N 33°15'34.03"   E 32°50'17.03"
  And Lat Long Decimal Minutes: N 33°15.567'   E 32°50.283'
  And MGRS GRID: 36S VB 84917 80062
