"""A Python Pulumi program"""

import os
import pulumi
import pulumi_docker as docker

stack = pulumi.get_stack()

# Pull the backend image
backend_image_name = "backend"
backend = docker.RemoteImage(f"{backend_image_name}_image",
                             name="pulumi/tutorial-pulumi-fundamentals-backend:latest"
                             )