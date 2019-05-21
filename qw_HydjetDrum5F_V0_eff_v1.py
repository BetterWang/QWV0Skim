import FWCore.ParameterSet.Config as cms

process = cms.Process("QWV0MC")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.load("RecoVertex.PrimaryVertexProducer.OfflinePrimaryVerticesRecovery_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
#process.MessageLogger.cerr.FwkReport.reportEvery = 100


process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring("file:reco_Hydjet.root"),
    secondaryFileNames = cms.untracked.vstring('file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/HydjetDrum5F_RECODEBUG.root')
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('v0.root')
    )


process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")

process.tpRecoAssocGeneralTracks = process.trackingParticleRecoTrackAsssociation.clone()
process.tpRecoAssocGeneralTracks.label_tr = cms.InputTag("generalTracks")

process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
process.quickTrackAssociatorByHits.SimToRecoDenominator = cms.string('reco')

process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")

process.V0valid = cms.EDAnalyzer('QWV0Validator',
        trackAssociatorMap = cms.untracked.InputTag('tpRecoAssocGeneralTracks'),
        trackingVertexCollection = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
        kShortCollection = cms.untracked.InputTag('generalV0CandidatesNew', 'Kshort'),
        lambdaCollection = cms.untracked.InputTag('generalV0CandidatesNew', 'Lambda'),
        )


process.ana = cms.Path(
#		process.tpClusterProducer *
#		process.quickTrackAssociatorByHits *
#		process.tpRecoAssocGeneralTracks *
		process.V0valid
		)

