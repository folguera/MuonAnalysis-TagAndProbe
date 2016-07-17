void slimTree(int step, TString dir="tpTree") {
    TTree *in  = (TTree *)gFile->Get(dir+"/fitter_tree");
    TFile *fout = new TFile(Form("tnpZ_slim_step%d.root", step), "RECREATE");
    TDirectory *dout = fout->mkdir(dir); dout->cd();
    if (1) {
        // Switch off everything
        in->SetBranchStatus("*", 0);
        
        // Necessary
        in->SetBranchStatus("mass",1);
        in->SetBranchStatus("pt",1);
        in->SetBranchStatus("abseta",1); in->SetBranchStatus("eta",1); 
        in->SetBranchStatus("phi",1);
        in->SetBranchStatus("PF",1);
        in->SetBranchStatus("tag_pt",1);
        in->SetBranchStatus("charge",1);
        in->SetBranchStatus("glbPtError",1);
        //in->SetBranchStatus("pfCombRelActivitydBCorr",1);
      
        in->SetBranchStatus("Loose",1);
        //in->SetBranchStatus("Medium",1);
        in->SetBranchStatus("Medium2016",1);
        // A few more ID requirements 
        //in->SetBranchStatus("Glb",1); 
        //in->SetBranchStatus("TM",1); in->SetBranchStatus("TMA",1); 
        //in->SetBranchStatus("GlbPT",1); 
        //in->SetBranchStatus("Tight2012",1);
	//in->SetBranchStatus("combRelIsoPF04dBeta",1);
        //in->SetBranchStatus("numberOfMatchedStations",1);
        //in->SetBranchStatus("tkPixelLay",1);
        //in->SetBranchStatus("tkTrackerLay",1);
	
	in->SetBranchStatus("JetPtRel",1);
	in->SetBranchStatus("JetBTagCSV",1);
	in->SetBranchStatus("JetNDauCharged",1);
	in->SetBranchStatus("JetPtRatio",1);

        // Impact parameter
        in->SetBranchStatus("SIP",1);
        in->SetBranchStatus("dzPV",1);
        in->SetBranchStatus("dxyBS",1);
        in->SetBranchStatus("pair_probeMultiplicity",1);
    
        in->SetBranchStatus("tag_nVertices",1);
        if (in->GetBranch("run"))    in->SetBranchStatus("run",1);
        if (in->GetBranch("mcTrue")) in->SetBranchStatus("mcTrue",1);

        // TAG selection
        in->SetBranchStatus("tag_IsoMu24_eta2p1",1); in->SetBranchStatus("tag_IsoMu24",1); 
        in->SetBranchStatus("tag_combRelIso",1); 
        in->SetBranchStatus("tag_chargedHadIso04",1);
        in->SetBranchStatus("tag_nVertices",1);
        in->SetBranchStatus("tag_abseta",1);
        in->SetBranchStatus("tag_combRelIsoPF04dBeta",1);

        // nVTX reweighting
        if (step == 2) in->SetBranchStatus("weight",1); 

        // EA Isolation
        if (step == 0) {
            in->SetBranchStatus("miniIsoCharged",1); 
            in->SetBranchStatus("miniIsoPhotons",1); 
            in->SetBranchStatus("miniIsoNeutrals",1); 
            in->SetBranchStatus("activity_miniIsoCharged",1); 
            in->SetBranchStatus("activity_miniIsoPUCharged",1); 
            in->SetBranchStatus("activity_miniIsoNeutrals",1); 
            in->SetBranchStatus("activity_miniIsoPhotons",1); 
            in->SetBranchStatus("fixedGridRhoFastjetCentralNeutral",1); 
            //in->SetBranchStatus("kt6RhoNeu05",1);
            //in->SetBranchStatus("kt6RhoAll",1);
        } else {
            in->SetBranchStatus("pfCombRelMiniIsoEACorr",1);
                                 
        }

        // MVA Isolation
        //if (step == 0) {
//            in->SetBranchStatus("kt6RhoAll",1);
//            in->SetBranchStatus("ChargedIso_DR0p0To0p1",1);
//            in->SetBranchStatus("ChargedIso_DR0p1To0p2",1);
//            in->SetBranchStatus("ChargedIso_DR0p2To0p3",1);
//            in->SetBranchStatus("ChargedIso_DR0p3To0p4",1);
//            in->SetBranchStatus("ChargedIso_DR0p4To0p5",1);
//            in->SetBranchStatus("NeutralHadronIso_DR0p0To0p1",1);
//            in->SetBranchStatus("NeutralHadronIso_DR0p1To0p2",1);
//            in->SetBranchStatus("NeutralHadronIso_DR0p2To0p3",1);
//            in->SetBranchStatus("NeutralHadronIso_DR0p3To0p4",1);
//            in->SetBranchStatus("NeutralHadronIso_DR0p4To0p5",1);
//            in->SetBranchStatus("GammaIso_DR0p0To0p1",1);
//            in->SetBranchStatus("GammaIso_DR0p1To0p2",1);
//            in->SetBranchStatus("GammaIso_DR0p2To0p3",1);
//            in->SetBranchStatus("GammaIso_DR0p3To0p4",1);
//            in->SetBranchStatus("GammaIso_DR0p4To0p5",1); 
        //} else {
            //in->SetBranchStatus("mvaIso",1);
//            in->SetBranchStatus("mvaIsoCut",1);
        //}

        // Trigger
        in->SetBranchStatus("tag_IsoMu20",1);
        in->SetBranchStatus("tag_IsoMu22",1);
//        in->SetBranchStatus("DoubleMu17Mu8_Mu8",1);
//        in->SetBranchStatus("DoubleMu17TkMu8_Mu17",1);
//        in->SetBranchStatus("DoubleMu17TkMu8_TkMu8",1);

        //in->SetBranchStatus("l3pt",1);
//        in->SetBranchStatus("HLT_Mu17",1);
//        in->SetBranchStatus("HLT_TkMu17",1);
//        in->SetBranchStatus("HLT_OrMu17",1);
//        in->SetBranchStatus("HLT_Mu8",1);
//        in->SetBranchStatus("HLT_TkMu8",1);
//        in->SetBranchStatus("HLT_OrMu8",1);
//        in->SetBranchStatus("HLT_IsoMu24_eta2p1",1);
    }



    TTree *out = in->CloneTree(0);
    out->CopyEntries(in, -1, "fast");
    std::cout << "INPUT TREE (" << in->GetEntries() << " ENTRIES)" << std::endl;
    //in->Print();
    std::cout << "OUTPUT TREE (" << out->GetEntries() << " ENTRIES)" << std::endl;
    //out->Print();
    dout->WriteTObject(out, "fitter_tree");
    fout->Close();
}
