# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AgentTag',
    'LocationEFSEc2Config',
    'LocationEFSTag',
    'LocationFSxWindowsTag',
    'LocationHDFSNameNode',
    'LocationHDFSQopConfiguration',
    'LocationHDFSTag',
    'LocationNFSMountOptions',
    'LocationNFSOnPremConfig',
    'LocationNFSTag',
    'LocationObjectStorageTag',
    'LocationS3S3Config',
    'LocationS3Tag',
    'LocationSMBMountOptions',
    'LocationSMBTag',
    'TaskFilterRule',
    'TaskOptions',
    'TaskSchedule',
    'TaskTag',
]

@pulumi.output_type
class AgentTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for an AWS resource tag.
        :param str value: The value for an AWS resource tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for an AWS resource tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for an AWS resource tag.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class LocationEFSEc2Config(dict):
    """
    The subnet and security group that DataSync uses to access target EFS file system.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "securityGroupArns":
            suggest = "security_group_arns"
        elif key == "subnetArn":
            suggest = "subnet_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LocationEFSEc2Config. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LocationEFSEc2Config.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LocationEFSEc2Config.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 security_group_arns: Sequence[str],
                 subnet_arn: str):
        """
        The subnet and security group that DataSync uses to access target EFS file system.
        :param Sequence[str] security_group_arns: The Amazon Resource Names (ARNs) of the security groups that are configured for the Amazon EC2 resource.
        :param str subnet_arn: The ARN of the subnet that DataSync uses to access the target EFS file system.
        """
        pulumi.set(__self__, "security_group_arns", security_group_arns)
        pulumi.set(__self__, "subnet_arn", subnet_arn)

    @property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> Sequence[str]:
        """
        The Amazon Resource Names (ARNs) of the security groups that are configured for the Amazon EC2 resource.
        """
        return pulumi.get(self, "security_group_arns")

    @property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> str:
        """
        The ARN of the subnet that DataSync uses to access the target EFS file system.
        """
        return pulumi.get(self, "subnet_arn")


@pulumi.output_type
class LocationEFSTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for an AWS resource tag.
        :param str value: The value for an AWS resource tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for an AWS resource tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for an AWS resource tag.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class LocationFSxWindowsTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for an AWS resource tag.
        :param str value: The value for an AWS resource tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for an AWS resource tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for an AWS resource tag.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class LocationHDFSNameNode(dict):
    """
    HDFS Name Node IP and port information.
    """
    def __init__(__self__, *,
                 hostname: str,
                 port: int):
        """
        HDFS Name Node IP and port information.
        :param str hostname: The DNS name or IP address of the Name Node in the customer's on premises HDFS cluster.
        :param int port: The port on which the Name Node is listening on for client requests.
        """
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        The DNS name or IP address of the Name Node in the customer's on premises HDFS cluster.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        The port on which the Name Node is listening on for client requests.
        """
        return pulumi.get(self, "port")


