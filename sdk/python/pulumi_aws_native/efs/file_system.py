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
from ._inputs import *

__all__ = ['FileSystemArgs', 'FileSystem']

@pulumi.input_type
class FileSystemArgs:
    def __init__(__self__, *,
                 availability_zone_name: Optional[pulumi.Input[str]] = None,
                 backup_policy: Optional[pulumi.Input['FileSystemBackupPolicyArgs']] = None,
                 bypass_policy_lockout_safety_check: Optional[pulumi.Input[bool]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 file_system_policy: Optional[Any] = None,
                 file_system_tags: Optional[pulumi.Input[Sequence[pulumi.Input['FileSystemElasticFileSystemTagArgs']]]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 lifecycle_policies: Optional[pulumi.Input[Sequence[pulumi.Input['FileSystemLifecyclePolicyArgs']]]] = None,
                 performance_mode: Optional[pulumi.Input[str]] = None,
                 provisioned_throughput_in_mibps: Optional[pulumi.Input[float]] = None,
                 replication_configuration: Optional[pulumi.Input['FileSystemReplicationConfigurationArgs']] = None,
                 throughput_mode: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FileSystem resource.
        :param pulumi.Input[bool] bypass_policy_lockout_safety_check: Whether to bypass the FileSystemPolicy lockout safety check. The policy lockout safety check determines whether the policy in the request will prevent the principal making the request to be locked out from making future PutFileSystemPolicy requests on the file system. Set BypassPolicyLockoutSafetyCheck to True only when you intend to prevent the principal that is making the request from making a subsequent PutFileSystemPolicy request on the file system. Defaults to false
        """
        if availability_zone_name is not None:
            pulumi.set(__self__, "availability_zone_name", availability_zone_name)
        if backup_policy is not None:
            pulumi.set(__self__, "backup_policy", backup_policy)
        if bypass_policy_lockout_safety_check is not None:
            pulumi.set(__self__, "bypass_policy_lockout_safety_check", bypass_policy_lockout_safety_check)
        if encrypted is not None:
            pulumi.set(__self__, "encrypted", encrypted)
        if file_system_policy is not None:
            pulumi.set(__self__, "file_system_policy", file_system_policy)
        if file_system_tags is not None:
            pulumi.set(__self__, "file_system_tags", file_system_tags)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if lifecycle_policies is not None:
            pulumi.set(__self__, "lifecycle_policies", lifecycle_policies)
        if performance_mode is not None:
            pulumi.set(__self__, "performance_mode", performance_mode)
        if provisioned_throughput_in_mibps is not None:
            pulumi.set(__self__, "provisioned_throughput_in_mibps", provisioned_throughput_in_mibps)
        if replication_configuration is not None:
            pulumi.set(__self__, "replication_configuration", replication_configuration)
        if throughput_mode is not None:
            pulumi.set(__self__, "throughput_mode", throughput_mode)

    @property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "availability_zone_name")

    @availability_zone_name.setter
    def availability_zone_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone_name", value)

    @property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> Optional[pulumi.Input['FileSystemBackupPolicyArgs']]:
        return pulumi.get(self, "backup_policy")

    @backup_policy.setter
    def backup_policy(self, value: Optional[pulumi.Input['FileSystemBackupPolicyArgs']]):
        pulumi.set(self, "backup_policy", value)

    @property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to bypass the FileSystemPolicy lockout safety check. The policy lockout safety check determines whether the policy in the request will prevent the principal making the request to be locked out from making future PutFileSystemPolicy requests on the file system. Set BypassPolicyLockoutSafetyCheck to True only when you intend to prevent the principal that is making the request from making a subsequent PutFileSystemPolicy request on the file system. Defaults to false
        """
        return pulumi.get(self, "bypass_policy_lockout_safety_check")

    @bypass_policy_lockout_safety_check.setter
    def bypass_policy_lockout_safety_check(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bypass_policy_lockout_safety_check", value)

    @property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "encrypted")

    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encrypted", value)

    @property
    @pulumi.getter(name="fileSystemPolicy")
    def file_system_policy(self) -> Optional[Any]:
        return pulumi.get(self, "file_system_policy")

    @file_system_policy.setter
    def file_system_policy(self, value: Optional[Any]):
        pulumi.set(self, "file_system_policy", value)

    @property
    @pulumi.getter(name="fileSystemTags")
    def file_system_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FileSystemElasticFileSystemTagArgs']]]]:
        return pulumi.get(self, "file_system_tags")

    @file_system_tags.setter
    def file_system_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FileSystemElasticFileSystemTagArgs']]]]):
        pulumi.set(self, "file_system_tags", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="lifecyclePolicies")
    def lifecycle_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FileSystemLifecyclePolicyArgs']]]]:
        return pulumi.get(self, "lifecycle_policies")

    @lifecycle_policies.setter
    def lifecycle_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FileSystemLifecyclePolicyArgs']]]]):
        pulumi.set(self, "lifecycle_policies", value)

    @property
    @pulumi.getter(name="performanceMode")
    def performance_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "performance_mode")

    @performance_mode.setter
    def performance_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "performance_mode", value)

    @property
    @pulumi.getter(name="provisionedThroughputInMibps")
    def provisioned_throughput_in_mibps(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "provisioned_throughput_in_mibps")

    @provisioned_throughput_in_mibps.setter
    def provisioned_throughput_in_mibps(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "provisioned_throughput_in_mibps", value)

    @property
    @pulumi.getter(name="replicationConfiguration")
    def replication_configuration(self) -> Optional[pulumi.Input['FileSystemReplicationConfigurationArgs']]:
        return pulumi.get(self, "replication_configuration")

    @replication_configuration.setter
    def replication_configuration(self, value: Optional[pulumi.Input['FileSystemReplicationConfigurationArgs']]):
        pulumi.set(self, "replication_configuration", value)

    @property
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "throughput_mode")

    @throughput_mode.setter
    def throughput_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "throughput_mode", value)


