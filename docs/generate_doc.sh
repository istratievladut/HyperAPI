#!/bin/bash

set -e

export PYTHONPATH=../hyper_api

sphinx-build $1 build -c .
