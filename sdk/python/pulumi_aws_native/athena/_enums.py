# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CapacityReservationStatus',
    'DataCatalogType',
    'WorkGroupEncryptionOption',
    'WorkGroupS3AclOption',
    'WorkGroupState',
]


class CapacityReservationStatus(str, Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    UPDATE_PENDING = "UPDATE_PENDING"


class DataCatalogType(str, Enum):
    """
    The type of data catalog to create: LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore. 
    """
    LAMBDA_ = "LAMBDA"
    GLUE = "GLUE"
    HIVE = "HIVE"


class WorkGroupEncryptionOption(str, Enum):
    """
    Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3), server-side encryption with KMS-managed keys (SSE-KMS), or client-side encryption with KMS-managed keys (CSE-KMS) is used.
    """
    SSE_S3 = "SSE_S3"
    SSE_KMS = "SSE_KMS"
    CSE_KMS = "CSE_KMS"


class WorkGroupS3AclOption(str, Enum):
    """
    The Amazon S3 canned ACL that Athena should specify when storing query results. Currently the only supported canned ACL is BUCKET_OWNER_FULL_CONTROL
    """
    BUCKET_OWNER_FULL_CONTROL = "BUCKET_OWNER_FULL_CONTROL"


class WorkGroupState(str, Enum):
    """
    The state of the workgroup: ENABLED or DISABLED.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
