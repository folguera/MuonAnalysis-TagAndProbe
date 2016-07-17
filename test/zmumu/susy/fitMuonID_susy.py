import FWCore.ParameterSet.Config as cms

#_*_*_*_*_*_*_*_*
#Input parameters
#_*_*_*_*_*_*_*_*

import sys, os
args = sys.argv[1:]
id_bins = '1'
if len(args) > 1: scenario = args[1]
if len(args) > 2: id_bins = args[2]
print "Will run scenario ", scenario 
print "id_bins = ", id_bins
#for MC

process = cms.Process("TagProbe")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

#_*_*_*_*_*_*_*_*_*_*_*_*
#Preparing the variables
#_*_*_*_*_*_*_*_*_*_*_*_*

_mrange = "70"
if (int(id_bins) > 4) and (int(id_bins) < 19): 
    _mrange = "77"


Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
        NumCPU = cms.uint32(1),
    SaveWorkspace = cms.bool(False),

    Variables = cms.PSet(
        weight = cms.vstring("weight","-100","100",""),
        #mass = cms.vstring("Tag-muon Mass", "70", "130", "GeV/c^{2}"),
        mass = cms.vstring("Tag-muon Mass", _mrange, "130", "GeV/c^{2}"),
        pt = cms.vstring("muon p_{T}", "0", "1000", "GeV/c"),
        eta    = cms.vstring("muon #eta", "-2.5", "2.5", ""),
        abseta = cms.vstring("muon |#eta|", "0", "2.5", ""),
        phi    = cms.vstring("muon #phi at vertex", "-3.1416", "3.1416", ""),
        charge = cms.vstring("muon charge", "-2.5", "2.5", ""),
        glbPtError = cms.vstring("p_{T} error", "0", "20", "GeV/c"),
        combRelIsoPF04dBeta = cms.vstring("dBeta rel iso dR 0.4", "-2", "9999999", ""),
        pfCombRelActivitydBCorr = cms.vstring("Rel. Activity", "-2", "9999999", ""),
#        pfCombRelMiniIsoEACorr = cms.vstring("Mini Iso", "-2", "9999999",""),
        #miniIsoCharged  = cms.vstring("Mini Iso Charged", "-2", "9999999",""),
        #miniIsoPhotons  = cms.vstring("Mini Iso Photons", "-2", "9999999",""),
        #miniIsoNeutrals = cms.vstring("Mini Iso Neutrals", "-2", "9999999",""),
        JetPtRel = cms.vstring("JetPtRel", "-2", "20",""),
        JetPtRatio = cms.vstring("JetPtRatio", "-2", "2000",""),
        tag_pt = cms.vstring("Tag p_{T}", "0", "500", "GeV/c"),
        tag_nVertices   = cms.vstring("Number of vertices", "0", "999", ""),
        tag_abseta = cms.vstring("|eta| of tag muon", "0", "2.5", ""),
        tag_combRelIsoPF04dBeta = cms.vstring("Tag dBeta rel iso dR 0.4", "-2", "999", ""),
        dzPV = cms.vstring("dzPV", "-100", "100", ""),
        dxyBS = cms.vstring("dxyBS", "-100", "100", ""),
        SIP = cms.vstring("SIP", "-100", "100", ""),
        pair_probeMultiplicity = cms.vstring("pair_probeMultiplicity", "0","30",""),
        ),

    Categories = cms.PSet(
        PF    = cms.vstring("PF Muon", "dummy[pass=1,fail=0]"),
        Medium   = cms.vstring("Medium Id. Muon", "dummy[pass=1,fail=0]"),
        Medium2016   = cms.vstring("Medium2016 Id. Muon", "dummy[pass=1,fail=0]"),
        tag_IsoMu20 = cms.vstring("PF Muon", "dummy[pass=1,fail=0]"),
    ),

    Expressions = cms.PSet(
        #ID no IP  1, 2
        Loose_noIPVar = cms.vstring("Loose_noIPVar", "PF==1", "PF"),
        Medium_noIPVar= cms.vstring("Medium_noIPVar", "Medium2016==1", "Medium2016"),

        #Mini Iso
        #LooseMiniIsoVar = cms.vstring("LooseMiniIsoVar" ,"(miniIsoCharged + miniIsoNeutrals + miniIsoPhotons)/pt < 0.4", "miniIsoCharged", "miniIsoNeutrals", "miniIsoPhotons", "pt"),
        #TightMiniIsoVar = cms.vstring("TightMiniIsoVar" ,"(miniIsoCharged + miniIsoNeutrals + miniIsoPhotons)/pt < 0.2", "miniIsoCharged", "miniIsoNeutrals", "miniIsoPhotons", "pt"),
        #Multi Iso
        #LooseMultiIsoVar = cms.vstring("LooseMultiIsoVar" , "(miniIsoCharged + miniIsoNeutrals + miniIsoPhotons)/pt < 0.20 && ( JetPtRel > 6.0 || JetPtRatio > 0.69 )", "miniIsoCharged", "miniIsoNeutrals", "miniIsoPhotons", "JetPtRel", "JetPtRatio", "pt"),
        #MediumMultiIsoVar= cms.vstring("MediumMultiIsoVar", "(miniIsoCharged + miniIsoNeutrals + miniIsoPhotons)/pt < 0.16 && ( JetPtRel > 7.2 || JetPtRatio > 0.76 )", "miniIsoCharged", "miniIsoNeutrals", "miniIsoPhotons", "JetPtRel", "JetPtRatio", "pt"),
        #VTMultiIsoVar    = cms.vstring("VTMultiIsoVar" ,    "(miniIsoCharged + miniIsoNeutrals + miniIsoPhotons)/pt < 0.09 && ( JetPtRel > 7.2 || JetPtRatio > 0.84 )", "miniIsoCharged", "miniIsoNeutrals", "miniIsoPhotons", "JetPtRel", "JetPtRatio", "pt"),

        #Mini Iso
#        LooseMiniIsoVar = cms.vstring("LooseMiniIsoVar" ,"pfCombRelMiniIsoEACorr < 0.4", "pfCombRelMiniIsoEACorr"),
#        TightMiniIsoVar = cms.vstring("TightMiniIsoVar" ,"pfCombRelMiniIsoEACorr < 0.2", "pfCombRelMiniIsoEACorr"),
        #Multi Iso
#        LooseMultiIsoVar = cms.vstring("LooseMultiIsoVar" , "pfCombRelMiniIsoEACorr < 0.20 && ( JetPtRel > 6.0 || JetPtRatio > 0.69 )", "JetPtRel", "JetPtRatio", "pfCombRelMiniIsoEACorr"),
#        MediumMultiIsoVar= cms.vstring("MediumMultiIsoVar", "pfCombRelMiniIsoEACorr < 0.16 && ( JetPtRel > 7.2 || JetPtRatio > 0.76 )", "JetPtRel", "JetPtRatio", "pfCombRelMiniIsoEACorr"),
#        VTMultiIsoVar    = cms.vstring("VTMultiIsoVar" ,    "pfCombRelMiniIsoEACorr < 0.09 && ( JetPtRel > 7.2 || JetPtRatio > 0.84 )", "JetPtRel", "JetPtRatio", "pfCombRelMiniIsoEACorr"),

        #IP   11, 12, 13
        MediumIP2DVar  = cms.vstring("MediumIP2DVar", "abs(dxyBS) < 0.2 && abs(dzPV) < 0.5", "dxyBS", "dzPV"),
        TightIP2DVar  = cms.vstring("TightIP2DVar", "abs(dxyBS) < 0.05 && abs(dzPV) < 0.1", "dxyBS", "dzPV"),
        TightIP3DVar  = cms.vstring("TightIP3DVar", "abs(SIP) < 4", "SIP"),
        pterrorVar    = cms.vstring("pterrorVar", "glbPtError/pt < 0.2", "glbPtError", "pt"),


        #Stacked requirements

        #Loose + Miniso02
       # Loose_plus_MiniIso02Var= cms.vstring("Loose_plus_MiniIso02Var" ,"PF==1 && pfCombRelMiniIsoEACorr < 0.2", "PF", "pfCombRelMiniIsoEACorr"),
        #Loose + Miniso02 + TightIP2D
        #Loose_plus_MiniIso02_puls_TightIP2DVar= cms.vstring("Loose_plus_MiniIso02_puls_TightIP2DVar" ,"PF==1 && pfCombRelMiniIsoEACorr < 0.2 && abs(dxyBS) < 0.02 && abs(dzPV) < 0.1", "PF", "pfCombRelMiniIsoEACorr", "dxyBS", "dzPV"),
        #Medium + Miniso02
        #Medium_plus_MiniIso02Var= cms.vstring("Medium_plus_MiniIso02Var" ,"Medium==1 && pfCombRelMiniIsoEACorr < 0.2", "Medium", "pfCombRelMiniIsoEACorr"),
        #Loose + Miniso02 + TightIP3D
        #Loose_plus_MiniIso02_puls_TightIP3DVar= cms.vstring("Loose_plus_MiniIso02_puls_TightIP3DVar" ,"PF==1 && pfCombRelMiniIsoEACorr < 0.2 && abs(SIP) < 4", "PF", "pfCombRelMiniIsoEACorr", "SIP"),
        #Medium + Miniso02 + TightIP3D
        #Medium_plus_MiniIso02_puls_TightIP3DVar= cms.vstring("Medium_plus_MiniIso02_puls_TightIP3DVar" ,"Medium==1 && pfCombRelMiniIsoEACorr < 0.2 && abs(SIP) < 4", "Medium", "pfCombRelMiniIsoEACorr", "SIP"),
        #Medium + Miniso02 + TightIP2D
        #Medium_plus_MiniIso02_puls_TightIP2DVar= cms.vstring("Medium_plus_MiniIso02_puls_TightIP2DVar" ,"Medium==1 && pfCombRelMiniIsoEACorr < 0.2 && abs(dxyBS) < 0.02 && abs(dzPV) < 0.1", "Medium", "pfCombRelMiniIsoEACorr", "dxyBS", "dzPV"),
        #Medium + MultiIsoMedium + TightIP2D + TightIP3D
        #Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3DVar= cms.vstring("Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3DVar" ,"Medium==1 && pfCombRelMiniIsoEACorr < 0.16 && ( JetPtRel > 7.2 || JetPtRatio > 0.76 ) && abs(dxyBS) < 0.02 && abs(dzPV) < 0.1 && abs(SIP) < 4", "Medium", "pfCombRelMiniIsoEACorr", "JetPtRel", "JetPtRatio", "dxyBS", "dzPV", "SIP"),
        #Loose + MiniIso04 + TightIP2D
        #Loose_plus_MiniIso04_puls_TightIP2DVar= cms.vstring("Loose_plus_MiniIso04_puls_TightIP2DVar" ,"PF==1 && pfCombRelMiniIsoEACorr < 0.4 && abs(dxyBS) < 0.02 && abs(dzPV) < 0.1", "PF", "pfCombRelMiniIsoEACorr", "dxyBS", "dzPV"),
    ),

