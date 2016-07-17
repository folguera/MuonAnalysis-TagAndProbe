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
        mass = cms.vstring("Tag-muon Mass", _mrange, "130", "GeV/c^{2}"),
        pt = cms.vstring("muon p_{T}", "0", "1000", "GeV/c"),
        eta    = cms.vstring("muon #eta", "-2.5", "2.5", ""),
        abseta = cms.vstring("muon |#eta|", "0", "2.5", ""),
        #charge = cms.vstring("muon charge", "-2.5", "2.5", ""),
        glbPtError = cms.vstring("p_{T} error", "0", "20", "GeV/c"),
        #combRelIsoPF04dBeta = cms.vstring("dBeta rel iso dR 0.4", "-2", "9999999", ""),
        #pfCombRelActivitydBCorr = cms.vstring("Rel. Activity", "-2", "9999999", ""),
#        pfCombRelMiniIsoEACorr = cms.vstring("Mini Iso", "-2", "9999999",""),
        #miniIsoCharged  = cms.vstring("Mini Iso Charged", "-2", "9999999",""),
        #miniIsoPhotons  = cms.vstring("Mini Iso Photons", "-2", "9999999",""),
        #miniIsoNeutrals = cms.vstring("Mini Iso Neutrals", "-2", "9999999",""),
        #JetPtRel = cms.vstring("JetPtRel", "-2", "20",""),
        #JetPtRatio = cms.vstring("JetPtRatio", "-2", "2000",""),
        tag_pt = cms.vstring("Tag p_{T}", "0", "500", "GeV/c"),
        tag_nVertices   = cms.vstring("Number of vertices", "0", "999", ""),
        tag_abseta = cms.vstring("|eta| of tag muon", "0", "2.5", ""),
        tag_combRelIsoPF04dBeta = cms.vstring("Tag dBeta rel iso dR 0.4", "-2", "999", ""),
        #dzPV = cms.vstring("dzPV", "-100", "100", ""),
        #dxyBS = cms.vstring("dxyBS", "-100", "100", ""),
        #SIP = cms.vstring("SIP", "-100", "100", ""),
        pair_probeMultiplicity = cms.vstring("pair_probeMultiplicity", "0","30",""),
        ),

    Categories = cms.PSet(
        PF    = cms.vstring("PF Muon", "dummy[pass=1,fail=0]"),
        #Medium   = cms.vstring("Medium Id. Muon", "dummy[pass=1,fail=0]"),
        Medium2016   = cms.vstring("Medium2016 Id. Muon", "dummy[pass=1,fail=0]"),
        tag_IsoMu20 = cms.vstring("PF Muon", "dummy[pass=1,fail=0]"),
    ),

    Expressions = cms.PSet(
        #ID no IP  1, 2
        Loose_noIPVar = cms.vstring("Loose_noIPVar", "PF==1", "PF"),
        Medium_noIPVar= cms.vstring("Medium_noIPVar", "Medium2016==1", "Medium2016"),

#        VTMultiIsoVar    = cms.vstring("VTMultiIsoVar" ,    "pfCombRelMiniIsoEACorr < 0.09 && ( JetPtRel > 7.2 || JetPtRatio > 0.84 )", "JetPtRel", "JetPtRatio", "pfCombRelMiniIsoEACorr"),

        #IP   11, 12, 13
        #MediumIP2DVar  = cms.vstring("MediumIP2DVar", "abs(dxyBS) < 0.2 && abs(dzPV) < 0.5", "dxyBS", "dzPV"),
        #TightIP2DVar  = cms.vstring("TightIP2DVar", "abs(dxyBS) < 0.05 && abs(dzPV) < 0.1", "dxyBS", "dzPV"),
        #TightIP3DVar  = cms.vstring("TightIP3DVar", "abs(SIP) < 4", "SIP"),
        pterrorVar    = cms.vstring("pterrorVar", "glbPtError/pt < 0.2", "glbPtError", "pt"),
    ),

#_*_*_*_*_*
#Numerators
#_*_*_*_*_*

    Cuts = cms.PSet(
        #ID no IP   1, 2
        Loose_noIP = cms.vstring("Loose_noIP", "Loose_noIPVar", "0.5"), 
        Medium_noIP= cms.vstring("Medium_noIP", "Medium_noIPVar", "0.5"),
        #MiniIsolations  3, 4, 5, 6
        #LooseMiniIso = cms.vstring("LooseMiniIso" ,"LooseMiniIsoVar", "0.5"),
        #TightMiniIso = cms.vstring("TightMiniIso" ,"TightMiniIsoVar", "0.5"),
        #Multi Iso  7, 8, 9
        #LooseMultiIso = cms.vstring("LoooseMultiIso" ,"LooseMultiIsoVar", "0.5"),
        #MediumMultiIso= cms.vstring("MediumMultiIso" ,"MediumMultiIsoVar", "0.5"),
       # VTMultiIso    = cms.vstring("VTMultiIso" ,"VTMultiIsoVar", "0.5"),
        #IP 10, 11, 12, 13
        #MediumIP2D = cms.vstring("MediumIP2D","MediumIP2DVar", "0.5"),
        #TightIP2D = cms.vstring("TightIP2D","TightIP2DVar", "0.5"),
        #TightIP3D = cms.vstring("TightIP3D","TightIP3DVar", "0.5"),
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
MEDIUM_ETA_BINS_INCLUSIVE_PT = cms.PSet(
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



#_*_*_*_
#Samples
#_*_*_*_

PREFIX = "root://eoscms//eos/cms/store/group/phys_muon/TagAndProbe/Run2016/"

#sampleId = '1'
if 'data_all' in scenario:
                print "The file is: /afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_Data.root"
                process.TnP_MuonID = Template.clone(
                InputFileNames = cms.vstring(
                  '/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_Data.root',
                    ),
                InputTreeName = cms.string("fitter_tree"),
                InputDirectoryName = cms.string("tpTree"),
                OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
                Efficiencies = cms.PSet(),
                )
elif 'mc_all' in scenario:
                process.TnP_MuonID = Template.clone(
                InputFileNames = cms.vstring(
                  '/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_DY_1.root',
                  '/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_DY_2.root',
                  '/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_DY_3.root',
                  '/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_DY_4.root',
                  '/afs/cern.ch/work/j/jrgonzal/TnPTrees/tnpZLast_DY_5.root',
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
    ]
if id_bins == '13':
    ID_BINS = [
    (("PtError"), ("NUM_PtError_DENOM_MediumID_VAR_eta",                 MEDIUM_ETA_BINS_INCLUSIVE_PT           )),
    (("PtError"), ("NUM_PtError_DENOM_MediumID_VAR_vtx",                 MEDIUM_VTX_BINS_INCLUSIVE_ETA_PT       )),
    (("PtError"), ("NUM_PtError_DENOM_MediumID_VAR_pt",                  MEDIUM_PT_BINS_INCLUSIVE_ETA           )),
    (("PtError"), ("NUM_PtError_DENOM_MediumID_VAR_map_pt_eta",              MEDIUM_PT_ETA_MAP                      )),
    ]

#Loose MiniIso
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
