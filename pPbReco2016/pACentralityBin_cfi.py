import FWCore.ParameterSet.Config as cms

centralityBin_HFPlusFwd = cms.EDProducer('CentralityBinProducer',
    Centrality = cms.InputTag("hiCentrality"),
    centralityVariable = cms.string("HFtowersPlusTrunc"),
    nonDefaultGlauberModel = cms.string(""),
    pPbRunFlip = cms.uint32(99999999),
)

centralityBin_HFMinusFwd = cms.EDProducer('CentralityBinProducer',
    Centrality = cms.InputTag("hiCentrality"),
    centralityVariable = cms.string("HFtowersMinusTrunc"),
    nonDefaultGlauberModel = cms.string(""),
    pPbRunFlip = cms.uint32(99999999),
)

centralityBin_HFSumFwd = cms.EDProducer('CentralityBinProducer',
    Centrality = cms.InputTag("hiCentrality"),
    centralityVariable = cms.string("HFtowers"),
    nonDefaultGlauberModel = cms.string(""),
    pPbRunFlip = cms.uint32(99999999),
)

