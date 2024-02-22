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
    'MemberApprovalThresholdPolicy',
    'MemberConfiguration',
    'MemberFabricConfiguration',
    'MemberFrameworkConfiguration',
    'MemberNetworkConfiguration',
    'MemberNetworkFabricConfiguration',
    'MemberNetworkFrameworkConfiguration',
    'MemberVotingPolicy',
    'NodeConfiguration',
]

@pulumi.output_type
class MemberApprovalThresholdPolicy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "proposalDurationInHours":
            suggest = "proposal_duration_in_hours"
        elif key == "thresholdComparator":
            suggest = "threshold_comparator"
        elif key == "thresholdPercentage":
            suggest = "threshold_percentage"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MemberApprovalThresholdPolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MemberApprovalThresholdPolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MemberApprovalThresholdPolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 proposal_duration_in_hours: Optional[int] = None,
                 threshold_comparator: Optional[str] = None,
                 threshold_percentage: Optional[int] = None):
        if proposal_duration_in_hours is not None:
            pulumi.set(__self__, "proposal_duration_in_hours", proposal_duration_in_hours)
        if threshold_comparator is not None:
            pulumi.set(__self__, "threshold_comparator", threshold_comparator)
        if threshold_percentage is not None:
            pulumi.set(__self__, "threshold_percentage", threshold_percentage)

    @property
    @pulumi.getter(name="proposalDurationInHours")
    def proposal_duration_in_hours(self) -> Optional[int]:
        return pulumi.get(self, "proposal_duration_in_hours")

    @property
    @pulumi.getter(name="thresholdComparator")
    def threshold_comparator(self) -> Optional[str]:
        return pulumi.get(self, "threshold_comparator")

    @property
    @pulumi.getter(name="thresholdPercentage")
    def threshold_percentage(self) -> Optional[int]:
        return pulumi.get(self, "threshold_percentage")


@pulumi.output_type
class MemberConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "memberFrameworkConfiguration":
            suggest = "member_framework_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MemberConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MemberConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MemberConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 description: Optional[str] = None,
                 member_framework_configuration: Optional['outputs.MemberFrameworkConfiguration'] = None):
        pulumi.set(__self__, "name", name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if member_framework_configuration is not None:
            pulumi.set(__self__, "member_framework_configuration", member_framework_configuration)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="memberFrameworkConfiguration")
    def member_framework_configuration(self) -> Optional['outputs.MemberFrameworkConfiguration']:
        return pulumi.get(self, "member_framework_configuration")


@pulumi.output_type
class MemberFabricConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "adminPassword":
            suggest = "admin_password"
        elif key == "adminUsername":
            suggest = "admin_username"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MemberFabricConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MemberFabricConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MemberFabricConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 admin_password: str,
                 admin_username: str):
        pulumi.set(__self__, "admin_password", admin_password)
        pulumi.set(__self__, "admin_username", admin_username)

    @property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> str:
        return pulumi.get(self, "admin_password")

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> str:
        return pulumi.get(self, "admin_username")


@pulumi.output_type
class MemberFrameworkConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "memberFabricConfiguration":
            suggest = "member_fabric_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MemberFrameworkConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MemberFrameworkConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MemberFrameworkConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 member_fabric_configuration: Optional['outputs.MemberFabricConfiguration'] = None):
        if member_fabric_configuration is not None:
            pulumi.set(__self__, "member_fabric_configuration", member_fabric_configuration)

    @property
    @pulumi.getter(name="memberFabricConfiguration")
    def member_fabric_configuration(self) -> Optional['outputs.MemberFabricConfiguration']:
        return pulumi.get(self, "member_fabric_configuration")


@pulumi.output_type
class MemberNetworkConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "frameworkVersion":
            suggest = "framework_version"
        elif key == "votingPolicy":
            suggest = "voting_policy"
        elif key == "networkFrameworkConfiguration":
            suggest = "network_framework_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MemberNetworkConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MemberNetworkConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MemberNetworkConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 framework: str,
                 framework_version: str,
                 name: str,
                 voting_policy: 'outputs.MemberVotingPolicy',
                 description: Optional[str] = None,
                 network_framework_configuration: Optional['outputs.MemberNetworkFrameworkConfiguration'] = None):
        pulumi.set(__self__, "framework", framework)
        pulumi.set(__self__, "framework_version", framework_version)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "voting_policy", voting_policy)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if network_framework_configuration is not None:
            pulumi.set(__self__, "network_framework_configuration", network_framework_configuration)

    @property
    @pulumi.getter
    def framework(self) -> str:
        return pulumi.get(self, "framework")

    @property
    @pulumi.getter(name="frameworkVersion")
    def framework_version(self) -> str:
        return pulumi.get(self, "framework_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="votingPolicy")
    def voting_policy(self) -> 'outputs.MemberVotingPolicy':
        return pulumi.get(self, "voting_policy")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="networkFrameworkConfiguration")
    def network_framework_configuration(self) -> Optional['outputs.MemberNetworkFrameworkConfiguration']:
        return pulumi.get(self, "network_framework_configuration")


@pulumi.output_type
class MemberNetworkFabricConfiguration(dict):
    def __init__(__self__, *,
                 edition: str):
        pulumi.set(__self__, "edition", edition)

    @property
    @pulumi.getter
    def edition(self) -> str:
        return pulumi.get(self, "edition")


@pulumi.output_type
class MemberNetworkFrameworkConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "networkFabricConfiguration":
            suggest = "network_fabric_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MemberNetworkFrameworkConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MemberNetworkFrameworkConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MemberNetworkFrameworkConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 network_fabric_configuration: Optional['outputs.MemberNetworkFabricConfiguration'] = None):
        if network_fabric_configuration is not None:
            pulumi.set(__self__, "network_fabric_configuration", network_fabric_configuration)

    @property
    @pulumi.getter(name="networkFabricConfiguration")
    def network_fabric_configuration(self) -> Optional['outputs.MemberNetworkFabricConfiguration']:
        return pulumi.get(self, "network_fabric_configuration")


@pulumi.output_type
class MemberVotingPolicy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "approvalThresholdPolicy":
            suggest = "approval_threshold_policy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MemberVotingPolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MemberVotingPolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MemberVotingPolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 approval_threshold_policy: Optional['outputs.MemberApprovalThresholdPolicy'] = None):
        if approval_threshold_policy is not None:
            pulumi.set(__self__, "approval_threshold_policy", approval_threshold_policy)

    @property
    @pulumi.getter(name="approvalThresholdPolicy")
    def approval_threshold_policy(self) -> Optional['outputs.MemberApprovalThresholdPolicy']:
        return pulumi.get(self, "approval_threshold_policy")


@pulumi.output_type
class NodeConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "availabilityZone":
            suggest = "availability_zone"
        elif key == "instanceType":
            suggest = "instance_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NodeConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NodeConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NodeConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 availability_zone: str,
                 instance_type: str):
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "instance_type", instance_type)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> str:
        return pulumi.get(self, "instance_type")


