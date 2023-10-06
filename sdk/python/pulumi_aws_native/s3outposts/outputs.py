# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'AccessPointVpcConfiguration',
    'BucketAbortIncompleteMultipartUpload',
    'BucketFilterAndOperatorProperties',
    'BucketFilterTag',
    'BucketLifecycleConfiguration',
    'BucketRule',
    'BucketRuleFilterProperties',
    'BucketTag',
    'EndpointFailedReason',
    'EndpointNetworkInterface',
]

@pulumi.output_type
class AccessPointVpcConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "vpcId":
            suggest = "vpc_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccessPointVpcConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccessPointVpcConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccessPointVpcConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 vpc_id: Optional[str] = None):
        """
        :param str vpc_id: Virtual Private Cloud (VPC) Id from which AccessPoint will allow requests.
        """
        AccessPointVpcConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            vpc_id=vpc_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             vpc_id: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if vpc_id is not None:
            _setter("vpc_id", vpc_id)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        """
        Virtual Private Cloud (VPC) Id from which AccessPoint will allow requests.
        """
        return pulumi.get(self, "vpc_id")


@pulumi.output_type
class BucketAbortIncompleteMultipartUpload(dict):
    """
    Specifies the days since the initiation of an incomplete multipart upload that Amazon S3Outposts will wait before permanently removing all parts of the upload.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "daysAfterInitiation":
            suggest = "days_after_initiation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketAbortIncompleteMultipartUpload. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketAbortIncompleteMultipartUpload.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketAbortIncompleteMultipartUpload.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 days_after_initiation: int):
        """
        Specifies the days since the initiation of an incomplete multipart upload that Amazon S3Outposts will wait before permanently removing all parts of the upload.
        :param int days_after_initiation: Specifies the number of days after which Amazon S3Outposts aborts an incomplete multipart upload.
        """
        BucketAbortIncompleteMultipartUpload._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            days_after_initiation=days_after_initiation,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             days_after_initiation: int,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("days_after_initiation", days_after_initiation)

    @property
    @pulumi.getter(name="daysAfterInitiation")
    def days_after_initiation(self) -> int:
        """
        Specifies the number of days after which Amazon S3Outposts aborts an incomplete multipart upload.
        """
        return pulumi.get(self, "days_after_initiation")


@pulumi.output_type
class BucketFilterAndOperatorProperties(dict):
    def __init__(__self__, *,
                 tags: Sequence['outputs.BucketFilterTag'],
                 prefix: Optional[str] = None):
        """
        :param Sequence['BucketFilterTag'] tags: All of these tags must exist in the object's tag set in order for the rule to apply.
        :param str prefix: Prefix identifies one or more objects to which the rule applies.
        """
        BucketFilterAndOperatorProperties._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            tags=tags,
            prefix=prefix,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             tags: Sequence['outputs.BucketFilterTag'],
             prefix: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("tags", tags)
        if prefix is not None:
            _setter("prefix", prefix)

    @property
    @pulumi.getter
    def tags(self) -> Sequence['outputs.BucketFilterTag']:
        """
        All of these tags must exist in the object's tag set in order for the rule to apply.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        """
        Prefix identifies one or more objects to which the rule applies.
        """
        return pulumi.get(self, "prefix")


@pulumi.output_type
class BucketFilterTag(dict):
    """
    Tag used to identify a subset of objects for an Amazon S3Outposts bucket.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        Tag used to identify a subset of objects for an Amazon S3Outposts bucket.
        """
        BucketFilterTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class BucketLifecycleConfiguration(dict):
    def __init__(__self__, *,
                 rules: Sequence['outputs.BucketRule']):
        """
        :param Sequence['BucketRule'] rules: A list of lifecycle rules for individual objects in an Amazon S3Outposts bucket.
        """
        BucketLifecycleConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rules=rules,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rules: Sequence['outputs.BucketRule'],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("rules", rules)

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.BucketRule']:
        """
        A list of lifecycle rules for individual objects in an Amazon S3Outposts bucket.
        """
        return pulumi.get(self, "rules")


@pulumi.output_type
class BucketRule(dict):
    """
    Specifies lifecycle rules for an Amazon S3Outposts bucket. You must specify at least one of the following: AbortIncompleteMultipartUpload, ExpirationDate, ExpirationInDays.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "abortIncompleteMultipartUpload":
            suggest = "abort_incomplete_multipart_upload"
        elif key == "expirationDate":
            suggest = "expiration_date"
        elif key == "expirationInDays":
            suggest = "expiration_in_days"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 abort_incomplete_multipart_upload: Optional['outputs.BucketAbortIncompleteMultipartUpload'] = None,
                 expiration_date: Optional[str] = None,
                 expiration_in_days: Optional[int] = None,
                 filter: Optional['outputs.BucketRuleFilterProperties'] = None,
                 id: Optional[str] = None,
                 status: Optional['BucketRuleStatus'] = None):
        """
        Specifies lifecycle rules for an Amazon S3Outposts bucket. You must specify at least one of the following: AbortIncompleteMultipartUpload, ExpirationDate, ExpirationInDays.
        :param 'BucketAbortIncompleteMultipartUpload' abort_incomplete_multipart_upload: Specifies a lifecycle rule that stops incomplete multipart uploads to an Amazon S3Outposts bucket.
        :param str expiration_date: Indicates when objects are deleted from Amazon S3Outposts. The date value must be in ISO 8601 format. The time is always midnight UTC.
        :param int expiration_in_days: Indicates the number of days after creation when objects are deleted from Amazon S3Outposts.
        :param 'BucketRuleFilterProperties' filter: The container for the filter of the lifecycle rule.
        :param str id: Unique identifier for the lifecycle rule. The value can't be longer than 255 characters.
        """
        BucketRule._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            abort_incomplete_multipart_upload=abort_incomplete_multipart_upload,
            expiration_date=expiration_date,
            expiration_in_days=expiration_in_days,
            filter=filter,
            id=id,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             abort_incomplete_multipart_upload: Optional['outputs.BucketAbortIncompleteMultipartUpload'] = None,
             expiration_date: Optional[str] = None,
             expiration_in_days: Optional[int] = None,
             filter: Optional['outputs.BucketRuleFilterProperties'] = None,
             id: Optional[str] = None,
             status: Optional['BucketRuleStatus'] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if abort_incomplete_multipart_upload is not None:
            _setter("abort_incomplete_multipart_upload", abort_incomplete_multipart_upload)
        if expiration_date is not None:
            _setter("expiration_date", expiration_date)
        if expiration_in_days is not None:
            _setter("expiration_in_days", expiration_in_days)
        if filter is not None:
            _setter("filter", filter)
        if id is not None:
            _setter("id", id)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="abortIncompleteMultipartUpload")
    def abort_incomplete_multipart_upload(self) -> Optional['outputs.BucketAbortIncompleteMultipartUpload']:
        """
        Specifies a lifecycle rule that stops incomplete multipart uploads to an Amazon S3Outposts bucket.
        """
        return pulumi.get(self, "abort_incomplete_multipart_upload")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[str]:
        """
        Indicates when objects are deleted from Amazon S3Outposts. The date value must be in ISO 8601 format. The time is always midnight UTC.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter(name="expirationInDays")
    def expiration_in_days(self) -> Optional[int]:
        """
        Indicates the number of days after creation when objects are deleted from Amazon S3Outposts.
        """
        return pulumi.get(self, "expiration_in_days")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.BucketRuleFilterProperties']:
        """
        The container for the filter of the lifecycle rule.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier for the lifecycle rule. The value can't be longer than 255 characters.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def status(self) -> Optional['BucketRuleStatus']:
        return pulumi.get(self, "status")


