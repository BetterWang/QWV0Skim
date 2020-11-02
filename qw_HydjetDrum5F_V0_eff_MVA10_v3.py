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


process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/reco_Hydjet.root"),
    secondaryFileNames = cms.untracked.vstring('file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/HydjetDrum5F_RECODEBUG.root')
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('v0.root')
    )


process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
#process.centralityBin.nonDefaultGlauberModel = cms.string("Drum5F")
process.dbCent = cms.EDProducer('QWInt2Double',
        src = cms.untracked.InputTag('centralityBin', 'HFtowers')
        )

process.load('RecoHI.HiCentralityAlgos.CentralityFilter_cfi')
process.CentFilter_0 = process.centralityFilter.clone(
        selectedBins = cms.vint32(
            *range(0, 20)
            ),
        BinLabel = cms.InputTag("centralityBin", "HFtowers")
        )
process.CentFilter_1 = process.centralityFilter.clone(
        selectedBins = cms.vint32(
            *range(20, 40)
            ),
        BinLabel = cms.InputTag("centralityBin", "HFtowers")
        )
process.CentFilter_2 = process.centralityFilter.clone(
        selectedBins = cms.vint32(
            *range(40, 60)
            ),
        BinLabel = cms.InputTag("centralityBin", "HFtowers")
        )
process.CentFilter_3 = process.centralityFilter.clone(
        selectedBins = cms.vint32(
            *range(60, 80)
            ),
        BinLabel = cms.InputTag("centralityBin", "HFtowers")
        )
process.CentFilter_4 = process.centralityFilter.clone(
        selectedBins = cms.vint32(
            *range(80, 100)
            ),
        BinLabel = cms.InputTag("centralityBin", "HFtowers")
        )
process.CentFilter_5 = process.centralityFilter.clone(
        selectedBins = cms.vint32(
            *range(100, 120)
            ),
        BinLabel = cms.InputTag("centralityBin", "HFtowers")
        )
process.CentFilter_6 = process.centralityFilter.clone(
        selectedBins = cms.vint32(
            *range(120, 140)
            ),
        BinLabel = cms.InputTag("centralityBin", "HFtowers")
        )
process.CentFilter_7 = process.centralityFilter.clone(
        selectedBins = cms.vint32(
            *range(140, 160)
            ),
        BinLabel = cms.InputTag("centralityBin", "HFtowers")
        )
process.CentFilter_8 = process.centralityFilter.clone(
        selectedBins = cms.vint32(
            *range(160, 180)
            ),
        BinLabel = cms.InputTag("centralityBin", "HFtowers")
        )
process.CentFilter_9 = process.centralityFilter.clone(
        selectedBins = cms.vint32(
            *range(180, 200)
            ),
        BinLabel = cms.InputTag("centralityBin", "HFtowers")
        )


process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")

process.tpRecoAssocGeneralTracks = process.trackingParticleRecoTrackAsssociation.clone()
process.tpRecoAssocGeneralTracks.label_tr = cms.InputTag("generalTracks")

process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
process.quickTrackAssociatorByHits.SimToRecoDenominator = cms.string('reco')

process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")

process.QWV0EventLm = cms.EDProducer('QWV0VectProducer'
        , vertexSrc = cms.untracked.InputTag('offlinePrimaryVerticesRecovery')
        , trackSrc = cms.untracked.InputTag('generalTracks')
        , V0Src = cms.untracked.InputTag('generalV0CandidatesNew', 'Lambda')
        , daughter_cuts = cms.untracked.PSet(
            )
        , cuts = cms.untracked.VPSet(
            cms.untracked.PSet(
                Massmin = cms.untracked.double(1.08)
                , Massmax = cms.untracked.double(1.16)
                , DecayXYZMin = cms.untracked.double(2.5)
                , ThetaXYZMin = cms.untracked.double(0.999)
                , ptMin = cms.untracked.double(0.2)
                , ptMax = cms.untracked.double(8.5)
                )
            )
        )


process.QWV0EventKs = cms.EDProducer('QWV0VectProducer'
        , vertexSrc = cms.untracked.InputTag('offlinePrimaryVerticesRecovery')
        , trackSrc = cms.untracked.InputTag('generalTracks')
        , V0Src = cms.untracked.InputTag('generalV0CandidatesNew', 'Kshort')
        , daughter_cuts = cms.untracked.PSet(
            )
        , cuts = cms.untracked.VPSet(
            cms.untracked.PSet(
                Massmin = cms.untracked.double(0.43)
                , Massmax = cms.untracked.double(0.565)
                , DecayXYZMin = cms.untracked.double(2.5)
                , ThetaXYZMin = cms.untracked.double(0.999)
                , ptMin = cms.untracked.double(0.2)
                , ptMax = cms.untracked.double(8.5)
                )
            )
        )


process.QWLmMVAMCFullRap1 = cms.EDProducer('QWV0MVAVectProducer'
        , vertexSrc = cms.untracked.InputTag('offlinePrimaryVerticesRecovery')
        , V0Src = cms.untracked.InputTag('QWV0EventLm', 'Lambda')
        , dbCent = cms.untracked.InputTag('dbCent')
        , mvaXML = cms.untracked.string('MC_Full_BDT250_D4.LM.weights.xml')
        , mvaCut = cms.untracked.double(0.10)
        )

