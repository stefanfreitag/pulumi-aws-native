# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DatasetGroupDomain',
    'DatasetType',
    'SchemaDomain',
    'SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesType',
]


class DatasetGroupDomain(str, Enum):
    """
    The domain of a Domain dataset group.
    """
    ECOMMERCE = "ECOMMERCE"
    VIDEO_ON_DEMAND = "VIDEO_ON_DEMAND"


class DatasetType(str, Enum):
    """
    The type of dataset
    """
    INTERACTIONS = "Interactions"
    ITEMS = "Items"
    USERS = "Users"


class SchemaDomain(str, Enum):
    """
    The domain of a Domain dataset group.
    """
    ECOMMERCE = "ECOMMERCE"
    VIDEO_ON_DEMAND = "VIDEO_ON_DEMAND"


class SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesType(str, Enum):
    """
    The type of the metric. Valid values are Maximize and Minimize.
    """
    MAXIMIZE = "Maximize"
    MINIMIZE = "Minimize"
