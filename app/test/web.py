#!/usr/bin/bash

import requests, sys

r = requests.get(sys.argv[1])
if r.status_code == 200:
    print "SUCCESS"
    sys.exit(0)
print "FAILED"
sys.exit(1)

