#include "TTree.h"
#include "TFile.h"
#include "TStopwatch.h"
#include "MuonEffectiveArea.h"

void addIsoWPs() {
    TTree *tIn  = (TTree *) gFile->Get("tpTree/fitter_tree");
    Float_t relMiniIso,JetPtRel,JetPtRatio;
    tIn->SetBranchAddress("pfCombRelMiniIsoEACorr", &relMiniIso);
    tIn->SetBranchAddress("JetPtRel", &JetPtRel);
    tIn->SetBranchAddress("JetPtRatio", &JetPtRatio);

    TFile *fOut = new TFile("tnpZ_withIsoWPs.root", "RECREATE");
    fOut->mkdir("tpTree")->cd();
    TTree *tOut = tIn->CloneTree(0);

    Bool_t RelMiniIso04, RelMiniIso02, MultiIsoL, MultiIsoM, MultiIsoVT;
    tOut->Branch("RelMiniIso04", &RelMiniIso04, "RelMiniIso04/O");
    tOut->Branch("RelMiniIso02", &RelMiniIso02, "RelMiniIso02/O");
    tOut->Branch("MultiIsoL" , &MultiIsoL , "MultiIsoL/O");
    tOut->Branch("MultiIsoM" , &MultiIsoM , "MultiIsoM/O");
    tOut->Branch("MultiIsoVT", &MultiIsoVT, "MultiIsoVT/O");

    int step = tIn->GetEntries()/1000;
    double evDenom = 100.0/double(tIn->GetEntries());
    TStopwatch timer; timer.Start();
    for (int i = 0, n = tIn->GetEntries(); i < n; ++i) {
        tIn->GetEntry(i);
	
	RelMiniIso04 =  relMiniIso < 0.4 ? true : false;
	RelMiniIso02 =  relMiniIso < 0.2 ? true : false;
	MultiIsoL    = (relMiniIso < 0.20 && ( JetPtRel > 6.0 || JetPtRatio > 0.69)) ? true : false;
	MultiIsoM    = (relMiniIso < 0.16 && ( JetPtRel > 7.2 || JetPtRatio > 0.76)) ? true : false;
	MultiIsoVT   = (relMiniIso < 0.09 && ( JetPtRel > 7.2 || JetPtRatio > 0.84)) ? true : false;
                
        tOut->Fill();
        //if (i > 10000) break;
        if ((i+1) % step == 0) { 
            double totalTime = timer.RealTime()/60.; timer.Continue();
            double fraction = double(i+1)/double(n+1), remaining = totalTime*(1-fraction)/fraction;
            printf("Done %9d/%9d   %5.1f%%   (elapsed %5.1f min, remaining %5.1f min)\n", i, n, i*evDenom, totalTime, remaining); 
            fflush(stdout); 
        }
    }

    tOut->AutoSave(); // according to root tutorial this is the right thing to do
    fOut->Close();
}