class FileSystem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone_name: Optional[pulumi.Input[str]] = None,
                 backup_policy: Optional[pulumi.Input[pulumi.InputType['FileSystemBackupPolicyArgs']]] = None,
                 bypass_policy_lockout_safety_check: Optional[pulumi.Input[bool]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 file_system_policy: Optional[Any] = None,
                 file_system_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileSystemElasticFileSystemTagArgs']]]]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 lifecycle_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileSystemLifecyclePolicyArgs']]]]] = None,
                 performance_mode: Optional[pulumi.Input[str]] = None,
                 provisioned_throughput_in_mibps: Optional[pulumi.Input[float]] = None,
                 replication_configuration: Optional[pulumi.Input[pulumi.InputType['FileSystemReplicationConfigurationArgs']]] = None,
                 throughput_mode: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EFS::FileSystem

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] bypass_policy_lockout_safety_check: Whether to bypass the FileSystemPolicy lockout safety check. The policy lockout safety check determines whether the policy in the request will prevent the principal making the request to be locked out from making future PutFileSystemPolicy requests on the file system. Set BypassPolicyLockoutSafetyCheck to True only when you intend to prevent the principal that is making the request from making a subsequent PutFileSystemPolicy request on the file system. Defaults to false
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[FileSystemArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EFS::FileSystem

        :param str resource_name: The name of the resource.
        :param FileSystemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FileSystemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone_name: Optional[pulumi.Input[str]] = None,
                 backup_policy: Optional[pulumi.Input[pulumi.InputType['FileSystemBackupPolicyArgs']]] = None,
                 bypass_policy_lockout_safety_check: Optional[pulumi.Input[bool]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 file_system_policy: Optional[Any] = None,
                 file_system_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileSystemElasticFileSystemTagArgs']]]]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 lifecycle_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileSystemLifecyclePolicyArgs']]]]] = None,
                 performance_mode: Optional[pulumi.Input[str]] = None,
                 provisioned_throughput_in_mibps: Optional[pulumi.Input[float]] = None,
                 replication_configuration: Optional[pulumi.Input[pulumi.InputType['FileSystemReplicationConfigurationArgs']]] = None,
                 throughput_mode: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FileSystemArgs.__new__(FileSystemArgs)

            __props__.__dict__["availability_zone_name"] = availability_zone_name
            __props__.__dict__["backup_policy"] = backup_policy
            __props__.__dict__["bypass_policy_lockout_safety_check"] = bypass_policy_lockout_safety_check
            __props__.__dict__["encrypted"] = encrypted
            __props__.__dict__["file_system_policy"] = file_system_policy
            __props__.__dict__["file_system_tags"] = file_system_tags
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["lifecycle_policies"] = lifecycle_policies
            __props__.__dict__["performance_mode"] = performance_mode
            __props__.__dict__["provisioned_throughput_in_mibps"] = provisioned_throughput_in_mibps
            __props__.__dict__["replication_configuration"] = replication_configuration
            __props__.__dict__["throughput_mode"] = throughput_mode
            __props__.__dict__["arn"] = None
            __props__.__dict__["file_system_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["availability_zone_name", "encrypted", "kms_key_id", "performance_mode"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(FileSystem, __self__).__init__(
            'aws-native:efs:FileSystem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FileSystem':
        """
        Get an existing FileSystem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FileSystemArgs.__new__(FileSystemArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["availability_zone_name"] = None
        __props__.__dict__["backup_policy"] = None
        __props__.__dict__["bypass_policy_lockout_safety_check"] = None
        __props__.__dict__["encrypted"] = None
        __props__.__dict__["file_system_id"] = None
        __props__.__dict__["file_system_policy"] = None
        __props__.__dict__["file_system_tags"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["lifecycle_policies"] = None
        __props__.__dict__["performance_mode"] = None
        __props__.__dict__["provisioned_throughput_in_mibps"] = None
        __props__.__dict__["replication_configuration"] = None
        __props__.__dict__["throughput_mode"] = None
        return FileSystem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "availability_zone_name")

    @property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> pulumi.Output[Optional['outputs.FileSystemBackupPolicy']]:
        return pulumi.get(self, "backup_policy")

    @property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to bypass the FileSystemPolicy lockout safety check. The policy lockout safety check determines whether the policy in the request will prevent the principal making the request to be locked out from making future PutFileSystemPolicy requests on the file system. Set BypassPolicyLockoutSafetyCheck to True only when you intend to prevent the principal that is making the request from making a subsequent PutFileSystemPolicy request on the file system. Defaults to false
        """
        return pulumi.get(self, "bypass_policy_lockout_safety_check")

    @property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "file_system_id")

    @property
    @pulumi.getter(name="fileSystemPolicy")
    def file_system_policy(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "file_system_policy")

    @property
    @pulumi.getter(name="fileSystemTags")
    def file_system_tags(self) -> pulumi.Output[Optional[Sequence['outputs.FileSystemElasticFileSystemTag']]]:
        return pulumi.get(self, "file_system_tags")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="lifecyclePolicies")
    def lifecycle_policies(self) -> pulumi.Output[Optional[Sequence['outputs.FileSystemLifecyclePolicy']]]:
        return pulumi.get(self, "lifecycle_policies")

    @property
    @pulumi.getter(name="performanceMode")
    def performance_mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "performance_mode")

    @property
    @pulumi.getter(name="provisionedThroughputInMibps")
    def provisioned_throughput_in_mibps(self) -> pulumi.Output[Optional[float]]:
        return pulumi.get(self, "provisioned_throughput_in_mibps")

    @property
    @pulumi.getter(name="replicationConfiguration")
    def replication_configuration(self) -> pulumi.Output[Optional['outputs.FileSystemReplicationConfiguration']]:
        return pulumi.get(self, "replication_configuration")

    @property
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "throughput_mode")

