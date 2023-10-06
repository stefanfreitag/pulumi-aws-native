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

__all__ = ['PushTemplateArgs', 'PushTemplate']

@pulumi.input_type
class PushTemplateArgs:
    def __init__(__self__, *,
                 template_name: pulumi.Input[str],
                 adm: Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']] = None,
                 apns: Optional[pulumi.Input['PushTemplateApnsPushNotificationTemplateArgs']] = None,
                 baidu: Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']] = None,
                 default: Optional[pulumi.Input['PushTemplateDefaultPushNotificationTemplateArgs']] = None,
                 default_substitutions: Optional[pulumi.Input[str]] = None,
                 gcm: Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']] = None,
                 tags: Optional[Any] = None,
                 template_description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PushTemplate resource.
        """
        PushTemplateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            template_name=template_name,
            adm=adm,
            apns=apns,
            baidu=baidu,
            default=default,
            default_substitutions=default_substitutions,
            gcm=gcm,
            tags=tags,
            template_description=template_description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             template_name: pulumi.Input[str],
             adm: Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']] = None,
             apns: Optional[pulumi.Input['PushTemplateApnsPushNotificationTemplateArgs']] = None,
             baidu: Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']] = None,
             default: Optional[pulumi.Input['PushTemplateDefaultPushNotificationTemplateArgs']] = None,
             default_substitutions: Optional[pulumi.Input[str]] = None,
             gcm: Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']] = None,
             tags: Optional[Any] = None,
             template_description: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("template_name", template_name)
        if adm is not None:
            _setter("adm", adm)
        if apns is not None:
            _setter("apns", apns)
        if baidu is not None:
            _setter("baidu", baidu)
        if default is not None:
            _setter("default", default)
        if default_substitutions is not None:
            _setter("default_substitutions", default_substitutions)
        if gcm is not None:
            _setter("gcm", gcm)
        if tags is not None:
            _setter("tags", tags)
        if template_description is not None:
            _setter("template_description", template_description)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "template_name", value)

    @property
    @pulumi.getter
    def adm(self) -> Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']]:
        return pulumi.get(self, "adm")

    @adm.setter
    def adm(self, value: Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']]):
        pulumi.set(self, "adm", value)

    @property
    @pulumi.getter
    def apns(self) -> Optional[pulumi.Input['PushTemplateApnsPushNotificationTemplateArgs']]:
        return pulumi.get(self, "apns")

    @apns.setter
    def apns(self, value: Optional[pulumi.Input['PushTemplateApnsPushNotificationTemplateArgs']]):
        pulumi.set(self, "apns", value)

    @property
    @pulumi.getter
    def baidu(self) -> Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']]:
        return pulumi.get(self, "baidu")

    @baidu.setter
    def baidu(self, value: Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']]):
        pulumi.set(self, "baidu", value)

    @property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input['PushTemplateDefaultPushNotificationTemplateArgs']]:
        return pulumi.get(self, "default")

    @default.setter
    def default(self, value: Optional[pulumi.Input['PushTemplateDefaultPushNotificationTemplateArgs']]):
        pulumi.set(self, "default", value)

    @property
    @pulumi.getter(name="defaultSubstitutions")
    def default_substitutions(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_substitutions")

    @default_substitutions.setter
    def default_substitutions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_substitutions", value)

    @property
    @pulumi.getter
    def gcm(self) -> Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']]:
        return pulumi.get(self, "gcm")

    @gcm.setter
    def gcm(self, value: Optional[pulumi.Input['PushTemplateAndroidPushNotificationTemplateArgs']]):
        pulumi.set(self, "gcm", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="templateDescription")
    def template_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "template_description")

    @template_description.setter
    def template_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_description", value)


warnings.warn("""PushTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class PushTemplate(pulumi.CustomResource):
    warnings.warn("""PushTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 adm: Optional[pulumi.Input[pulumi.InputType['PushTemplateAndroidPushNotificationTemplateArgs']]] = None,
                 apns: Optional[pulumi.Input[pulumi.InputType['PushTemplateApnsPushNotificationTemplateArgs']]] = None,
                 baidu: Optional[pulumi.Input[pulumi.InputType['PushTemplateAndroidPushNotificationTemplateArgs']]] = None,
                 default: Optional[pulumi.Input[pulumi.InputType['PushTemplateDefaultPushNotificationTemplateArgs']]] = None,
                 default_substitutions: Optional[pulumi.Input[str]] = None,
                 gcm: Optional[pulumi.Input[pulumi.InputType['PushTemplateAndroidPushNotificationTemplateArgs']]] = None,
                 tags: Optional[Any] = None,
                 template_description: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Pinpoint::PushTemplate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PushTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Pinpoint::PushTemplate

        :param str resource_name: The name of the resource.
        :param PushTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PushTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PushTemplateArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 adm: Optional[pulumi.Input[pulumi.InputType['PushTemplateAndroidPushNotificationTemplateArgs']]] = None,
                 apns: Optional[pulumi.Input[pulumi.InputType['PushTemplateApnsPushNotificationTemplateArgs']]] = None,
                 baidu: Optional[pulumi.Input[pulumi.InputType['PushTemplateAndroidPushNotificationTemplateArgs']]] = None,
                 default: Optional[pulumi.Input[pulumi.InputType['PushTemplateDefaultPushNotificationTemplateArgs']]] = None,
                 default_substitutions: Optional[pulumi.Input[str]] = None,
                 gcm: Optional[pulumi.Input[pulumi.InputType['PushTemplateAndroidPushNotificationTemplateArgs']]] = None,
                 tags: Optional[Any] = None,
                 template_description: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""PushTemplate is deprecated: PushTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PushTemplateArgs.__new__(PushTemplateArgs)

            if adm is not None and not isinstance(adm, PushTemplateAndroidPushNotificationTemplateArgs):
                adm = adm or {}
                def _setter(key, value):
                    adm[key] = value
                PushTemplateAndroidPushNotificationTemplateArgs._configure(_setter, **adm)
            __props__.__dict__["adm"] = adm
            if apns is not None and not isinstance(apns, PushTemplateApnsPushNotificationTemplateArgs):
                apns = apns or {}
                def _setter(key, value):
                    apns[key] = value
                PushTemplateApnsPushNotificationTemplateArgs._configure(_setter, **apns)
            __props__.__dict__["apns"] = apns
            if baidu is not None and not isinstance(baidu, PushTemplateAndroidPushNotificationTemplateArgs):
                baidu = baidu or {}
                def _setter(key, value):
                    baidu[key] = value
                PushTemplateAndroidPushNotificationTemplateArgs._configure(_setter, **baidu)
            __props__.__dict__["baidu"] = baidu
            if default is not None and not isinstance(default, PushTemplateDefaultPushNotificationTemplateArgs):
                default = default or {}
                def _setter(key, value):
                    default[key] = value
                PushTemplateDefaultPushNotificationTemplateArgs._configure(_setter, **default)
            __props__.__dict__["default"] = default
            __props__.__dict__["default_substitutions"] = default_substitutions
            if gcm is not None and not isinstance(gcm, PushTemplateAndroidPushNotificationTemplateArgs):
                gcm = gcm or {}
                def _setter(key, value):
                    gcm[key] = value
                PushTemplateAndroidPushNotificationTemplateArgs._configure(_setter, **gcm)
            __props__.__dict__["gcm"] = gcm
            __props__.__dict__["tags"] = tags
            __props__.__dict__["template_description"] = template_description
            if template_name is None and not opts.urn:
                raise TypeError("Missing required property 'template_name'")
            __props__.__dict__["template_name"] = template_name
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["template_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(PushTemplate, __self__).__init__(
            'aws-native:pinpoint:PushTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PushTemplate':
        """
        Get an existing PushTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PushTemplateArgs.__new__(PushTemplateArgs)

        __props__.__dict__["adm"] = None
        __props__.__dict__["apns"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["baidu"] = None
        __props__.__dict__["default"] = None
        __props__.__dict__["default_substitutions"] = None
        __props__.__dict__["gcm"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["template_description"] = None
        __props__.__dict__["template_name"] = None
        return PushTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def adm(self) -> pulumi.Output[Optional['outputs.PushTemplateAndroidPushNotificationTemplate']]:
        return pulumi.get(self, "adm")

    @property
    @pulumi.getter
    def apns(self) -> pulumi.Output[Optional['outputs.PushTemplateApnsPushNotificationTemplate']]:
        return pulumi.get(self, "apns")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def baidu(self) -> pulumi.Output[Optional['outputs.PushTemplateAndroidPushNotificationTemplate']]:
        return pulumi.get(self, "baidu")

    @property
    @pulumi.getter
    def default(self) -> pulumi.Output[Optional['outputs.PushTemplateDefaultPushNotificationTemplate']]:
        return pulumi.get(self, "default")

    @property
    @pulumi.getter(name="defaultSubstitutions")
    def default_substitutions(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_substitutions")

    @property
    @pulumi.getter
    def gcm(self) -> pulumi.Output[Optional['outputs.PushTemplateAndroidPushNotificationTemplate']]:
        return pulumi.get(self, "gcm")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateDescription")
    def template_description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "template_description")

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "template_name")