@pulumi.output_type
class LocationHDFSQopConfiguration(dict):
    """
    Configuration information for RPC Protection and Data Transfer Protection. These parameters can be set to AUTHENTICATION, INTEGRITY, or PRIVACY. The default value is PRIVACY.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataTransferProtection":
            suggest = "data_transfer_protection"
        elif key == "rpcProtection":
            suggest = "rpc_protection"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LocationHDFSQopConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LocationHDFSQopConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LocationHDFSQopConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 data_transfer_protection: Optional['LocationHDFSQopConfigurationDataTransferProtection'] = None,
                 rpc_protection: Optional['LocationHDFSQopConfigurationRpcProtection'] = None):
        """
        Configuration information for RPC Protection and Data Transfer Protection. These parameters can be set to AUTHENTICATION, INTEGRITY, or PRIVACY. The default value is PRIVACY.
        :param 'LocationHDFSQopConfigurationDataTransferProtection' data_transfer_protection: Configuration for Data Transfer Protection.
        :param 'LocationHDFSQopConfigurationRpcProtection' rpc_protection: Configuration for RPC Protection.
        """
        if data_transfer_protection is not None:
            pulumi.set(__self__, "data_transfer_protection", data_transfer_protection)
        if rpc_protection is not None:
            pulumi.set(__self__, "rpc_protection", rpc_protection)

    @property
    @pulumi.getter(name="dataTransferProtection")
    def data_transfer_protection(self) -> Optional['LocationHDFSQopConfigurationDataTransferProtection']:
        """
        Configuration for Data Transfer Protection.
        """
        return pulumi.get(self, "data_transfer_protection")

    @property
    @pulumi.getter(name="rpcProtection")
    def rpc_protection(self) -> Optional['LocationHDFSQopConfigurationRpcProtection']:
        """
        Configuration for RPC Protection.
        """
        return pulumi.get(self, "rpc_protection")


@pulumi.output_type
class LocationHDFSTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class LocationNFSMountOptions(dict):
    """
    The NFS mount options that DataSync can use to mount your NFS share.
    """
    def __init__(__self__, *,
                 version: Optional['LocationNFSMountOptionsVersion'] = None):
        """
        The NFS mount options that DataSync can use to mount your NFS share.
        :param 'LocationNFSMountOptionsVersion' version: The specific NFS version that you want DataSync to use to mount your NFS share.
        """
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def version(self) -> Optional['LocationNFSMountOptionsVersion']:
        """
        The specific NFS version that you want DataSync to use to mount your NFS share.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class LocationNFSOnPremConfig(dict):
    """
    Contains a list of Amazon Resource Names (ARNs) of agents that are used to connect an NFS server.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "agentArns":
            suggest = "agent_arns"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LocationNFSOnPremConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LocationNFSOnPremConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LocationNFSOnPremConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 agent_arns: Sequence[str]):
        """
        Contains a list of Amazon Resource Names (ARNs) of agents that are used to connect an NFS server.
        :param Sequence[str] agent_arns: ARN(s) of the agent(s) to use for an NFS location.
        """
        pulumi.set(__self__, "agent_arns", agent_arns)

    @property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> Sequence[str]:
        """
        ARN(s) of the agent(s) to use for an NFS location.
        """
        return pulumi.get(self, "agent_arns")


@pulumi.output_type
class LocationNFSTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for an AWS resource tag.
        :param str value: The value for an AWS resource tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for an AWS resource tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for an AWS resource tag.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class LocationObjectStorageTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for an AWS resource tag.
        :param str value: The value for an AWS resource tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for an AWS resource tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for an AWS resource tag.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class LocationS3S3Config(dict):
    """
    The Amazon Resource Name (ARN) of the AWS IAM role that is used to access an Amazon S3 bucket.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bucketAccessRoleArn":
            suggest = "bucket_access_role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LocationS3S3Config. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LocationS3S3Config.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LocationS3S3Config.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket_access_role_arn: str):
        """
        The Amazon Resource Name (ARN) of the AWS IAM role that is used to access an Amazon S3 bucket.
        :param str bucket_access_role_arn: The ARN of the IAM role of the Amazon S3 bucket.
        """
        pulumi.set(__self__, "bucket_access_role_arn", bucket_access_role_arn)

    @property
    @pulumi.getter(name="bucketAccessRoleArn")
    def bucket_access_role_arn(self) -> str:
        """
        The ARN of the IAM role of the Amazon S3 bucket.
        """
        return pulumi.get(self, "bucket_access_role_arn")


