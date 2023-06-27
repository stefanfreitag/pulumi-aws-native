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
    'GetCellResult',
    'AwaitableGetCellResult',
    'get_cell',
    'get_cell_output',
]

@pulumi.output_type
class GetCellResult:
    def __init__(__self__, cell_arn=None, cells=None, parent_readiness_scopes=None, tags=None):
        if cell_arn and not isinstance(cell_arn, str):
            raise TypeError("Expected argument 'cell_arn' to be a str")
        pulumi.set(__self__, "cell_arn", cell_arn)
        if cells and not isinstance(cells, list):
            raise TypeError("Expected argument 'cells' to be a list")
        pulumi.set(__self__, "cells", cells)
        if parent_readiness_scopes and not isinstance(parent_readiness_scopes, list):
            raise TypeError("Expected argument 'parent_readiness_scopes' to be a list")
        pulumi.set(__self__, "parent_readiness_scopes", parent_readiness_scopes)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="cellArn")
    def cell_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the cell.
        """
        return pulumi.get(self, "cell_arn")

    @property
    @pulumi.getter
    def cells(self) -> Optional[Sequence[str]]:
        """
        A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific Regions.
        """
        return pulumi.get(self, "cells")

    @property
    @pulumi.getter(name="parentReadinessScopes")
    def parent_readiness_scopes(self) -> Optional[Sequence[str]]:
        """
        The readiness scope for the cell, which can be a cell Amazon Resource Name (ARN) or a recovery group ARN. This is a list but currently can have only one element.
        """
        return pulumi.get(self, "parent_readiness_scopes")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.CellTag']]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")


class AwaitableGetCellResult(GetCellResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCellResult(
            cell_arn=self.cell_arn,
            cells=self.cells,
            parent_readiness_scopes=self.parent_readiness_scopes,
            tags=self.tags)


def get_cell(cell_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCellResult:
    """
    The API Schema for AWS Route53 Recovery Readiness Cells.


    :param str cell_name: The name of the cell to create.
    """
    __args__ = dict()
    __args__['cellName'] = cell_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:route53recoveryreadiness:getCell', __args__, opts=opts, typ=GetCellResult).value

    return AwaitableGetCellResult(
        cell_arn=__ret__.cell_arn,
        cells=__ret__.cells,
        parent_readiness_scopes=__ret__.parent_readiness_scopes,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_cell)
def get_cell_output(cell_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCellResult]:
    """
    The API Schema for AWS Route53 Recovery Readiness Cells.


    :param str cell_name: The name of the cell to create.
    """
    ...
