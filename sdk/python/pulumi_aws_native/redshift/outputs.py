# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'ClusterEndpoint',
    'ClusterLoggingProperties',
    'ClusterParameterGroupParameter',
    'EndpointAccessNetworkInterface',
    'EndpointAccessVpcSecurityGroup',
    'ScheduledActionType',
    'VpcEndpointProperties',
]

@pulumi.output_type
class ClusterEndpoint(dict):
    def __init__(__self__, *,
                 address: Optional[str] = None,
                 port: Optional[str] = None):
        if address is not None:
            pulumi.set(__self__, "address", address)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        return pulumi.get(self, "port")


@pulumi.output_type
class ClusterLoggingProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bucketName":
            suggest = "bucket_name"
        elif key == "s3KeyPrefix":
            suggest = "s3_key_prefix"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterLoggingProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterLoggingProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterLoggingProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket_name: Optional[str] = None,
                 s3_key_prefix: Optional[str] = None):
        if bucket_name is not None:
            pulumi.set(__self__, "bucket_name", bucket_name)
        if s3_key_prefix is not None:
            pulumi.set(__self__, "s3_key_prefix", s3_key_prefix)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[str]:
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[str]:
        return pulumi.get(self, "s3_key_prefix")


@pulumi.output_type
class ClusterParameterGroupParameter(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "parameterName":
            suggest = "parameter_name"
        elif key == "parameterValue":
            suggest = "parameter_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterParameterGroupParameter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterParameterGroupParameter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterParameterGroupParameter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 parameter_name: str,
                 parameter_value: str):
        """
        :param str parameter_name: The name of the parameter.
        :param str parameter_value: The value of the parameter. If `ParameterName` is `wlm_json_configuration`, then the maximum size of `ParameterValue` is 8000 characters.
        """
        pulumi.set(__self__, "parameter_name", parameter_name)
        pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> str:
        """
        The name of the parameter.
        """
        return pulumi.get(self, "parameter_name")

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> str:
        """
        The value of the parameter. If `ParameterName` is `wlm_json_configuration`, then the maximum size of `ParameterValue` is 8000 characters.
        """
        return pulumi.get(self, "parameter_value")


@pulumi.output_type
class EndpointAccessNetworkInterface(dict):
    """
    Describes a network interface.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "availabilityZone":
            suggest = "availability_zone"
        elif key == "networkInterfaceId":
            suggest = "network_interface_id"
        elif key == "privateIpAddress":
            suggest = "private_ip_address"
        elif key == "subnetId":
            suggest = "subnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointAccessNetworkInterface. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointAccessNetworkInterface.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointAccessNetworkInterface.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 availability_zone: Optional[str] = None,
                 network_interface_id: Optional[str] = None,
                 private_ip_address: Optional[str] = None,
                 subnet_id: Optional[str] = None):
        """
        Describes a network interface.
        :param str availability_zone: The Availability Zone.
        :param str network_interface_id: The network interface identifier.
        :param str private_ip_address: The IPv4 address of the network interface within the subnet.
        :param str subnet_id: The subnet identifier.
        """
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if network_interface_id is not None:
            pulumi.set(__self__, "network_interface_id", network_interface_id)
        if private_ip_address is not None:
            pulumi.set(__self__, "private_ip_address", private_ip_address)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        """
        The Availability Zone.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[str]:
        """
        The network interface identifier.
        """
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[str]:
        """
        The IPv4 address of the network interface within the subnet.
        """
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[str]:
        """
        The subnet identifier.
        """
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class EndpointAccessVpcSecurityGroup(dict):
    """
    Describes the members of a VPC security group.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "vpcSecurityGroupId":
            suggest = "vpc_security_group_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointAccessVpcSecurityGroup. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointAccessVpcSecurityGroup.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointAccessVpcSecurityGroup.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 status: Optional[str] = None,
                 vpc_security_group_id: Optional[str] = None):
        """
        Describes the members of a VPC security group.
        :param str status: The status of the VPC security group.
        :param str vpc_security_group_id: The identifier of the VPC security group.
        """
        if status is not None:
            pulumi.set(__self__, "status", status)
        if vpc_security_group_id is not None:
            pulumi.set(__self__, "vpc_security_group_id", vpc_security_group_id)

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the VPC security group.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcSecurityGroupId")
    def vpc_security_group_id(self) -> Optional[str]:
        """
        The identifier of the VPC security group.
        """
        return pulumi.get(self, "vpc_security_group_id")


@pulumi.output_type
class ScheduledActionType(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class VpcEndpointProperties(dict):
    """
    The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "networkInterfaces":
            suggest = "network_interfaces"
        elif key == "vpcEndpointId":
            suggest = "vpc_endpoint_id"
        elif key == "vpcId":
            suggest = "vpc_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VpcEndpointProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VpcEndpointProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VpcEndpointProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 network_interfaces: Optional[Sequence['outputs.EndpointAccessNetworkInterface']] = None,
                 vpc_endpoint_id: Optional[str] = None,
                 vpc_id: Optional[str] = None):
        """
        The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.
        :param Sequence['EndpointAccessNetworkInterface'] network_interfaces: One or more network interfaces of the endpoint. Also known as an interface endpoint.
        :param str vpc_endpoint_id: The connection endpoint ID for connecting an Amazon Redshift cluster through the proxy.
        :param str vpc_id: The VPC identifier that the endpoint is associated.
        """
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if vpc_endpoint_id is not None:
            pulumi.set(__self__, "vpc_endpoint_id", vpc_endpoint_id)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence['outputs.EndpointAccessNetworkInterface']]:
        """
        One or more network interfaces of the endpoint. Also known as an interface endpoint.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[str]:
        """
        The connection endpoint ID for connecting an Amazon Redshift cluster through the proxy.
        """
        return pulumi.get(self, "vpc_endpoint_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        """
        The VPC identifier that the endpoint is associated.
        """
        return pulumi.get(self, "vpc_id")


