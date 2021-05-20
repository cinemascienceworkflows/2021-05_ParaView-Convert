![research](https://pantheonscience.github.io/states/research.png)

# Pantheon Workflow Template v <noop name="version">1.2</noop>

A repository template for the Pantheon project workflows.

## Using this repository

The main loop is in the `execute` script. From there, you can see the steps taken, and can follow the scripts to create your own examples.

## Edit these files
| file | what to do |
|------|---------|
|`bootstrap.env` | edit the `COMPUTE_ALLOCATION` and `PANTHEON_BASE_PATH` to match your environment |
|`pantheon/pantheon.yaml` | edit this to reflect the information from Pantheon for your workflow. If you do not have Pantheon settings information, you may leave this file unedited. |
|`postprocess/postprocess.sh` | edit this to call your postprocessing scripts, if you have them. |
|`readme.md` | edit the top line to indicate what type of Pantheon pipeline this is. |
|`run/run.sh` | edit this to copy files as needed by the application. |
|`run/submit.sh` | edit this to properly submit your job. |
|`setup/install-deps.sh` | edit to install dependencies |
|`setup/install-app.sh` | edit to install application  |


## DO NOT edit these files

1. `pantheon/pantheon.env`
