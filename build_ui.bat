echo off
echo "_______python build_______"
cd ui
echo "UI build..."
"D:\Python\Python27\python.exe" ~QT_UI_Conv.py
echo "Copy image resouce..."
copy pyimg_rc.py ..\src\app\layout\pyimg_rc.py
echo "Copy ui resouce..."
copy ui*.py ..\src\app\layout