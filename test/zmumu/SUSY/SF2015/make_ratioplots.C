#include "TString.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TGraphAsymmErrors.h"
#include "TAxis.h"
#include "TGaxis.h"
#include "TH1F.h"
#include "TROOT.h"
#include "TLegend.h"
#include "TGaxis.h"
#include "tdrstyle.C"
#include "CMS_lumi.C"
#include "TLegendEntry.h"

#include <iostream> //#include <ofstream>

//!! To compute SF = MC/Data
TH1F* DividTGraphs(TGraphAsymmErrors* gr1, TGraphAsymmErrors* gr2){

    int nbins = gr1->GetN();
    double xbins[nbins+1];

    for(int i = 0;  i < nbins; ++i){

        Double_t x = 999; 
        Double_t x_hi = 999; 
        Double_t x_low = 999; 
        Double_t y = 999; 
        gr1->GetPoint(i,x,y);
        x_hi = gr1->GetErrorXhigh(i);
        x_low = gr1->GetErrorXlow(i);
        if(i == nbins-1){
            xbins[i] = x-x_low;
            xbins[i+1] = x+x_hi;
        }else{
            xbins[i] = x-x_low;
        }
    }

    TH1F *h0 = new TH1F("h0","h0",nbins,xbins);
    TH1F *h1 = new TH1F("h1","h1",nbins,xbins);

    TGraphAsymmErrors* gr[2] = {gr1, gr2};
    TH1F* h[2] = {h0, h1};

    //Loop over bins to do ratio
    //
    for (int k = 0; k < 2; ++k){
        for(int i = 0;  i < nbins; ++i){
            //
            //TGraph
            //
            Double_t num_x = 999; 
            Double_t num_y = 999; 
            Double_t num_y_hi = 999; 
            Double_t num_y_low = 999; 

            gr[k]->GetPoint(i,num_x,num_y);
            num_y_hi = gr[k]->GetErrorYhigh(i);
            num_y_low = gr[k]->GetErrorYlow(i);

            double max_error = max(num_y_hi,num_y_low);

            //Convert into TH1D
            h[k]->SetBinContent(h[k]->FindBin(num_x), num_y);
            h[k]->SetBinError(h[k]->FindBin(num_x), max_error);
        }
    }

    //ratio histogram
    h[0]->Divide(h[1]);
    delete h[1];

    return h[0]; 

}


