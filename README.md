# pyrmont

## Pico tool for Rainmeter skins code generation

Uses Python script embedded to `.ini` file that writes
skin contents with `print()` function.

Also, you can import your custom modules from Python files
that are neighbour to `.pyrm` file via the `import_module()` function.
for example, you have Rainmeter config path with structure:

```plain-text
- SkinPackRootDir
  - Skin1
    - 1.ini
    - 1.pyrm
    - scraper.py
```

...and, you can write this in your `1.pyrm` file:

```py
scraper = import_module('scraper')
data = scraper.process()
print(f'''
    [MeterX]
        Meter=String
        Text={data}
    ''')
```

### Launching

`python pyrmont.py <path to Rainmeter skin directory>`

This will automatically generate `<filename>.ini`
skins from all `<filename>.pyrm` files found.

Add `--silent` argument if you don't want pyrmont to produce unnecessary output.

### Examples

`skin.pyrm` (input):

```ini
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

`skin.ini` (output):

```ini
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
