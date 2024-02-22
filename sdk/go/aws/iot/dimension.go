// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A dimension can be used to limit the scope of a metric used in a security profile for AWS IoT Device Defender.
type Dimension struct {
	pulumi.CustomResourceState

	// The ARN (Amazon resource name) of the created dimension.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A unique identifier for the dimension.
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// Specifies the value or list of values for the dimension.
	StringValues pulumi.StringArrayOutput `pulumi:"stringValues"`
	// Metadata that can be used to manage the dimension.
	Tags aws.TagArrayOutput `pulumi:"tags"`
	// Specifies the type of the dimension.
	Type DimensionTypeOutput `pulumi:"type"`
}

// NewDimension registers a new resource with the given unique name, arguments, and options.
func NewDimension(ctx *pulumi.Context,
	name string, args *DimensionArgs, opts ...pulumi.ResourceOption) (*Dimension, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.StringValues == nil {
		return nil, errors.New("invalid value for required argument 'StringValues'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
		"type",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Dimension
	err := ctx.RegisterResource("aws-native:iot:Dimension", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDimension gets an existing Dimension resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDimension(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DimensionState, opts ...pulumi.ResourceOption) (*Dimension, error) {
	var resource Dimension
	err := ctx.ReadResource("aws-native:iot:Dimension", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Dimension resources.
type dimensionState struct {
}

type DimensionState struct {
}

func (DimensionState) ElementType() reflect.Type {
	return reflect.TypeOf((*dimensionState)(nil)).Elem()
}

type dimensionArgs struct {
	// A unique identifier for the dimension.
	Name *string `pulumi:"name"`
	// Specifies the value or list of values for the dimension.
	StringValues []string `pulumi:"stringValues"`
	// Metadata that can be used to manage the dimension.
	Tags []aws.Tag `pulumi:"tags"`
	// Specifies the type of the dimension.
	Type DimensionType `pulumi:"type"`
}

// The set of arguments for constructing a Dimension resource.
type DimensionArgs struct {
	// A unique identifier for the dimension.
	Name pulumi.StringPtrInput
	// Specifies the value or list of values for the dimension.
	StringValues pulumi.StringArrayInput
	// Metadata that can be used to manage the dimension.
	Tags aws.TagArrayInput
	// Specifies the type of the dimension.
	Type DimensionTypeInput
}

func (DimensionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dimensionArgs)(nil)).Elem()
}

type DimensionInput interface {
	pulumi.Input

	ToDimensionOutput() DimensionOutput
	ToDimensionOutputWithContext(ctx context.Context) DimensionOutput
}

func (*Dimension) ElementType() reflect.Type {
	return reflect.TypeOf((**Dimension)(nil)).Elem()
}

func (i *Dimension) ToDimensionOutput() DimensionOutput {
	return i.ToDimensionOutputWithContext(context.Background())
}

func (i *Dimension) ToDimensionOutputWithContext(ctx context.Context) DimensionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DimensionOutput)
}

type DimensionOutput struct{ *pulumi.OutputState }

func (DimensionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Dimension)(nil)).Elem()
}

func (o DimensionOutput) ToDimensionOutput() DimensionOutput {
	return o
}

func (o DimensionOutput) ToDimensionOutputWithContext(ctx context.Context) DimensionOutput {
	return o
}

// The ARN (Amazon resource name) of the created dimension.
func (o DimensionOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Dimension) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// A unique identifier for the dimension.
func (o DimensionOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Dimension) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// Specifies the value or list of values for the dimension.
func (o DimensionOutput) StringValues() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Dimension) pulumi.StringArrayOutput { return v.StringValues }).(pulumi.StringArrayOutput)
}

// Metadata that can be used to manage the dimension.
func (o DimensionOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Dimension) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

// Specifies the type of the dimension.
func (o DimensionOutput) Type() DimensionTypeOutput {
	return o.ApplyT(func(v *Dimension) DimensionTypeOutput { return v.Type }).(DimensionTypeOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DimensionInput)(nil)).Elem(), &Dimension{})
	pulumi.RegisterOutputType(DimensionOutput{})
}
