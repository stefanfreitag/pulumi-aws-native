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
from ._enums import *
from ._inputs import *

__all__ = ['StackSetArgs', 'StackSet']

@pulumi.input_type
class StackSetArgs:
    def __init__(__self__, *,
                 permission_model: pulumi.Input['StackSetPermissionModel'],
                 administration_role_arn: Optional[pulumi.Input[str]] = None,
                 auto_deployment: Optional[pulumi.Input['StackSetAutoDeploymentArgs']] = None,
                 call_as: Optional[pulumi.Input['StackSetCallAs']] = None,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetCapability']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_role_name: Optional[pulumi.Input[str]] = None,
                 managed_execution: Optional[pulumi.Input['ManagedExecutionPropertiesArgs']] = None,
                 operation_preferences: Optional[pulumi.Input['StackSetOperationPreferencesArgs']] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetParameterArgs']]]] = None,
                 stack_instances_group: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetStackInstancesArgs']]]] = None,
                 stack_set_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetTagArgs']]]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StackSet resource.
        :param pulumi.Input['StackSetPermissionModel'] permission_model: Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.
        :param pulumi.Input[str] administration_role_arn: The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.
        :param pulumi.Input['StackSetAutoDeploymentArgs'] auto_deployment: Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.
        :param pulumi.Input['StackSetCallAs'] call_as: Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.
        :param pulumi.Input[Sequence[pulumi.Input['StackSetCapability']]] capabilities: In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.
        :param pulumi.Input[str] description: A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
        :param pulumi.Input[str] execution_role_name: The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.
        :param pulumi.Input['ManagedExecutionPropertiesArgs'] managed_execution: Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
        :param pulumi.Input[Sequence[pulumi.Input['StackSetParameterArgs']]] parameters: The input parameters for the stack set template.
        :param pulumi.Input[Sequence[pulumi.Input['StackSetStackInstancesArgs']]] stack_instances_group: A group of stack instances with parameters in some specific accounts and regions.
        :param pulumi.Input[str] stack_set_name: The name to associate with the stack set. The name must be unique in the Region where you create your stack set.
        :param pulumi.Input[Sequence[pulumi.Input['StackSetTagArgs']]] tags: The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
        :param pulumi.Input[str] template_body: The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        :param pulumi.Input[str] template_url: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
        """
        StackSetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            permission_model=permission_model,
            administration_role_arn=administration_role_arn,
            auto_deployment=auto_deployment,
            call_as=call_as,
            capabilities=capabilities,
            description=description,
            execution_role_name=execution_role_name,
            managed_execution=managed_execution,
            operation_preferences=operation_preferences,
            parameters=parameters,
            stack_instances_group=stack_instances_group,
            stack_set_name=stack_set_name,
            tags=tags,
            template_body=template_body,
            template_url=template_url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             permission_model: pulumi.Input['StackSetPermissionModel'],
             administration_role_arn: Optional[pulumi.Input[str]] = None,
             auto_deployment: Optional[pulumi.Input['StackSetAutoDeploymentArgs']] = None,
             call_as: Optional[pulumi.Input['StackSetCallAs']] = None,
             capabilities: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetCapability']]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             execution_role_name: Optional[pulumi.Input[str]] = None,
             managed_execution: Optional[pulumi.Input['ManagedExecutionPropertiesArgs']] = None,
             operation_preferences: Optional[pulumi.Input['StackSetOperationPreferencesArgs']] = None,
             parameters: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetParameterArgs']]]] = None,
             stack_instances_group: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetStackInstancesArgs']]]] = None,
             stack_set_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetTagArgs']]]] = None,
             template_body: Optional[pulumi.Input[str]] = None,
             template_url: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("permission_model", permission_model)
        if administration_role_arn is not None:
            _setter("administration_role_arn", administration_role_arn)
        if auto_deployment is not None:
            _setter("auto_deployment", auto_deployment)
        if call_as is not None:
            _setter("call_as", call_as)
        if capabilities is not None:
            _setter("capabilities", capabilities)
        if description is not None:
            _setter("description", description)
        if execution_role_name is not None:
            _setter("execution_role_name", execution_role_name)
        if managed_execution is not None:
            _setter("managed_execution", managed_execution)
        if operation_preferences is not None:
            _setter("operation_preferences", operation_preferences)
        if parameters is not None:
            _setter("parameters", parameters)
        if stack_instances_group is not None:
            _setter("stack_instances_group", stack_instances_group)
        if stack_set_name is not None:
            _setter("stack_set_name", stack_set_name)
        if tags is not None:
            _setter("tags", tags)
        if template_body is not None:
            _setter("template_body", template_body)
        if template_url is not None:
            _setter("template_url", template_url)

    @property
    @pulumi.getter(name="permissionModel")
    def permission_model(self) -> pulumi.Input['StackSetPermissionModel']:
        """
        Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.
        """
        return pulumi.get(self, "permission_model")

    @permission_model.setter
    def permission_model(self, value: pulumi.Input['StackSetPermissionModel']):
        pulumi.set(self, "permission_model", value)

    @property
    @pulumi.getter(name="administrationRoleArn")
    def administration_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.
        """
        return pulumi.get(self, "administration_role_arn")

    @administration_role_arn.setter
    def administration_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administration_role_arn", value)

    @property
    @pulumi.getter(name="autoDeployment")
    def auto_deployment(self) -> Optional[pulumi.Input['StackSetAutoDeploymentArgs']]:
        """
        Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.
        """
        return pulumi.get(self, "auto_deployment")

    @auto_deployment.setter
    def auto_deployment(self, value: Optional[pulumi.Input['StackSetAutoDeploymentArgs']]):
        pulumi.set(self, "auto_deployment", value)

    @property
    @pulumi.getter(name="callAs")
    def call_as(self) -> Optional[pulumi.Input['StackSetCallAs']]:
        """
        Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.
        """
        return pulumi.get(self, "call_as")

    @call_as.setter
    def call_as(self, value: Optional[pulumi.Input['StackSetCallAs']]):
        pulumi.set(self, "call_as", value)

    @property
    @pulumi.getter
    def capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackSetCapability']]]]:
        """
        In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.
        """
        return pulumi.get(self, "capabilities")

    @capabilities.setter
    def capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetCapability']]]]):
        pulumi.set(self, "capabilities", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="executionRoleName")
    def execution_role_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.
        """
        return pulumi.get(self, "execution_role_name")

    @execution_role_name.setter
    def execution_role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "execution_role_name", value)

    @property
    @pulumi.getter(name="managedExecution")
    def managed_execution(self) -> Optional[pulumi.Input['ManagedExecutionPropertiesArgs']]:
        """
        Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
        """
        return pulumi.get(self, "managed_execution")

    @managed_execution.setter
    def managed_execution(self, value: Optional[pulumi.Input['ManagedExecutionPropertiesArgs']]):
        pulumi.set(self, "managed_execution", value)

    @property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> Optional[pulumi.Input['StackSetOperationPreferencesArgs']]:
        return pulumi.get(self, "operation_preferences")

    @operation_preferences.setter
    def operation_preferences(self, value: Optional[pulumi.Input['StackSetOperationPreferencesArgs']]):
        pulumi.set(self, "operation_preferences", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackSetParameterArgs']]]]:
        """
        The input parameters for the stack set template.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetParameterArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="stackInstancesGroup")
    def stack_instances_group(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackSetStackInstancesArgs']]]]:
        """
        A group of stack instances with parameters in some specific accounts and regions.
        """
        return pulumi.get(self, "stack_instances_group")

    @stack_instances_group.setter
    def stack_instances_group(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetStackInstancesArgs']]]]):
        pulumi.set(self, "stack_instances_group", value)

    @property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name to associate with the stack set. The name must be unique in the Region where you create your stack set.
        """
        return pulumi.get(self, "stack_set_name")

    @stack_set_name.setter
    def stack_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stack_set_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackSetTagArgs']]]]:
        """
        The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[pulumi.Input[str]]:
        """
        The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        """
        return pulumi.get(self, "template_body")

    @template_body.setter
    def template_body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_body", value)

    @property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> Optional[pulumi.Input[str]]:
        """
        Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
        """
        return pulumi.get(self, "template_url")

    @template_url.setter
    def template_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_url", value)


class StackSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administration_role_arn: Optional[pulumi.Input[str]] = None,
                 auto_deployment: Optional[pulumi.Input[pulumi.InputType['StackSetAutoDeploymentArgs']]] = None,
                 call_as: Optional[pulumi.Input['StackSetCallAs']] = None,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetCapability']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_role_name: Optional[pulumi.Input[str]] = None,
                 managed_execution: Optional[pulumi.Input[pulumi.InputType['ManagedExecutionPropertiesArgs']]] = None,
                 operation_preferences: Optional[pulumi.Input[pulumi.InputType['StackSetOperationPreferencesArgs']]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackSetParameterArgs']]]]] = None,
                 permission_model: Optional[pulumi.Input['StackSetPermissionModel']] = None,
                 stack_instances_group: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackSetStackInstancesArgs']]]]] = None,
                 stack_set_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackSetTagArgs']]]]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        StackSet as a resource provides one-click experience for provisioning a StackSet and StackInstances

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administration_role_arn: The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.
        :param pulumi.Input[pulumi.InputType['StackSetAutoDeploymentArgs']] auto_deployment: Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.
        :param pulumi.Input['StackSetCallAs'] call_as: Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.
        :param pulumi.Input[Sequence[pulumi.Input['StackSetCapability']]] capabilities: In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.
        :param pulumi.Input[str] description: A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
        :param pulumi.Input[str] execution_role_name: The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.
        :param pulumi.Input[pulumi.InputType['ManagedExecutionPropertiesArgs']] managed_execution: Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackSetParameterArgs']]]] parameters: The input parameters for the stack set template.
        :param pulumi.Input['StackSetPermissionModel'] permission_model: Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackSetStackInstancesArgs']]]] stack_instances_group: A group of stack instances with parameters in some specific accounts and regions.
        :param pulumi.Input[str] stack_set_name: The name to associate with the stack set. The name must be unique in the Region where you create your stack set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackSetTagArgs']]]] tags: The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
        :param pulumi.Input[str] template_body: The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        :param pulumi.Input[str] template_url: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StackSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        StackSet as a resource provides one-click experience for provisioning a StackSet and StackInstances

        :param str resource_name: The name of the resource.
        :param StackSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StackSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            StackSetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administration_role_arn: Optional[pulumi.Input[str]] = None,
                 auto_deployment: Optional[pulumi.Input[pulumi.InputType['StackSetAutoDeploymentArgs']]] = None,
                 call_as: Optional[pulumi.Input['StackSetCallAs']] = None,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input['StackSetCapability']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_role_name: Optional[pulumi.Input[str]] = None,
                 managed_execution: Optional[pulumi.Input[pulumi.InputType['ManagedExecutionPropertiesArgs']]] = None,
                 operation_preferences: Optional[pulumi.Input[pulumi.InputType['StackSetOperationPreferencesArgs']]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackSetParameterArgs']]]]] = None,
                 permission_model: Optional[pulumi.Input['StackSetPermissionModel']] = None,
                 stack_instances_group: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackSetStackInstancesArgs']]]]] = None,
                 stack_set_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackSetTagArgs']]]]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StackSetArgs.__new__(StackSetArgs)

            __props__.__dict__["administration_role_arn"] = administration_role_arn
            if auto_deployment is not None and not isinstance(auto_deployment, StackSetAutoDeploymentArgs):
                auto_deployment = auto_deployment or {}
                def _setter(key, value):
                    auto_deployment[key] = value
                StackSetAutoDeploymentArgs._configure(_setter, **auto_deployment)
            __props__.__dict__["auto_deployment"] = auto_deployment
            __props__.__dict__["call_as"] = call_as
            __props__.__dict__["capabilities"] = capabilities
            __props__.__dict__["description"] = description
            __props__.__dict__["execution_role_name"] = execution_role_name
            if managed_execution is not None and not isinstance(managed_execution, ManagedExecutionPropertiesArgs):
                managed_execution = managed_execution or {}
                def _setter(key, value):
                    managed_execution[key] = value
                ManagedExecutionPropertiesArgs._configure(_setter, **managed_execution)
            __props__.__dict__["managed_execution"] = managed_execution
            if operation_preferences is not None and not isinstance(operation_preferences, StackSetOperationPreferencesArgs):
                operation_preferences = operation_preferences or {}
                def _setter(key, value):
                    operation_preferences[key] = value
                StackSetOperationPreferencesArgs._configure(_setter, **operation_preferences)
            __props__.__dict__["operation_preferences"] = operation_preferences
            __props__.__dict__["parameters"] = parameters
            if permission_model is None and not opts.urn:
                raise TypeError("Missing required property 'permission_model'")
            __props__.__dict__["permission_model"] = permission_model
            __props__.__dict__["stack_instances_group"] = stack_instances_group
            __props__.__dict__["stack_set_name"] = stack_set_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["template_body"] = template_body
            __props__.__dict__["template_url"] = template_url
            __props__.__dict__["stack_set_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["permission_model", "stack_set_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(StackSet, __self__).__init__(
            'aws-native:cloudformation:StackSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StackSet':
        """
        Get an existing StackSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StackSetArgs.__new__(StackSetArgs)

        __props__.__dict__["administration_role_arn"] = None
        __props__.__dict__["auto_deployment"] = None
        __props__.__dict__["call_as"] = None
        __props__.__dict__["capabilities"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["execution_role_name"] = None
        __props__.__dict__["managed_execution"] = None
        __props__.__dict__["operation_preferences"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["permission_model"] = None
        __props__.__dict__["stack_instances_group"] = None
        __props__.__dict__["stack_set_id"] = None
        __props__.__dict__["stack_set_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["template_body"] = None
        __props__.__dict__["template_url"] = None
        return StackSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administrationRoleArn")
    def administration_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.
        """
        return pulumi.get(self, "administration_role_arn")

    @property
    @pulumi.getter(name="autoDeployment")
    def auto_deployment(self) -> pulumi.Output[Optional['outputs.StackSetAutoDeployment']]:
        """
        Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.
        """
        return pulumi.get(self, "auto_deployment")

    @property
    @pulumi.getter(name="callAs")
    def call_as(self) -> pulumi.Output[Optional['StackSetCallAs']]:
        """
        Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.
        """
        return pulumi.get(self, "call_as")

    @property
    @pulumi.getter
    def capabilities(self) -> pulumi.Output[Optional[Sequence['StackSetCapability']]]:
        """
        In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="executionRoleName")
    def execution_role_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.
        """
        return pulumi.get(self, "execution_role_name")

    @property
    @pulumi.getter(name="managedExecution")
    def managed_execution(self) -> pulumi.Output[Optional['outputs.ManagedExecutionProperties']]:
        """
        Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
        """
        return pulumi.get(self, "managed_execution")

    @property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> pulumi.Output[Optional['outputs.StackSetOperationPreferences']]:
        return pulumi.get(self, "operation_preferences")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence['outputs.StackSetParameter']]]:
        """
        The input parameters for the stack set template.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="permissionModel")
    def permission_model(self) -> pulumi.Output['StackSetPermissionModel']:
        """
        Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.
        """
        return pulumi.get(self, "permission_model")

    @property
    @pulumi.getter(name="stackInstancesGroup")
    def stack_instances_group(self) -> pulumi.Output[Optional[Sequence['outputs.StackSetStackInstances']]]:
        """
        A group of stack instances with parameters in some specific accounts and regions.
        """
        return pulumi.get(self, "stack_instances_group")

    @property
    @pulumi.getter(name="stackSetId")
    def stack_set_id(self) -> pulumi.Output[str]:
        """
        The ID of the stack set that you're creating.
        """
        return pulumi.get(self, "stack_set_id")

    @property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> pulumi.Output[str]:
        """
        The name to associate with the stack set. The name must be unique in the Region where you create your stack set.
        """
        return pulumi.get(self, "stack_set_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.StackSetTag']]]:
        """
        The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> pulumi.Output[Optional[str]]:
        """
        The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        """
        return pulumi.get(self, "template_body")

    @property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> pulumi.Output[Optional[str]]:
        """
        Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
        """
        return pulumi.get(self, "template_url")

