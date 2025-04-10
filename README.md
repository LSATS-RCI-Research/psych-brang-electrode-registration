# Electrode Registration App

A GUI application for registering ECoG electrodes onto pre-implant dura surface.
```sh
python3 app/app.py
```

## Screenshot

![screenshot](https://raw.github.com/towle-lab/electrode-registration-app/master/screenshot.register+label.png)

## Dependencies
- Python 3.11
- [mayavi](https://github.com/enthought/mayavi/zipball/main)
  - `pip install https://github.com/enthought/mayavi/zipball/main`
- VTK
- ansicolors
- nibabel
- numpy==1.26.4
- scipy
- nibabel
- PySide6
- PyQt5

You can install the required Python packages via:

```sh
$ pip install -r requirements.txt
```

## Usage
Demo data exists in [Dropbox](https://www.dropbox.com/scl/fi/kre4a67yw61ktsg6qyllb/Demo-Data.zip?rlkey=aquw3ojn87dvyl2dlcn7guavg&st=l2vlttvc&dl=0). Use the .lh for 1208UM and the .rh dura file for 1206UM.