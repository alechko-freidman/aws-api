#!/usr/bin/env python

## Import modules
import boto3
import pprint

## Globals
pp = pprint.PrettyPrinter(indent=4)
resourceTypes = ['AWS::EC2::CustomerGateway','AWS::EC2::EIP','AWS::EC2::Host','AWS::EC2::Instance','AWS::EC2::InternetGateway','AWS::EC2::NetworkAcl','AWS::EC2::NetworkInterface','AWS::EC2::RouteTable','AWS::EC2::SecurityGroup','AWS::EC2::Subnet','AWS::CloudTrail::Trail','AWS::EC2::Volume','AWS::EC2::VPC','AWS::EC2::VPNConnection','AWS::EC2::VPNGateway','AWS::IAM::Group','AWS::IAM::Policy','AWS::IAM::Role','AWS::IAM::User','AWS::ACM::Certificate','AWS::RDS::DBInstance','AWS::RDS::DBSubnetGroup','AWS::RDS::DBSecurityGroup','AWS::RDS::DBSnapshot','AWS::RDS::EventSubscription','AWS::ElasticLoadBalancingV2::LoadBalancer','AWS::S3::Bucket','AWS::SSM::ManagedInstanceInventory','AWS::Redshift::Cluster','AWS::Redshift::ClusterSnapshot','AWS::Redshift::ClusterParameterGroup','AWS::Redshift::ClusterSecurityGroup','AWS::Redshift::ClusterSubnetGroup','AWS::Redshift::EventSubscription','AWS::CloudWatch::Alarm','AWS::CloudFormation::Stack','AWS::DynamoDB::Table','AWS::AutoScaling::AutoScalingGroup','AWS::AutoScaling::LaunchConfiguration','AWS::AutoScaling::ScalingPolicy','AWS::AutoScaling::ScheduledAction','AWS::CodeBuild::Project','AWS::WAF::RateBasedRule','AWS::WAF::Rule','AWS::WAF::WebACL','AWS::WAFRegional::RateBasedRule','AWS::WAFRegional::Rule','AWS::WAFRegional::WebACL','AWS::CloudFront::Distribution','AWS::CloudFront::StreamingDistribution','AWS::WAF::RuleGroup','AWS::WAFRegional::RuleGroup','AWS::Lambda::Function','AWS::ElasticBeanstalk::Application','AWS::ElasticBeanstalk::ApplicationVersion','AWS::ElasticBeanstalk::Environment','AWS::ElasticLoadBalancing::LoadBalancer','AWS::XRay::EncryptionConfig']

## Retrieve all (ec2) regions
ec2 = boto3.client('ec2')
response = ec2.describe_regions()
regions = sorted([region['RegionName'] for region in response['Regions'] ])

print ("Available regions are:\n")
for r in regions:
    print r
# print ("Please enter region: ")
region=raw_input("\nPlease enter region: ")

## Use specific profile configured by 'aws configure'
# session = boto3.session.Session(profile_name='labs', region_name=region)
session = boto3.session.Session(region_name=region)

## Create aws client to config service
config = session.client('config')

## Iterate over all resourceTypes
for res_type in resourceTypes:
    ## Create Paginator
    paginator = config.get_paginator('list_discovered_resources')
    ## Create a PageIterator from the Paginator
    page_iterator = paginator.paginate(resourceType=res_type)
    ## List of all resources, in case of multiple pages
    all_resources = []
    for page in page_iterator:
        # response = config.list_discovered_resources(
        #     resourceType=res_type
        # )
        resources = page['resourceIdentifiers']
        all_resources += resources
    ## Now we have all resources, print them
    num_resources = len(all_resources)
    if num_resources != 0:
        print "---> There are %d Resources in %s ResourceType" % (num_resources, res_type)
        for res in all_resources:
            pp.pprint(res)
    # else:
    #     print("---> There are NO resources in %s ResourceType" % (res_type))
    # print response
