import os
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.ui'):
            os.system("D:\Python\Python27\python.exe" ' "D:\Python\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" -o ui_%s.py %s' %
                      (file.rsplit('.', 1)[0], file))
            # print "D:\Python\Python27\python.exe" ' "D:\Python\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" -o ui_%s.py %s' % (
            #    file.rsplit('.', 1)[0], file)
        elif file.endswith('.qrc'):
            os.system('"D:\Python\Python27\Lib\site-packages\PyQt4\pyrcc4.exe" -o %s_rc.py %s' %
                      (file.rsplit('.', 1)[0], file))
