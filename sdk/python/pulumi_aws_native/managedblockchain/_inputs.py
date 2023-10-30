# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AccessorTagArgs',
    'MemberApprovalThresholdPolicyArgs',
    'MemberConfigurationArgs',
    'MemberFabricConfigurationArgs',
    'MemberFrameworkConfigurationArgs',
    'MemberNetworkConfigurationArgs',
    'MemberNetworkFabricConfigurationArgs',
    'MemberNetworkFrameworkConfigurationArgs',
    'MemberVotingPolicyArgs',
    'NodeConfigurationArgs',
]

@pulumi.input_type
class AccessorTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class MemberApprovalThresholdPolicyArgs:
    def __init__(__self__, *,
                 proposal_duration_in_hours: Optional[pulumi.Input[int]] = None,
                 threshold_comparator: Optional[pulumi.Input[str]] = None,
                 threshold_percentage: Optional[pulumi.Input[int]] = None):
        if proposal_duration_in_hours is not None:
            pulumi.set(__self__, "proposal_duration_in_hours", proposal_duration_in_hours)
        if threshold_comparator is not None:
            pulumi.set(__self__, "threshold_comparator", threshold_comparator)
        if threshold_percentage is not None:
            pulumi.set(__self__, "threshold_percentage", threshold_percentage)

    @property
    @pulumi.getter(name="proposalDurationInHours")
    def proposal_duration_in_hours(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "proposal_duration_in_hours")

    @proposal_duration_in_hours.setter
    def proposal_duration_in_hours(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "proposal_duration_in_hours", value)

    @property
    @pulumi.getter(name="thresholdComparator")
    def threshold_comparator(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "threshold_comparator")

    @threshold_comparator.setter
    def threshold_comparator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "threshold_comparator", value)

    @property
    @pulumi.getter(name="thresholdPercentage")
    def threshold_percentage(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "threshold_percentage")

    @threshold_percentage.setter
    def threshold_percentage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "threshold_percentage", value)


@pulumi.input_type
class MemberConfigurationArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 member_framework_configuration: Optional[pulumi.Input['MemberFrameworkConfigurationArgs']] = None):
        pulumi.set(__self__, "name", name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if member_framework_configuration is not None:
            pulumi.set(__self__, "member_framework_configuration", member_framework_configuration)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="memberFrameworkConfiguration")
    def member_framework_configuration(self) -> Optional[pulumi.Input['MemberFrameworkConfigurationArgs']]:
        return pulumi.get(self, "member_framework_configuration")

    @member_framework_configuration.setter
    def member_framework_configuration(self, value: Optional[pulumi.Input['MemberFrameworkConfigurationArgs']]):
        pulumi.set(self, "member_framework_configuration", value)


@pulumi.input_type
class MemberFabricConfigurationArgs:
    def __init__(__self__, *,
                 admin_password: pulumi.Input[str],
                 admin_username: pulumi.Input[str]):
        pulumi.set(__self__, "admin_password", admin_password)
        pulumi.set(__self__, "admin_username", admin_username)

    @property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "admin_password")

    @admin_password.setter
    def admin_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "admin_password", value)

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> pulumi.Input[str]:
        return pulumi.get(self, "admin_username")

    @admin_username.setter
    def admin_username(self, value: pulumi.Input[str]):
        pulumi.set(self, "admin_username", value)


@pulumi.input_type
class MemberFrameworkConfigurationArgs:
    def __init__(__self__, *,
                 member_fabric_configuration: Optional[pulumi.Input['MemberFabricConfigurationArgs']] = None):
        if member_fabric_configuration is not None:
            pulumi.set(__self__, "member_fabric_configuration", member_fabric_configuration)

    @property
    @pulumi.getter(name="memberFabricConfiguration")
    def member_fabric_configuration(self) -> Optional[pulumi.Input['MemberFabricConfigurationArgs']]:
        return pulumi.get(self, "member_fabric_configuration")

    @member_fabric_configuration.setter
    def member_fabric_configuration(self, value: Optional[pulumi.Input['MemberFabricConfigurationArgs']]):
        pulumi.set(self, "member_fabric_configuration", value)


