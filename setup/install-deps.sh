#!/bin/bash -l

# adding comment

source ./pantheon/env.sh

echo "PTN: Establishing Pantheon workflow directory:"
echo $PANTHEON_WORKFLOW_DIR

PANTHEON_SOURCE_ROOT=$PWD

# these settings allow you to control what gets built ... 
BUILD_CLEAN=true
INSTALL_APP=true

# ---------------------------------------------------------------------------
#
# Build things, based on flags set above
#
# ---------------------------------------------------------------------------

START_TIME=$(date +"%r %Z")
echo ----------------------------------------------------------------------
echo "PTN: Start time: $START_TIME" 
echo ----------------------------------------------------------------------

# if a clean build, remove everything
if $BUILD_CLEAN; then
    echo ----------------------------------------------------------------------
    echo "PTN: clean build ..."
    echo ----------------------------------------------------------------------

    if [ -d $PANTHEON_WORKFLOW_DIR ]; then
        rm -rf $PANTHEON_WORKFLOW_DIR
    fi
    if [ ! -d $PANTHEON_PATH ]; then
        mkdir $PANTHEON_PATH
    fi
    if [ ! -d $PANTHEON_PROJECT_DIR ]; then
        mkdir $PANTHEON_PROJECT_DIR
    fi
    mkdir $PANTHEON_WORKFLOW_DIR
    mkdir $PANTHEON_DATA_DIR
    mkdir $PANTHEON_RUN_DIR
fi

# build the application and parts as needed
if $INSTALL_APP; then
    echo ----------------------------------------------------------------------
    echo "PTN: installing app ..."
    echo ----------------------------------------------------------------------

    source $PANTHEON_SOURCE_ROOT/setup/install-app.sh
fi

END_TIME=$(date +"%r %Z")
echo ----------------------------------------------------------------------
echo "PTN: statistics" 
echo "PTN: start: $START_TIME"
echo "PTN: end  : $END_TIME"
echo ----------------------------------------------------------------------

