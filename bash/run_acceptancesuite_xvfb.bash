#!/bin/bash
#
# Run Maven-based acceptance suite (Selenium-based automated browser tests) on
# a headless server, which still has virtual framebuffer X server (Xvfb) and a
# browser installed.
#
# Also expects to find a suitable and working Maven installation in the server.
#
# This script is public domain. No warranties and no guarantees about fitness
# for any particular purpose. Might not even work on any other system but the
# one it was originally created for.

# Launch the X server:
echo "Launching virtual X server"
Xvfb :10 -screen 0 1024x768x24 > Xvfb.log 2>&1 &
xvfbpid=$!

# Run the test suite
export DISPLAY=:10
mvn -o -Pci-acceptance -Dtest=AcceptanceSuite clean test
mvn_ret=$?

# Stop the X server when finished
echo "Stopping X server"
kill $xvfbpid

# Finally return with Maven return code to tell CI
# server about the build result
exit $mvn_ret

