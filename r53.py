import boto3
import sys
import inspect





class AWSRoute53:
    '''




    '''
    def __init__(self,profile_name,debug=1):
        '''
            open AWS session and client
        '''
        self.profile_name = profile_name;
        self.session = boto3.session.Session(profile_name=profile_name)
        self.client = self.session.client('route53')
        self.debug = debug
        if self.debug: print "DEBUG: inside %r" % sys._getframe().f_code.co_name

    def get_zone_id_by_name(self,dns_name):
        if self.debug: print "DEBUG: inside %r" % sys._getframe().f_code.co_name
        my_zone = self.client.list_hosted_zones_by_name(DNSName=dns_name)['HostedZones'][0]
        if not my_zone['Name'] == dns_name + '.':
            print "ERROR: domain {} not found".format(dns_name)
            sys.exit(1)
        # return removing the '/hostedzone/' prefix
        return my_zone['Id'].split('/hostedzone/')[1]

    def list_resource_record_sets(self,zone_id,start_record_name='',start_record_type=''):
        '''
            list resource record sets
        '''
        if self.debug: print "DEBUG: inside %r" % sys._getframe().f_code.co_name
        try:
            rrs = self.client.list_resource_record_sets(
                HostedZoneId=zone_id,
                StartRecordName=start_record_name,
                StartRecordType=start_record_type
            )
        except Exception, e:
            print "****"
            print "message: {}".format(e.response['Error']['Message'])
            print "HTTPStatusCode: {}".format(e.response['ResponseMetadata']['HTTPStatusCode'])
            print "****"
            sys.exit(1)
        return rrs

    def find_rrs_by_name_and_type(self,dns_name,rrs_name,rrs_type):
        # 1. get zone id
        zone_id = self.client.get_zone_id_by_name(dns_name)
        print "zone_id: {}".format(zone_id)
        # 2. get list of rrs for domain via zone_id
        
        # 3. search

