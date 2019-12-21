# pyrmont
## Tool for Rainmeter skins code generation.
Uses embedded Python script that writes
skin contents with `print()` function.

### Launching
`pyrmont.py <path to Rainmeter skin directory>`

This will automatically generate `<filename>.ini`
skins from all `<filename>.pyrm` files found. 

### Example:

skin.pyrm (input):
```
...
;#region macro
for i in range(25):
    print(f'''
    [MeasureBand{i}]
        Measure=Plugin
        Plugin=AudioLevel
        Parent=MeasureAudio
        Type=Band
        BandIdx={i}
    ''')
...
;#endregion macro
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
... (25 times as above)
```
