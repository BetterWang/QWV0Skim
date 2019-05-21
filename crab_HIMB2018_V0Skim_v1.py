from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIMB1A_V0Skim_v1'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qw_PbPb18_withV0_Skim_v1.py'
config.JobType.maxJobRuntimeMin = 2500
#config.JobType.inputFiles = ['Hydjet_PbPb_eff_v1.root', 'Hydjet_ppReco_v5_loose.root']
config.Data.inputDataset = '/HIMinimumBias1/HIRun2018A-PromptReco-v2/AOD'
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5
config.Data.outLFNDirBase = '/store/user/qwang/PbPb2015/'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.publication = True
#config.Data.outputDatasetTag = ''
config.Data.useParent = False
config.Site.storageSite = 'T2_US_Vanderbilt'
##config.Data.allowNonValidInputDataset = True
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIMB2A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias2/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB3A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias3/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB4A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias4/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB5A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias5/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB6A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias6/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB7A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias7/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB8A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias8/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB9A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias9/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB10A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias10/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB11A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias11/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB12A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias12/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB13A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias13/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB14A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias14/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB15A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias15/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB16A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias16/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB17A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias17/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB18A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias18/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB19A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias19/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB0A_V0Skim_v1'
config.Data.inputDataset = '/HIMinimumBias0/HIRun2018A-PromptReco-v2/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

