#!/bin/bash

#bsub -q 8nh -u pippo1234 run.sh NEWstack 1 data_all 25ns 2015D
#bsub -q 8nh -u pippo1234 run.sh NEWstack 2 data_all 25ns 2015D
#bsub -q 8nh -u pippo1234 run.sh NEWstack 3 data_all 25ns 2015D
#bsub -q 8nh -u pippo1234 run.sh NEWstack 4 data_all 25ns 2015D
#bsub -q 8nh -u pippo1234 run.sh NEWstack 5 data_all 25ns 2015D
#bsub -q 8nh -u pippo1234 run.sh NEWstack 6 data_all 25ns 2015D
#bsub -q 8nh -u pippo1234 run.sh NEWstack 7 data_all 25ns 2015D
#bsub -q 8nh -u pippo1234 run.sh NEWstack 8 data_all 25ns 2015D
#bsub -q 8nh -u pippo1234 run.sh NEWstack 9 data_all 25ns 2015D
#bsub -q 8nh -u pippo1234 run.sh NEWstack 10 data_all 25ns 2015D
bsub -R "pool>30000" -q 8nh -u pippo1234 run.sh NEWstack2 11 data_all 25ns 2015D
bsub -R "pool>30000" -q 8nh -u pippo1234 run.sh NEWstack2 12 data_all 25ns 2015D
bsub -R "pool>30000" -q 8nh -u pippo1234 run.sh NEWstack2 13 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh -u pippo1234 run.sh NEWstack2 14 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh -u pippo1234 run.sh NEWstack2 15 data_all 25ns 2015D
bsub -R "pool>30000" -q 8nh -u pippo1234 run.sh NEWstack2 16 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh -u pippo1234 run.sh NEWstack2 17 data_all 25ns 2015D
bsub -R "pool>30000" -q 8nh -u pippo1234 run.sh NEWstack2 18 data_all 25ns 2015D

#bsub -q 8nh -u pippo1234 run.sh NEWstack 1 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 2 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 3 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 4 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 5 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 6 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 7 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 8 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 9 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 10 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 11 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 12 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 13 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 14 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 15 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 16 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 17 mc_all 25ns 2015D LO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 18 mc_all 25ns 2015D LO

#bsub -q 8nh -u pippo1234 run.sh NEWstack 1 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 2 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 3 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 4 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 5 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 6 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 7 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 8 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 9 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 10 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 11 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 12 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 13 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 14 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 15 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 16 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 17 mc_all 25ns 2015D NLO
#bsub -q 8nh -u pippo1234 run.sh NEWstack 18 mc_all 25ns 2015D NLO
