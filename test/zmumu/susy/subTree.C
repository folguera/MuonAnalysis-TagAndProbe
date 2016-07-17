void subTree(TString dir="tpTree", TString cut="(tag_IsoMu20 || tag_IsoMu22) && tag_combRelIsoPF04dBeta/tag_pt < 0.2 && tag_pt > 22", TString newFile="skimmedTree.root") {
    TTree *in  = (TTree *)gFile->Get(dir+"/fitter_tree");
    TFile *fout = new TFile(newFile, "RECREATE");
    TDirectory *dout = fout->mkdir(dir); dout->cd();

    TTree *out = in->CopyTree(cut, "", 2000);
    std::cout << "INPUT TREE (" << in->GetEntries() << " ENTRIES)" << std::endl;
    //in->Print();
    std::cout << "OUTPUT TREE (" << out->GetEntries() << " ENTRIES)" << std::endl;
    //out->Print();
    dout->WriteTObject(out, "fitter_tree");
    fout->Close();
}
