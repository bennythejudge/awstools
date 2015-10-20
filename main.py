from r53 import AWSRoute53


if __name__ == "__main__":
    # process options
    
    
    # preliminary test for changing a DNS record
    print "inside main"
    a = AWSRoute53(profile_name="mojdsd")
    zone_id = a.get_zone_id_by_name(dns_name='dsd.io')
    print zone_id
    rrs = a.list_resource_record_sets(
        zone_id,
        start_record_name='api-sandbox-adp.dsd.io.',
        start_record_type='A'
    )
    for r in rrs:
        print r
    print rrs['IsTruncated']
    my_rrs = rrs['ResourceRecordSets'][0]