def getParameter(param_name):
    """
    This function reads a secure parameter from AWS' SSM service.

    The request must be passed a valid parameter name, as well as
    temporary credentials which can be used to access the parameter.

    The parameter's value is returned.
    """
    # Create the SSM Client
    ssm_client = boto3.client('ssm',
                       region_name='ap-southeast-1'
                       )

    # Get the requested parameter
    response = ssm_client.get_parameters(
        Names=[
            param_name,
        ],
        WithDecryption=True
    )

    # Store the credentials in a variable
    credentials = response['Parameters'][0]['Value']

    return credentials


if __name__ == '__main__':
    print("SSM parameter value is :",getParameter('FirstVar'))