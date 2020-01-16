#!/usr/bin/env bash

for i in {0..100}; do echo $i;  echo '%'$i'$s' | ./format-0 ; done;
