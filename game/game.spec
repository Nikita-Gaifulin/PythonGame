# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
         ( '/imagesAndSounds', 'imagesAndSounds'),  # Loads the 'folder' folder (left) and creates
                                      # an equivalent folder called 'b folder' (right)
                                      # on the destination path
         #( 'level_1/level2', 'level_2' ),  # Loads the 'level_2' folder
                                           # that's inside the 'level_1' folder
                                           # and outputs it on the root folder
         ( 'comic_sans.ttf', '.'),  # Loads the 'comic_sans.ttf' file from
                                    # your root folder and outputs it with
                                    # the same name on the same place.
         ( 'imagesAndSounds/*.mp3', '.')  # Loads all the .mp3 files from 'folder'.
         ]

a = Analysis(['game.py'],
             pathex=['C:\\Users\\USER\\PycharmProjects\\game'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
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
          name='game',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='game_icon.ico')
