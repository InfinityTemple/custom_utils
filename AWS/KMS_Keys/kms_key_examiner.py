import boto3
from datetime import datetime, timezone

def list_kms_key_grants():
    kms_client = boto3.client('kms')
    keys = kms_client.list_keys()['Keys']
    grants_data = []

    for key in keys:
        key_id = key['KeyId']
        grants = kms_client.list_grants(KeyId=key_id)['Grants']
        
        for grant in grants:
            grant_id = grant['GrantId']
            grant_name = grant.get('Name', 'N/A')
            grantee_principal = grant['GranteePrincipal']
            creation_date = grant['CreationDate']
            last_used_date = 'N/A'

            # Fetch additional metadata, such as last used date if available
            grant_details = kms_client.describe_key(KeyId=key_id)
            if 'KeyMetadata' in grant_details and 'LastUsedDate' in grant_details['KeyMetadata']:
                last_used_date = grant_details['KeyMetadata']['LastUsedDate']

            grant_info = {
                'KeyId': key_id,
                'GrantId': grant_id,
                'GrantName': grant_name,
                'GranteePrincipal': grantee_principal,
                'CreationDate': creation_date,
                'LastUsedDate': last_used_date
            }
            grants_data.append(grant_info)

    return grants_data

def main():
    grants_data = list_kms_key_grants()
    for grant in grants_data:
        print(f"KeyId: {grant['KeyId']}, GrantId: {grant['GrantId']}, GrantName: {grant['GrantName']}, "
              f"GranteePrincipal: {grant['GranteePrincipal']}, CreationDate: {grant['CreationDate']}, "
              f"LastUsedDate: {grant['LastUsedDate']}")

if __name__ == '__main__':
    main()