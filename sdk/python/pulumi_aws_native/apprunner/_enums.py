# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ObservabilityConfigurationTraceConfigurationVendor',
    'ServiceCodeConfigurationConfigurationSource',
    'ServiceCodeConfigurationValuesRuntime',
    'ServiceEgressConfigurationEgressType',
    'ServiceHealthCheckConfigurationProtocol',
    'ServiceImageRepositoryImageRepositoryType',
    'ServiceNetworkConfigurationIpAddressType',
    'ServiceSourceCodeVersionType',
    'VpcIngressConnectionStatus',
]


class ObservabilityConfigurationTraceConfigurationVendor(str, Enum):
    """
    The implementation provider chosen for tracing App Runner services.
    """
    AWSXRAY = "AWSXRAY"


class ServiceCodeConfigurationConfigurationSource(str, Enum):
    """
    Configuration Source
    """
    REPOSITORY = "REPOSITORY"
    API = "API"


class ServiceCodeConfigurationValuesRuntime(str, Enum):
    """
    Runtime
    """
    PYTHON3 = "PYTHON_3"
    NODEJS12 = "NODEJS_12"
    NODEJS14 = "NODEJS_14"
    CORRETTO8 = "CORRETTO_8"
    CORRETTO11 = "CORRETTO_11"
    NODEJS16 = "NODEJS_16"
    GO1 = "GO_1"
    DOTNET6 = "DOTNET_6"
    PHP81 = "PHP_81"
    RUBY31 = "RUBY_31"
    PYTHON311 = "PYTHON_311"
    NODEJS18 = "NODEJS_18"


class ServiceEgressConfigurationEgressType(str, Enum):
    """
    Network egress type.
    """
    DEFAULT = "DEFAULT"
    VPC = "VPC"


class ServiceHealthCheckConfigurationProtocol(str, Enum):
    """
    Health Check Protocol
    """
    TCP = "TCP"
    HTTP = "HTTP"


class ServiceImageRepositoryImageRepositoryType(str, Enum):
    """
    Image Repository Type
    """
    ECR = "ECR"
    ECR_PUBLIC = "ECR_PUBLIC"


class ServiceNetworkConfigurationIpAddressType(str, Enum):
    """
    App Runner service endpoint IP address type
    """
    IPV4 = "IPV4"
    DUAL_STACK = "DUAL_STACK"


class ServiceSourceCodeVersionType(str, Enum):
    """
    Source Code Version Type
    """
    BRANCH = "BRANCH"


class VpcIngressConnectionStatus(str, Enum):
    """
    The current status of the VpcIngressConnection.
    """
    AVAILABLE = "AVAILABLE"
    PENDING_CREATION = "PENDING_CREATION"
    PENDING_UPDATE = "PENDING_UPDATE"
    PENDING_DELETION = "PENDING_DELETION"
    FAILED_CREATION = "FAILED_CREATION"
    FAILED_UPDATE = "FAILED_UPDATE"
    FAILED_DELETION = "FAILED_DELETION"
    DELETED = "DELETED"
