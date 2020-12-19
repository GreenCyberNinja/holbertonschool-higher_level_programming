#!/bin/bash
# takes url argument returns size of body
curl $1 -s -I | grep Content-length | awk '{print $2}'
