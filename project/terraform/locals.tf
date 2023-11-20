locals {
  region                          = "us-west-1"
  prefix                          = "acoes"
  account_id                      = "469691162657"
  kms_key_alias                   = concat("alias/", local.prefix)
  common_tags                     = { Project = "pipeline-dados" }
  names                           = ["script", "bronze", "silver", "gold"]
  buckets_name                    = [for i in local.names: concat(local.prefix, "-", i, "-", local.account_id)]
}

