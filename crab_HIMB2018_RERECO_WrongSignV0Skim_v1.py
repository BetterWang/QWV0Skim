from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIMB19_RERECO_WrongSignV0Skim_run327237_v5'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qw_PbPb18_withV0_WrongSignSkim_v3.py'
#config.JobType.maxJobRuntimeMin = 2500
#config.JobType.inputFiles = ['HeavyIonRPRcd_PbPb2018_offline.db']
config.Data.inputDataset = '/HIMinimumBias19/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5
config.Data.outLFNDirBase = '/store/user/qwang/V0Production2018/'
config.Data.lumiMask = 'run327237.txt'
config.Data.publication = True
config.Data.outputDatasetTag = 'V0SkimWrongSign_v3'
config.Data.useParent = False
config.Site.storageSite = 'T2_US_Vanderbilt'
config.JobType.allowUndistributedCMSSW = True
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

###
config.General.requestName = 'HIMB4_RERECO_WrongSignV0Skim_v5'
config.Data.inputDataset = '/HIMinimumBias2/HIRun2018A-04Apr2019-v1/AOD'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