@pulumi.output_type
class BucketRuleFilterProperties(dict):
    """
    The container for the filter of the lifecycle rule.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "andOperator":
            suggest = "and_operator"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketRuleFilterProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketRuleFilterProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketRuleFilterProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 and_operator: Optional['outputs.BucketFilterAndOperatorProperties'] = None,
                 prefix: Optional[str] = None,
                 tag: Optional['outputs.BucketFilterTag'] = None):
        """
        The container for the filter of the lifecycle rule.
        :param 'BucketFilterAndOperatorProperties' and_operator: The container for the AND condition for the lifecycle rule. A combination of Prefix and 1 or more Tags OR a minimum of 2 or more tags.
        :param str prefix: Object key prefix that identifies one or more objects to which this rule applies.
        :param 'BucketFilterTag' tag: Specifies a tag used to identify a subset of objects for an Amazon S3Outposts bucket.
        """
        BucketRuleFilterProperties._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            and_operator=and_operator,
            prefix=prefix,
            tag=tag,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             and_operator: Optional['outputs.BucketFilterAndOperatorProperties'] = None,
             prefix: Optional[str] = None,
             tag: Optional['outputs.BucketFilterTag'] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if and_operator is not None:
            _setter("and_operator", and_operator)
        if prefix is not None:
            _setter("prefix", prefix)
        if tag is not None:
            _setter("tag", tag)

    @property
    @pulumi.getter(name="andOperator")
    def and_operator(self) -> Optional['outputs.BucketFilterAndOperatorProperties']:
        """
        The container for the AND condition for the lifecycle rule. A combination of Prefix and 1 or more Tags OR a minimum of 2 or more tags.
        """
        return pulumi.get(self, "and_operator")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        """
        Object key prefix that identifies one or more objects to which this rule applies.
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter
    def tag(self) -> Optional['outputs.BucketFilterTag']:
        """
        Specifies a tag used to identify a subset of objects for an Amazon S3Outposts bucket.
        """
        return pulumi.get(self, "tag")


@pulumi.output_type
class BucketTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        BucketTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class EndpointFailedReason(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "errorCode":
            suggest = "error_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointFailedReason. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointFailedReason.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointFailedReason.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 error_code: Optional[str] = None,
                 message: Optional[str] = None):
        """
        :param str error_code: The failure code, if any, for a create or delete endpoint operation.
        :param str message: Additional error details describing the endpoint failure and recommended action.
        """
        EndpointFailedReason._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            error_code=error_code,
            message=message,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             error_code: Optional[str] = None,
             message: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if error_code is not None:
            _setter("error_code", error_code)
        if message is not None:
            _setter("message", message)

    @property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[str]:
        """
        The failure code, if any, for a create or delete endpoint operation.
        """
        return pulumi.get(self, "error_code")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        Additional error details describing the endpoint failure and recommended action.
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class EndpointNetworkInterface(dict):
    """
    The container for the network interface.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "networkInterfaceId":
            suggest = "network_interface_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointNetworkInterface. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointNetworkInterface.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointNetworkInterface.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 network_interface_id: str):
        """
        The container for the network interface.
        """
        EndpointNetworkInterface._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            network_interface_id=network_interface_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             network_interface_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("network_interface_id", network_interface_id)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> str:
        return pulumi.get(self, "network_interface_id")


