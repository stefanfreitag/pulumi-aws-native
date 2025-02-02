# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
    'get_application_output',
]

@pulumi.output_type
class GetApplicationResult:
    def __init__(__self__, application_name=None, application_tag_key=None, application_tag_value=None, arn=None, description=None, id=None, name=None, tags=None):
        if application_name and not isinstance(application_name, str):
            raise TypeError("Expected argument 'application_name' to be a str")
        pulumi.set(__self__, "application_name", application_name)
        if application_tag_key and not isinstance(application_tag_key, str):
            raise TypeError("Expected argument 'application_tag_key' to be a str")
        pulumi.set(__self__, "application_tag_key", application_tag_key)
        if application_tag_value and not isinstance(application_tag_value, str):
            raise TypeError("Expected argument 'application_tag_value' to be a str")
        pulumi.set(__self__, "application_tag_value", application_tag_value)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[str]:
        """
        The name of the application. 
        """
        return pulumi.get(self, "application_name")

    @property
    @pulumi.getter(name="applicationTagKey")
    def application_tag_key(self) -> Optional[str]:
        """
        The key of the AWS application tag, which is awsApplication. Applications created before 11/13/2023 or applications without the AWS application tag resource group return no value.
        """
        return pulumi.get(self, "application_tag_key")

    @property
    @pulumi.getter(name="applicationTagValue")
    def application_tag_value(self) -> Optional[str]:
        """
        The value of the AWS application tag, which is the identifier of an associated resource. Applications created before 11/13/2023 or applications without the AWS application tag resource group return no value. 
        """
        return pulumi.get(self, "application_tag_value")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the application. 
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the application. 
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "tags")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            application_name=self.application_name,
            application_tag_key=self.application_tag_key,
            application_tag_value=self.application_tag_value,
            arn=self.arn,
            description=self.description,
            id=self.id,
            name=self.name,
            tags=self.tags)


def get_application(id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    Resource Schema for AWS::ServiceCatalogAppRegistry::Application
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:servicecatalogappregistry:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        application_name=pulumi.get(__ret__, 'application_name'),
        application_tag_key=pulumi.get(__ret__, 'application_tag_key'),
        application_tag_value=pulumi.get(__ret__, 'application_tag_value'),
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_application)
def get_application_output(id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationResult]:
    """
    Resource Schema for AWS::ServiceCatalogAppRegistry::Application
    """
    ...
