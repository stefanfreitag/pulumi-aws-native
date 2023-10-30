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
from ._enums import *

__all__ = [
    'AnnotationStoreFormatToHeader',
    'AnnotationStoreReferenceItem',
    'AnnotationStoreSchemaItem',
    'AnnotationStoreSseConfig',
    'AnnotationStoreStoreOptionsProperties',
    'AnnotationStoreTagMap',
    'AnnotationStoreTsvStoreOptions',
    'ReferenceStoreSseConfig',
    'ReferenceStoreTagMap',
    'RunGroupTagMap',
    'SequenceStoreSseConfig',
    'SequenceStoreTagMap',
    'VariantStoreReferenceItem',
    'VariantStoreSseConfig',
    'VariantStoreTagMap',
    'WorkflowParameterTemplate',
    'WorkflowTagMap',
]

@pulumi.output_type
class AnnotationStoreFormatToHeader(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class AnnotationStoreReferenceItem(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "referenceArn":
            suggest = "reference_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AnnotationStoreReferenceItem. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AnnotationStoreReferenceItem.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AnnotationStoreReferenceItem.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 reference_arn: str):
        pulumi.set(__self__, "reference_arn", reference_arn)

    @property
    @pulumi.getter(name="referenceArn")
    def reference_arn(self) -> str:
        return pulumi.get(self, "reference_arn")


@pulumi.output_type
class AnnotationStoreSchemaItem(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class AnnotationStoreSseConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyArn":
            suggest = "key_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AnnotationStoreSseConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AnnotationStoreSseConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AnnotationStoreSseConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: 'AnnotationStoreEncryptionType',
                 key_arn: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if key_arn is not None:
            pulumi.set(__self__, "key_arn", key_arn)

    @property
    @pulumi.getter
    def type(self) -> 'AnnotationStoreEncryptionType':
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> Optional[str]:
        return pulumi.get(self, "key_arn")


@pulumi.output_type
class AnnotationStoreStoreOptionsProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "tsvStoreOptions":
            suggest = "tsv_store_options"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AnnotationStoreStoreOptionsProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AnnotationStoreStoreOptionsProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AnnotationStoreStoreOptionsProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 tsv_store_options: 'outputs.AnnotationStoreTsvStoreOptions'):
        pulumi.set(__self__, "tsv_store_options", tsv_store_options)

    @property
    @pulumi.getter(name="tsvStoreOptions")
    def tsv_store_options(self) -> 'outputs.AnnotationStoreTsvStoreOptions':
        return pulumi.get(self, "tsv_store_options")


@pulumi.output_type
class AnnotationStoreTagMap(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class AnnotationStoreTsvStoreOptions(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "annotationType":
            suggest = "annotation_type"
        elif key == "formatToHeader":
            suggest = "format_to_header"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AnnotationStoreTsvStoreOptions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AnnotationStoreTsvStoreOptions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AnnotationStoreTsvStoreOptions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 annotation_type: Optional['AnnotationStoreAnnotationType'] = None,
                 format_to_header: Optional['outputs.AnnotationStoreFormatToHeader'] = None,
                 schema: Optional[Sequence['outputs.AnnotationStoreSchemaItem']] = None):
        if annotation_type is not None:
            pulumi.set(__self__, "annotation_type", annotation_type)
        if format_to_header is not None:
            pulumi.set(__self__, "format_to_header", format_to_header)
        if schema is not None:
            pulumi.set(__self__, "schema", schema)

    @property
    @pulumi.getter(name="annotationType")
    def annotation_type(self) -> Optional['AnnotationStoreAnnotationType']:
        return pulumi.get(self, "annotation_type")

    @property
    @pulumi.getter(name="formatToHeader")
    def format_to_header(self) -> Optional['outputs.AnnotationStoreFormatToHeader']:
        return pulumi.get(self, "format_to_header")

    @property
    @pulumi.getter
    def schema(self) -> Optional[Sequence['outputs.AnnotationStoreSchemaItem']]:
        return pulumi.get(self, "schema")


@pulumi.output_type
class ReferenceStoreSseConfig(dict):
    """
    Server-side encryption (SSE) settings for a store.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyArn":
            suggest = "key_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ReferenceStoreSseConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ReferenceStoreSseConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ReferenceStoreSseConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: 'ReferenceStoreEncryptionType',
                 key_arn: Optional[str] = None):
        """
        Server-side encryption (SSE) settings for a store.
        :param str key_arn: An encryption key ARN.
        """
        pulumi.set(__self__, "type", type)
        if key_arn is not None:
            pulumi.set(__self__, "key_arn", key_arn)

    @property
    @pulumi.getter
    def type(self) -> 'ReferenceStoreEncryptionType':
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> Optional[str]:
        """
        An encryption key ARN.
        """
        return pulumi.get(self, "key_arn")


@pulumi.output_type
class ReferenceStoreTagMap(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class RunGroupTagMap(dict):
    """
    A map of resource tags
    """
    def __init__(__self__):
        """
        A map of resource tags
        """
        pass


@pulumi.output_type
class SequenceStoreSseConfig(dict):
    """
    Server-side encryption (SSE) settings for a store.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyArn":
            suggest = "key_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SequenceStoreSseConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SequenceStoreSseConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SequenceStoreSseConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: 'SequenceStoreEncryptionType',
                 key_arn: Optional[str] = None):
        """
        Server-side encryption (SSE) settings for a store.
        :param str key_arn: An encryption key ARN.
        """
        pulumi.set(__self__, "type", type)
        if key_arn is not None:
            pulumi.set(__self__, "key_arn", key_arn)

    @property
    @pulumi.getter
    def type(self) -> 'SequenceStoreEncryptionType':
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> Optional[str]:
        """
        An encryption key ARN.
        """
        return pulumi.get(self, "key_arn")


@pulumi.output_type
class SequenceStoreTagMap(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class VariantStoreReferenceItem(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "referenceArn":
            suggest = "reference_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VariantStoreReferenceItem. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VariantStoreReferenceItem.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VariantStoreReferenceItem.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 reference_arn: str):
        pulumi.set(__self__, "reference_arn", reference_arn)

    @property
    @pulumi.getter(name="referenceArn")
    def reference_arn(self) -> str:
        return pulumi.get(self, "reference_arn")


@pulumi.output_type
class VariantStoreSseConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyArn":
            suggest = "key_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VariantStoreSseConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VariantStoreSseConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VariantStoreSseConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: 'VariantStoreEncryptionType',
                 key_arn: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if key_arn is not None:
            pulumi.set(__self__, "key_arn", key_arn)

    @property
    @pulumi.getter
    def type(self) -> 'VariantStoreEncryptionType':
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> Optional[str]:
        return pulumi.get(self, "key_arn")


@pulumi.output_type
class VariantStoreTagMap(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class WorkflowParameterTemplate(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class WorkflowTagMap(dict):
    """
    A map of resource tags
    """
    def __init__(__self__):
        """
        A map of resource tags
        """
        pass


