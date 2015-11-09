#!/bin/bash

bsub -q 8nh -u pippo1234 run.sh _151109 1 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151109 2 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151109 3 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151109 4 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151109 5 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151109 6 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151109 7 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151109 8 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151109 9 data_all 25ns 2015D
bsub -q 8nh -u pippo1234 run.sh _151109 10 data_all 25ns 2015D

bsub -q 8nh -u pippo1234 run.sh _151109 1 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151109 2 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151109 3 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151109 4 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151109 5 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151109 6 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151109 7 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151109 8 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151109 9 mc_all 25ns 2015D LO
bsub -q 8nh -u pippo1234 run.sh _151109 10 mc_all 25ns 2015D LO

bsub -q 8nh -u pippo1234 run.sh _151109 1 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151109 2 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151109 3 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151109 4 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151109 5 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151109 6 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151109 7 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151109 8 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151109 9 mc_all 25ns 2015D NLO
bsub -q 8nh -u pippo1234 run.sh _151109 10 mc_all 25ns 2015D NLO

