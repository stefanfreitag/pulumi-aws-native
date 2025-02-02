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
    'GetSqlInjectionMatchSetResult',
    'AwaitableGetSqlInjectionMatchSetResult',
    'get_sql_injection_match_set',
    'get_sql_injection_match_set_output',
]

@pulumi.output_type
class GetSqlInjectionMatchSetResult:
    def __init__(__self__, id=None, sql_injection_match_tuples=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sql_injection_match_tuples and not isinstance(sql_injection_match_tuples, list):
            raise TypeError("Expected argument 'sql_injection_match_tuples' to be a list")
        pulumi.set(__self__, "sql_injection_match_tuples", sql_injection_match_tuples)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="sqlInjectionMatchTuples")
    def sql_injection_match_tuples(self) -> Optional[Sequence['outputs.SqlInjectionMatchSetSqlInjectionMatchTuple']]:
        return pulumi.get(self, "sql_injection_match_tuples")


class AwaitableGetSqlInjectionMatchSetResult(GetSqlInjectionMatchSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlInjectionMatchSetResult(
            id=self.id,
            sql_injection_match_tuples=self.sql_injection_match_tuples)


def get_sql_injection_match_set(id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlInjectionMatchSetResult:
    """
    Resource Type definition for AWS::WAF::SqlInjectionMatchSet
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:waf:getSqlInjectionMatchSet', __args__, opts=opts, typ=GetSqlInjectionMatchSetResult).value

    return AwaitableGetSqlInjectionMatchSetResult(
        id=pulumi.get(__ret__, 'id'),
        sql_injection_match_tuples=pulumi.get(__ret__, 'sql_injection_match_tuples'))


@_utilities.lift_output_func(get_sql_injection_match_set)
def get_sql_injection_match_set_output(id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlInjectionMatchSetResult]:
    """
    Resource Type definition for AWS::WAF::SqlInjectionMatchSet
    """
    ...
