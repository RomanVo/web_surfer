#!/bin/sh

if [ ! -d e2evenv ];
then
       virtualenv e2evenv
   fi
   . e2evenv/bin/activate && \
       pip install -U -r requirements.txt
