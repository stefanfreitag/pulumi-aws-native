# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EnvironmentAccountConnectionStatus',
    'EnvironmentTemplateProvisioning',
    'ServiceTemplateProvisioning',
]


class EnvironmentAccountConnectionStatus(str, Enum):
    PENDING = "PENDING"
    CONNECTED = "CONNECTED"
    REJECTED = "REJECTED"


class EnvironmentTemplateProvisioning(str, Enum):
    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"


class ServiceTemplateProvisioning(str, Enum):
    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"
