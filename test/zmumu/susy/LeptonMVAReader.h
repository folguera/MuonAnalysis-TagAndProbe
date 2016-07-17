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

class LeptonMVAReader{
  public:
    LeptonMVAReader():fTMVAReader(0):fisInitialized(kFalse):fMethodName("BDTG") {};
    ~LeptonMVAReader(); 
  
    void     initialize(std::string weightsfile) { 
      
      fTMVAReader = new TMVA::Reader("!Color:!Silent:Error" );
      fTMVAReader->AddVariable("fMVAVar_pt",                &fMVAVar_pt               );
      fTMVAReader->AddVariable("fMVAVar_eta",               &fMVAVar_eta              );
      fTMVAReader->AddVariable("fMVAVar_JetNDauCharged",    &fMVAVar_JetNDauCharged   );
      fTMVAReader->AddVariable("fMVAVar_miniRelIsoCharged", &fMVAVar_miniRelIsoCharged);
      fTMVAReader->AddVariable("fMVAVar_miniRelIsoNeutral", &fMVAVar_miniRelIsoNeutral);
      fTMVAReader->AddVariable("fMVAVar_JetPtRel",          &fMVAVar_JetPtRel         );
      fTMVAReader->AddVariable("fMVAVar_JetPtRatio",        &fMVAVar_JetPtRatio       );
      fTMVAReader->AddVariable("fMVAVar_JetBTagCSV",        &fMVAVar_JetBTagCSV       );
      fTMVAReader->AddVariable("fMVAVar_SIP",               &fMVAVar_SIP              );
      fTMVAReader->AddVariable("fMVAVar_dxyBS",             &fMVAVar_dxyBS            ); 
      fTMVAReader->AddVariable("fMVAVar_dzPV",              &fMVAVar_dzPV             );
      
      fTMVAReader->BookMVA(fMethodName,weightsfile);
      std::cout << "MVA Loaded with weiths: " << weightsfile << std::endl;
      fisInitialized = kTRUE
    };
    
    Bool_t   isInitialized() const { return fisInitialized; };
            
    Float_t getMVAValue(Float_t pt,
			Float_t eta,
			Int_t JetNDauCharged,
			Float_t miniRelIsoCharged,
			Float_t miniRelIsoNeutral,
			Float_t JetPtRel,
			Float_t JetPtRatio,
			Float_t JetBTagCSV,
			Float_t SIP,
			Float_t dxyBS,
			Float_t dzPV) {
      if (!fisInitialized) { 
	std::cout << "Error: MuonMVAEstimator not properly initialized.\n"; 
	return -9999;
      }
       fMVAVar_pt =                 pt               ;
       fMVAVar_eta =                eta              ;
       fMVAVar_JetNDauCharged =     JetNDauCharged   ;
       fMVAVar_miniRelIsoCharged =  miniRelIsoCharged;
       fMVAVar_miniRelIsoNeutral =  miniRelIsoNeutral;
       fMVAVar_JetPtRel =           JetPtRel         ;
       fMVAVar_JetPtRatio =         JetPtRatio       ;
       fMVAVar_JetBTagCSV =         JetBTagCSV       ;
       fMVAVar_SIP =                SIP              ;
       fMVAVar_dxyBS =              dxyBS            ; 
       fMVAVar_dzPV =               dzPV             ;
       
       return fTMVAReader->EvaluateMVA(fMethodName);

    };

  private:
    TMVA::Reader* fTMVAReader;
    std::string                fMethodname;
    Bool_t                     fisInitialized;
    Bool_t                     fPrintMVADebug;

    /// MVA VAriables:
    Float_t fMVAVar_pt;
    Float_t fMVAVar_eta;
    Int_t   fMVAVar_JetNDauCharged;
    Float_t fMVAVar_miniRelIsoCharged;
    Float_t fMVAVar_miniRelIsoNeutral;
    Float_t fMVAVar_JetPtRel;
    Float_t fMVAVar_JetPtRatio;
    Float_t fMVAVar_JetBTagCSV;
    Float_t fMVAVar_SIP;
    Float_t fMVAVar_dxyBS; 
    Float_t fMVAVar_dzPV;            
    
};

#endif
