// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotcoredeviceadvisor

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// An example resource schema demonstrating some basic constructs and validation rules.
type SuiteDefinition struct {
	pulumi.CustomResourceState

	// The Amazon Resource name for the suite definition.
	SuiteDefinitionArn           pulumi.StringOutput                          `pulumi:"suiteDefinitionArn"`
	SuiteDefinitionConfiguration SuiteDefinitionConfigurationPropertiesOutput `pulumi:"suiteDefinitionConfiguration"`
	// The unique identifier for the suite definition.
	SuiteDefinitionId pulumi.StringOutput `pulumi:"suiteDefinitionId"`
	// The suite definition version of a test suite.
	SuiteDefinitionVersion pulumi.StringOutput `pulumi:"suiteDefinitionVersion"`
	// An array of key-value pairs to apply to this resource.
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewSuiteDefinition registers a new resource with the given unique name, arguments, and options.
func NewSuiteDefinition(ctx *pulumi.Context,
	name string, args *SuiteDefinitionArgs, opts ...pulumi.ResourceOption) (*SuiteDefinition, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SuiteDefinitionConfiguration == nil {
		return nil, errors.New("invalid value for required argument 'SuiteDefinitionConfiguration'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SuiteDefinition
	err := ctx.RegisterResource("aws-native:iotcoredeviceadvisor:SuiteDefinition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSuiteDefinition gets an existing SuiteDefinition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSuiteDefinition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SuiteDefinitionState, opts ...pulumi.ResourceOption) (*SuiteDefinition, error) {
	var resource SuiteDefinition
	err := ctx.ReadResource("aws-native:iotcoredeviceadvisor:SuiteDefinition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SuiteDefinition resources.
type suiteDefinitionState struct {
}

type SuiteDefinitionState struct {
}

func (SuiteDefinitionState) ElementType() reflect.Type {
	return reflect.TypeOf((*suiteDefinitionState)(nil)).Elem()
}

type suiteDefinitionArgs struct {
	SuiteDefinitionConfiguration SuiteDefinitionConfigurationProperties `pulumi:"suiteDefinitionConfiguration"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a SuiteDefinition resource.
type SuiteDefinitionArgs struct {
	SuiteDefinitionConfiguration SuiteDefinitionConfigurationPropertiesInput
	// An array of key-value pairs to apply to this resource.
	Tags aws.TagArrayInput
}

func (SuiteDefinitionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*suiteDefinitionArgs)(nil)).Elem()
}

type SuiteDefinitionInput interface {
	pulumi.Input

	ToSuiteDefinitionOutput() SuiteDefinitionOutput
	ToSuiteDefinitionOutputWithContext(ctx context.Context) SuiteDefinitionOutput
}

func (*SuiteDefinition) ElementType() reflect.Type {
	return reflect.TypeOf((**SuiteDefinition)(nil)).Elem()
}

func (i *SuiteDefinition) ToSuiteDefinitionOutput() SuiteDefinitionOutput {
	return i.ToSuiteDefinitionOutputWithContext(context.Background())
}

func (i *SuiteDefinition) ToSuiteDefinitionOutputWithContext(ctx context.Context) SuiteDefinitionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SuiteDefinitionOutput)
}

type SuiteDefinitionOutput struct{ *pulumi.OutputState }

func (SuiteDefinitionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SuiteDefinition)(nil)).Elem()
}

func (o SuiteDefinitionOutput) ToSuiteDefinitionOutput() SuiteDefinitionOutput {
	return o
}

func (o SuiteDefinitionOutput) ToSuiteDefinitionOutputWithContext(ctx context.Context) SuiteDefinitionOutput {
	return o
}

// The Amazon Resource name for the suite definition.
func (o SuiteDefinitionOutput) SuiteDefinitionArn() pulumi.StringOutput {
	return o.ApplyT(func(v *SuiteDefinition) pulumi.StringOutput { return v.SuiteDefinitionArn }).(pulumi.StringOutput)
}

func (o SuiteDefinitionOutput) SuiteDefinitionConfiguration() SuiteDefinitionConfigurationPropertiesOutput {
	return o.ApplyT(func(v *SuiteDefinition) SuiteDefinitionConfigurationPropertiesOutput {
		return v.SuiteDefinitionConfiguration
	}).(SuiteDefinitionConfigurationPropertiesOutput)
}

// The unique identifier for the suite definition.
func (o SuiteDefinitionOutput) SuiteDefinitionId() pulumi.StringOutput {
	return o.ApplyT(func(v *SuiteDefinition) pulumi.StringOutput { return v.SuiteDefinitionId }).(pulumi.StringOutput)
}

// The suite definition version of a test suite.
func (o SuiteDefinitionOutput) SuiteDefinitionVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *SuiteDefinition) pulumi.StringOutput { return v.SuiteDefinitionVersion }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o SuiteDefinitionOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *SuiteDefinition) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SuiteDefinitionInput)(nil)).Elem(), &SuiteDefinition{})
	pulumi.RegisterOutputType(SuiteDefinitionOutput{})
}
