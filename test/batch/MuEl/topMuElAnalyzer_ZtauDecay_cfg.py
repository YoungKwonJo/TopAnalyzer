import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntuple")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring()
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('vallot_ZtauDecay.root')
)

process.load("KoPFA.TopAnalyzer.Sources.EMU.MC.Spring11.patTuple_DYJetsToLL_cff")
process.load("KoPFA.TopAnalyzer.topAnalysis_cff")

process.GenZmassFilter.applyFilter = True
process.GenZmassFilter.decayMode = [15]
process.GenZmassFilter.min = 50
process.GenZmassFilter.max = 999999

process.p = cms.Path(
    process.topMuElAnalysisMCSequence
)


