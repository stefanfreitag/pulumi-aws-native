// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::IoT::Thing
type Thing struct {
	pulumi.CustomResourceState

	Arn              pulumi.StringOutput            `pulumi:"arn"`
	AttributePayload ThingAttributePayloadPtrOutput `pulumi:"attributePayload"`
	ThingName        pulumi.StringPtrOutput         `pulumi:"thingName"`
}

// NewThing registers a new resource with the given unique name, arguments, and options.
func NewThing(ctx *pulumi.Context,
	name string, args *ThingArgs, opts ...pulumi.ResourceOption) (*Thing, error) {
	if args == nil {
		args = &ThingArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"thingName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Thing
	err := ctx.RegisterResource("aws-native:iot:Thing", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetThing gets an existing Thing resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetThing(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ThingState, opts ...pulumi.ResourceOption) (*Thing, error) {
	var resource Thing
	err := ctx.ReadResource("aws-native:iot:Thing", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Thing resources.
type thingState struct {
}

type ThingState struct {
}

func (ThingState) ElementType() reflect.Type {
	return reflect.TypeOf((*thingState)(nil)).Elem()
}

type thingArgs struct {
	AttributePayload *ThingAttributePayload `pulumi:"attributePayload"`
	ThingName        *string                `pulumi:"thingName"`
}

// The set of arguments for constructing a Thing resource.
type ThingArgs struct {
	AttributePayload ThingAttributePayloadPtrInput
	ThingName        pulumi.StringPtrInput
}

func (ThingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*thingArgs)(nil)).Elem()
}

type ThingInput interface {
	pulumi.Input

	ToThingOutput() ThingOutput
	ToThingOutputWithContext(ctx context.Context) ThingOutput
}

func (*Thing) ElementType() reflect.Type {
	return reflect.TypeOf((**Thing)(nil)).Elem()
}

func (i *Thing) ToThingOutput() ThingOutput {
	return i.ToThingOutputWithContext(context.Background())
}

func (i *Thing) ToThingOutputWithContext(ctx context.Context) ThingOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ThingOutput)
}

func (i *Thing) ToOutput(ctx context.Context) pulumix.Output[*Thing] {
	return pulumix.Output[*Thing]{
		OutputState: i.ToThingOutputWithContext(ctx).OutputState,
	}
}

type ThingOutput struct{ *pulumi.OutputState }

func (ThingOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Thing)(nil)).Elem()
}

func (o ThingOutput) ToThingOutput() ThingOutput {
	return o
}

func (o ThingOutput) ToThingOutputWithContext(ctx context.Context) ThingOutput {
	return o
}

func (o ThingOutput) ToOutput(ctx context.Context) pulumix.Output[*Thing] {
	return pulumix.Output[*Thing]{
		OutputState: o.OutputState,
	}
}

func (o ThingOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Thing) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o ThingOutput) AttributePayload() ThingAttributePayloadPtrOutput {
	return o.ApplyT(func(v *Thing) ThingAttributePayloadPtrOutput { return v.AttributePayload }).(ThingAttributePayloadPtrOutput)
}

func (o ThingOutput) ThingName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Thing) pulumi.StringPtrOutput { return v.ThingName }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ThingInput)(nil)).Elem(), &Thing{})
	pulumi.RegisterOutputType(ThingOutput{})
}
