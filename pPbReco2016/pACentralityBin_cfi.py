import FWCore.ParameterSet.Config as cms

centralityBinHFPlusFwd = cms.EDProducer('CentralityBinProducer',
    Centrality = cms.InputTag("pACentrality"),
    centralityVariable = cms.string("HFtowersPlusTrunc"),
    nonDefaultGlauberModel = cms.string(""),
    pPbRunFlip = cms.uint32(99999999),
)

centralityBinHFMinusFwd = cms.EDProducer('CentralityBinProducer',
    Centrality = cms.InputTag("pACentrality"),
    centralityVariable = cms.string("HFtowersMinusTrunc"),
    nonDefaultGlauberModel = cms.string(""),
    pPbRunFlip = cms.uint32(99999999),
)

centralityBinHFSumFwd = cms.EDProducer('CentralityBinProducer',
    Centrality = cms.InputTag("pACentrality"),
    centralityVariable = cms.string("HFtowers"),
    nonDefaultGlauberModel = cms.string(""),
    pPbRunFlip = cms.uint32(99999999),
)

