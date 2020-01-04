# pyrmont
## Tool for Rainmeter skins code generation
Uses Python script embedded to `.ini` file that writes
skin contents with `print()` function.

### Launching
`pyrmont.py <path to Rainmeter skin directory>`

This will automatically generate `<filename>.ini`
skins from all `<filename>.pyrm` files found. 

### Examples

skin.pyrm (input):
```
...
;macro
for i in range(25):
    print(f'''
    [MeasureBand{i}]
        Measure=Plugin
        Plugin=AudioLevel
        Parent=MeasureAudio
        Type=Band
        BandIdx={i}
    ''')
;endmacro
...
```

skin.ini (output):
```
...
[MeasureBand0]
    Measure=Plugin
    Plugin=AudioLevel
    Parent=MeasureAudio
    Type=Band
    BandIdx=0

[MeasureBand1]
    Measure=Plugin
    Plugin=AudioLevel
    Parent=MeasureAudio
    Type=Band
    BandIdx=1

[MeasureBand2]
    Measure=Plugin
    Plugin=AudioLevel
    Parent=MeasureAudio
    Type=Band
    BandIdx=2

[MeasureBand3]
    Measure=Plugin
    Plugin=AudioLevel
    Parent=MeasureAudio
    Type=Band
    BandIdx=3
...and so on until MeasureBand24
```
