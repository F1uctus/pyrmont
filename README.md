<h1 align="center">pyrmont</h1>
<h3 align="center">Simple static skins generator for Rainmeter ✒️ 🌧️</h3>

This tool uses Python scripts embedded into Rainmeter config file.<br>
The `.pyrm` extension is used for source code, resulting `.ini` file
with the same name will appear near the source file after generation.

### Launching

`python pyrmont.py <path to Rainmeter suite directory>`

This will generate `<filename>.ini` config from every `<filename>.pyrm` file found.

Add `--silent` argument if you don't want pyrmont to produce unnecessary output.

### Features

To embed any code into resulting `.ini` config, use the built-in `e(args)` function,
where `args` is any amount of `str`s.

There is a neat example showing how you can generate sound measures
for visualizer with just couple of lines:

`skin.pyrm` (input):

```ini
...
;macro
for i in range(25):
    e(f'''
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

...and so on until MeasureBand24
```

Also, you can import your custom modules from Python files
that are located near to `.pyrm` file via the `require(file_name)` function.

For example, if you have Rainmeter config path with structure:

```plain-text
- SuiteDir
  - Skin1
    - 1.ini
    - 1.pyrm
    - scraper.py
```

...you can do this in your `1.pyrm` file:

```py
scraper = require('scraper')
data = scraper.process()
e(f'''
[MeterData]
    Meter=String
    Text={data}
''')
```

`import` for any module installed in your system's Python distribution is supported too.

### Contributions
... are welcome! Feel free to report issues and submit pull requests if you want to.<br>
And give this project a 🌟 if you like it!
