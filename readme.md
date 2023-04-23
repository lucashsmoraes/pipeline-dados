## Criando pipeline de dados com glue

### Pre-requisito

* Conta github
* Conta app.terraform
* Conta AWS
* Experiência em terraform
* Experiência em github Actions
* Experiência em AWS

### Como configurar Terraform com GitHub

* configuração: https://developer.hashicorp.com/terraform/tutorials/automation/github-actions

### Como configurar provider AWS

* configuração: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
    * Exemplo:
      ```json 
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
                organization = "<organization app.terraform>"
            
                workspaces {
                  name = "<workspace app.terraform>"
                }
              }
            }
            provider "aws" {
              region = "us-east-1"
            }
      ```

