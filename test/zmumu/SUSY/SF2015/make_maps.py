import ROOT as r
import os
import glob
import sys

debug = True
nEtaBins = 2


args = sys.argv[1:]
iteration = '1'
if len(args) > 0: iteration =  args[0]
print "The iteration is ", iteration
#_sample = '/DATA25ns2015D/'
_sample = '/MC25ns2015DLO/'
#_sample = '/MC25ns2015DNLO/'
if len(args) > 1: _sample =  args[1]
print "The sample is", _sample 
_folder = os.getcwd() + '/Efficiency' + iteration + '/' + _sample + '/'
_folder_out = _folder +  'Maps/'
if not os.path.exists(_folder + '/Maps'):
    os.makedirs(_folder + '/Maps')

_tptree = 'tpTree'
dir = os.listdir(_folder)
os.chdir(_folder)
for file in glob.glob("*map_pt_eta*.root"):
    if debug: print 'the file is ', file
    if file.find('TnP_MuonID') != -1: 
        if not os.path.isfile(_folder + '/' + file):
            if debug: print 'The file ', file, 'doesn\'t exist in ', _folder
            continue
        else:
            if debug: print 'The file', file, 'exists !'
            f = r.TFile.Open(_folder+file)
            r.gDirectory.cd(_tptree)
            for key in  r.gDirectory.GetListOfKeys():
                print "The name of the key is", key.GetName()
                r.gDirectory.cd(key.GetName())
                r.gDirectory.cd('fit_eff_plots')
                PLOTS = r.gDirectory.GetListOfKeys()
                PLOTS.ls()
                for plot in PLOTS:
                    if plot.GetName().startswith("pt_abseta_PLOT_pair_probeMultiplicity_bin0"):
                        print plot.GetName()
                        canvas = plot.ReadObj()
                        HISTS = canvas.GetListOfPrimitives()
                        for hist in HISTS:
                            if hist.GetName().startswith("pt_abseta_PLOT_pair_probeMultiplicity_bin0"):
                                print "found map"
                                SFmap = hist
                    if plot.GetName().startswith("pt_PLOT_abseta_bin0"):
                        canvas = plot.ReadObj()
                        HISTS = canvas.GetListOfPrimitives()
                        for hist in HISTS:
                            print hist
                            if hist.GetName().startswith("hxy_fit_eff"):
                                print "found etabin0"
                                etabin0 = hist
                    if plot.GetName().startswith("pt_PLOT_abseta_bin1"):
                        canvas = plot.ReadObj()
                        HISTS = canvas.GetListOfPrimitives()
                        for hist in HISTS:
                            print hist
                            if hist.GetName().startswith("hxy_fit_eff"):
                                print "found etabin1"
                                etabin1 = hist
    pt = 0
    eff = 0
    pt = r.Double(pt)
    eff = r.Double(eff)
 
    for eta in range(nEtaBins):
        for i in range(etabin0.GetN()):
            if eta==0:
                etabin0.GetPoint(i, pt, eff)
                err = max(etabin0.GetErrorYhigh(i),etabin0.GetErrorYlow(i))
                print i, pt , eff 
                SFmap.SetBinContent(i+1, eta+1, eff)
                SFmap.SetBinError(i+1, eta+1, err)
            if eta==1:
                etabin1.GetPoint(i, pt, eff) 
                print i, pt , eff 
                SFmap.SetBinContent(i+1, eta+1, eff)
                SFmap.SetBinError(i+1, eta+1, err)
 

    print _folder_out            
    fout = r.TFile(_folder_out + file, "RECREATE");
    SFmap.Write();
    fout.Close();



