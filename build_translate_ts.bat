echo off
echo "_______python build translate_______"
cd src\app
"D:\Python\Python27\Lib\site-packages\PyQt4\pylupdate4.exe" windows_main.py -ts ..\Lang\zh_CN.ts
"D:\Python\Python27\Lib\site-packages\PyQt4\pylupdate4.exe" layout\ui_layout_main.py -ts ..\Lang\zh_CN.ts
"D:\Python\Python27\Lib\site-packages\PyQt4\pylupdate4.exe" layout\ui_layout_comm.py -ts ..\Lang\zh_CN.ts
"D:\Python\Python27\Lib\site-packages\PyQt4\pylupdate4.exe" layout\ui_layout_option.py -ts ..\Lang\zh_CN.ts
"D:\Python\Python27\Lib\site-packages\PyQt4\pylupdate4.exe" layout\ui_layout_upgrade.py -ts ..\Lang\zh_CN.ts
"D:\Python\Python27\Lib\site-packages\PyQt4\pylupdate4.exe" layout\ui_layout_product.py -ts ..\Lang\zh_CN.ts