#!/bin/bash

if [ $# -eq 0 ]
  then
    poetry run flask --app app run
fi

if [[ $* == *--debug* || $* == *-d* ]]
    then
        poetry run flask --app app run --debug
fi
