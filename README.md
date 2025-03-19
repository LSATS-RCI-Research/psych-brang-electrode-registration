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

## Known Issues
It's currently unclear what `nifti` is in core.io.read_nifti