import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = readFiles
)
readFiles.extend([
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_1_3_dls.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_2_3_v85.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_3_0_7mb.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_4_0_A0j.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_5_0_jaV.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_6_0_jHF.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_7_0_yKo.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_8_0_2S0.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_9_1_nOR.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_10_0_w0D.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_11_1_dBR.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_12_0_vqs.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_13_1_Lpv.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_14_0_hX3.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_15_0_hXX.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_16_0_vUN.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_17_1_Ovv.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_18_0_KJh.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_19_0_MNC.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_20_1_wIs.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_21_0_4Vt.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_22_0_pPL.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_23_0_13F.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_24_2_vHD.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_25_0_pdc.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_26_1_adM.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_27_0_nJM.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_28_2_Qnb.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_29_0_vaQ.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_30_3_iVE.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_31_2_2Wf.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_32_2_C8G.root",
    "rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuEl/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_33_0_fn3.root",
])