process.QWKsMVAMCFullRap1 = cms.EDProducer('QWV0MVAVectProducer'
        , vertexSrc = cms.untracked.InputTag('offlinePrimaryVerticesRecovery')
        , V0Src = cms.untracked.InputTag('QWV0EventKs', 'Kshort')
        , dbCent = cms.untracked.InputTag('dbCent')
        , mvaXML = cms.untracked.string('MC_Full_BDT250_D4.KS.weights.xml')
        , mvaCut = cms.untracked.double(0.10)
        )

process.V0valid = cms.EDAnalyzer('QWV0Validator',
        trackAssociatorMap = cms.untracked.InputTag('tpRecoAssocGeneralTracks'),
        trackingVertexCollection = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
        kShortCollection = cms.untracked.InputTag('QWKsMVAMCFullRap1', 'Kshort'),
        lambdaCollection = cms.untracked.InputTag('QWLmMVAMCFullRap1', 'Lambda'),
        )

process.V0valid_0 = process.V0valid.clone()
process.V0valid_1 = process.V0valid.clone()
process.V0valid_2 = process.V0valid.clone()
process.V0valid_3 = process.V0valid.clone()
process.V0valid_4 = process.V0valid.clone()
process.V0valid_5 = process.V0valid.clone()
process.V0valid_6 = process.V0valid.clone()
process.V0valid_7 = process.V0valid.clone()
process.V0valid_8 = process.V0valid.clone()
process.V0valid_9 = process.V0valid.clone()

process.RECO = cms.OutputModule("PoolOutputModule",
        outputCommands = cms.untracked.vstring(
            'drop *',
            'keep *_*_*_QWV0MC',
            ),
        SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('ana_0', 'ana_1', 'ana_3', 'ana_5')
            ),
        fileName = cms.untracked.string('recoV0.root')
        )

process.ana_0 = cms.Path(
        process.dbCent *
        process.CentFilter_0 *
        process.QWV0EventKs *
        process.QWV0EventLm *
        process.QWKsMVAMCFullRap1 *
        process.QWLmMVAMCFullRap1 *
        process.V0valid_0
		)
process.ana_1 = cms.Path(
        process.dbCent *
        process.CentFilter_1 *
        process.QWV0EventKs *
        process.QWV0EventLm *
        process.QWKsMVAMCFullRap1 *
        process.QWLmMVAMCFullRap1 *
        process.V0valid_1
		)
process.ana_2 = cms.Path(
        process.dbCent *
        process.CentFilter_2 *
        process.QWV0EventKs *
        process.QWV0EventLm *
        process.QWKsMVAMCFullRap1 *
        process.QWLmMVAMCFullRap1 *
        process.V0valid_2
		)
process.ana_3 = cms.Path(
        process.dbCent *
        process.CentFilter_3 *
        process.QWV0EventKs *
        process.QWV0EventLm *
        process.QWKsMVAMCFullRap1 *
        process.QWLmMVAMCFullRap1 *
        process.V0valid_3
		)
process.ana_4 = cms.Path(
        process.dbCent *
        process.CentFilter_4 *
        process.QWV0EventKs *
        process.QWV0EventLm *
        process.QWKsMVAMCFullRap1 *
        process.QWLmMVAMCFullRap1 *
        process.V0valid_4
		)
process.ana_5 = cms.Path(
        process.dbCent *
        process.CentFilter_5 *
        process.QWV0EventKs *
        process.QWV0EventLm *
        process.QWKsMVAMCFullRap1 *
        process.QWLmMVAMCFullRap1 *
        process.V0valid_5
		)
process.ana_6 = cms.Path(
        process.dbCent *
        process.CentFilter_6 *
        process.QWV0EventKs *
        process.QWV0EventLm *
        process.QWKsMVAMCFullRap1 *
        process.QWLmMVAMCFullRap1 *
        process.V0valid_6
		)
process.ana_7 = cms.Path(
        process.dbCent *
        process.CentFilter_7 *
        process.QWV0EventKs *
        process.QWV0EventLm *
        process.QWKsMVAMCFullRap1 *
        process.QWLmMVAMCFullRap1 *
        process.V0valid_7
		)
process.ana_8 = cms.Path(
        process.dbCent *
        process.CentFilter_8 *
        process.QWV0EventKs *
        process.QWV0EventLm *
        process.QWKsMVAMCFullRap1 *
        process.QWLmMVAMCFullRap1 *
        process.V0valid_8
		)
process.ana_9 = cms.Path(
        process.dbCent *
        process.CentFilter_9 *
        process.QWV0EventKs *
        process.QWV0EventLm *
        process.QWKsMVAMCFullRap1 *
        process.QWLmMVAMCFullRap1 *
        process.V0valid_9
		)
process.schedule = cms.Schedule(
        process.ana_0,
        process.ana_1,
        process.ana_2,
        process.ana_3,
        process.ana_4,
        process.ana_5,
        process.ana_6,
        process.ana_7,
        process.ana_8,
        process.ana_9,
        )
#process.out = cms.EndPath(process.RECO)
from HLTrigger.Configuration.CustomConfigs import MassReplaceInputTag
process = MassReplaceInputTag(process,"offlinePrimaryVertices","offlinePrimaryVerticesRecovery")
process.offlinePrimaryVerticesRecovery.oldVertexLabel = "offlinePrimaryVertices"

