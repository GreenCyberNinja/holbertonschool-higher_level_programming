#!/bin/bash
# takes url argument returns size of body
curl -sI "$1"| grep Content-Length | awk '{print $2}'
