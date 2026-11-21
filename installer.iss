[Setup]
AppName=InputTester
AppVersion=1.0
DefaultDirName={autopf}\InputTester
DefaultGroupName=InputTester
OutputDir=Output
OutputBaseFilename=InputTesterSetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
Source: "dist\InputTester.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\InputTester"; Filename: "{app}\InputTester.exe"
Name: "{autodesktop}\InputTester"; Filename: "{app}\InputTester.exe"

[Run]
Filename: "{app}\InputTester.exe"; Description: "InputTester を起動"; Flags: nowait postinstall skipifsilent