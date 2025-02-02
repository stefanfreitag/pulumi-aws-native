# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import outputs as _root_outputs

__all__ = [
    'GetTrustStoreResult',
    'AwaitableGetTrustStoreResult',
    'get_trust_store',
    'get_trust_store_output',
]

@pulumi.output_type
class GetTrustStoreResult:
    def __init__(__self__, associated_portal_arns=None, certificate_list=None, tags=None, trust_store_arn=None):
        if associated_portal_arns and not isinstance(associated_portal_arns, list):
            raise TypeError("Expected argument 'associated_portal_arns' to be a list")
        pulumi.set(__self__, "associated_portal_arns", associated_portal_arns)
        if certificate_list and not isinstance(certificate_list, list):
            raise TypeError("Expected argument 'certificate_list' to be a list")
        pulumi.set(__self__, "certificate_list", certificate_list)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if trust_store_arn and not isinstance(trust_store_arn, str):
            raise TypeError("Expected argument 'trust_store_arn' to be a str")
        pulumi.set(__self__, "trust_store_arn", trust_store_arn)

    @property
    @pulumi.getter(name="associatedPortalArns")
    def associated_portal_arns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "associated_portal_arns")

    @property
    @pulumi.getter(name="certificateList")
    def certificate_list(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "certificate_list")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustStoreArn")
    def trust_store_arn(self) -> Optional[str]:
        return pulumi.get(self, "trust_store_arn")


class AwaitableGetTrustStoreResult(GetTrustStoreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrustStoreResult(
            associated_portal_arns=self.associated_portal_arns,
            certificate_list=self.certificate_list,
            tags=self.tags,
            trust_store_arn=self.trust_store_arn)


def get_trust_store(trust_store_arn: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrustStoreResult:
    """
    Definition of AWS::WorkSpacesWeb::TrustStore Resource Type
    """
    __args__ = dict()
    __args__['trustStoreArn'] = trust_store_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:workspacesweb:getTrustStore', __args__, opts=opts, typ=GetTrustStoreResult).value

    return AwaitableGetTrustStoreResult(
        associated_portal_arns=pulumi.get(__ret__, 'associated_portal_arns'),
        certificate_list=pulumi.get(__ret__, 'certificate_list'),
        tags=pulumi.get(__ret__, 'tags'),
        trust_store_arn=pulumi.get(__ret__, 'trust_store_arn'))


@_utilities.lift_output_func(get_trust_store)
def get_trust_store_output(trust_store_arn: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrustStoreResult]:
    """
    Definition of AWS::WorkSpacesWeb::TrustStore Resource Type
    """
    ...
