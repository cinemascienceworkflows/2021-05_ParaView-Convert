# build and install the application

source ./pantheon/env.sh > /dev/null 2>&1

echo ----------------------------------------------------------------------
echo "PTN: building $PANTHEON_APP"

pushd $PANTHEON_WORKFLOW_DIR > /dev/null 2>&1

echo "PTN: nothing to install for $PANTHEON_APP" 
echo ----------------------------------------------------------------------

popd > /dev/null 2>&1
