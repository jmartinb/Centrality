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

centralityBinHFSum = cms.EDProducer('CentralityBinProducer',
    Centrality = cms.InputTag("pACentrality"),
    centralityVariable = cms.string("HFtowers"),
    nonDefaultGlauberModel = cms.string(""),
    pPbRunFlip = cms.uint32(99999999),
)

centralityBinZDCPlus = cms.EDProducer('CentralityBinProducer',
    Centrality = cms.InputTag("pACentrality"),
    centralityVariable = cms.string("ZDChitsPlus"),
    nonDefaultGlauberModel = cms.string(""),
    pPbRunFlip = cms.uint32(99999999),
    )

centralityBinZDCMinus = cms.EDProducer('CentralityBinProducer',
    Centrality = cms.InputTag("pACentrality"),
    centralityVariable = cms.string("ZDChitsMinus"),
    nonDefaultGlauberModel = cms.string(""),
    pPbRunFlip = cms.uint32(99999999),
    )
