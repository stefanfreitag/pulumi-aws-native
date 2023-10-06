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
    'GetClassifierResult',
    'AwaitableGetClassifierResult',
    'get_classifier',
    'get_classifier_output',
]

@pulumi.output_type
class GetClassifierResult:
    def __init__(__self__, csv_classifier=None, grok_classifier=None, id=None, json_classifier=None, xml_classifier=None):
        if csv_classifier and not isinstance(csv_classifier, dict):
            raise TypeError("Expected argument 'csv_classifier' to be a dict")
        pulumi.set(__self__, "csv_classifier", csv_classifier)
        if grok_classifier and not isinstance(grok_classifier, dict):
            raise TypeError("Expected argument 'grok_classifier' to be a dict")
        pulumi.set(__self__, "grok_classifier", grok_classifier)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if json_classifier and not isinstance(json_classifier, dict):
            raise TypeError("Expected argument 'json_classifier' to be a dict")
        pulumi.set(__self__, "json_classifier", json_classifier)
        if xml_classifier and not isinstance(xml_classifier, dict):
            raise TypeError("Expected argument 'xml_classifier' to be a dict")
        pulumi.set(__self__, "xml_classifier", xml_classifier)

    @property
    @pulumi.getter(name="csvClassifier")
    def csv_classifier(self) -> Optional['outputs.ClassifierCsvClassifier']:
        return pulumi.get(self, "csv_classifier")

    @property
    @pulumi.getter(name="grokClassifier")
    def grok_classifier(self) -> Optional['outputs.ClassifierGrokClassifier']:
        return pulumi.get(self, "grok_classifier")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="jsonClassifier")
    def json_classifier(self) -> Optional['outputs.ClassifierJsonClassifier']:
        return pulumi.get(self, "json_classifier")

    @property
    @pulumi.getter(name="xmlClassifier")
    def xml_classifier(self) -> Optional['outputs.ClassifierXmlClassifier']:
        return pulumi.get(self, "xml_classifier")


class AwaitableGetClassifierResult(GetClassifierResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClassifierResult(
            csv_classifier=self.csv_classifier,
            grok_classifier=self.grok_classifier,
            id=self.id,
            json_classifier=self.json_classifier,
            xml_classifier=self.xml_classifier)


def get_classifier(id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClassifierResult:
    """
    Resource Type definition for AWS::Glue::Classifier
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:glue:getClassifier', __args__, opts=opts, typ=GetClassifierResult).value

    return AwaitableGetClassifierResult(
        csv_classifier=pulumi.get(__ret__, 'csv_classifier'),
        grok_classifier=pulumi.get(__ret__, 'grok_classifier'),
        id=pulumi.get(__ret__, 'id'),
        json_classifier=pulumi.get(__ret__, 'json_classifier'),
        xml_classifier=pulumi.get(__ret__, 'xml_classifier'))


@_utilities.lift_output_func(get_classifier)
def get_classifier_output(id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClassifierResult]:
    """
    Resource Type definition for AWS::Glue::Classifier
    """
    ...
