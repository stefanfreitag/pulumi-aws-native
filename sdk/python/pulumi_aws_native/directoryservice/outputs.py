# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'MicrosoftAdVpcSettings',
    'SimpleAdVpcSettings',
]

@pulumi.output_type
class MicrosoftAdVpcSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetIds":
            suggest = "subnet_ids"
        elif key == "vpcId":
            suggest = "vpc_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MicrosoftAdVpcSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MicrosoftAdVpcSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MicrosoftAdVpcSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_ids: Sequence[str],
                 vpc_id: str):
        MicrosoftAdVpcSettings._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             subnet_ids: Sequence[str],
             vpc_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("subnet_ids", subnet_ids)
        _setter("vpc_id", vpc_id)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        return pulumi.get(self, "vpc_id")


@pulumi.output_type
class SimpleAdVpcSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetIds":
            suggest = "subnet_ids"
        elif key == "vpcId":
            suggest = "vpc_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SimpleAdVpcSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SimpleAdVpcSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SimpleAdVpcSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_ids: Sequence[str],
                 vpc_id: str):
        """
        :param Sequence[str] subnet_ids: The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.
        :param str vpc_id: The identifier of the VPC in which to create the directory.
        """
        SimpleAdVpcSettings._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             subnet_ids: Sequence[str],
             vpc_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("subnet_ids", subnet_ids)
        _setter("vpc_id", vpc_id)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The identifier of the VPC in which to create the directory.
        """
        return pulumi.get(self, "vpc_id")


