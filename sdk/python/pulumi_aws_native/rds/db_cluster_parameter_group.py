# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs

__all__ = ['DbClusterParameterGroupArgs', 'DbClusterParameterGroup']

@pulumi.input_type
class DbClusterParameterGroupArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 family: pulumi.Input[str],
                 parameters: Any,
                 db_cluster_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a DbClusterParameterGroup resource.
        :param pulumi.Input[str] description: A friendly description for this DB cluster parameter group.
        :param pulumi.Input[str] family: The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.
        :param Any parameters: An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::RDS::DBClusterParameterGroup` for more information about the expected schema for this property.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The list of tags for the cluster parameter group.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "family", family)
        pulumi.set(__self__, "parameters", parameters)
        if db_cluster_parameter_group_name is not None:
            pulumi.set(__self__, "db_cluster_parameter_group_name", db_cluster_parameter_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        A friendly description for this DB cluster parameter group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def family(self) -> pulumi.Input[str]:
        """
        The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: pulumi.Input[str]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def parameters(self) -> Any:
        """
        An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::RDS::DBClusterParameterGroup` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Any):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "db_cluster_parameter_group_name")

    @db_cluster_parameter_group_name.setter
    def db_cluster_parameter_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_cluster_parameter_group_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The list of tags for the cluster parameter group.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class DbClusterParameterGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_cluster_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::RDS::DBClusterParameterGroup resource creates a new Amazon RDS DB cluster parameter group. For more information, see Managing an Amazon Aurora DB Cluster in the Amazon Aurora User Guide.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A friendly description for this DB cluster parameter group.
        :param pulumi.Input[str] family: The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.
        :param Any parameters: An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::RDS::DBClusterParameterGroup` for more information about the expected schema for this property.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: The list of tags for the cluster parameter group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DbClusterParameterGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::RDS::DBClusterParameterGroup resource creates a new Amazon RDS DB cluster parameter group. For more information, see Managing an Amazon Aurora DB Cluster in the Amazon Aurora User Guide.

        :param str resource_name: The name of the resource.
        :param DbClusterParameterGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DbClusterParameterGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_cluster_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DbClusterParameterGroupArgs.__new__(DbClusterParameterGroupArgs)

            __props__.__dict__["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if family is None and not opts.urn:
                raise TypeError("Missing required property 'family'")
            __props__.__dict__["family"] = family
            if parameters is None and not opts.urn:
                raise TypeError("Missing required property 'parameters'")
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["db_cluster_parameter_group_name", "description", "family"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DbClusterParameterGroup, __self__).__init__(
            'aws-native:rds:DbClusterParameterGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DbClusterParameterGroup':
        """
        Get an existing DbClusterParameterGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DbClusterParameterGroupArgs.__new__(DbClusterParameterGroupArgs)

        __props__.__dict__["db_cluster_parameter_group_name"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["family"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["tags"] = None
        return DbClusterParameterGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "db_cluster_parameter_group_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A friendly description for this DB cluster parameter group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def family(self) -> pulumi.Output[str]:
        """
        The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Any]:
        """
        An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::RDS::DBClusterParameterGroup` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The list of tags for the cluster parameter group.
        """
        return pulumi.get(self, "tags")

