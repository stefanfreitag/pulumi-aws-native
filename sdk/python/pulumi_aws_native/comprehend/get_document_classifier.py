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
    'GetDocumentClassifierResult',
    'AwaitableGetDocumentClassifierResult',
    'get_document_classifier',
    'get_document_classifier_output',
]

@pulumi.output_type
class GetDocumentClassifierResult:
    def __init__(__self__, arn=None, model_policy=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if model_policy and not isinstance(model_policy, str):
            raise TypeError("Expected argument 'model_policy' to be a str")
        pulumi.set(__self__, "model_policy", model_policy)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="modelPolicy")
    def model_policy(self) -> Optional[str]:
        return pulumi.get(self, "model_policy")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")


class AwaitableGetDocumentClassifierResult(GetDocumentClassifierResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDocumentClassifierResult(
            arn=self.arn,
            model_policy=self.model_policy,
            tags=self.tags)


def get_document_classifier(arn: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDocumentClassifierResult:
    """
    Document Classifier enables training document classifier models.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:comprehend:getDocumentClassifier', __args__, opts=opts, typ=GetDocumentClassifierResult).value

    return AwaitableGetDocumentClassifierResult(
        arn=pulumi.get(__ret__, 'arn'),
        model_policy=pulumi.get(__ret__, 'model_policy'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_document_classifier)
def get_document_classifier_output(arn: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDocumentClassifierResult]:
    """
    Document Classifier enables training document classifier models.
    """
    ...
