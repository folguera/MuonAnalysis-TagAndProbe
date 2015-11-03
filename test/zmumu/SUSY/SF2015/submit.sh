#!/bin/bash

bsub -q 8nh -u pippo1234 run.sh _151103 1 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151103 2 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151103 3 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151103 4 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151103 5 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151103 6 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151103 7 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151103 8 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151103 9 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151103 10 data_all 25ns 2015D

bsub -q 8nh -u pippo1234 run.sh _151103 1 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151103 2 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151103 3 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151103 4 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151103 5 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151103 6 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151103 7 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151103 8 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151103 9 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151103 10 mc_all 25ns 2015D LO

bsub -q 8nh -u pippo1234 run.sh _151103 1 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151103 2 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151103 3 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151103 4 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151103 5 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151103 6 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151103 7 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151103 8 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151103 9 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151103 10 mc_all 25ns 2015D NLO

