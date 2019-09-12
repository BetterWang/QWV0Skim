import FWCore.ParameterSet.Config as cms

process = cms.Process("QWV0Skim")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.load("RecoVertex.PrimaryVertexProducer.OfflinePrimaryVerticesRecovery_cfi")

process.load("RecoHI.HiEvtPlaneAlgos.HiEvtPlane_cfi")
process.load("RecoHI.HiEvtPlaneAlgos.hiEvtPlaneFlat_cfi")

#process.load("CondCore.CondDB.CondDB_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_dataRun2_Prompt_v2', '')

process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
	cms.PSet(record = cms.string("HeavyIonRcd"),
		tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline"),
		connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
		label = cms.untracked.string("HFtowers")
		),
	])

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")


#process.CondDB.connect = "sqlite_file:HeavyIonRPRcd_PbPb2018_offline.db"
#process.PoolDBESSource = cms.ESSource("PoolDBESSource",
#        process.CondDB,
#        toGet = cms.VPSet(cms.PSet(record = cms.string('HeavyIonRPRcd'),
#            tag = cms.string('HeavyIonRPRcd_PbPb2018_offline')
#            )
#            )
#        )
#process.es_prefer_flatparms = cms.ESPrefer('PoolDBESSource','')
#
#process.hiEvtPlane.trackTag = cms.InputTag("generalTracks")
#process.hiEvtPlane.vertexTag = cms.InputTag("offlinePrimaryVerticesRecovery")
#process.hiEvtPlane.loadDB = cms.bool(True)
#process.hiEvtPlane.useNtrk = cms.untracked.bool(False)
#process.hiEvtPlane.caloCentRef = cms.double(-1)
#process.hiEvtPlane.caloCentRefWidth = cms.double(-1)
#process.hiEvtPlaneFlat.caloCentRef = cms.double(-1)
#process.hiEvtPlaneFlat.caloCentRefWidth = cms.double(-1)
#process.hiEvtPlaneFlat.vertexTag = cms.InputTag("offlinePrimaryVerticesRecovery")
#process.hiEvtPlaneFlat.useNtrk = cms.untracked.bool(False)
#


process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:/eos/cms/store/hidata/HIRun2018A/HIMinimumBias19/AOD/04Apr2019-v1/260000/FF31F840-542E-1A49-ACF7-9043F8169E67.root")
)

import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltMB = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMB.HLTPaths = [
	"HLT_HIMinimumBias_*"
	]
process.hltMB.andOr = cms.bool(True)
process.hltMB.throw = cms.bool(False)


process.load("RecoVertex.V0Producer.generalV0Candidates_cff")

#process.generalV0CandidatesNew = process.generalV0Candidates.clone (
#	tkNhitsCut = cms.int32(3),
#	tkChi2Cut = cms.double(7.0),
#	dauTransImpactSigCut = cms.double(1.0),
#	dauLongImpactSigCut = cms.double(1.0),
#	vtxSignificance2DCut = cms.double(0.0),
#	vtxSignificance3DCut = cms.double(2.5),
#	collinearityCut = cms.double(0.997),
#	vertexRecoAlgorithm = cms.InputTag('GMOVertex'),
#)
process.generalV0CandidatesNew = process.generalV0Candidates.clone (
    selectD0s = cms.bool(False),
    selectLambdaCs = cms.bool(False),
    selectXis = cms.bool(False),
    selectOmegas = cms.bool(False),

    isWrongSign = cms.untracked.bool(True),

    tkNhitsCut = cms.int32(3),
    tkChi2Cut = cms.double(7.0),
    dauTransImpactSigCut = cms.double(1.0),
    dauLongImpactSigCut = cms.double(1.0),
    xiVtxSignificance3DCut = cms.double(0.0),
    xiVtxSignificance2DCut = cms.double(0.0),
    vtxSignificance2DCut = cms.double(0.0),
    vtxSignificance3DCut = cms.double(2.5),

    collinearityCut = cms.double(0.997),
    vertexRecoAlgorithm = cms.InputTag('offlinePrimaryVerticesRecovery'),

    innerHitPosCut = cms.double(-1)
)

process.RECO = cms.OutputModule("PoolOutputModule",
		outputCommands = cms.untracked.vstring(
			'keep *_TriggerResults_*_*',
			'keep *_offlinePrimaryVerticesRecovery_*_*',
			'keep *_centralityBin_*_*',
			'keep *_generalV0CandidatesNew_Kshort_*',
			'keep *_generalV0CandidatesNew_Lambda_*',
			'keep *_hiEvtPlane_*_*',
			'keep *_hiEvtPlaneFlat_*_*',
			),
		SelectEvents = cms.untracked.PSet(
			SelectEvents = cms.vstring('ana')
			),
		fileName = cms.untracked.string('reco.root')
		)

process.ana = cms.Path(
		process.hltMB *
		process.centralityBin *
		process.offlinePrimaryVerticesRecovery *
		process.generalV0CandidatesNew
		)

process.out = cms.EndPath(process.RECO)

process.schedule = cms.Schedule(
	process.ana,
	process.out
)

from HLTrigger.Configuration.CustomConfigs import MassReplaceInputTag
process = MassReplaceInputTag(process,"offlinePrimaryVertices","offlinePrimaryVerticesRecovery")
process.offlinePrimaryVerticesRecovery.oldVertexLabel = "offlinePrimaryVertices"

