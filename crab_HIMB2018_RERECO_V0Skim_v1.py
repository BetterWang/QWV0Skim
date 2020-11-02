from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIMB1_RERECO_V0Skim_v3_rerun'
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
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt'
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


#config.General.requestName = 'HIMB2_RERECO_V0Skim_v3_rerun'
#config.Data.inputDataset = '/HIMinimumBias2/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)


#config.General.requestName = 'HIMB3_RERECO_V0Skim_v3_rerun'
#config.Data.inputDataset = '/HIMinimumBias3/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB4_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias4/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB19_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias19/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

#config.Data.splitting = 'Automatic'
#config.General.requestName = 'HIMB18_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias18/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

#config.General.requestName = 'HIMB17_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias17/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

#config.General.requestName = 'HIMB16_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias16/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

#config.General.requestName = 'HIMB14_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias14/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB13_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias13/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB15_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias15/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB12_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias12/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB11_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias11/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB10_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias10/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB9_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias9/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB8_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias8/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB7_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias7/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB6_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias6/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#config.General.requestName = 'HIMB5_RERECO_V0Skim_v3'
#config.Data.inputDataset = '/HIMinimumBias5/HIRun2018A-04Apr2019-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
config.General.requestName = 'HIMB0_RERECO_V0Skim_v3'
config.Data.inputDataset = '/HIMinimumBias0/HIRun2018A-04Apr2019-v1/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

