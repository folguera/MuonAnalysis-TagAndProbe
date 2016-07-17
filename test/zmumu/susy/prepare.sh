#cd /afs/cern.ch/user/j/jrgonzal/CMSSW_8_0_11/src/
#eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/j/jrgonzal/TnPTrees/
pathtofiles='/afs/cern.ch/user/j/jrgonzal/CMSSW_8_0_11/src/MuonAnalysis/TagAndProbe/test/zmumu/'
pathDY='root://eoscms//eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v3/DY_madgraphMLM/'
pathData='root://eoscms//eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v3/data/TnPTree_80X_Run2016B_v2_GoldenJSON_Run271036to275125_incomplete.root'

# Slim 0
echo "### Slimming the trees ###"
for id in `seq 1 5`; do
  echo " >>> Slimming DY sample $id"
  root.exe -l -b -q root://eoscms//eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v3/DY_madgraphMLM/TnPTree_80X_DYLL_M50_MadGraphMLM_part$id.root  $pathtofiles/ZZ4L/preprocessing/slimTree.cxx\(0\)
  echo " >>> Created tnpZ_slim_step0.root, moving into ---> tnpZ_slim_step0_DY_$id.root"
  mv tnpZ_slim_step0.root tnpZ_slim_step0_DY_$id.root
done
echo " >>> Slimming data sample"
root.exe -l -b -q $pathData $pathtofiles/ZZ4L/preprocessing/slimTree.cxx\(0\)
echo " >>> Created tnpZ_slim_step0.root, moving into ---> tnpZ_slim_step0_Data.root"
mv tnpZ_slim_step0.root tnpZ_slim_step0_Data.root

# Skim
echo "### Skimming the trees ###"
for id in `seq 1 5`; do
  echo " >>> Skimming the DY sample $id"
  root.exe -l -b -q tnpZ_slim_step0_DY_$id.root  $pathtofiles/ZZ4L/preprocessing/subTree.C
  echo " >>> Created skimmedTree.root, moving into ---> skimmedTree_DY_$id.root"
  mv skimmedTree.root skimmedTree_DY_$id.root
done
echo " >>> Skimming the data sample"
root.exe -l -b -q tnpZ_slim_step0_Data.root $pathtofiles/ZZ4L/preprocessing/subTree.C
echo " >>> Created skimmedTree.root, moving into ---> skimmedTree_Data.root"
mv skimmedTree.root skimmedTree_Data.root

# Adding EA Iso
echo "### Adding Effective Area corrections ###"
for id in `seq 1 5`; do
  echo " >>> Adding EAminiIso to DY sample $id"
  root.exe -l -b -q skimmedTree_DY_$id.root $pathtofiles/addEAMiniIso.cxx
  echo " >>> Created tnpZ_withEAMiniIso.root, moving into ---> tnpZ_withEAMiniIso_DY_$id.root"
  mv tnpZ_withEAMiniIso.root tnpZ_withEAMiniIso_DY_$id.root
done
echo " >>> Adding EAminiIso to data sample"
root.exe -l -b -q skimmedTree_Data.root $pathtofiles/addEAMiniIso.cxx
echo " >>> Created tnpZ_withEAMiniIso.root, moving into ---> tnpZ_Data.root"
mv tnpZ_withEAMiniIso.root tnpZ_Data.root

# Adding PU weights
echo "### Adding PU weights ###"
for id in `seq 1 5`; do
  echo " >>> Adding PU weights to DY sample $id"
  root.exe -l -b -q tnpZ_Data.root tnpZ_withEAMiniIso_DY_$id.root $pathtofiles/addNVtxWeight.cxx+
  echo " >>> Created tnpZ_withNVtxWeights.root. moving into ---> tnpZ_DY$id.root"
  mv tnpZ_withNVtxWeights.root tnpZ_DY$id.root
done

echo "### Final slimming ###"
for id in `seq 1 5`; do
  echo " >>> Slimming DY sample $id"
  root.exe -l -b -q tnpZ_DY$id.root $pathtofiles/ZZ4L/preprocessing/slimTree.cxx\(2\)
  echo " >>> Created tnpZ_slim_step2.root, moving into ---> tnpZLast_DY_$id.root"
  mv tnpZ_slim_step2.root tnpZLast_DY_$id.root
done
echo " >>> Slimming data sample"
root.exe -l -b -q tnpZ_Data.root $pathtofiles/ZZ4L/preprocessing/slimTree.cxx\(2\)
echo " >>> Created tnpZ_slim_step2.root, moving into ---> tnpZLast_Data.root"
mv tnpZ_slim_step2.root tnpZLast_Data.root

echo " XXXxxx### DONE ###xxxXXX "
echo  - New Data and DY TnP trees created
echo  - Removing intermediate steps... rm *skimmedTree*, rm tnpZ_*
rm *skimmedTree*
rm tnpZ_*

