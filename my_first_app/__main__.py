"""A Python Pulumi program"""

import os
import pulumi
import pulumi_docker as docker

# Get configuration values
config = pulumi.Config()
frontend_port = config.require_int("frontendPort")
backend_port = config.require_int("backendPort")
mongo_port = config.require_int("mongoPort")


stack = pulumi.get_stack()

# Pull the backend image
backend_image_name = "backend"
backend = docker.RemoteImage(f"{backend_image_name}_image",
                             name="pulumi/tutorial-pulumi-fundamentals-backend:latest"
                             )

# Pull the frontend image
frontend_image_name = "frontend"
frontend = docker.RemoteImage(f"{frontend_image_name}_image",
                              name="pulumi/tutorial-pulumi-fundamentals-frontend:latest"
                              )

# Pull the MongoDB image
mongo_image = docker.RemoteImage("mongo_image",
                                 name="pulumi/tutorial-pulumi-fundamentals-database-local:latest"
                                 )