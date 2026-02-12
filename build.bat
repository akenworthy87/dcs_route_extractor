pyinstaller main.spec --clean --noconfirm
xcopy .\terrain_specs\*.* .\dist\dcs_route_extractor\terrain_specs\ /E /I /Y
powershell Compress-Archive -Force -Path .\dist\dcs_route_extractor\. -DestinationPath .\dist\dcs_route_extractor.zip