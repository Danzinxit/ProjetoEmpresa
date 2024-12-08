block_cipher = None

a = Analysis(['main.py'],  # Atualize aqui para main.py
             pathex=[],
             binaries=[],
             datas=[('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\tcl\\tcl8.6', 'tcl'),
                    ('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\tcl\\tk8.6', 'tk')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',  # Mude para main
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
