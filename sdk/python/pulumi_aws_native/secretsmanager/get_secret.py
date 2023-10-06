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

__all__ = [
    'GetSecretResult',
    'AwaitableGetSecretResult',
    'get_secret',
    'get_secret_output',
]

@pulumi.output_type
class GetSecretResult:
    def __init__(__self__, description=None, id=None, kms_key_id=None, replica_regions=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if replica_regions and not isinstance(replica_regions, list):
            raise TypeError("Expected argument 'replica_regions' to be a list")
        pulumi.set(__self__, "replica_regions", replica_regions)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        (Optional) Specifies a user-provided description of the secret.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        secret Id, the Arn of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        (Optional) Specifies the ARN, Key ID, or alias of the AWS KMS customer master key (CMK) used to encrypt the SecretString.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="replicaRegions")
    def replica_regions(self) -> Optional[Sequence['outputs.SecretReplicaRegion']]:
        """
        (Optional) A list of ReplicaRegion objects. The ReplicaRegion type consists of a Region (required) and the KmsKeyId which can be an ARN, Key ID, or Alias.
        """
        return pulumi.get(self, "replica_regions")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SecretTag']]:
        """
        The list of user-defined tags associated with the secret. Use tags to manage your AWS resources. For additional information about tags, see TagResource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            description=self.description,
            id=self.id,
            kms_key_id=self.kms_key_id,
            replica_regions=self.replica_regions,
            tags=self.tags)


def get_secret(id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretResult:
    """
    Resource Type definition for AWS::SecretsManager::Secret


    :param str id: secret Id, the Arn of the resource.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:secretsmanager:getSecret', __args__, opts=opts, typ=GetSecretResult).value

    return AwaitableGetSecretResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        replica_regions=pulumi.get(__ret__, 'replica_regions'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_secret)
def get_secret_output(id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecretResult]:
    """
    Resource Type definition for AWS::SecretsManager::Secret


    :param str id: secret Id, the Arn of the resource.
    """
    ...
