Feature: Waypoint conversions from offsets to LLP, LLDM, and MGRS

	Scenario Outline: Waypoints
		Given Map is <map>
		When Metric: X<offset_x> Z<offset_z>
		Then Lat Long Precise: <llp_n>   <llp_e>
		And Lat Long Decimal Minutes: <lldm_n>   <lldm_e>
		And MGRS GRID: <mgrs>
  
		Examples: Kola
			| map  | offset_x         | offset_z        | llp_n          | llp_e          | lldm_n       | lldm_e       | mgrs               |
      | Kola | +00202541.640625 | +00332102.06250 | N 69°31'42.20" | E 31°09'17.99" | N 69°31.703' | E 31°09.299' | 36W VC 27994 14368 |
      | Kola | +00155326.359375 | +00443092.18750 | N 68°55'44.32" | E 33°40'59.19" | N 68°55.738' | E 33°40.986' | 36W WB 27408 46595 |
      | Kola | -00144544.109375 | +00323891.90625 | N 66°28'05.64" | E 29°42'00.06" | N 66°28.094' | E 29°42.001' | 35W PP 20263 74701 |
      | Kola | -00231814.000000 | -00333095.00000 | N 65°48'46.27" | E 15°04'43.47" | N 65°48.771' | E 15°04.724' | 33W WN 03600 99052 |

