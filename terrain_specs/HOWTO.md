# How to create a Terrain Spec file

Make a new (or copy and edit an existing) yaml file.

Name the file the same as a DCS route file for that terrain for compatibility

## Properties

### scale_factor

Will probably be 0.9996

### origin_mgrs

- Open the mission editor and make a blank misson on that terrain
- Run the mission and go to the F10 map
- Find the default Bullseye location
- Zoom all the way in on the Bullseye
- Alt-Left_Click as accurately as possible on the Bullseye
- Copy the MGRS coordinates from the Coordinates popup

### central_meridian

This one is a bit tricky and might need some guesswork. You can read more about central meridians [here](https://gisgeography.com/central-meridian/).

Basically if you look at the degrees **longitude** of the bullseye point the central meridian will be the closest number divisable by 3 (or actually a (multiple of 6 minus 3) as the range -177 to 177, with a step of 6, see below)
Meridians: (-177, -171, -165, -159, -153, -147, -141, -135, -129, -123, -117, -111, -105, -99, -93, -87, -81, -75, -69, -63, -57, -51, -45, -39, -33, -27, -21, -15, -9, -3, 3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141, 147, 153, 159, 165, 171, 177)