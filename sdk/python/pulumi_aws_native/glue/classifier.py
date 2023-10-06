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
from ._inputs import *

__all__ = ['ClassifierArgs', 'Classifier']

@pulumi.input_type
class ClassifierArgs:
    def __init__(__self__, *,
                 csv_classifier: Optional[pulumi.Input['ClassifierCsvClassifierArgs']] = None,
                 grok_classifier: Optional[pulumi.Input['ClassifierGrokClassifierArgs']] = None,
                 json_classifier: Optional[pulumi.Input['ClassifierJsonClassifierArgs']] = None,
                 xml_classifier: Optional[pulumi.Input['ClassifierXmlClassifierArgs']] = None):
        """
        The set of arguments for constructing a Classifier resource.
        """
        ClassifierArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            csv_classifier=csv_classifier,
            grok_classifier=grok_classifier,
            json_classifier=json_classifier,
            xml_classifier=xml_classifier,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             csv_classifier: Optional[pulumi.Input['ClassifierCsvClassifierArgs']] = None,
             grok_classifier: Optional[pulumi.Input['ClassifierGrokClassifierArgs']] = None,
             json_classifier: Optional[pulumi.Input['ClassifierJsonClassifierArgs']] = None,
             xml_classifier: Optional[pulumi.Input['ClassifierXmlClassifierArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if csv_classifier is not None:
            _setter("csv_classifier", csv_classifier)
        if grok_classifier is not None:
            _setter("grok_classifier", grok_classifier)
        if json_classifier is not None:
            _setter("json_classifier", json_classifier)
        if xml_classifier is not None:
            _setter("xml_classifier", xml_classifier)

    @property
    @pulumi.getter(name="csvClassifier")
    def csv_classifier(self) -> Optional[pulumi.Input['ClassifierCsvClassifierArgs']]:
        return pulumi.get(self, "csv_classifier")

    @csv_classifier.setter
    def csv_classifier(self, value: Optional[pulumi.Input['ClassifierCsvClassifierArgs']]):
        pulumi.set(self, "csv_classifier", value)

    @property
    @pulumi.getter(name="grokClassifier")
    def grok_classifier(self) -> Optional[pulumi.Input['ClassifierGrokClassifierArgs']]:
        return pulumi.get(self, "grok_classifier")

    @grok_classifier.setter
    def grok_classifier(self, value: Optional[pulumi.Input['ClassifierGrokClassifierArgs']]):
        pulumi.set(self, "grok_classifier", value)

    @property
    @pulumi.getter(name="jsonClassifier")
    def json_classifier(self) -> Optional[pulumi.Input['ClassifierJsonClassifierArgs']]:
        return pulumi.get(self, "json_classifier")

    @json_classifier.setter
    def json_classifier(self, value: Optional[pulumi.Input['ClassifierJsonClassifierArgs']]):
        pulumi.set(self, "json_classifier", value)

    @property
    @pulumi.getter(name="xmlClassifier")
    def xml_classifier(self) -> Optional[pulumi.Input['ClassifierXmlClassifierArgs']]:
        return pulumi.get(self, "xml_classifier")

    @xml_classifier.setter
    def xml_classifier(self, value: Optional[pulumi.Input['ClassifierXmlClassifierArgs']]):
        pulumi.set(self, "xml_classifier", value)


warnings.warn("""Classifier is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Classifier(pulumi.CustomResource):
    warnings.warn("""Classifier is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 csv_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierCsvClassifierArgs']]] = None,
                 grok_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierGrokClassifierArgs']]] = None,
                 json_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierJsonClassifierArgs']]] = None,
                 xml_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierXmlClassifierArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Glue::Classifier

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ClassifierArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Glue::Classifier

        :param str resource_name: The name of the resource.
        :param ClassifierArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClassifierArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ClassifierArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 csv_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierCsvClassifierArgs']]] = None,
                 grok_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierGrokClassifierArgs']]] = None,
                 json_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierJsonClassifierArgs']]] = None,
                 xml_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierXmlClassifierArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""Classifier is deprecated: Classifier is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClassifierArgs.__new__(ClassifierArgs)

            if csv_classifier is not None and not isinstance(csv_classifier, ClassifierCsvClassifierArgs):
                csv_classifier = csv_classifier or {}
                def _setter(key, value):
                    csv_classifier[key] = value
                ClassifierCsvClassifierArgs._configure(_setter, **csv_classifier)
            __props__.__dict__["csv_classifier"] = csv_classifier
            if grok_classifier is not None and not isinstance(grok_classifier, ClassifierGrokClassifierArgs):
                grok_classifier = grok_classifier or {}
                def _setter(key, value):
                    grok_classifier[key] = value
                ClassifierGrokClassifierArgs._configure(_setter, **grok_classifier)
            __props__.__dict__["grok_classifier"] = grok_classifier
            if json_classifier is not None and not isinstance(json_classifier, ClassifierJsonClassifierArgs):
                json_classifier = json_classifier or {}
                def _setter(key, value):
                    json_classifier[key] = value
                ClassifierJsonClassifierArgs._configure(_setter, **json_classifier)
            __props__.__dict__["json_classifier"] = json_classifier
            if xml_classifier is not None and not isinstance(xml_classifier, ClassifierXmlClassifierArgs):
                xml_classifier = xml_classifier or {}
                def _setter(key, value):
                    xml_classifier[key] = value
                ClassifierXmlClassifierArgs._configure(_setter, **xml_classifier)
            __props__.__dict__["xml_classifier"] = xml_classifier
        super(Classifier, __self__).__init__(
            'aws-native:glue:Classifier',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Classifier':
        """
        Get an existing Classifier resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClassifierArgs.__new__(ClassifierArgs)

        __props__.__dict__["csv_classifier"] = None
        __props__.__dict__["grok_classifier"] = None
        __props__.__dict__["json_classifier"] = None
        __props__.__dict__["xml_classifier"] = None
        return Classifier(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="csvClassifier")
    def csv_classifier(self) -> pulumi.Output[Optional['outputs.ClassifierCsvClassifier']]:
        return pulumi.get(self, "csv_classifier")

    @property
    @pulumi.getter(name="grokClassifier")
    def grok_classifier(self) -> pulumi.Output[Optional['outputs.ClassifierGrokClassifier']]:
        return pulumi.get(self, "grok_classifier")

    @property
    @pulumi.getter(name="jsonClassifier")
    def json_classifier(self) -> pulumi.Output[Optional['outputs.ClassifierJsonClassifier']]:
        return pulumi.get(self, "json_classifier")

    @property
    @pulumi.getter(name="xmlClassifier")
    def xml_classifier(self) -> pulumi.Output[Optional['outputs.ClassifierXmlClassifier']]:
        return pulumi.get(self, "xml_classifier")