int make_ratioplots(TString _file, TString _canvas, TString _path1, TString _path2, TString _output, TString comparison){

    setTDRStyle();
    gROOT->SetBatch(kTRUE);


    TString _par = "";
    if(_canvas.Contains("pt_PLOT_abseta_bin0")){_par = "abseta_bin0";}
    else if(_canvas.Contains("pt_PLOT_abseta_bin1")){_par = "abseta_bin1";}

    //cout<<_file<<endl;
    TFile *f1 = TFile::Open(_path1 + _file);
    TCanvas* c1 = (TCanvas*) f1->Get(_canvas);
    TGraphAsymmErrors* eff1 = (TGraphAsymmErrors*)c1->GetPrimitive("hxy_fit_eff");
    TFile *f2 = TFile::Open(_path2 + _file);
    TCanvas* c2 = (TCanvas*) f2->Get(_canvas);
    TGraphAsymmErrors* eff2 = (TGraphAsymmErrors*)c2->GetPrimitive("hxy_fit_eff");

    TH1F* ratio = DividTGraphs(eff1, eff2);
    ratio->SetStats(0);

    int nbins = eff1->GetN();
    double x,y;
    eff1->GetPoint(0,x,y);
    double x_low = x-eff1->GetErrorXlow(0);
    eff1->GetPoint(nbins-1,x,y);
    double x_hi = x+eff1->GetErrorXhigh(nbins-1);

    TCanvas* c3 = new TCanvas("c3","c3");
    TPad *pad1 = new TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
    pad1->SetBottomMargin(0.); 
    pad1->SetTopMargin(0.1); 
    pad1->Draw();
    pad1->cd();
    eff1->Draw("AP");
    eff1->SetTitle("");
    eff1->GetYaxis()->SetTitle("Efficiency");
    eff1->GetXaxis()->SetRangeUser(x_low, x_hi);
    eff1->GetXaxis()->SetLabelOffset(999);
    eff1->GetXaxis()->SetLabelSize(0);
    TString _xtitle = eff1->GetXaxis()->GetTitle();
    if(_xtitle.Contains("tag_nVertices")){_xtitle = "N(primary vertices)";
    }else if (_xtitle.Contains("phi")){_xtitle = "muon #phi";}
    else if (_xtitle.Contains("eta")){_xtitle = "muon #eta";}
    else if (_xtitle.Contains("pt")){_xtitle = "muon p_{t} [GeV]";}
    else if (_xtitle.Contains("pfCombAbsActivitydBCorr")){_xtitle = "Abs Activity";}
    else if (_xtitle.Contains("pfCombRelActivitydBCorr")){_xtitle = "Rel Activity";}
    else{_xtitle = "Rel Activity";}
    eff1->GetXaxis()->SetTitle(_xtitle);
    TString _title = eff1->GetXaxis()->GetTitle();
    if(_xtitle == "Rel Activity"){
        pad1->SetLogx();
    }   
    eff1->GetXaxis()->SetTitle("");
    eff1->GetYaxis()->SetRangeUser(0.885, 1.05);
    eff1->GetYaxis()->SetTitleSize(27);
    eff1->GetYaxis()->SetTitleFont(63);
    eff1->GetYaxis()->SetLabelFont(43);
    eff1->SetMarkerStyle(20);
    eff1->GetYaxis()->SetLabelSize(20);
    eff1->GetYaxis()->SetTitleOffset(1.5);
    
    float xmin = eff1->GetXaxis()->GetXmin();
    float xmax = eff1->GetXaxis()->GetXmax();

    eff2->Draw("P");
    eff2->SetLineColor(4);
    eff2->SetMarkerStyle(21);
    eff2->SetMarkerColor(4);
    TString _legtext = "";

    if(_canvas.Contains("/Loose_noIP_eta")){
        _legtext = "Loose Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/Loose_noIP_vtx_bin")){
        _legtext = "Loose Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/Loose_noIP_pt_alleta_bin")){
        _legtext = "Loose Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/Loose_noIP_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Loose Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("/Loose_noIP_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Loose Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/Medium_noIP_eta")){
        _legtext = "Medium Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/Medium_noIP_vtx")){
        if(_canvas.Contains("/Medium_noIP_vtx_bin_vtx_highabseta")){
        _legtext = "Medium Id, p_{T} #geq 20 GeV, #||{#eta} #geq 2.1";
        }else if(_canvas.Contains("/Medium_noIP_vtx_bin")){
        _legtext = "Medium Id, p_{T} #geq 20 GeV";
        }
    }else if(_canvas.Contains("/Medium_noIP_pt_alleta_bin")){
        _legtext = "Medium Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/Medium_noIP_phi_loweta")){
        _legtext = "Medium Id, -2.4 #leq #eta #leq -2.1";
    }else if(_canvas.Contains("/Medium_noIP_phi_higheta")){
        _legtext = "Medium Id, 2.1 #leq #eta #leq 2.4";
    }else if(_canvas.Contains("/Medium_noIP_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Medium Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("/Medium_noIP_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/Medium_noIP_pt_highabseta")){
        _legtext = "Medium Id, p_{T} #geq 20 GeV, #||{#eta} #geq 2.1";
    }else if(_canvas.Contains("/Tight2012_zIPCut_eta")){
        _legtext = "Tight Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/Tight2012_zIPCut_vtx_bin")){
        _legtext = "Tight Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/Tight2012_zIPCut_pt_alleta_bin")){
        _legtext = "Tight Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/Tight2012_zIPCut_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Tight Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("/Tight2012_zIPCut_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Tight Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/LooseIso4_loose_eta")){
        _legtext = "Loose Iso/Loose Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/LooseIso4_loose_vtx_bin")){
        _legtext = "Loose Iso/Loose Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/LooseIso4_loose_pt_alleta_bin")){
        _legtext = "Loose Iso/Loose Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/LooseIso4_loose_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Loose Iso/Loose Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("/LooseIso4_loose_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Loose Iso/Loose Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/LooseIso4_medium_eta")){
        _legtext = "Loose Iso/Medium Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/LooseIso4_medium_vtx_bin")){
        _legtext = "Loose Iso/Medium Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/LooseIso4_medium_pt_alleta_bin")){
        _legtext = "Loose Iso/Medium Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/LooseIso4_medium_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Loose Iso/Medium Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("/LooseIso4_medium_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Loose Iso/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/LooseIso4_tightip_eta")){
        _legtext = "Loose Iso/Tight Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/LooseIso4_tightip_vtx_bin")){
        _legtext = "Loose Iso/Tight Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/LooseIso4_tightip_pt_alleta_bin")){
        _legtext = "Loose Iso/Tight Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/LooseIso4_tightip_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Loose Iso/Tight Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("/LooseIso4_tightip_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Loose Iso/Tight Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/TightIso4_loose_eta")){
        _legtext = "Tight Iso/Loose Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/TightIso4_loose_vtx_bin")){
        _legtext = "Tight Iso/Loose Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/TightIso4_loose_pt_alleta_bin")){
        _legtext = "Tight Iso/Loose Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/TightIso4_loose_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Tight Iso/Loose Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("/TightIso4_loose_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Tight Iso/Loose Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/TightIso4_tightip_eta")){
        _legtext = "Tight Iso/Tight Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/TightIso4_tightip_vtx_bin")){
        _legtext = "Tight Iso/Tight Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/TightIso4_tightip_pt_alleta_bin")){
        _legtext = "Tight Iso/Tight Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/TightIso4_tightip_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Tight Iso/Tight Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("/TightIso4_tightip_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Tight Iso/Tight Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/TightIso4_medium_eta")){
        _legtext = "Loose Iso/Medium Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/TightIso4_medium_vtx_bin")){
        _legtext = "Loose Iso/Medium Id, p_{T} #geq 20 GeV";
    }else if(_canvas.Contains("/TightIso4_medium_pt_alleta_bin")){
        _legtext = "Loose Iso/Medium Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("/TightIso4_medium_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Loose Iso/Medium Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("/TightIso4_medium_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Loose Iso/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightIP3D_medium_eta")){
        _legtext = "Tight IP 3D/Medium Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightIP3D_medium_eta")){
        _legtext = "Tight IP 3D/Medium Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("LooseMiniIso_loose_eta")){
        _legtext = "Loose MiniIso/Loose Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightMiniIso_medium_eta")){
        _legtext = "Tight MiniIso/Medium Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightMiniIso_loose_eta")){
        _legtext = "Tight MiniIso/Loose Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("MediumMultiIso_medium_eta")){
        _legtext = "Multi Iso/Medium Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("MediumMultiIso_medium_vtx_bin1_24")){
        _legtext = "Multi Iso/Medium Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightMiniIso_loose_vtx_bin1_24")){
        _legtext = "Tight MiniIso/Loose Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightIP3D_medium_vtx_bin1_24")){
        _legtext = "Tight IP 3D/Medium Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightMiniIso_medium_vtx_bin1_24")){
        _legtext = "Tight MiniIso/Medium Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("LooseMiniIso_loose_vtx_bin1_24")){
        _legtext = "Loose MiniIso/Loose Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("MediumMultiIso_medium_pt_alleta_bin1")){
        _legtext = "MultiIso/Medium Id, 0 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightMiniIso_loose_pt_alleta_bin1")){
        _legtext = "Tight MiniIso/Loose Id, 0 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_alleta_bin1")){
        _legtext = "Tight MiniIso/Medium Id, 0 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightIP3D_medium_pt_alleta_bin1")){
        _legtext = "Tight IP 3D/Medium Id, 0 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("LooseMiniIso_loose_pt_alleta_bin1")){
        _legtext = "Loose MiniIso/Loose Id, 0 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightMiniIso_loose_pt_spliteta_bin") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Tight MiniIso/Loose Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("TightMiniIso_loose_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Tight MiniIso/Loose Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("MediumMultiIso_medium_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Multi Iso/Medium Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("MediumMultiIso_medium_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Multi Iso/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightIP3D_medium_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Tight IP 3D/Medium Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("TightIP3D_medium_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Tight IP 3D/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Loose MiniIso/Loose Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("LooseMiniIso_loose_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Loose MiniIso/Loose Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("LooseMiniIso_loose_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Loose MiniIso/Loose Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Tight MiniIso/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightMiniIso_loose_pt_activity_barrel")){
        _legtext = "Tight MiniIso/Loose Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("MediumMultiIso_medium_pt_activity_barrel")){
        _legtext = "Mutli Iso/Medium Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_activity_barrel")){
        _legtext = "Tight MiniIso/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightMiniIso_loose_pt_activity_endcap")){
        _legtext = "Tight MiniIso/Loose Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("LooseMiniIso_loose_pt_activity_barrel")){
        _legtext = "Loose MiniIso/Loose Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_activity_endcap")){
        _legtext = "Tight MiniIso/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("MediumMultiIso_medium_pt_activity_endcap")){
        _legtext = "Multi Iso/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_activity_endcap")){
        _legtext = "Tight MiniIso/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("MediumMultiIso_medium_pt_activity_endcap")){
        _legtext = "Multi Iso/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("LooseMiniIso_loose_pt_activity_endcap")){
        _legtext = "Loose MiniIso/Loose Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightIP2D_loose_eta")){
        _legtext = "Tight IP 2D/Loose Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightIP2D_medium_eta")){
        _legtext = "Tight IP 2D/Medium Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightIP3D_loose_eta")){
        _legtext = "Tight IP 3D/Loose Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightIP2D_loose_vtx_bin1_24")){
        _legtext = "Tight IP 2D/Loose Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightIP2D_medium_vtx_bin1_24")){
        _legtext = "Tight IP 2D/Medium Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightIP3D_loose_pt_alleta_bin1")){
        _legtext = "Tight IP 3D/Loose Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightIP3D_loose_vtx_bin1_24")){
        _legtext = "Tight IP 3D/Medium Id, p_{T} #geq 10 GeV";
    }else if(_canvas.Contains("TightIP2D_medium_pt_alleta_bin1")){
        _legtext = "Tight IP 2D/Medium Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightIP2D_loose_pt_alleta_bin1")){
        _legtext = "Tight IP 2D/Loose Id, #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightIP2D_medium_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Tight IP2D/Medium Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("TightIP2D_medium_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Tight IP2D/Medium Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightIP2D_loose_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Tight IP2D/Loose Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("TightIP2D_loose_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Tight IP2D/Loose Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightIP3D_loose_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin0")){
        _legtext = "Tight IP3D/Loose Id, #||{#eta} #leq 1.2";
    }else if(_canvas.Contains("/TightIP3D_loose_pt_spliteta_bin1") && _canvas.Contains("pt_PLOT_abseta_bin1")){
        _legtext = "Tight IP3D/Loose Id, 1.2 < #||{#eta} #leq 2.4";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_activity_medpt")){
        _legtext = "Tight MiniIso/Medium Id, 40 < p_{T} #leq 80 GeV";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_activity_lowpt")){
        _legtext = "Tight MiniIso/Medium Id, 10 < p_{T} #leq 40 GeV";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_activity_highpt")){
        _legtext = "Tight MiniIso/Medium Id, 80 < p_{T} #leq 200 GeV";
    }else if(_canvas.Contains("TightMiniIso_loose_pt_activity_medpt")){
        _legtext = "Tight MiniIso/Loose Id, 40 < p_{T} #leq 80 GeV";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_activity_medpt")){
        _legtext = "Tight MiniIso/Medium Id, 40 < p_{T} #leq 80 GeV";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_activity_lowpt")){
        _legtext = "Tight MiniIso/Medium Id, 10 < p_{T} #leq 40 GeV";
    }else if(_canvas.Contains("TightMiniIso_medium_pt_activity_highpt")){
        _legtext = "Tight MiniIso/Medium Id, 80 < p_{T} #leq 200 GeV";
    }else if(_canvas.Contains("TightMiniIso_loose_pt_activity_medpt")){
        _legtext = "Tight MiniIso/Loose Id, 40 < p_{T} #leq 80 GeV";
    }else if(_canvas.Contains("TightMiniIso_loose_pt_activity_lowp")){
        _legtext = "Tight MiniIso/Loose Id, 10 < p_{T} #leq 40 GeV";
    }else if(_canvas.Contains("TightMiniIso_loose_pt_activity_highpt")){
        _legtext = "Tight MiniIso/Loose Id, 80 < p_{T} #leq 200 GeV";
    }else if(_canvas.Contains("MediumMultiIso_medium_pt_activity_medpt")){
        _legtext = "Multi Iso /Medium Id, 40 < p_{T} #leq 80 GeV";
    }else if(_canvas.Contains("MediumMultiIso_medium_pt_activity_lowpt")){
        _legtext = "Multi Iso /Medium Id, 10 < p_{T} #leq 40 GeV";
    }else if(_canvas.Contains("MediumMultiIso_medium_pt_activity_highp")){
        _legtext = "Multi Iso /Medium Id, 80 < p_{T} #leq 200 GeV";
    }else if(_canvas.Contains("LooseMiniIso_loose_pt_activity_medpt")){
        _legtext = "Loose MiniIso/Loose Id, 40 < p_{T} #leq 80 GeV";
    }else if(_canvas.Contains("LooseMiniIso_loose_pt_activity_lowpt")){
        _legtext = "Loose MiniIso/Loose Id, 10 < p_{T} #leq 40 GeV";
    }else if(_canvas.Contains("LooseMiniIso_loose_pt_activity_highpt")){
        _legtext = "Loose MiniIso/Loose Id, 80 < p_{T} #leq 200 GeV";
    }else{
        std::cout<<"=============================="<<std::endl;
        std::cout<<"ERROR: No corresponding legend"<<std::endl;
        std::cout<<"=============================="<<std::endl;
	std::cout<<"canvas is"<<_canvas<<endl;
        //return 1;
    }
    TLegend* leg = new TLegend(0.40, 0.65, 0.70 , 0.85);
    leg->SetHeader(_legtext);
    TLegendEntry *header = (TLegendEntry*)leg->GetListOfPrimitives()->First();
    //header->SetTextAlign(22);
    header->SetTextColor(1);
    header->SetTextFont(43);
    header->SetTextSize(16);
    TString _leg1 = "";
    TString _leg2 = "";
    if(_path1.Contains("DATA")) _leg1 = "data";
    else if(_path1.Contains("MC")){ 
        if(_path1.Contains("NLO")) _leg1 = "MC NLO"; 
        else if(_path1.Contains("LO")) _leg1 = "MC LO";
    }
    
    if(_path2.Contains("DATA")) _leg2 = "data";
    else if(_path2.Contains("MC")){ 
        if(_path2.Contains("NLO")) _leg2 = "MC NLO";
        else if(_path2.Contains("LO")) _leg2 = "MC LO";
    }
    

    leg->AddEntry(eff1, _leg1, "LP");
    leg->AddEntry(eff2, _leg2,"LP");
    
    /*
    if (comparison == "mcdata"){
    leg->AddEntry(eff1, "Data", "LP");
    leg->AddEntry(eff2, "MC","LP");
    } 
    else if (comparison == "mcmc"){
    leg->AddEntry(eff1, "LO", "LP");
    leg->AddEntry(eff2, "NLO","LP");
    } 
    */
    leg->SetBorderSize(0.);
    leg->SetTextFont(43);
    leg->SetTextSize(20);
    leg->Draw();
    _file.ReplaceAll("root","pdf");
    TGaxis *axis = new TGaxis( -5, 20, -5, 220, 20,220,510,"");
    axis->SetLabelFont(43); // Absolute font size in pixel (precision 3)
    axis->SetLabelSize(15);
    axis->Draw();

    c3->cd();
    TPad *pad2 = new TPad("pad2", "pad2", 0, 0., 1, 0.3);
    pad2->SetTopMargin(0.0); 
    pad2->SetBottomMargin(0.35); 
    pad2->SetGridy(); 
    pad2->Draw();
    pad2->cd();
    TH1* h;
    //float xmin = 0.001;
    //float xmax = 10000;
    float ymin = 0.950001;
    float ymax = 1.049999;

    if(_xtitle == "Rel Activity")
        h = pad2->DrawFrame(xmin,ymin,xmax,ymax);
    else 
        h = ratio;

    h->SetTitle("");
    h->SetLineWidth(2);
    h->SetLineColor(1);
    h->SetMarkerStyle(20);
    h->SetMarkerColor(1);
    //ratio->GetYaxis()->SetRangeUser(0.9,1.0999);
    h->GetYaxis()->SetRangeUser(ymin,ymax);
    //raftio->GetYaxis()->SetRangeUser(0.98,1.01999);
    h->GetYaxis()->SetTitle("Data/MC");
    h->GetYaxis()->SetNdivisions(505);
    h->GetYaxis()->SetLabelSize(20);
    h->GetYaxis()->SetTitleFont(63);
    h->GetYaxis()->SetTitleOffset(1.5);
    h->GetYaxis()->SetLabelFont(43); // Absolute font size in pixel (precision 3)
    h->GetYaxis()->SetTitleSize(27);
    h->GetXaxis()->SetTitleSize(27);
    h->GetXaxis()->SetLabelSize(20);
    h->GetXaxis()->SetTitle(_title);
    h->GetXaxis()->SetTitleFont(63);
    h->GetXaxis()->SetTitleSize(27);
    h->GetXaxis()->SetTitleOffset(3);
    h->GetXaxis()->SetLabelFont(43); // Absolute font size in pixel (precision 3)
    if(_xtitle == "Rel Activity"){
        ratio->GetXaxis()->SetRangeUser(xmin,xmax);
        pad2->SetLogx();
        ratio->Draw("same");
        pad2->Update();
    }   
    else 
        ratio->Draw();

    cout<<" "<<ratio->GetXaxis()->GetXmin()<<"-"<<ratio->GetXaxis()->GetXmax()<<endl;
    //cout<<" "<<ratio->GetXaxis()->Maximum()<<"-"<<ratio->GetXaxis()->Minimum()
    cout << "xxxxxxxxxxxxxxxxxxxx" << endl;
    cout << ratio->GetSize() << " " << ratio->GetBinLowEdge(1)<<"-"<<ratio->GetBinLowEdge(6)<<" "<<ratio->GetNbinsX() << endl;
    CMS_lumi(pad1, 4, 11);
    c3->Update();

    c3->SaveAs(_output + _par + "_" + _file);
    _file.ReplaceAll("pdf","png");
    c3->SaveAs(_output + _par + "_" + _file);

    //TFile *f_out = TFile::Open("TEST.root","recreate");
    //f_out->cd();
    //c3->Write();

    //_*_*_*_*_*_*_*_*_*
    //Write SF into file
    //_*_*_*_*_*_*_*_*_*

    //ofstream myfile;
    //myfile.open(_output + 


    return 0;

}

