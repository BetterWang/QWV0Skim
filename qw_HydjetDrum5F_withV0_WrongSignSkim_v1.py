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

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic', '')

process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
	cms.PSet(record = cms.string("HeavyIonRcd"),
		tag = cms.string("CentralityTable_HFtowers200_HydjetDrum5F_v1020x01_mc"),
		connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
		label = cms.untracked.string("HFtowers")
		),
	])

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")


process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/HydjetDrum5F_RECODEBUG.root"),
#        secondaryFileNames = cms.untracked.vstring(
#		"root://xrootd.unl.edu//store/himc/HINPbPbAutumn18DR/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM-RAW/NoPU_103X_upgrade2018_realistic_HI_v11-v1/50000/2D7D7C84-0D3A-BB4E-ABBB-C4DD754916AE.root"
#		)
)



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

process.load('SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi')
process.load('SimTracker.TrackAssociatorProducers.trackAssociatorByHits_cfi')
process.load('SimGeneral.TrackingAnalysis.simHitTPAssociation_cfi')

process.RECO = cms.OutputModule("PoolOutputModule",
		outputCommands = cms.untracked.vstring(
			'keep *_TriggerResults_*_*',
			'keep *_offlinePrimaryVerticesRecovery_*_*',
			'keep *_centralityBin_*_*',
			'keep *_generalV0CandidatesNew_Kshort_*',
			'keep *_generalV0CandidatesNew_Lambda_*',
			'keep *_tpRecoAssocGeneralTracks_*_*',
			),
		SelectEvents = cms.untracked.PSet(
			SelectEvents = cms.vstring('ana')
			),
		fileName = cms.untracked.string('reco_Hydjet.root')
		)

process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")

process.tpRecoAssocGeneralTracks = process.trackingParticleRecoTrackAsssociation.clone()
process.tpRecoAssocGeneralTracks.label_tr = cms.InputTag("generalTracks")

process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
process.quickTrackAssociatorByHits.SimToRecoDenominator = cms.string('reco')

process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")

process.ana = cms.Path(
		process.tpClusterProducer *
		process.quickTrackAssociatorByHits *
		process.tpRecoAssocGeneralTracks *
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

