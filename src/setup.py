# -*- coding: utf-8 -*-
#
# @author: Toso
# @created: 2019-05-01T11:34:15.897Z+08:00
# @comment: ______________
#

import matplotlib
from distutils.core import setup
import py2exe
import glob
import sys
sys.setrecursionlimit(5000)  # or more

includes = ['numpy', 'numpy.core',
            'pyqtgraph', 'pyqtgraph.Qt', 'pyqtgraph.Qt.*', 'pyqtgraph.Point', 'pyqtgraph.parametertree', 'pyqtgraph.parametertree.*', 'pyqtgraph.parametertree.parameterTypes',
            'sip',
            'PyQt4.QtCore', 'PyQt4.QtGui', 'PyQt4.Qt', 'PyQt4.*',
            'serial', 'serial.tools.list_ports',
            'struct',
            'configobj']
opts = {'py2exe': {
    # 'optimize': 0,
    # 'packages': packages,
    'includes': includes,
    # 将dll_excludes忽略
    'dll_excludes': ['libansari.R6EA3HQP5KZ6TAXU4Y4ZVTRPT7UVA53Z.gfortran-win_amd64.dll',
                     'libbanded5x.EPO3VOLIMBSWR5EBYYGUZIII4JTSIKCW.gfortran-win_amd64.dll',
                     'libbispeu.5N2XSD7URZS4WTOSLTOG4DDMA4HGB46U.gfortran-win_amd64.dll',
                     'libblkdta00.76LNUGMFEDSDS4KEP5PTBYTKKJJAHE5Z.gfortran-win_amd64.dll',
                     'libchkder.6HLXPVTQJEGRZGLI5DFRMNW3SS76BHP6.gfortran-win_amd64.dll',
                     'libcobyla2.JEGTSUUFJ7DFXWZN5PAYZTTLBDATC4WD.gfortran-win_amd64.dll',
                     'libdcosqb.K4J3XBR4PEETMRHZICUWW4LXG5UONZ34.gfortran-win_amd64.dll',
                     'libdcosqb.QRGA36MB6CFHWLQN6ETWARR4M4E6P3C2.gfortran-win_amd64.dll',
                     'libdcsrch.I2AOPDCXAPDRFNPWY55H5UE7XZSU5CVN.gfortran-win_amd64.dll',
                     'libdet.2M66HSCLZZK6I6IJVQFUMYOUHKK6ZJN5.gfortran-win_amd64.dll',
                     'libdfft_sub.DYGBOM2QJIMP64CLTILUIH2B4XOZS4CV.gfortran-win_amd64.dll',
                     'libdfitpack.QJETH3WQTI46QRA26NBC5EHXEKDDQHVM.gfortran-win_amd64.dll',
                     'libdgamln.VWCBXTPY2N6XPFSJHDH64YKJTYJBLIU3.gfortran-win_amd64.dll',
                     'libdop853.6TJTQZW3I3Q3QIDQHEOBEZKJ3NYRXI4B.gfortran-win_amd64.dll',
                     'libdqag.KE6RUICD4G2PT76UOVV6SUKPPQ445X3D.gfortran-win_amd64.dll',
                     'libd_odr.EO474VK6SM3CS4E77PHHQRZ6EYZM6PTR.gfortran-win_amd64.dll',
                     'libgetbreak.3BXCMS2TPADW4VWV3RLQMXYHQ2L6Y6ZE.gfortran-win_amd64.dll',
                     'liblbfgsb.VFXCLNAS7QYFDQWHFYI2O27SQO7ZFQWK.gfortran-win_amd64.dll',
                     'libmvndst.E7WORYHCUYKXRCTY52YFSWPSH7ZCMCDB.gfortran-win_amd64.dll',
                     'libnnls.IXEEHJUCGHJL42YZEM6UIEMROJWXHMLJ.gfortran-win_amd64.dll',
                     'libopenblas.BNVRK7633HSX7YVO2TADGR4A5KEKXJAW.gfortran-win_amd64.dll',
                     'libslsqp_op.NNY57ZXZ43A4RH3YWFA7BKHP5PC2K3I5.gfortran-win_amd64.dll',
                     'libspecfun.BHLTWMBI4EYWDACZN4DQUESSDJRJNGEL.gfortran-win_amd64.dll',
                     'libvode.NV2XAN4GN7QVB22GLBI6AN75S2HAS4A6.gfortran-win_amd64.dll',
                     'libwrap_dum.3JE75BTAMY365PQTISKAXOYQME2W77HP.gfortran-win_amd64.dll',
                     'libwrap_dum.FVYPJH4EZPKATTZPKAAFERQIBYG6E5KF.gfortran-win_amd64.dll',
                     'lib_arpack-.EWPUDJIVHPZWP7X43YGM5BFUJAPSP6OO.gfortran-win_amd64.dll',
                     'lib_blas_su.QCLBWCJMHBTJN3O55W77ICXS5RFIL45H.gfortran-win_amd64.dll',
                     'lib_test_fo.JF5HTWMUPBXWGAYEBVEJU3OZAHTSVKCT.gfortran-win_amd64.dll',
                     'Microsoft.VC90.CRT.manifest',
                     'msvcm90.dll',
                     'msvcp90.dll',
                     'msvcr90.dll'],
    # 'dist_dir': dist,
    # 'bundle_files': 2,
    # 'xref': False,
    # 'skip_archive': True,
    # 'ascii': False,
    # 'custom_boot_script': '',
    # 'compressed': False,
}}
data_files = [
    ('commlog', glob.glob('./commlog/*')),
    ('Config', glob.glob('./Config/*')),
    ('Lang', glob.glob('./Lang/*')),
    ('Log', glob.glob('./Log/*')),
    ('Product/ENGLISH', glob.glob('./Product/ENGLISH/*')),
    ('Product/zh_CN', glob.glob('./Product/zh_CN/*')),
    ('Upgrade', glob.glob('./Upgrade/*')),
    ('imageformats', glob.glob(
        'D:\Python\Python27\Lib\site-packages\PyQt4\plugins\imageformats\*')),
    ('.', glob.glob('D:\Python\Python27\Lib\site-packages\scipy\extra-dll\*'))
]
setup(
    windows=[{
        'script': 'ScopeAcq.py',
        'icon_resources': [(1, u'setup.ico')],
        'version':'1.0.0',
        'company_name':u'soshare.cn',
        'copyright':u'copyright ©2019 soshare.cn',
        'name': u'ScopeModbus',
        'description':u'Modbus'
    }],
    options=opts,
    zipfile=None,
    data_files=data_files
)
