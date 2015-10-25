#!/bin/bash

bsub -q 8nh -u pippo1234 run.sh test1 1 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh test1 2 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh test1 3 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh test1 4 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh test1 5 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh test1 6 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh test1 7 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh test1 8 data_all 25ns 2015D 
bsub -q 8nh -u pippo1234 run.sh test1 9 data_all 25ns 2015D 
bsub -q 8nh -u pippo1234 run.sh test1 10 data_all 25ns 2015D 
#
bsub -q 8nh -u pippo1234 run.sh test1 1 mc_all 25ns 2015D NLO 
bsub -q 8nh -u pippo1234 run.sh test1 2 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh test1 3 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh test1 4 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh test1 5 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh test1 6 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh test1 7 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh test1 8 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh test1 9 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh test1 10 mc_all 25ns 2015D NLO
#
bsub -q 8nh -u pippo1234 run.sh test1 1 mc_all 25ns 2015D LO 
bsub -q 8nh -u pippo1234 run.sh test1 2 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh test1 3 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh test1 4 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh test1 5 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh test1 6 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh test1 7 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh test1 8 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh test1 9 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh test1 10 mc_all 25ns 2015D LO

