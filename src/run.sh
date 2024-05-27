#!/bin/bash

if [ $# -eq 0 ]
  then
    poetry run flask --app krouth_site/app run
fi

if [[ $* == *--debug* || $* == *-d* ]]
    then
        poetry run flask --app krouth_site/app run --debug
fi
