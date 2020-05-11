# argovis-test
test suite that checks that argovis project is operational. Can be run as a docker container that sends email on failure, or run on Travis-CI (preferred)

## Travis-CI

Setup a cron script on Travis-CI to run run_tests.py periodically. travis.yml stores setup for Travis-CI.

## Docker test

Not currently configured. The idea is to have a docker container run the tests and email the user on a failure. The trouble is storing the password. 