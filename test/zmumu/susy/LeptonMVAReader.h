//--------------------------------------------------------------------------------------------------
// $Id $
//
// LeptonMVAReader 
//
// Helper Class for reading LeptonMVA weights
//
// Authors: S.Folgueras
//--------------------------------------------------------------------------------------------------

//#define STANDALONE   // <---- this line

#ifndef LeptonMVAReader_H
#define LeptonMVAReader_H

#include <vector>
#include <TROOT.h>
#include "TMVA/Factory.h"
#include "TMVA/Tools.h"
#include "TMVA/Reader.h"

#ifndef STANDALONE
#endif

class LeptonMVAReader{
 public:
  LeptonMVAReader(){
    fTMVAReader = new TMVA::Reader("!Color:!Silent:Error" );
  };
  ~LeptonMVAReader(); 
  
  void initialize(std::string weightsfile) { 
    fTMVAReader->AddVariable("LepGood_pt",                &LepGood_pt               );
    fTMVAReader->AddVariable("LepGood_eta",               &LepGood_eta              );
    fTMVAReader->AddVariable("LepGood_jetNDauChargedMVASel",&LepGood_JetNDauCharged   );
    fTMVAReader->AddVariable("LepGood_miniRelIsoCharged", &LepGood_miniRelIsoCharged);
    fTMVAReader->AddVariable("LepGood_miniRelIsoNeutral", &LepGood_miniRelIsoNeutral);
    fTMVAReader->AddVariable("LepGood_jetPtRelv2",        &LepGood_JetPtRel         );
    fTMVAReader->AddVariable("min(LepGood_jetPtRatiov2,1.5)",      &LepGood_JetPtRatio       );
    fTMVAReader->AddVariable("max(LepGood_jetBTagCSV,0)",        &LepGood_JetBTagCSV       );
    fTMVAReader->AddVariable("LepGood_sip3d",               &LepGood_SIP              );
    fTMVAReader->AddVariable("log(abs(LepGood_dxy))",             &LepGood_dxyBS            ); 
    fTMVAReader->AddVariable("log(abs(LepGood_dz))",              &LepGood_dzPV             );
    fTMVAReader->AddVariable("LepGood_segmentCompatibility", &LepGood_segmentCompatibility);
    fTMVAReader->BookMVA("BDTG",weightsfile);
    std::cout << "MVA Loaded with weiths: " << weightsfile << std::endl;
    fisInitialized = true;
  };
  
  Bool_t   isInitialized() const { return fisInitialized; };
  
  Float_t getMVAValue(Float_t pt,
		      Float_t eta,
		      Float_t JetNDauCharged,
		      Float_t miniRelIsoCharged,
		      Float_t miniRelIsoNeutral,
		      Float_t JetPtRel,
		      Float_t JetPtRatio,
		      Float_t JetBTagCSV,
		      Float_t SIP,
		      Float_t dxyBS,
		      Float_t dzPV,
		      Float_t segmentCompatibility) {
    if (!fisInitialized) { 
      std::cout << "Error: MuonMVAEstimator not properly initialized.\n"; 
      return -9999;
    }
    LepGood_pt =                   pt               ;
    LepGood_eta =                  eta              ;
    LepGood_JetNDauCharged =       JetNDauCharged   ;
    LepGood_miniRelIsoCharged =    miniRelIsoCharged;
    LepGood_miniRelIsoNeutral =    miniRelIsoNeutral;
    LepGood_JetPtRel =             JetPtRel         ;
    LepGood_JetPtRatio =           min(JetPtRatio,(float)1.5);
    LepGood_JetBTagCSV =           max(JetBTagCSV,(float)0);
    LepGood_SIP =                  SIP              ;
    LepGood_dxyBS =                log(abs(dxyBS))  ; 
    LepGood_dzPV =                 log(abs(dzPV))   ;
    LepGood_segmentCompatibility = segmentCompatibility;
    return fTMVAReader->EvaluateMVA("BDTG");
    
  };
  
 private:
  TMVA::Reader* fTMVAReader;
  Bool_t                     fisInitialized;
  Bool_t                     fPrintMVADebug;
  
  /// MVA VAriables:
  Float_t LepGood_pt;
  Float_t LepGood_eta;
  Float_t LepGood_JetNDauCharged;
  Float_t LepGood_miniRelIsoCharged;
  Float_t LepGood_miniRelIsoNeutral;
  Float_t LepGood_JetPtRel;
  Float_t LepGood_JetPtRatio;
  Float_t LepGood_JetBTagCSV;
  Float_t LepGood_SIP;
  Float_t LepGood_dxyBS; 
  Float_t LepGood_dzPV;            
  Float_t LepGood_segmentCompatibility;
};

#endif