@pulumi.input_type
class MemberNetworkConfigurationArgs:
    def __init__(__self__, *,
                 framework: pulumi.Input[str],
                 framework_version: pulumi.Input[str],
                 name: pulumi.Input[str],
                 voting_policy: pulumi.Input['MemberVotingPolicyArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 network_framework_configuration: Optional[pulumi.Input['MemberNetworkFrameworkConfigurationArgs']] = None):
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
    def framework(self) -> pulumi.Input[str]:
        return pulumi.get(self, "framework")

    @framework.setter
    def framework(self, value: pulumi.Input[str]):
        pulumi.set(self, "framework", value)

    @property
    @pulumi.getter(name="frameworkVersion")
    def framework_version(self) -> pulumi.Input[str]:
        return pulumi.get(self, "framework_version")

    @framework_version.setter
    def framework_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "framework_version", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="votingPolicy")
    def voting_policy(self) -> pulumi.Input['MemberVotingPolicyArgs']:
        return pulumi.get(self, "voting_policy")

    @voting_policy.setter
    def voting_policy(self, value: pulumi.Input['MemberVotingPolicyArgs']):
        pulumi.set(self, "voting_policy", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="networkFrameworkConfiguration")
    def network_framework_configuration(self) -> Optional[pulumi.Input['MemberNetworkFrameworkConfigurationArgs']]:
        return pulumi.get(self, "network_framework_configuration")

    @network_framework_configuration.setter
    def network_framework_configuration(self, value: Optional[pulumi.Input['MemberNetworkFrameworkConfigurationArgs']]):
        pulumi.set(self, "network_framework_configuration", value)


@pulumi.input_type
class MemberNetworkFabricConfigurationArgs:
    def __init__(__self__, *,
                 edition: pulumi.Input[str]):
        pulumi.set(__self__, "edition", edition)

    @property
    @pulumi.getter
    def edition(self) -> pulumi.Input[str]:
        return pulumi.get(self, "edition")

    @edition.setter
    def edition(self, value: pulumi.Input[str]):
        pulumi.set(self, "edition", value)


@pulumi.input_type
class MemberNetworkFrameworkConfigurationArgs:
    def __init__(__self__, *,
                 network_fabric_configuration: Optional[pulumi.Input['MemberNetworkFabricConfigurationArgs']] = None):
        if network_fabric_configuration is not None:
            pulumi.set(__self__, "network_fabric_configuration", network_fabric_configuration)

    @property
    @pulumi.getter(name="networkFabricConfiguration")
    def network_fabric_configuration(self) -> Optional[pulumi.Input['MemberNetworkFabricConfigurationArgs']]:
        return pulumi.get(self, "network_fabric_configuration")

    @network_fabric_configuration.setter
    def network_fabric_configuration(self, value: Optional[pulumi.Input['MemberNetworkFabricConfigurationArgs']]):
        pulumi.set(self, "network_fabric_configuration", value)


@pulumi.input_type
class MemberVotingPolicyArgs:
    def __init__(__self__, *,
                 approval_threshold_policy: Optional[pulumi.Input['MemberApprovalThresholdPolicyArgs']] = None):
        if approval_threshold_policy is not None:
            pulumi.set(__self__, "approval_threshold_policy", approval_threshold_policy)

    @property
    @pulumi.getter(name="approvalThresholdPolicy")
    def approval_threshold_policy(self) -> Optional[pulumi.Input['MemberApprovalThresholdPolicyArgs']]:
        return pulumi.get(self, "approval_threshold_policy")

    @approval_threshold_policy.setter
    def approval_threshold_policy(self, value: Optional[pulumi.Input['MemberApprovalThresholdPolicyArgs']]):
        pulumi.set(self, "approval_threshold_policy", value)


@pulumi.input_type
class NodeConfigurationArgs:
    def __init__(__self__, *,
                 availability_zone: pulumi.Input[str],
                 instance_type: pulumi.Input[str]):
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "instance_type", instance_type)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Input[str]:
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)


