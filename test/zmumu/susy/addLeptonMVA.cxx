#include "TTree.h"
#include "TFile.h"
#include "TSystem.h"
#include "TStopwatch.h"
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#define STANDALONE
#include "LeptonMVAReader.h"

void addLeptonMVA() {
    std::string weights = "forMoriond16_mu_sigTTZ_bkgTT_BDTG.weights.xml";
    
    std::cout<<"Initializing MVA" <<std::endl;
    LeptonMVAReader *lepMVA  = new LeptonMVAReader();
    lepMVA->initialize(weights);

    TTree *tIn  = (TTree *) ((TFile*)gROOT->GetListOfFiles()->At(0))->Get("tpTree/fitter_tree");
    Float_t pt, eta;
    Int_t JetNDauCharged;
    Float_t JetPtRel,JetPtRatio,JetBTagCSV;
    Float_t miniRelIsoCharged, miniRelIsoNeutral;
    Float_t SIP,dxyBS,dzPV,segmentCompatibility;
    tIn->SetBranchAddress("pt",  &pt);
    tIn->SetBranchAddress("eta", &eta);
    tIn->SetBranchAddress("JetNDauCharged",&JetNDauCharged);
    tIn->SetBranchAddress("miniRelIsoCharged",&miniRelIsoCharged);
    tIn->SetBranchAddress("miniRelIsoNeutral",&miniRelIsoNeutral);
    tIn->SetBranchAddress("JetPtRel",&JetPtRel);
    tIn->SetBranchAddress("JetPtRatio",&JetPtRatio);
    tIn->SetBranchAddress("JetBTagCSV",&JetBTagCSV);
    tIn->SetBranchAddress("SIP",&SIP);    
    tIn->SetBranchAddress("dxyBS",&dxyBS);
    tIn->SetBranchAddress("dzPV",&dzPV);
    tIn->SetBranchAddress("segmentCompatibility",&segmentCompatibility);

    TFile *fOut = new TFile("tnpZ_withLeptonMVA.root", "RECREATE");
    fOut->mkdir("tpTree")->cd();
    TTree *tOut = tIn->CloneTree(0);
    Float_t mvaSUSY;
    tOut->Branch("mvaSUSY", &mvaSUSY, "mvaSUSY/F");

    int step = tIn->GetEntries()/1000;
    double evDenom = 100.0/double(tIn->GetEntries());
    TStopwatch timer; timer.Start();
    for (int i = 0, n = tIn->GetEntries(); i < n; ++i) {
        tIn->GetEntry(i);

	mvaSUSY = lepMVA->getMVAValue(pt, eta, JetNDauCharged, 
				      miniRelIsoCharged, miniRelIsoNeutral,
				      JetPtRel, JetPtRatio,JetBTagCSV,SIP,dxyBS,dzPV,
				      segmentCompatibility);
        tOut->Fill();
        if ((i+1) % step == 0) { 
	  double totalTime = timer.RealTime()/60.; timer.Continue();
	  double fraction = double(i+1)/double(n+1), remaining = totalTime*(1-fraction)/fraction;
	  printf("Done %9d/%9d   %5.1f%%   (elapsed %5.1f min, remaining %5.1f min)\n", i, n, i*evDenom, totalTime, remaining); 
	  fflush(stdout); 
        }
    }

    tOut->Write();
    fOut->Close();
}
