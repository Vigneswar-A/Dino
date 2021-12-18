# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Main.py'],
             pathex=['C:\\Users\\viguv\\OneDrive\\Desktop\\Dino'],
             binaries=[],
             datas=[("./Icon.ico","."),("./BGM.wav","."),("./Lose.wav","."),("./Jump.wav","."),("./Sprites/Cactus/Cactus.png","./Sprites/Cactus"),("./Sprites/BG.jpg","./Sprites"),("./Sprites/LTEnergy.ttf","./Sprites"),("./Sprites/Dinosaur/Run1.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Run2.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Run3.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Run4.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Run5.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Run6.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Run7.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Run8.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Dead1.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Dead2.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Dead3.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Dead4.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Dead5.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Dead6.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Dead7.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Dead8.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump1.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump2.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump3.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump4.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump5.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump6.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump7.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump8.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump9.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump10.png","./Sprites/Dinosaur"),("./Sprites/Dinosaur/Jump11.png","./Sprites/Dinosaur")],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='Icon.ico')