#_*_*_*_*_*
#Numerators
#_*_*_*_*_*

    Cuts = cms.PSet(
        #ID no IP   1, 2
        Loose_noIP = cms.vstring("Loose_noIP", "Loose_noIPVar", "0.5"), 
        Medium_noIP= cms.vstring("Medium_noIP", "Medium_noIPVar", "0.5"),
        #MiniIsolations  3, 4, 5, 6
        LooseMiniIso = cms.vstring("LooseMiniIso" ,"LooseMiniIsoVar", "0.5"),
        TightMiniIso = cms.vstring("TightMiniIso" ,"TightMiniIsoVar", "0.5"),
        #Multi Iso  7, 8, 9
        LooseMultiIso = cms.vstring("LoooseMultiIso" ,"LooseMultiIsoVar", "0.5"),
        MediumMultiIso= cms.vstring("MediumMultiIso" ,"MediumMultiIsoVar", "0.5"),
        VTMultiIso    = cms.vstring("VTMultiIso" ,"VTMultiIsoVar", "0.5"),
        #IP 10, 11, 12, 13
        MediumIP2D = cms.vstring("MediumIP2D","MediumIP2DVar", "0.5"),
        TightIP2D = cms.vstring("TightIP2D","TightIP2DVar", "0.5"),
        TightIP3D = cms.vstring("TightIP3D","TightIP3DVar", "0.5"),
        PtError   = cms.vstring("PtError", "pterrorVar", "0.5"),
        #Loose + Miniso02
        #Loose_plus_MiniIso02= cms.vstring("Loose_plus_MiniIso02" ,"Loose_plus_MiniIso02Var", "0.5"),
        #Loose + Miniso02 + TightIP2D
        #Loose_plus_MiniIso02_puls_TightIP2D= cms.vstring("Loose_plus_MiniIso02_puls_TightIP2D", "Loose_plus_MiniIso02_puls_TightIP2DVar" , "0.5"),
        #Medium + Miniso02
        #Medium_plus_MiniIso02= cms.vstring("Medium_plus_MiniIso02", "Medium_plus_MiniIso02Var", "0.5" ),
        #Loose + Miniso02 + TightIP3D
        #Loose_plus_MiniIso02_puls_TightIP3D= cms.vstring("Loose_plus_MiniIso02_puls_TightIP3D", "Loose_plus_MiniIso02_puls_TightIP3DVar", "0.5" ),
        #Medium + Miniso02 + TightIP3D
        #Medium_plus_MiniIso02_puls_TightIP3D= cms.vstring("Medium_plus_MiniIso02_puls_TightIP3D", "Medium_plus_MiniIso02_puls_TightIP3DVar", "0.5" ),
        #Medium + Miniso02 + TightIP2D
        #Medium_plus_MiniIso02_puls_TightIP2D= cms.vstring("Medium_plus_MiniIso02_puls_TightIP2D", "Medium_plus_MiniIso02_puls_TightIP2DVar", "0.5" ),
        #Medium + MultiIsoMedium + TightIP2D + TightIP3D
        #Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D= cms.vstring("Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D", "Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3DVar", "0.5" ),
        #Loose + MiniIso04 + TightIP2D
        #Loose_plus_MiniIso04_puls_TightIP2D= cms.vstring("Loose_plus_MiniIso04_puls_TightIP2D", "Loose_plus_MiniIso04_puls_TightIP2DVar", "0.5" ),
    ),

