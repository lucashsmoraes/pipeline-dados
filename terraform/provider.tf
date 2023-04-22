terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
    random = {
      source = "hashicorp/random"
    }
  }

  cloud {
    organization = "TCC-PIPLINE"

    workspaces {
      name = "WORKSPACE"
    }
  }
}