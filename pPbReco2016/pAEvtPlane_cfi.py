import FWCore.ParameterSet.Config as cms

hiEvtPlaneHFPlusFwd = cms.EDProducer("EvtPlaneProducer",
                            vertexTag = cms.InputTag("offlinePrimaryVertices"),
                            caloTag = cms.InputTag("towerMaker"),
                            castorTag = cms.InputTag("CastorTowerReco"),
                            trackTag = cms.InputTag("generalTracks"),
                            centralityBinTag = cms.InputTag("centralityBinHFPlusFwd","HFtowersPlusTrunc"),
                            centralityVariable = cms.string("HFtowersPlusTrunc"),
                            nonDefaultGlauberModel = cms.string(""),
                            FlatOrder = cms.int32(9),
                            NumFlatBins = cms.int32(40),
                            CentBinCompression = cms.int32(5),
                            caloCentRef = cms.double(80.),
                            caloCentRefWidth = cms.double(5.0),
                            loadDB = cms.bool(False),
                            minet = cms.double(-1.),
                            maxet = cms.double(-1.),
                            minpt = cms.double(0.3),
                            maxpt = cms.double(3.0),
                            minvtx = cms.double(-25.),
                            maxvtx = cms.double(25.),
                            dzerr = cms.double(10.),
                            chi2 = cms.double(40.)
                            )

hiEvtPlaneHFMinusFwd = cms.EDProducer("EvtPlaneProducer",
                            vertexTag = cms.InputTag("offlinePrimaryVertices"),
                            caloTag = cms.InputTag("towerMaker"),
                            castorTag = cms.InputTag("CastorTowerReco"),
                            trackTag = cms.InputTag("generalTracks"),
                            centralityBinTag = cms.InputTag("centralityBinHFMinusFwd","HFtowersMinusTrunc"),
                            centralityVariable = cms.string("HFtowersMinusTrunc"),
                            nonDefaultGlauberModel = cms.string(""),
                            FlatOrder = cms.int32(9),
                            NumFlatBins = cms.int32(40),
                            CentBinCompression = cms.int32(5),
                            caloCentRef = cms.double(80.),
                            caloCentRefWidth = cms.double(5.0),
                            loadDB = cms.bool(False),
                            minet = cms.double(-1.),
                            maxet = cms.double(-1.),
                            minpt = cms.double(0.3),
                            maxpt = cms.double(3.0),
                            minvtx = cms.double(-25.),
                            maxvtx = cms.double(25.),
                            dzerr = cms.double(10.),
                            chi2 = cms.double(40.)
                            )

hiEvtPlaneHFSum = cms.EDProducer("EvtPlaneProducer",
                            vertexTag = cms.InputTag("offlinePrimaryVertices"),
                            caloTag = cms.InputTag("towerMaker"),
                            castorTag = cms.InputTag("CastorTowerReco"),
                            trackTag = cms.InputTag("generalTracks"),
                            centralityBinTag = cms.InputTag("centralityBinHFSum","HFtowers"),
                            centralityVariable = cms.string("HFtowers"),
                            nonDefaultGlauberModel = cms.string(""),
                            FlatOrder = cms.int32(9),
                            NumFlatBins = cms.int32(40),
                            CentBinCompression = cms.int32(5),
                            caloCentRef = cms.double(80.),
                            caloCentRefWidth = cms.double(5.0),
                            loadDB = cms.bool(False),
                            minet = cms.double(-1.),
                            maxet = cms.double(-1.),
                            minpt = cms.double(0.3),
                            maxpt = cms.double(3.0),
                            minvtx = cms.double(-25.),
                            maxvtx = cms.double(25.),
                            dzerr = cms.double(10.),
                            chi2 = cms.double(40.)
                            )

hiEvtPlaneZDCPlus = cms.EDProducer("EvtPlaneProducer",
                            vertexTag = cms.InputTag("offlinePrimaryVertices"),
                            caloTag = cms.InputTag("towerMaker"),
                            castorTag = cms.InputTag("CastorTowerReco"),
                            trackTag = cms.InputTag("generalTracks"),
                            centralityBinTag = cms.InputTag("centralityBinZDCPlus","ZDChitsPlus"),
                            centralityVariable = cms.string("ZDChitsPlus"),
                            nonDefaultGlauberModel = cms.string(""),
                            FlatOrder = cms.int32(9),
                            NumFlatBins = cms.int32(40),
                            CentBinCompression = cms.int32(5),
                            caloCentRef = cms.double(80.),
                            caloCentRefWidth = cms.double(5.0),
                            loadDB = cms.bool(False),
                            minet = cms.double(-1.),
                            maxet = cms.double(-1.),
                            minpt = cms.double(0.3),
                            maxpt = cms.double(3.0),
                            minvtx = cms.double(-25.),
                            maxvtx = cms.double(25.),
                            dzerr = cms.double(10.),
                            chi2 = cms.double(40.)
                            )

hiEvtPlaneZDCMinus = cms.EDProducer("EvtPlaneProducer",
                            vertexTag = cms.InputTag("offlinePrimaryVertices"),
                            caloTag = cms.InputTag("towerMaker"),
                            castorTag = cms.InputTag("CastorTowerReco"),
                            trackTag = cms.InputTag("generalTracks"),
                            centralityBinTag = cms.InputTag("centralityBinZDCMinus","ZDChitsMinus"),
                            centralityVariable = cms.string("ZDChitsMinus"),
                            nonDefaultGlauberModel = cms.string(""),
                            FlatOrder = cms.int32(9),
                            NumFlatBins = cms.int32(40),
                            CentBinCompression = cms.int32(5),
                            caloCentRef = cms.double(80.),
                            caloCentRefWidth = cms.double(5.0),
                            loadDB = cms.bool(False),
                            minet = cms.double(-1.),
                            maxet = cms.double(-1.),
                            minpt = cms.double(0.3),
                            maxpt = cms.double(3.0),
                            minvtx = cms.double(-25.),
                            maxvtx = cms.double(25.),
                            dzerr = cms.double(10.),
                            chi2 = cms.double(40.)
                            )
