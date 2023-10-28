import boto3
import argparse
ssm = boto3.client('ssm')

parser - argparse.ArgumentParser()
parser.add_argument("--parameter", type = str, required=True)
parser.add_argument("--decrypt, type = str, required=False)
args = parser.parse_args()

def get_parameter(name, decrypt):
    if decrypt == 'True':
        decrypt = True
    else:
        decrypt = False
    parameter = ssm.get_parameter(Name=name, WithDecryption=decrypt)
    return(parameter['Parameter']['Value'])
    
def main():
    parameter_name = args.parameter
    decrypt = args.decrypt
    parameter=get_parameter(parameter_name, decrypt)
    print("@@Result=" + str(parameter))
    
if _name_ == '__main__':
    main()
