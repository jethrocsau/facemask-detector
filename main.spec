# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
libiconv_dll = '/Users/Jethro/opt/anaconda3/pkgs/libiconv-1.16-h1de35cc_0/lib/libiconv.dylib'
libz_dll = '/Users/Jethro/opt/anaconda3/lib/libzbar.0.dylib'
libtorch_dll = '/Users/Jethro/opt/anaconda3/envs/pycv1/lib/python3.9/site-packages/torch/lib/libtorch_global_deps.dylib'

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[(libiconv_dll,"."), (libz_dll,"."),(libtorch_dll,"torch/lib/")],
    datas=[('templates','templates'),('ultralytics','ultralytics'),('weights','weights')],
    hiddenimports=['torch', 'numpy','logging','logging.config','seaborn','Pillow','opencv-python','matplotlib','PyYAML','psutil','requests','thop','torch.jit'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['webcam.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='mask-detector',
    icon=['webcam.ico']
)

app = BUNDLE(exe,
        name='mask-detector.app',
        icon='webcam.ico',
        bundle_identifier=None
)