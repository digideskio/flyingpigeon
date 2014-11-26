import nose.tools
from nose import SkipTest
from nose.plugins.attrib import attr

from malleefowl import wpsclient

import __init__ as base

import json
import tempfile
import urllib

def setup():
    pass

@attr('online')   
def test_icclim():
    raise SkipTest
    result = wpsclient.execute(
        service = base.SERVICE,
        identifier = "icclim",
        inputs = [('file_identifier', 'http://localhost:8090/thredds/fileServer/test/nils.hempelmann@hzg.de/tasmax_day_MPI-ESM-LR_historical_r1i1p1_20040101-20051231.nc'),
        ('SU','True'),
        ], #http://localhost:8090/thredds/fileServer/test/nils.hempelmann_hzg.de/tasmax_EUR11_test-pywpsInputbtel_q.nc
        outputs = [('output', True)],
        verbose=False
        )

    nose.tools.ok_('txt' in result[0]['reference'], result)
    content = urllib.urlopen(result[0]['reference']).read()
    nose.tools.ok_(not ('failed' in content), content)

@attr('online')
def test_visualisation():
    raise SkipTest

    result = wpsclient.execute(
    service = base.SERVICE,
    identifier = "visualisation",
    inputs = [('file_identifier', 'http://localhost:8080/thredds/fileServer/test/nils.hempelmann@hzg.de/tas_MNA-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_20010101-20051231.nc')],
    outputs = [('output', True)],
    verbose=True
    ) 

    nose.tools.ok_('html' in result, result)

@attr('online')
def test_icclim():
    raise SkipTest
    result = wpsclient.execute(
        service = base.SERVICE,
        identifier = "de.csc.icclim.worker",
        inputs = [('file_identifier', 'http://localhost:8090/thredds/fileServer/test/nils.hempelmann@hzg.de/tasmax_day_MPI-ESM-LR_historical_r1i1p1_20040101-20051231.nc'),
        ('SU','True'),
        ('token', TEST_TOKEN)], #http://localhost:8090/thredds/fileServer/test/nils.hempelmann_hzg.de/tasmax_EUR11_test-pywpsInputbtel_q.nc
        outputs = [('output', True)],
        verbose=False
        )

    nose.tools.ok_('txt' in result[0]['reference'], result)
    content = urllib.urlopen(result[0]['reference']).read()
    nose.tools.ok_(not ('failed' in content), content)

@attr('online')
def test_extractpoints():
    raise SkipTest
    result = wpsclient.execute(
        service = base.SERVICE,
        identifier = "extractpoints",
        inputs = [('file_identifier', 'http://localhost:8090/thredds/fileServer/test/nils.hempelmann@hzg.de/tasmax_day_MPI-ESM-LR_historical_r1i1p1_20040101-20051231.nc'),
        ('SU','True'),
        ], #http://localhost:8090/thredds/fileServer/test/nils.hempelmann_hzg.de/tasmax_EUR11_test-pywpsInputbtel_q.nc
        outputs = [('output', True)],
        verbose=False
        )

    nose.tools.ok_('txt' in result[0]['reference'], result)
    content = urllib.urlopen(result[0]['reference']).read()
    nose.tools.ok_(not ('failed' in content), content)
    
#def test_indices():
    
    #result = wpsclient.execute(
        #service = base.SERVICE,
        #identifier = "de.csc.indices.worker",
        #inputs = [('file_identifier', 'http://localhost:8080/thredds/fileServer/test/nils.hempelmann_hzg.de/tas_MNA-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_20010101-20051231.nc'), 
        #('file_identifier', 'http://localhost:8080/thredds/fileServer/test/nils.hempelmann_hzg.de/pr_MNA-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_20010101-20051231.nc'),
        #('tas_yearmean', 'True'), 
        #('pr_yearsum', 'False'), 
        #('tas_5to9mean', 'False'), 
        #('tas_6to8mean', 'True'),
        #('pr_5to9sum', 'False'), 
        #('pr_6to8sum', 'True'), 
        #('heavyprecip','True'), 
        #('prThreshold','20') ],
        #outputs = [('output', True)],
        #verbose=True
        #)
        
    #nose.tools.ok_('tar' in result[0]['reference'], result)
    
#def test_icclim2():
    
    #from malleefowl import cscenv
    
    #ncfile = ['/var/lib/pywps/files/nils.hempelmann_hzg.de/tasmax_EUR-11_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v1_day_20010101-20051231.nc']
    #outdir = '/var/lib/pywps/files/nils.hempelmann@hzg.de/'
    #result = cscenv.indices( outdir, ncfile, Coord=None, TG=False, TX=False, TN=False, RR=False, TG_5to9=False, TG_6to8=False, RR_5to9=False, RR_6to8=False, SU=False )# outdir, files, TG=False, TN=False, TX=False, SU=True, DTR=False, ETR=False , HI=False 
    ##result = cscenv.indices(outdir, self.get_nc_files(), self.Coord.getValue(), self.TG.getValue(), self.TX.getValue(), self.TN.getValue(), self.RR.getValue(), self.TG_5to9.getValue(), self.TG_6to8.getValue(), self.RR_5to9.getValue(), self.RR_6to8.getValue(), self.SU.getValue())

    ## '/var/lib/pywps/files/nils.hempelmann_hzg.de/tasmax_day_MPI-ESM-LR_historical_r1i1p1_20000101-20051231.nc' ,   ,
    
    #nose.tools.ok_('nc' in result, result)

   
