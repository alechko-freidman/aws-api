#!/usr/bin/env python

## Import modules
import boto3

## Use specific profile configured by 'aws configure'
# labs = boto3.session.Session(profile_name='ci')
labs = boto3.session.Session()


res = labs.get_available_services()
print res

## Get aws client to config service
# client = boto3.client('config')
client = labs.client('ecr')

print client
