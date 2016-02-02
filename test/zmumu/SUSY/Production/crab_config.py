#This configuration is to perform produciton on DATA
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#!!
#!!Change to run on other samples
#!!
#config.General.requestName = '2015D_v4'
#config.General.workArea = 'crab_tnp_DATA_25ns'
config.General.requestName = 'NLO'
config.General.workArea = 'crab_tnp_MC_25ns'
#!!
#!!DataSet
#!!
#DATA
#config.Data.inputDataset = '/SingleMuon/Run2015D-PromptReco-v3/AOD'
#config.Data.inputDataset = '/SingleMuon/Run2015D-PromptReco-v4/AOD'
#MC
#25ns LO
#config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
#25ns NLO
config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/AODSIM'
#!!
#!!JSON
#!!
#25ns 
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt'
#!!
#!!RunRange
#!!
#config.Data.runRange = '246908-251884'
#!!
#!!config file
#!!
#config.JobType.psetName = 'tp_from_aod_Data.py'
config.JobType.psetName = 'tp_from_aod_MC.py'

config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.pluginName = 'Analysis'
python_file_list = []
f = open('input', 'r')
for line in f:
    python_file_list.append(line.strip('\n'))

config.JobType.inputFiles = python_file_list
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 50
config.Data.outLFNDirBase = '/store/user/%s/' % getUsernameFromSiteDB()
config.Data.publication = True
config.Data.publishDataName = 'crab_tnp_production_data'
config.Site.storageSite = 'T2_CH_CSCS'

