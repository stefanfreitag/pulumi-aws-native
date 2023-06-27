// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package stepfunctions

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for StateMachineAlias
type StateMachineAlias struct {
	pulumi.CustomResourceState

	// The ARN of the alias.
	Arn                  pulumi.StringOutput                            `pulumi:"arn"`
	DeploymentPreference StateMachineAliasDeploymentPreferencePtrOutput `pulumi:"deploymentPreference"`
	// An optional description of the alias.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The alias name.
	Name                 pulumi.StringPtrOutput                                  `pulumi:"name"`
	RoutingConfiguration StateMachineAliasRoutingConfigurationVersionArrayOutput `pulumi:"routingConfiguration"`
}

// NewStateMachineAlias registers a new resource with the given unique name, arguments, and options.
func NewStateMachineAlias(ctx *pulumi.Context,
	name string, args *StateMachineAliasArgs, opts ...pulumi.ResourceOption) (*StateMachineAlias, error) {
	if args == nil {
		args = &StateMachineAliasArgs{}
	}

	var resource StateMachineAlias
	err := ctx.RegisterResource("aws-native:stepfunctions:StateMachineAlias", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStateMachineAlias gets an existing StateMachineAlias resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStateMachineAlias(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StateMachineAliasState, opts ...pulumi.ResourceOption) (*StateMachineAlias, error) {
	var resource StateMachineAlias
	err := ctx.ReadResource("aws-native:stepfunctions:StateMachineAlias", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StateMachineAlias resources.
type stateMachineAliasState struct {
}

type StateMachineAliasState struct {
}

func (StateMachineAliasState) ElementType() reflect.Type {
	return reflect.TypeOf((*stateMachineAliasState)(nil)).Elem()
}

type stateMachineAliasArgs struct {
	DeploymentPreference *StateMachineAliasDeploymentPreference `pulumi:"deploymentPreference"`
	// An optional description of the alias.
	Description *string `pulumi:"description"`
	// The alias name.
	Name                 *string                                        `pulumi:"name"`
	RoutingConfiguration []StateMachineAliasRoutingConfigurationVersion `pulumi:"routingConfiguration"`
}

// The set of arguments for constructing a StateMachineAlias resource.
type StateMachineAliasArgs struct {
	DeploymentPreference StateMachineAliasDeploymentPreferencePtrInput
	// An optional description of the alias.
	Description pulumi.StringPtrInput
	// The alias name.
	Name                 pulumi.StringPtrInput
	RoutingConfiguration StateMachineAliasRoutingConfigurationVersionArrayInput
}

func (StateMachineAliasArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stateMachineAliasArgs)(nil)).Elem()
}

type StateMachineAliasInput interface {
	pulumi.Input

	ToStateMachineAliasOutput() StateMachineAliasOutput
	ToStateMachineAliasOutputWithContext(ctx context.Context) StateMachineAliasOutput
}

func (*StateMachineAlias) ElementType() reflect.Type {
	return reflect.TypeOf((**StateMachineAlias)(nil)).Elem()
}

func (i *StateMachineAlias) ToStateMachineAliasOutput() StateMachineAliasOutput {
	return i.ToStateMachineAliasOutputWithContext(context.Background())
}

func (i *StateMachineAlias) ToStateMachineAliasOutputWithContext(ctx context.Context) StateMachineAliasOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StateMachineAliasOutput)
}

type StateMachineAliasOutput struct{ *pulumi.OutputState }

func (StateMachineAliasOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StateMachineAlias)(nil)).Elem()
}

func (o StateMachineAliasOutput) ToStateMachineAliasOutput() StateMachineAliasOutput {
	return o
}

func (o StateMachineAliasOutput) ToStateMachineAliasOutputWithContext(ctx context.Context) StateMachineAliasOutput {
	return o
}

// The ARN of the alias.
func (o StateMachineAliasOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *StateMachineAlias) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o StateMachineAliasOutput) DeploymentPreference() StateMachineAliasDeploymentPreferencePtrOutput {
	return o.ApplyT(func(v *StateMachineAlias) StateMachineAliasDeploymentPreferencePtrOutput {
		return v.DeploymentPreference
	}).(StateMachineAliasDeploymentPreferencePtrOutput)
}

// An optional description of the alias.
func (o StateMachineAliasOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StateMachineAlias) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The alias name.
func (o StateMachineAliasOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StateMachineAlias) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o StateMachineAliasOutput) RoutingConfiguration() StateMachineAliasRoutingConfigurationVersionArrayOutput {
	return o.ApplyT(func(v *StateMachineAlias) StateMachineAliasRoutingConfigurationVersionArrayOutput {
		return v.RoutingConfiguration
	}).(StateMachineAliasRoutingConfigurationVersionArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StateMachineAliasInput)(nil)).Elem(), &StateMachineAlias{})
	pulumi.RegisterOutputType(StateMachineAliasOutput{})
}
