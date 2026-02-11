pyinstaller main.spec --clean --noconfirm
powershell Compress-Archive -Force -Path .\dist\dcs_route_extractor\. -DestinationPath .\dist\dcs_route_extractor.zip