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
    'DataIntegrationFileConfiguration',
    'DataIntegrationObjectConfiguration',
    'DataIntegrationScheduleConfig',
    'EventIntegrationEventFilter',
]

@pulumi.output_type
class DataIntegrationFileConfiguration(dict):
    """
    The configuration for what files should be pulled from the source.
    """
    def __init__(__self__, *,
                 folders: Sequence[str],
                 filters: Optional[Mapping[str, Sequence[str]]] = None):
        """
        The configuration for what files should be pulled from the source.
        :param Sequence[str] folders: Identifiers for the source folders to pull all files from recursively.
        :param Mapping[str, Sequence[str]] filters: Restrictions for what files should be pulled from the source.
        """
        pulumi.set(__self__, "folders", folders)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)

    @property
    @pulumi.getter
    def folders(self) -> Sequence[str]:
        """
        Identifiers for the source folders to pull all files from recursively.
        """
        return pulumi.get(self, "folders")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Mapping[str, Sequence[str]]]:
        """
        Restrictions for what files should be pulled from the source.
        """
        return pulumi.get(self, "filters")


@pulumi.output_type
class DataIntegrationObjectConfiguration(dict):
    """
    The configuration for what data should be pulled from the source.
    """
    def __init__(__self__):
        """
        The configuration for what data should be pulled from the source.
        """
        pass


@pulumi.output_type
class DataIntegrationScheduleConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "scheduleExpression":
            suggest = "schedule_expression"
        elif key == "firstExecutionFrom":
            suggest = "first_execution_from"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DataIntegrationScheduleConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DataIntegrationScheduleConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DataIntegrationScheduleConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 schedule_expression: str,
                 first_execution_from: Optional[str] = None,
                 object: Optional[str] = None):
        """
        :param str schedule_expression: How often the data should be pulled from data source.
        :param str first_execution_from: The start date for objects to import in the first flow run. Epoch or ISO timestamp format is supported.
        :param str object: The name of the object to pull from the data source.
        """
        pulumi.set(__self__, "schedule_expression", schedule_expression)
        if first_execution_from is not None:
            pulumi.set(__self__, "first_execution_from", first_execution_from)
        if object is not None:
            pulumi.set(__self__, "object", object)

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> str:
        """
        How often the data should be pulled from data source.
        """
        return pulumi.get(self, "schedule_expression")

    @property
    @pulumi.getter(name="firstExecutionFrom")
    def first_execution_from(self) -> Optional[str]:
        """
        The start date for objects to import in the first flow run. Epoch or ISO timestamp format is supported.
        """
        return pulumi.get(self, "first_execution_from")

    @property
    @pulumi.getter
    def object(self) -> Optional[str]:
        """
        The name of the object to pull from the data source.
        """
        return pulumi.get(self, "object")


@pulumi.output_type
class EventIntegrationEventFilter(dict):
    def __init__(__self__, *,
                 source: str):
        """
        :param str source: The source of the events.
        """
        pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        The source of the events.
        """
        return pulumi.get(self, "source")


