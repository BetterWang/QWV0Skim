from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIMB19_RERECO_WrongSignV0Skim_run327237_v3'
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
config.Data.unitsPerJob = 2
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/V0Production2018/'
config.Data.lumiMask = 'run327237.txt'
config.Data.publication = True
config.Data.outputDatasetTag = 'V0Skim_v3'
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
config.Site.whitelist = ['T2_CH_CERN']
config.Data.allowNonValidInputDataset = True
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

