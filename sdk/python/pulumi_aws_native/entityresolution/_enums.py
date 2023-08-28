# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'MatchingWorkflowResolutionTechniquesResolutionType',
    'MatchingWorkflowRuleBasedPropertiesAttributeMatchingModel',
    'SchemaMappingSchemaAttributeType',
]


class MatchingWorkflowResolutionTechniquesResolutionType(str, Enum):
    RULE_MATCHING = "RULE_MATCHING"
    ML_MATCHING = "ML_MATCHING"


class MatchingWorkflowRuleBasedPropertiesAttributeMatchingModel(str, Enum):
    ONE_TO_ONE = "ONE_TO_ONE"
    MANY_TO_MANY = "MANY_TO_MANY"


class SchemaMappingSchemaAttributeType(str, Enum):
    NAME = "NAME"
    NAME_FIRST = "NAME_FIRST"
    NAME_MIDDLE = "NAME_MIDDLE"
    NAME_LAST = "NAME_LAST"
    ADDRESS = "ADDRESS"
    ADDRESS_STREET1 = "ADDRESS_STREET1"
    ADDRESS_STREET2 = "ADDRESS_STREET2"
    ADDRESS_STREET3 = "ADDRESS_STREET3"
    ADDRESS_CITY = "ADDRESS_CITY"
    ADDRESS_STATE = "ADDRESS_STATE"
    ADDRESS_COUNTRY = "ADDRESS_COUNTRY"
    ADDRESS_POSTALCODE = "ADDRESS_POSTALCODE"
    PHONE = "PHONE"
    PHONE_NUMBER = "PHONE_NUMBER"
    PHONE_COUNTRYCODE = "PHONE_COUNTRYCODE"
    EMAIL_ADDRESS = "EMAIL_ADDRESS"
    UNIQUE_ID = "UNIQUE_ID"
    DATE = "DATE"
    STRING = "STRING"