@pulumi.output_type
class LocationS3Tag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for an AWS resource tag.
        :param str value: The value for an AWS resource tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for an AWS resource tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for an AWS resource tag.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class LocationSMBMountOptions(dict):
    """
    The mount options used by DataSync to access the SMB server.
    """
    def __init__(__self__, *,
                 version: Optional['LocationSMBMountOptionsVersion'] = None):
        """
        The mount options used by DataSync to access the SMB server.
        :param 'LocationSMBMountOptionsVersion' version: The specific SMB version that you want DataSync to use to mount your SMB share.
        """
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def version(self) -> Optional['LocationSMBMountOptionsVersion']:
        """
        The specific SMB version that you want DataSync to use to mount your SMB share.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class LocationSMBTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for an AWS resource tag.
        :param str value: The value for an AWS resource tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for an AWS resource tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for an AWS resource tag.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class TaskFilterRule(dict):
    """
    Specifies which files folders and objects to include or exclude when transferring files from source to destination.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "filterType":
            suggest = "filter_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TaskFilterRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TaskFilterRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TaskFilterRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 filter_type: Optional['TaskFilterRuleFilterType'] = None,
                 value: Optional[str] = None):
        """
        Specifies which files folders and objects to include or exclude when transferring files from source to destination.
        :param 'TaskFilterRuleFilterType' filter_type: The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.
        :param str value: A single filter string that consists of the patterns to include or exclude. The patterns are delimited by "|".
        """
        if filter_type is not None:
            pulumi.set(__self__, "filter_type", filter_type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> Optional['TaskFilterRuleFilterType']:
        """
        The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.
        """
        return pulumi.get(self, "filter_type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        A single filter string that consists of the patterns to include or exclude. The patterns are delimited by "|".
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class TaskOptions(dict):
    """
    Represents the options that are available to control the behavior of a StartTaskExecution operation.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bytesPerSecond":
            suggest = "bytes_per_second"
        elif key == "logLevel":
            suggest = "log_level"
        elif key == "overwriteMode":
            suggest = "overwrite_mode"
        elif key == "posixPermissions":
            suggest = "posix_permissions"
        elif key == "preserveDeletedFiles":
            suggest = "preserve_deleted_files"
        elif key == "preserveDevices":
            suggest = "preserve_devices"
        elif key == "securityDescriptorCopyFlags":
            suggest = "security_descriptor_copy_flags"
        elif key == "taskQueueing":
            suggest = "task_queueing"
        elif key == "transferMode":
            suggest = "transfer_mode"
        elif key == "verifyMode":
            suggest = "verify_mode"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TaskOptions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TaskOptions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TaskOptions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 atime: Optional['TaskOptionsAtime'] = None,
                 bytes_per_second: Optional[int] = None,
                 gid: Optional['TaskOptionsGid'] = None,
                 log_level: Optional['TaskOptionsLogLevel'] = None,
                 mtime: Optional['TaskOptionsMtime'] = None,
                 overwrite_mode: Optional['TaskOptionsOverwriteMode'] = None,
                 posix_permissions: Optional['TaskOptionsPosixPermissions'] = None,
                 preserve_deleted_files: Optional['TaskOptionsPreserveDeletedFiles'] = None,
                 preserve_devices: Optional['TaskOptionsPreserveDevices'] = None,
                 security_descriptor_copy_flags: Optional['TaskOptionsSecurityDescriptorCopyFlags'] = None,
                 task_queueing: Optional['TaskOptionsTaskQueueing'] = None,
                 transfer_mode: Optional['TaskOptionsTransferMode'] = None,
                 uid: Optional['TaskOptionsUid'] = None,
                 verify_mode: Optional['TaskOptionsVerifyMode'] = None):
        """
        Represents the options that are available to control the behavior of a StartTaskExecution operation.
        :param 'TaskOptionsAtime' atime: A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to).
        :param int bytes_per_second: A value that limits the bandwidth used by AWS DataSync.
        :param 'TaskOptionsGid' gid: The group ID (GID) of the file's owners.
        :param 'TaskOptionsLogLevel' log_level: A value that determines the types of logs that DataSync publishes to a log stream in the Amazon CloudWatch log group that you provide.
        :param 'TaskOptionsMtime' mtime: A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.
        :param 'TaskOptionsOverwriteMode' overwrite_mode: A value that determines whether files at the destination should be overwritten or preserved when copying files.
        :param 'TaskOptionsPosixPermissions' posix_permissions: A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.
        :param 'TaskOptionsPreserveDeletedFiles' preserve_deleted_files: A value that specifies whether files in the destination that don't exist in the source file system should be preserved.
        :param 'TaskOptionsPreserveDevices' preserve_devices: A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.
        :param 'TaskOptionsSecurityDescriptorCopyFlags' security_descriptor_copy_flags: A value that determines which components of the SMB security descriptor are copied during transfer.
        :param 'TaskOptionsTaskQueueing' task_queueing: A value that determines whether tasks should be queued before executing the tasks.
        :param 'TaskOptionsTransferMode' transfer_mode: A value that determines whether DataSync transfers only the data and metadata that differ between the source and the destination location, or whether DataSync transfers all the content from the source, without comparing to the destination location.
        :param 'TaskOptionsUid' uid: The user ID (UID) of the file's owner.
        :param 'TaskOptionsVerifyMode' verify_mode: A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.
        """
        if atime is not None:
            pulumi.set(__self__, "atime", atime)
        if bytes_per_second is not None:
            pulumi.set(__self__, "bytes_per_second", bytes_per_second)
        if gid is not None:
            pulumi.set(__self__, "gid", gid)
        if log_level is not None:
            pulumi.set(__self__, "log_level", log_level)
        if mtime is not None:
            pulumi.set(__self__, "mtime", mtime)
        if overwrite_mode is not None:
            pulumi.set(__self__, "overwrite_mode", overwrite_mode)
        if posix_permissions is not None:
            pulumi.set(__self__, "posix_permissions", posix_permissions)
        if preserve_deleted_files is not None:
            pulumi.set(__self__, "preserve_deleted_files", preserve_deleted_files)
        if preserve_devices is not None:
            pulumi.set(__self__, "preserve_devices", preserve_devices)
        if security_descriptor_copy_flags is not None:
            pulumi.set(__self__, "security_descriptor_copy_flags", security_descriptor_copy_flags)
        if task_queueing is not None:
            pulumi.set(__self__, "task_queueing", task_queueing)
        if transfer_mode is not None:
            pulumi.set(__self__, "transfer_mode", transfer_mode)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)
        if verify_mode is not None:
            pulumi.set(__self__, "verify_mode", verify_mode)

    @property
    @pulumi.getter
    def atime(self) -> Optional['TaskOptionsAtime']:
        """
        A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to).
        """
        return pulumi.get(self, "atime")

    @property
    @pulumi.getter(name="bytesPerSecond")
    def bytes_per_second(self) -> Optional[int]:
        """
        A value that limits the bandwidth used by AWS DataSync.
        """
        return pulumi.get(self, "bytes_per_second")

    @property
    @pulumi.getter
    def gid(self) -> Optional['TaskOptionsGid']:
        """
        The group ID (GID) of the file's owners.
        """
        return pulumi.get(self, "gid")

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional['TaskOptionsLogLevel']:
        """
        A value that determines the types of logs that DataSync publishes to a log stream in the Amazon CloudWatch log group that you provide.
        """
        return pulumi.get(self, "log_level")

    @property
    @pulumi.getter
    def mtime(self) -> Optional['TaskOptionsMtime']:
        """
        A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.
        """
        return pulumi.get(self, "mtime")

    @property
    @pulumi.getter(name="overwriteMode")
    def overwrite_mode(self) -> Optional['TaskOptionsOverwriteMode']:
        """
        A value that determines whether files at the destination should be overwritten or preserved when copying files.
        """
        return pulumi.get(self, "overwrite_mode")

    @property
    @pulumi.getter(name="posixPermissions")
    def posix_permissions(self) -> Optional['TaskOptionsPosixPermissions']:
        """
        A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.
        """
        return pulumi.get(self, "posix_permissions")

    @property
    @pulumi.getter(name="preserveDeletedFiles")
    def preserve_deleted_files(self) -> Optional['TaskOptionsPreserveDeletedFiles']:
        """
        A value that specifies whether files in the destination that don't exist in the source file system should be preserved.
        """
        return pulumi.get(self, "preserve_deleted_files")

    @property
    @pulumi.getter(name="preserveDevices")
    def preserve_devices(self) -> Optional['TaskOptionsPreserveDevices']:
        """
        A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.
        """
        return pulumi.get(self, "preserve_devices")

    @property
    @pulumi.getter(name="securityDescriptorCopyFlags")
    def security_descriptor_copy_flags(self) -> Optional['TaskOptionsSecurityDescriptorCopyFlags']:
        """
        A value that determines which components of the SMB security descriptor are copied during transfer.
        """
        return pulumi.get(self, "security_descriptor_copy_flags")

    @property
    @pulumi.getter(name="taskQueueing")
    def task_queueing(self) -> Optional['TaskOptionsTaskQueueing']:
        """
        A value that determines whether tasks should be queued before executing the tasks.
        """
        return pulumi.get(self, "task_queueing")

    @property
    @pulumi.getter(name="transferMode")
    def transfer_mode(self) -> Optional['TaskOptionsTransferMode']:
        """
        A value that determines whether DataSync transfers only the data and metadata that differ between the source and the destination location, or whether DataSync transfers all the content from the source, without comparing to the destination location.
        """
        return pulumi.get(self, "transfer_mode")

    @property
    @pulumi.getter
    def uid(self) -> Optional['TaskOptionsUid']:
        """
        The user ID (UID) of the file's owner.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="verifyMode")
    def verify_mode(self) -> Optional['TaskOptionsVerifyMode']:
        """
        A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.
        """
        return pulumi.get(self, "verify_mode")


@pulumi.output_type
class TaskSchedule(dict):
    """
    Specifies the schedule you want your task to use for repeated executions.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "scheduleExpression":
            suggest = "schedule_expression"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TaskSchedule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TaskSchedule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TaskSchedule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 schedule_expression: str):
        """
        Specifies the schedule you want your task to use for repeated executions.
        :param str schedule_expression: A cron expression that specifies when AWS DataSync initiates a scheduled transfer from a source to a destination location
        """
        pulumi.set(__self__, "schedule_expression", schedule_expression)

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> str:
        """
        A cron expression that specifies when AWS DataSync initiates a scheduled transfer from a source to a destination location
        """
        return pulumi.get(self, "schedule_expression")


@pulumi.output_type
class TaskTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for an AWS resource tag.
        :param str value: The value for an AWS resource tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for an AWS resource tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for an AWS resource tag.
        """
        return pulumi.get(self, "value")


