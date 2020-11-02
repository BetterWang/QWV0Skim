from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getLumiListInValidFiles
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException
from WMCore.DataStructs.LumiList import LumiList


config = config()

config.General.requestName = 'HIMB1_RERECO_V0Skim_v3_recovery'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qw_PbPb18_withV0_Skim_v3.py'
#config.JobType.maxJobRuntimeMin = 2500
#config.JobType.inputFiles = ['HeavyIonRPRcd_PbPb2018_offline.db']
config.Data.inputDataset = '/HIMinimumBias1/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5
config.Data.outLFNDirBase = '/store/user/qwang/V0Production2018/'
config.Data.lumiMask = 'MB1_recovery.json'
config.Data.publication = True
config.Data.outputDatasetTag = 'V0Skim_v3'
config.Data.useParent = False
config.Site.storageSite = 'T2_US_Vanderbilt'
##config.Data.allowNonValidInputDataset = True
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB2_RERECO_V0Skim_v3_recovery2'
#config.Data.inputDataset = '/HIMinimumBias2/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB2_recovery2.json'
#config.Data.unitsPerJob = 2
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'HIMB3_RERECO_V0Skim_v3_recovery'
#config.Data.inputDataset = '/HIMinimumBias3/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB3_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'HIMB3_RERECO_V0Skim_v3_recovery3'
#config.Data.inputDataset = '/HIMinimumBias3/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB3_recovery3.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#

#config.General.requestName = 'HIMB19_RERECO_V0Skim_v3_recovery'
#config.Data.inputDataset = '/HIMinimumBias19/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB19_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB18_RERECO_V0Skim_v3_recovery'
#config.Data.inputDataset = '/HIMinimumBias18/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB18_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'HIMB3_RERECO_V0Skim_v3_recovery4'
#config.Data.inputDataset = '/HIMinimumBias3/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB3_recovery4.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB14_RERECO_V0Skim_v3_recovery'
#config.Data.inputDataset = '/HIMinimumBias14/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB14_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

#config.General.requestName = 'HIMB17_RERECO_V0Skim_v3_recovery'
#config.Data.inputDataset = '/HIMinimumBias17/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB17_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB16_RERECO_V0Skim_v3_recovery'
#config.Data.inputDataset = '/HIMinimumBias16/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB16_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.Data.unitsPerJob = 1
#config.General.requestName = 'HIMB13_RERECO_V0Skim_v3_recovery_v2'
#config.Data.inputDataset = '/HIMinimumBias13/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB13_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.Data.unitsPerJob = 1
#config.General.requestName = 'HIMB15_RERECO_V0Skim_v3_recovery_v2'
#config.Data.inputDataset = '/HIMinimumBias15/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB15_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#

config.Data.unitsPerJob = 1
#config.General.requestName = 'HIMB11_RERECO_V0Skim_v3_recovery_v2'
#config.Data.inputDataset = '/HIMinimumBias11/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB11_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB10_RERECO_V0Skim_v3_recovery_v2'
#config.Data.inputDataset = '/HIMinimumBias10/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB10_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB9_RERECO_V0Skim_v3_recovery_v2'
#config.Data.inputDataset = '/HIMinimumBias9/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB9_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB8_RERECO_V0Skim_v3_recovery_v2'
#config.Data.inputDataset = '/HIMinimumBias8/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.lumiMask = 'MB8_recovery.json'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
config.General.requestName = 'HIMB6_RERECO_V0Skim_v3_recovery_v2'
config.Data.inputDataset = '/HIMinimumBias6/HIRun2018A-04Apr2019-v1/AOD'
config.Data.lumiMask = 'MB6_recovery.json'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

