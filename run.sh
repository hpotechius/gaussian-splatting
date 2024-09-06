#!/bin/sh

#SBATCH --job-name=GaussianSplatting
#SBATCH --partition=moveki-gpu  
#SBATCH --gres=gpu:4
#SBATCH --nodes=2
#SBATCH --tasks-per-node=1
#SBATCH --mem=24000             # memory in Mb
#SBATCH -o outfile              # send stdout to outfile
#SBATCH -e errfile              # send stderr to errfile
#SBATCH -t 24:00:00             # time requested in hour:minute:second

module purge
module load tools/python/3.8
source /home/po87taj/Projects/gaussian-splatting/env/bin/activate
python3 train.py -s /home/po87taj/Projects/gaussian-splatting/datasets/EAHStatue -r 1