#_*_*_*_*_*_*_*_*_*_*_*_*_*
#Functions used for the fit
#_*_*_*_*_*_*_*_*_*_*_*_*_*
                          
    PDFs = cms.PSet(
        voigtPlusExpo = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpo = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpoMin70 = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])",
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusCheb = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])",
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "RooChebychev::backgroundPass(mass, {a0[0.25,0,0.5], a1[-0.25,-1,0.1],a2[0.,-0.25,0.25]})",
            "RooChebychev::backgroundFail(mass, {a0[0.25,0,0.5], a1[-0.25,-1,0.1],a2[0.,-0.25,0.25]})",
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
            )

    ),

    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),
    saveDistributionsPlot = cms.bool(False),

    Efficiencies = cms.PSet(), # will be filled later
)

#_*_*_*_*_*_*_*_*_*_*_*_*
#Denominators and binning
#_*_*_*_*_*_*_*_*_*_*_*_*

#For ID

ETA_BINS_INCLUSIVE_PT = cms.PSet(
    pt  = cms.vdouble(10, 500),
    eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
VTX_BINS_INCLUSIVE_ETA_PT  = cms.PSet(
    pt     = cms.vdouble(10 , 500),
    abseta = cms.vdouble(0.0, 2.4),
    tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
PT_BINS_INCLUSIVE_ETA = cms.PSet(
    pt     = cms.vdouble(10, 20, 25, 30, 40, 50, 60, 80, 120, 200),
    abseta = cms.vdouble(  0.0, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
PT_ETA_MAP = cms.PSet(
    pt     = cms.vdouble(10, 20, 25, 30, 40, 50, 60, 120),
    abseta = cms.vdouble( 0.0, 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)

ACTIVITY_ETA_MAP_INCLUSIVE_PT = cms.PSet(
    pfCombRelActivitydBCorr = cms.vdouble(0, 0.02, 0.05, 0.15, 1, 9999),
    pt     = cms.vdouble(10, 500),
    abseta = cms.vdouble( 0, 1.2, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)

ACTIVITY_PT_MAP_INCLUSIVE_ETA = cms.PSet(
    pfCombRelActivitydBCorr = cms.vdouble(0, 0.02, 0.05, 0.15, 1, 9999),
    pt     = cms.vdouble(10, 40, 80, 200),
    abseta = cms.vdouble( 0, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)

#For IP,ISO on ID
LOOSE_ETA_BINS_INCLUSIVE_PT = cms.PSet(
    pt  = cms.vdouble(10, 500),
    eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
LOOSE_VTX_BINS_INCLUSIVE_ETA_PT  = cms.PSet(
    pt     = cms.vdouble(10, 500 ),
    abseta = cms.vdouble(  0.0, 2.4),
    tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
LOOSE_PT_BINS_INCLUSIVE_ETA = cms.PSet(
    pt     = cms.vdouble(10, 20, 25, 30, 40, 50, 60, 80, 120, 200),
    abseta = cms.vdouble(  0.0, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
LOOSE_PT_ETA_MAP = cms.PSet(
    pt     = cms.vdouble(10, 20, 25, 30, 40, 50, 60, 120),
    abseta = cms.vdouble( 0.0, 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
LOOSE_ACTIVITY_ETA_MAP_INCLUSIVE_PT = cms.PSet(
    pfCombRelActivitydBCorr = cms.vdouble(0, 0.02, 0.05, 0.15, 1, 9999),
    pt     = cms.vdouble(10, 500),
    abseta = cms.vdouble( 0, 1.2, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)

LOOSE_ACTIVITY_PT_MAP_INCLUSIVE_ETA = cms.PSet(
    pfCombRelActivitydBCorr = cms.vdouble(0, 0.02, 0.05, 0.15, 1, 9999),
    pt     = cms.vdouble(10, 40, 80, 200),
    abseta = cms.vdouble( 0, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)

MEDIUMEDIUM_ETA_BINS_INCLUSIVE_PT = cms.PSet(
    pt  = cms.vdouble(10, 500),
    eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium2016 = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
MEDIUM_VTX_BINS_INCLUSIVE_ETA_PT  = cms.PSet(
    pt     = cms.vdouble(10, 500),
    abseta = cms.vdouble(0.0, 2.4),
    tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium2016 = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
MEDIUM_PT_BINS_INCLUSIVE_ETA = cms.PSet(
    pt     = cms.vdouble(10, 20, 25, 30, 40, 50, 60, 80, 120, 200),
    abseta = cms.vdouble(  0.0, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium2016 = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
MEDIUM_PT_ETA_MAP = cms.PSet(
    pt     = cms.vdouble(10, 20, 25, 30, 40, 50, 60, 120),
    abseta = cms.vdouble( 0.0, 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium2016 = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
MEDIUM_ACTIVITY_ETA_MAP_INCLUSIVE_PT = cms.PSet(
    pfCombRelActivitydBCorr = cms.vdouble(0, 0.02, 0.05, 0.15, 1, 9999),
    pt     = cms.vdouble(10, 500),
    abseta = cms.vdouble( 0, 1.2, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium2016 = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)

MEDIUM_ACTIVITY_PT_MAP_INCLUSIVE_ETA= cms.PSet(
    pfCombRelActivitydBCorr = cms.vdouble(0, 0.02, 0.05, 0.15, 1, 9999),
    pt     = cms.vdouble(10, 40, 80, 200),
    abseta = cms.vdouble( 0, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium2016 = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(21, 500),
    tag_IsoMu20 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)


#_*_*_*_
#Samples
#_*_*_*_

#PREFIX="/afs/cern.ch/user/j/jrgonzal/eos/cms/store/group/phys_muon/TagAndProbe/Run2016/"
PREFIX = "root://eoscms//eos/cms/store/group/phys_muon/TagAndProbe/Run2016/"

#sampleId = '1'
if 'data_all' in scenario:
                #if scenario[-1] in ['1', '2', '3', '4', '5', '6', '7']: sampleId = scenario[-1]
                #TheSample =  PREFIX+'80X_v1/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run274241to274421.root' # 1.3 /fb
                #if   sampleId == '1': pass
                #elif sampleId == '2': TheSample = PREFIX+'80X_v2/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run274444to275125.root' # 1.4 /fb 
                #elif sampleId == '3': TheSample = PREFIX+'80X_v2/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run274422to274443.root' # 0.5 /fb
                #elif sampleId == '4': TheSample = PREFIX+'80X_v1/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run273731_to_274240_IncludingMissingLumi_Completed.root'# 218.8 /pb 
                #elif sampleId == '5': TheSample = PREFIX+'80X_v1/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run271036to273730_NotCompleted.root' #585.4 /pb 
                #elif sampleId == '6': TheSample = PREFIX+'80X_v3/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run271036to275125_incomplete.root'
                #elif sampleId == '7': TheSample = 'InducingError'
                print "The file is: /afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_Data.root"
                process.TnP_MuonID = Template.clone(
                InputFileNames = cms.vstring(
                  #PREFIX+'80X_v2/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run274422to274443.root',
                  #PREFIX+'80X_v1/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run274241to274421.root',
                  #PREFIX+'80X_v2/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run274422to274443.root',
                  #PREFIX+'80X_v1/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run273731_to_274240_IncludingMissingLumi_Completed.root',
                  #PREFIX+'80X_v1/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run271036to273730_NotCompleted.root',
                  '/afs/cern.ch/work/j/jrgonzal/TnPTrees/ayer/tnpZLast_Data.root',
                    ),
                InputTreeName = cms.string("fitter_tree"),
                InputDirectoryName = cms.string("tpTree"),
                OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
                Efficiencies = cms.PSet(),
                )
elif 'mc_all' in scenario:
                #if scenario[-1] in ['1', '2', '3', '4', '5', '6', '7']: sampleId = scenario[-1]
                #print "The file is: ", PREFIX + '/80X_v1/DY_madgraphMLM/TnPTree_80X_DYLL_M50_MadGraphMLM_part' + sampleId + '.root'
                process.TnP_MuonID = Template.clone(
                InputFileNames = cms.vstring(
                  #'/afs/cern.ch/work/j/jrgonzal/TnPTrees/trees/DY/tnpZ_withNVtxWeights' + sampleId + '.root',
                  '/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_DY_1.root',
                  #'/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_DY_2.root',
                  #'/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_DY_3.root',
                  #'/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_DY_4.root',
                  #'/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_DY_5.root',
                  #PREFIX + '/80X_v1/DY_madgraphMLM/TnPTree_80X_DYLL_M50_MadGraphMLM_part' + sampleId + '.root',
                  #PREFIX + '/80X_v1/DY_madgraphMLM/TnPTree_80X_DYLL_M50_MadGraphMLM_part1.root',
                  #'/afs/cern.ch/work/j/jrgonzal/TnPTrees/trees/DY.root',
                #"/afs/cern.ch/work/j/jrgonzal/TnPTrees/TnPTree_80X_DYLL_M50_MadGraphMLM.root"
                    ),
                InputTreeName = cms.string("fitter_tree"),
                InputDirectoryName = cms.string("tpTree"),
                OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
                Efficiencies = cms.PSet(),
                )
                process.TnP_MuonID.WeightVariable = cms.string("weight")
                process.TnP_MuonID.Variables.weight = cms.vstring("weight","-10","10","")

#_*_*_*_*_*_*_*_*_*_*_*_*_*_*
#Choose Numerator/Denominator
#_*_*_*_*_*_*_*_*_*_*_*_*_*_*

ID_BINS = []

#_*_
#IDs
#_*_
#Loose ID
if id_bins == '1':
    ID_BINS = [
    (("Loose_noIP"), ("NUM_LooseID_DENOM_generalTracks_VAR_eta",            ETA_BINS_INCLUSIVE_PT           )),
    (("Loose_noIP"), ("NUM_LooseID_DENOM_generalTracks_VAR_vtx",            VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("Loose_noIP"), ("NUM_LooseID_DENOM_generalTracks_VAR_pt",             PT_BINS_INCLUSIVE_ETA           )),
    (("Loose_noIP"), ("NUM_LooseID_DENOM_generalTracks_VAR_map_pt_eta",         PT_ETA_MAP                      )),
    ]
#Medium ID
if id_bins == '2':
    ID_BINS = [
    (("Medium_noIP"), ("NUM_MediumID_DENOM_generalTracks_VAR_eta",          ETA_BINS_INCLUSIVE_PT           )),
    (("Medium_noIP"), ("NUM_MediumID_DENOM_generalTracks_VAR_vtx",          VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("Medium_noIP"), ("NUM_MediumID_DENOM_generalTracks_VAR_pt",           PT_BINS_INCLUSIVE_ETA           )),
    (("Medium_noIP"), ("NUM_MediumID_DENOM_generalTracks_VAR_map_pt_eta",       PT_ETA_MAP                      )),
    (("Medium_noIP"), ("NUM_MediumID_DENOM_generalTracks_VAR_map_activity_eta",   ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
    (("Medium_noIP"), ("NUM_MediumID_DENOM_generalTracks_VAR_map_activity_pt",    ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
    ]
#Tight MiniIso
if id_bins == '3':
    ID_BINS = [
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_MediumID_VAR_eta",                  MEDIUM_ETA_BINS_INCLUSIVE_PT           )),
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_MediumID_VAR_vtx",                  MEDIUM_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_MediumID_VAR_pt",                   MEDIUM_PT_BINS_INCLUSIVE_ETA           )),
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_MediumID_VAR_map_pt_eta",               MEDIUM_PT_ETA_MAP                      )),
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_MediumID_VAR_map_activity_eta",         MEDIUM_ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_MediumID_VAR_map_activity_pt",          MEDIUM_ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
    ]
if id_bins == '4':
    ID_BINS = [
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_LooseID_VAR_eta",                   LOOSE_ETA_BINS_INCLUSIVE_PT           )), 
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_LooseID_VAR_vtx",                   LOOSE_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_LooseID_VAR_pt",                    LOOSE_PT_BINS_INCLUSIVE_ETA           )),
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_LooseID_VAR_map_pt_eta",                LOOSE_PT_ETA_MAP                      )),
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_LooseID_VAR_map_activity_eta",          LOOSE_ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
    (("TightMiniIso"), ("NUM_MiniIsoTight_DENOM_LooseID_VAR_map_activity_pt",           LOOSE_ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
    ]
#Loose MiniIso
if id_bins == '5':
    ID_BINS = [
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_MediumID_VAR_eta",                   MEDIUM_ETA_BINS_INCLUSIVE_PT           )),
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_MediumID_VAR_vtx",                   MEDIUM_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_MediumID_VAR_pt",                    MEDIUM_PT_BINS_INCLUSIVE_ETA           )),
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_MediumID_VAR_map_pt_eta",            MEDIUM_PT_ETA_MAP                      )),
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_MediumID_VAR_map_activity_eta",      MEDIUM_ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
    ]
if id_bins == '6':
    ID_BINS = [
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_LooseID_VAR_eta",                   LOOSE_ETA_BINS_INCLUSIVE_PT           )),
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_LooseID_VAR_vtx",                   LOOSE_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_LooseID_VAR_pt",                    LOOSE_PT_BINS_INCLUSIVE_ETA           )),
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_LooseID_VAR_map_pt_eta",                LOOSE_PT_ETA_MAP                      )),
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_LooseID_VAR_map_activity_eta",          LOOSE_ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
    (("LooseMiniIso"), ("NUM_MiniIsoLoose_DENOM_LooseID_VAR_map_activity_pt",           LOOSE_ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
    ]
#MultiIso
if id_bins == '7':
    ID_BINS = [
    (("LooseMultiIso"), ("NUM_MultiIsoLoose_DENOM_MediumID_VAR_eta",              MEDIUM_ETA_BINS_INCLUSIVE_PT           )), 
    (("LooseMultiIso"), ("NUM_MultiIsoLoose_DENOM_MediumID_VAR_vtx",              MEDIUM_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("LooseMultiIso"), ("NUM_MultiIsoLoose_DENOM_MediumID_VAR_pt",               MEDIUM_PT_BINS_INCLUSIVE_ETA           )),
    (("LooseMultiIso"), ("NUM_MultiIsoLoose_DENOM_MediumID_VAR_map_pt_eta",           MEDIUM_PT_ETA_MAP                      )),
    (("LooseMultiIso"), ("NUM_MultiIsoLoose_DENOM_MediumID_VAR_map_activity_eta",     MEDIUM_ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
    (("LooseMultiIso"), ("NUM_MultiIsoLoose_DENOM_MediumID_VAR_map_activity_pt",      MEDIUM_ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
    ]
if id_bins == '8':
    ID_BINS = [
    (("MediumMultiIso"), ("NUM_MultiIsoMedium_DENOM_MediumID_VAR_eta",              MEDIUM_ETA_BINS_INCLUSIVE_PT           )), 
    (("MediumMultiIso"), ("NUM_MultiIsoMedium_DENOM_MediumID_VAR_vtx",              MEDIUM_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("MediumMultiIso"), ("NUM_MultiIsoMedium_DENOM_MediumID_VAR_pt",               MEDIUM_PT_BINS_INCLUSIVE_ETA           )),
    (("MediumMultiIso"), ("NUM_MultiIsoMedium_DENOM_MediumID_VAR_map_pt_eta",           MEDIUM_PT_ETA_MAP                      )),
    (("MediumMultiIso"), ("NUM_MultiIsoMedium_DENOM_MediumID_VAR_map_activity_eta",     MEDIUM_ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
    (("MediumMultiIso"), ("NUM_MultiIsoMedium_DENOM_MediumID_VAR_map_activity_pt",      MEDIUM_ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
    ]
if id_bins == '9':
    ID_BINS = [
    (("VTMultiIso"), ("NUM_MultiIsoVT_DENOM_MediumID_VAR_eta",              MEDIUM_ETA_BINS_INCLUSIVE_PT           )), 
    (("VTMultiIso"), ("NUM_MultiIsoVT_DENOM_MediumID_VAR_vtx",              MEDIUM_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("VTMultiIso"), ("NUM_MultiIsoVT_DENOM_MediumID_VAR_pt",               MEDIUM_PT_BINS_INCLUSIVE_ETA           )),
    (("VTMultiIso"), ("NUM_MultiIsoVT_DENOM_MediumID_VAR_map_pt_eta",           MEDIUM_PT_ETA_MAP                      )),
    (("VTMultiIso"), ("NUM_MultiIsoVT_DENOM_MediumID_VAR_map_activity_eta",     MEDIUM_ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
    (("VTMultiIso"), ("NUM_MultiIsoVT_DENOM_MediumID_VAR_map_activity_pt",      MEDIUM_ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
    ]
# IPs
if id_bins == '10':
    ID_BINS = [
    (("MediumIP2D"), ("NUM_MediumIP2D_DENOM_LooseID_VAR_eta",                 LOOSE_ETA_BINS_INCLUSIVE_PT           )),
    (("MediumIP2D"), ("NUM_MediumIP2D_DENOM_LooseID_VAR_vtx",                 LOOSE_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("MediumIP2D"), ("NUM_MediumIP2D_DENOM_LooseID_VAR_pt",                  LOOSE_PT_BINS_INCLUSIVE_ETA           )),
    (("MediumIP2D"), ("NUM_MediumIP2D_DENOM_LooseID_VAR_map_pt_eta",              LOOSE_PT_ETA_MAP                      )),
    ]                                                                                                                
if id_bins == '11':                                                                                                   
    ID_BINS = [                                                                                                      
    (("TightIP2D"), ("NUM_TightIP2D_DENOM_MediumID_VAR_eta",                MEDIUM_ETA_BINS_INCLUSIVE_PT           )), 
    (("TightIP2D"), ("NUM_TightIP2D_DENOM_MediumID_VAR_vtx",                MEDIUM_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("TightIP2D"), ("NUM_TightIP2D_DENOM_MediumID_VAR_pt",                 MEDIUM_PT_BINS_INCLUSIVE_ETA           )),
    (("TightIP2D"), ("NUM_TightIP2D_DENOM_MediumID_VAR_map_pt_eta",             MEDIUM_PT_ETA_MAP                      )),
    ]
if id_bins == '12':
    ID_BINS = [
    (("TightIP3D"), ("NUM_TightIP3D_DENOM_MediumID_VAR_eta",                 MEDIUM_ETA_BINS_INCLUSIVE_PT           )),
    (("TightIP3D"), ("NUM_TightIP3D_DENOM_MediumID_VAR_vtx",                 MEDIUM_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("TightIP3D"), ("NUM_TightIP3D_DENOM_MediumID_VAR_pt",                  MEDIUM_PT_BINS_INCLUSIVE_ETA           )),
    (("TightIP3D"), ("NUM_TightIP3D_DENOM_MediumID_VAR_map_pt_eta",              MEDIUM_PT_ETA_MAP                      )),
    ]
if id_bins == '13':
    ID_BINS = [
    (("PtError"), ("NUM_PtError_DENOM_MediumID_VAR_eta",                 MEDIUM_ETA_BINS_INCLUSIVE_PT           )),
    (("PtError"), ("NUM_PtError_DENOM_MediumID_VAR_vtx",                 MEDIUM_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("PtError"), ("NUM_PtError_DENOM_MediumID_VAR_pt",                  MEDIUM_PT_BINS_INCLUSIVE_ETA           )),
    (("PtError"), ("NUM_PtError_DENOM_MediumID_VAR_map_pt_eta",              MEDIUM_PT_ETA_MAP                      )),
    ]

#Loose+MiniIso02
# if id_bins == '11':
#     ID_BINS = [
#     (("Loose_plus_MiniIso02"), ("NUM_LooseID_plus_MiniIso02_DENOM_generalTracks_VAR_eta",                                           ETA_BINS_INCLUSIVE_PT           )),
#     (("Loose_plus_MiniIso02"), ("NUM_LooseID_plus_MiniIso02_DENOM_generalTracks_VAR_vtx",                                           VTX_BINS_INCLUSIVE_ETA_PT       )),
#     (("Loose_plus_MiniIso02"), ("NUM_LooseID_plus_MiniIso02_DENOM_generalTracks_VAR_pt",                                            PT_BINS_INCLUSIVE_ETA           )),
#     (("Loose_plus_MiniIso02"), ("NUM_LooseID_plus_MiniIso02_DENOM_generalTracks_VAR_map_pt_eta",                                        PT_ETA_MAP                      )),
#     (("Loose_plus_MiniIso02"), ("NUM_LooseID_plus_MiniIso02_DENOM_generalTracks_VAR_map_activity_eta",                                  ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
#     (("Loose_plus_MiniIso02"), ("NUM_LooseID_plus_MiniIso02_DENOM_generalTracks_VAR_map_activity_pt",                                   ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
#     ]
# #Loose+MiniIso02+TightIP2D
# if id_bins == '12':
#     ID_BINS = [
#     (("Loose_plus_MiniIso02_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_eta",             ETA_BINS_INCLUSIVE_PT           )),
#     (("Loose_plus_MiniIso02_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_vtx",             VTX_BINS_INCLUSIVE_ETA_PT       )),
#     (("Loose_plus_MiniIso02_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_pt",              PT_BINS_INCLUSIVE_ETA           )),
#     (("Loose_plus_MiniIso02_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_map_pt_eta",          PT_ETA_MAP                      )),
#     (("Loose_plus_MiniIso02_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_map_activity_eta",    ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
#     (("Loose_plus_MiniIso02_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_map_activity_pt",     ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
#     ]
# #Medium+MiniIso02
# if id_bins == '13':
#     ID_BINS = [
#     (("Medium_plus_MiniIso02"), ("NUM_MediumID_plus_MiniIso02_DENOM_generalTracks_VAR_eta",                                         ETA_BINS_INCLUSIVE_PT           )),
#     (("Medium_plus_MiniIso02"), ("NUM_MediumID_plus_MiniIso02_DENOM_generalTracks_VAR_vtx",                                         VTX_BINS_INCLUSIVE_ETA_PT       )),
#     (("Medium_plus_MiniIso02"), ("NUM_MediumID_plus_MiniIso02_DENOM_generalTracks_VAR_pt",                                          PT_BINS_INCLUSIVE_ETA           )),
#     (("Medium_plus_MiniIso02"), ("NUM_MediumID_plus_MiniIso02_DENOM_generalTracks_VAR_map_pt_eta",                                      PT_ETA_MAP                      )),
#     (("Medium_plus_MiniIso02"), ("NUM_MediumID_plus_MiniIso02_DENOM_generalTracks_VAR_map_activity_eta",                                ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
#     (("Medium_plus_MiniIso02"), ("NUM_MediumID_plus_MiniIso02_DENOM_generalTracks_VAR_map_activity_pt",                                 ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
#     ]
# #Loose+MiniIso02+TightIP3D
# if id_bins == '14':
#     ID_BINS = [
#     (("Loose_plus_MiniIso02_puls_TightIP3D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_eta",             ETA_BINS_INCLUSIVE_PT           )),
#     (("Loose_plus_MiniIso02_puls_TightIP3D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_vtx",             VTX_BINS_INCLUSIVE_ETA_PT       )),
#     (("Loose_plus_MiniIso02_puls_TightIP3D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_pt",              PT_BINS_INCLUSIVE_ETA           )),
#     (("Loose_plus_MiniIso02_puls_TightIP3D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_map_pt_eta",          PT_ETA_MAP                      )),
#     (("Loose_plus_MiniIso02_puls_TightIP3D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_map_activity_eta",    ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
#     (("Loose_plus_MiniIso02_puls_TightIP3D"), ("NUM_LooseID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_map_activity_pt",     ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
#     ]
# #Medium+MiniIso02+TightIP3D
# if id_bins == '15':
#     ID_BINS = [
#     (("Medium_plus_MiniIso02_puls_TightIP3D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_eta",           ETA_BINS_INCLUSIVE_PT           )),
#     (("Medium_plus_MiniIso02_puls_TightIP3D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_vtx",           VTX_BINS_INCLUSIVE_ETA_PT       )),
#     (("Medium_plus_MiniIso02_puls_TightIP3D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_pt",            PT_BINS_INCLUSIVE_ETA           )),
#     (("Medium_plus_MiniIso02_puls_TightIP3D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_map_pt_eta",        PT_ETA_MAP                      )),
#     (("Medium_plus_MiniIso02_puls_TightIP3D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_map_activity_eta",  ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
#     (("Medium_plus_MiniIso02_puls_TightIP3D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP3D_DENOM_generalTracks_VAR_map_activity_pt",   ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
#     ]
# #Medium+MiniIso02+TightIP2D
# if id_bins == '16':
#     ID_BINS = [
#     (("Medium_plus_MiniIso02_puls_TightIP2D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_eta",           ETA_BINS_INCLUSIVE_PT           )),
#     (("Medium_plus_MiniIso02_puls_TightIP2D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_vtx",           VTX_BINS_INCLUSIVE_ETA_PT       )),
#     (("Medium_plus_MiniIso02_puls_TightIP2D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_pt",            PT_BINS_INCLUSIVE_ETA           )),
#     (("Medium_plus_MiniIso02_puls_TightIP2D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_map_pt_eta",        PT_ETA_MAP                      )),
#     (("Medium_plus_MiniIso02_puls_TightIP2D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_map_activity_eta",  ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
#     (("Medium_plus_MiniIso02_puls_TightIP2D"), ("NUM_MediumID_plus_MiniIso02_puls_TightIP2D_DENOM_generalTracks_VAR_map_activity_pt",   ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
#     ]
# #Medium+MultiIsoMedium+TightIP2D+TightIP3D
# if id_bins == '17':
#     ID_BINS = [
#     (("Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D"), ("NUM_MediumID_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D_DENOM_generalTracks_VAR_eta",           ETA_BINS_INCLUSIVE_PT           )),
#     (("Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D"), ("NUM_MediumID_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D_DENOM_generalTracks_VAR_vtx",           VTX_BINS_INCLUSIVE_ETA_PT       )),
#     (("Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D"), ("NUM_MediumID_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D_DENOM_generalTracks_VAR_pt",            PT_BINS_INCLUSIVE_ETA           )),
#     (("Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D"), ("NUM_MediumID_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D_DENOM_generalTracks_VAR_map_pt_eta",        PT_ETA_MAP                      )),
#     (("Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D"), ("NUM_MediumID_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D_DENOM_generalTracks_VAR_map_activity_eta",  ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
#     (("Medium_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D"), ("NUM_MediumID_plus_MediumMultiIso_plus_TightIP2D_plus_TightIP3D_DENOM_generalTracks_VAR_map_activity_pt",   ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
#     ]
# 
# #Loose+MiniIso04+TightIP2D
# if id_bins == '18':
#     ID_BINS = [
#     (("Loose_plus_MiniIso04_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso04_puls_TightIP2D_DENOM_generalTracks_VAR_eta",             ETA_BINS_INCLUSIVE_PT           )),
#     (("Loose_plus_MiniIso04_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso04_puls_TightIP2D_DENOM_generalTracks_VAR_vtx",             VTX_BINS_INCLUSIVE_ETA_PT       )),
#     (("Loose_plus_MiniIso04_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso04_puls_TightIP2D_DENOM_generalTracks_VAR_pt",              PT_BINS_INCLUSIVE_ETA           )),
#     (("Loose_plus_MiniIso04_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso04_puls_TightIP2D_DENOM_generalTracks_VAR_map_pt_eta",          PT_ETA_MAP                      )),
#     (("Loose_plus_MiniIso04_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso04_puls_TightIP2D_DENOM_generalTracks_VAR_map_activity_eta",    ACTIVITY_ETA_MAP_INCLUSIVE_PT   )),
#     (("Loose_plus_MiniIso04_puls_TightIP2D"), ("NUM_LooseID_plus_MiniIso04_puls_TightIP2D_DENOM_generalTracks_VAR_map_activity_pt",     ACTIVITY_PT_MAP_INCLUSIVE_ETA   )),
#     ]

#_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
#Produce the efficiency .root files
#_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*


for ID, ALLBINS in ID_BINS:
    X = ALLBINS[0]
    B = ALLBINS[1]
    _output = os.getcwd() + '/Efficiency' 
    if not os.path.exists(_output):
        print 'Creating', _output, 'directory where the fits are stored'  
        os.makedirs(_output)
    if 'data_all' in scenario:
        _output += '/DATA'
    elif 'mc_all' in scenario:
        _output += '/MC'
    if not os.path.exists(_output):
        os.makedirs(_output)
    module = process.TnP_MuonID.clone(OutputFileName = cms.string(_output + "/TnP_MuonID_%s.root" % (X)))
    shape = cms.vstring("vpvPlusExpo")
    #shape = cms.vstring("vpvPlusCheb")

    if(("Iso" in ID) and (not "plus" in ID)):
        shape = cms.vstring("vpvPlusExpo")
    else:
    #if not "Iso" in ID:  #customize only for ID
        if ALLBINS[0].find('VAR_pt') != -1: 
                shape = cms.vstring("vpvPlusExpo","*pt_bin6*","vpvPlusCheb","*pt_bin7*","vpvPlusCheb","*pt_bin8*","vpvPlusCheb")
        if ALLBINS[0].find('VAR_map_pt_eta') != -1: 
                shape = cms.vstring("vpvPlusExpo","*pt_bin6*","vpvPlusCheb")
    
        #if (len(B.pt)>=8):  #customize only when the pT have the high pt bins
        #    if "Loose_noIP" in ID:
        #        shape = cms.vstring("vpvPlusExpo","*pt_bin5*","vpvPlusCheb","*pt_bin6*","vpvPlusCheb","*pt_bin7*","vpvPlusCheb","*pt_bin8*","vpvPlusCheb")
        #    else:
        #        shape = cms.vstring("vpvPlusExpo","*pt_bin6*","vpvPlusCheb","*pt_bin7*","vpvPlusCheb","*pt_bin8*","vpvPlusCheb")
    DEN = B.clone(); num = ID;
    #compute isolation efficiency 
    if 'data_all' in scenario:
        setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
        EfficiencyCategoryAndState = cms.vstring(num,"above"),
        UnbinnedVariables = cms.vstring("mass"),
        BinnedVariables = DEN,
        BinToPDFmap = shape
        ))
        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)        
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))
    elif 'mc_all' in scenario:
        setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
        EfficiencyCategoryAndState = cms.vstring(num,"above"),
        UnbinnedVariables = cms.vstring("mass","weight"),
        #UnbinnedVariables = cms.vstring("mass"),
        BinnedVariables = DEN,
        BinToPDFmap = shape
        ))
        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)        
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))
