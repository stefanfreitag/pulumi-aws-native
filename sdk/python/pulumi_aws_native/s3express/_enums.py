# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DirectoryBucketDataRedundancy',
]


class DirectoryBucketDataRedundancy(str, Enum):
    """
    Specifies the number of Avilability Zone that's used for redundancy for the bucket.
    """
    SINGLE_AVAILABILITY_ZONE = "SingleAvailabilityZone"
