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

__all__ = [
    'GetDataQualityRulesetResult',
    'AwaitableGetDataQualityRulesetResult',
    'get_data_quality_ruleset',
    'get_data_quality_ruleset_output',
]

@pulumi.output_type
class GetDataQualityRulesetResult:
    def __init__(__self__, client_token=None, description=None, id=None, name=None, ruleset=None, tags=None, target_table=None):
        if client_token and not isinstance(client_token, str):
            raise TypeError("Expected argument 'client_token' to be a str")
        pulumi.set(__self__, "client_token", client_token)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if ruleset and not isinstance(ruleset, str):
            raise TypeError("Expected argument 'ruleset' to be a str")
        pulumi.set(__self__, "ruleset", ruleset)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_table and not isinstance(target_table, dict):
            raise TypeError("Expected argument 'target_table' to be a dict")
        pulumi.set(__self__, "target_table", target_table)

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> Optional[str]:
        return pulumi.get(self, "client_token")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ruleset(self) -> Optional[str]:
        return pulumi.get(self, "ruleset")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DataQualityRuleset` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetTable")
    def target_table(self) -> Optional['outputs.DataQualityRulesetDataQualityTargetTable']:
        return pulumi.get(self, "target_table")


class AwaitableGetDataQualityRulesetResult(GetDataQualityRulesetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataQualityRulesetResult(
            client_token=self.client_token,
            description=self.description,
            id=self.id,
            name=self.name,
            ruleset=self.ruleset,
            tags=self.tags,
            target_table=self.target_table)


def get_data_quality_ruleset(id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataQualityRulesetResult:
    """
    Resource Type definition for AWS::Glue::DataQualityRuleset
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:glue:getDataQualityRuleset', __args__, opts=opts, typ=GetDataQualityRulesetResult).value

    return AwaitableGetDataQualityRulesetResult(
        client_token=pulumi.get(__ret__, 'client_token'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        ruleset=pulumi.get(__ret__, 'ruleset'),
        tags=pulumi.get(__ret__, 'tags'),
        target_table=pulumi.get(__ret__, 'target_table'))


@_utilities.lift_output_func(get_data_quality_ruleset)
def get_data_quality_ruleset_output(id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataQualityRulesetResult]:
    """
    Resource Type definition for AWS::Glue::DataQualityRuleset
    """
    ...
