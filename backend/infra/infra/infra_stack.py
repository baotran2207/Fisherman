from aws_cdk import (
    # Duration,
    DockerImageAssetSource,
    Stack,
    aws_lambda ,
    aws_apigatewayv2 as apig,
    aws_apigatewayv2_integrations  as api_integration,
    # aws_sqs as sqs,
    aws_ecr
)


from constructs import Construct
from pathlib import Path
parent_path = Path().resolve().parent

AWS_LAMBDA_DOCKER_FILE = 'Dockerfile.aws.lambda'
APP_PATH = f"{parent_path}/fisherman"

print(APP_PATH)
class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ## lambda <- apigateway

        lambda_helo_world = aws_lambda.DockerImageFunction(
            self, 'fishermand-hello_world',
            function_name='fisherman-hello_world',
            code= aws_lambda.DockerImageCode.from_image_asset(
                file=AWS_LAMBDA_DOCKER_FILE,
                directory=APP_PATH
            )
        )


        hello_integration = api_integration.HttpLambdaIntegration()