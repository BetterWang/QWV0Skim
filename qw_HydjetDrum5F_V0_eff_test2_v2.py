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


process.QWV0EventLambda = cms.EDProducer('QWV0VectProducer'
        , vertexSrc = cms.untracked.InputTag('offlinePrimaryVerticesRecovery')
        , trackSrc = cms.untracked.InputTag('generalTracks')
        , V0Src = cms.untracked.InputTag('generalV0CandidatesNew', 'Lambda')
        , daughter_cuts = cms.untracked.PSet(
                dauPtMin = cms.untracked.double(0.4),
                dauEtaMin = cms.untracked.double(-2.4),
                dauEtaMax = cms.untracked.double(2.4),
            )
        , cuts = cms.untracked.VPSet(
            cms.untracked.PSet(
                Massmin = cms.untracked.double(1.08)
                , Massmax = cms.untracked.double(1.16)
                , DecayXYZMin = cms.untracked.double(5.0)
                , ThetaXYZMin = cms.untracked.double(0.99999)
                , ptMin = cms.untracked.double(0.2)
                , ptMax = cms.untracked.double(8.5)
                )
            )
        )

process.V0valid = cms.EDAnalyzer('QWV0Validator',
        trackAssociatorMap = cms.untracked.InputTag('tpRecoAssocGeneralTracks'),
        trackingVertexCollection = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
        kShortCollection = cms.untracked.InputTag('generalV0CandidatesNew', 'Kshort'),
        lambdaCollection = cms.untracked.InputTag('QWV0EventLambda'),
        )

process.ana = cms.Path(
#		process.tpClusterProducer *
#		process.quickTrackAssociatorByHits *
#		process.tpRecoAssocGeneralTracks *
        process.QWV0EventLambda *
        process.V0valid
		)

