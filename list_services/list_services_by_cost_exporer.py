#!/usr/bin/env python

## Import modules
import boto3
import datetime
# import pprint

## Globals
# pp = pprint.PrettyPrinter(indent=4)

## Retrieve all (ec2) regions
ec2 = boto3.client('ec2')
response = ec2.describe_regions()
regions = sorted([region['RegionName'] for region in response['Regions'] ])

print ("Available regions are:\n")
for r in regions:
    print r
# print ("Please enter region: ")
region=raw_input("\nPlease enter region: ")

## Get session per profile
session = boto3.session.Session(profile_name='ci')

## Create aws client to config service
client = session.client('ce')

today = datetime.date.today()
yesterday = today - datetime.timedelta(1)

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': str(yesterday),
        'End': str(today)},
    Granularity='DAILY',
    Metrics=['AmortizedCost'],
    GroupBy=[
        {
            'Type': 'DIMENSION',
            'Key': 'SERVICE'
        }
    ],
    Filter={
        'Dimensions': {
            'Key':'REGION',
            'Values': [
                region,
            ]
        }
    }

)

print ("The following services are in use in region %s:\n" % (region))
for service in response["ResultsByTime"][0]["Groups"]:
    print (service['Keys'][0])

