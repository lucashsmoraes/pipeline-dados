locals {
  region                          = "us-west-1"
  prefix                          = "acoes"
  account_id                      = "469691162657"
  kms_key_alias                   = "alias/${local.prefix}"
  common_tags                     = { Project = "pipeline-dados" }
  names                           = ["script", "bronze", "silver", "gold"]
  buckets_name                    = [for i in local.names: format("bucket-%s-%s-%s", local.prefix, i, local.account_id)]
  teste = tolist(local.buckets_name)
}

