#!/bin/bash

bsub -R "pool>30000" -q 8nh run.sh newLO 1 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh -u pippo1234 run.sh newLO 2 data_all 25ns 2015D
bsub -R "pool>30000" -q 8nh run.sh newLO 3 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newLO 4 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newLO 5 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newLO 6 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newLO 7 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newLO 8 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newLO 9 data_all 25ns 2015D
bsub -R "pool>30000" -q 8nh run.sh newLO 10 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newD 11 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newD 12 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newD 13 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newD 14 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newD 15 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newD 16 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newD 17 data_all 25ns 2015D
#bsub -R "pool>30000" -q 8nh run.sh newD 18 data_all 25ns 2015D

#bsub -R "pool>30000" -q 8nh run.sh newLO 1 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 2 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 3 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 4 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 5 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 6 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 7 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 8 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 9 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 10 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 11 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 12 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 13 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 14 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 15 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 16 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 17 mc_all 25ns 2015D LO
#bsub -R "pool>30000" -q 8nh run.sh newLO 18 mc_all 25ns 2015D LO

#bsub -R "pool>30000" -q 8nh run.sh newLO 1 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 2 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 3 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 4 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 5 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 6 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 7 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 8 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 9 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 10 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 11 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 12 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 13 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 14 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 15 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 16 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 17 mc_all 25ns 2015D NLO
#bsub -R "pool>30000" -q 8nh run.sh newLO 18 mc_all 25ns 2015D NLO
