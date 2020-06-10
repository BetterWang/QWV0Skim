from CRABClient.UserUtilities import config, getLumiListInValidFiles
from WMCore.DataStructs.LumiList import LumiList

taskALumis = getLumiListInValidFiles(dataset='/HIMinimumBias15/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER', dbsurl='phys03')

officialLumiMask = LumiList(filename='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt')

newLumiMask = officialLumiMask - taskALumis

newLumiMask.writeJSON('t.json')

