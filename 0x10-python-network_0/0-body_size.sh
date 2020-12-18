#!/bin/bash
# takes url argument returns size of body
curl $1 -s | wc -c
