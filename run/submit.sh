#!/bin/bash

#BSUB -J <pantheon_workflow_jid> 
#BSUB -P <compute_allocation> 
#BSUB -W 0:03
#BSUB -nnodes 1

# --------------------------------------------------------------------
# BEGIN: EDIT THIS SECTION
#     add the bsub settings, modules and execution for your application

# load modules required by the executable

# submit the job
jsrun -n1 <pantheon_run_dir>/executable-to-run
# END: EDIT THIS SECTION
# --------------------------------------------------------------------

