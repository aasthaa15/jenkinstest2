#!/usr/bin/python3
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for aastha in response['Reservations']:
	for sarthak in aastha['Instances']:
		print(sarthak['InstanceId'] + ":" + sarthak['Placement']['AvailabilityZone'])

