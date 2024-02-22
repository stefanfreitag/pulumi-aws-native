// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotfleetwise

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::IoTFleetWise::Fleet Resource Type
//
// Deprecated: Fleet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Fleet struct {
	pulumi.CustomResourceState

	Arn                  pulumi.StringOutput    `pulumi:"arn"`
	CreationTime         pulumi.StringOutput    `pulumi:"creationTime"`
	Description          pulumi.StringPtrOutput `pulumi:"description"`
	LastModificationTime pulumi.StringOutput    `pulumi:"lastModificationTime"`
	SignalCatalogArn     pulumi.StringOutput    `pulumi:"signalCatalogArn"`
	Tags                 aws.TagArrayOutput     `pulumi:"tags"`
}

// NewFleet registers a new resource with the given unique name, arguments, and options.
func NewFleet(ctx *pulumi.Context,
	name string, args *FleetArgs, opts ...pulumi.ResourceOption) (*Fleet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SignalCatalogArn == nil {
		return nil, errors.New("invalid value for required argument 'SignalCatalogArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"signalCatalogArn",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Fleet
	err := ctx.RegisterResource("aws-native:iotfleetwise:Fleet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFleet gets an existing Fleet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFleet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FleetState, opts ...pulumi.ResourceOption) (*Fleet, error) {
	var resource Fleet
	err := ctx.ReadResource("aws-native:iotfleetwise:Fleet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Fleet resources.
type fleetState struct {
}

type FleetState struct {
}

func (FleetState) ElementType() reflect.Type {
	return reflect.TypeOf((*fleetState)(nil)).Elem()
}

type fleetArgs struct {
	Description      *string   `pulumi:"description"`
	SignalCatalogArn string    `pulumi:"signalCatalogArn"`
	Tags             []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a Fleet resource.
type FleetArgs struct {
	Description      pulumi.StringPtrInput
	SignalCatalogArn pulumi.StringInput
	Tags             aws.TagArrayInput
}

func (FleetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*fleetArgs)(nil)).Elem()
}

type FleetInput interface {
	pulumi.Input

	ToFleetOutput() FleetOutput
	ToFleetOutputWithContext(ctx context.Context) FleetOutput
}

func (*Fleet) ElementType() reflect.Type {
	return reflect.TypeOf((**Fleet)(nil)).Elem()
}

func (i *Fleet) ToFleetOutput() FleetOutput {
	return i.ToFleetOutputWithContext(context.Background())
}

func (i *Fleet) ToFleetOutputWithContext(ctx context.Context) FleetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FleetOutput)
}

type FleetOutput struct{ *pulumi.OutputState }

func (FleetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Fleet)(nil)).Elem()
}

func (o FleetOutput) ToFleetOutput() FleetOutput {
	return o
}

func (o FleetOutput) ToFleetOutputWithContext(ctx context.Context) FleetOutput {
	return o
}

func (o FleetOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o FleetOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

func (o FleetOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o FleetOutput) LastModificationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringOutput { return v.LastModificationTime }).(pulumi.StringOutput)
}

func (o FleetOutput) SignalCatalogArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringOutput { return v.SignalCatalogArn }).(pulumi.StringOutput)
}

func (o FleetOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Fleet) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FleetInput)(nil)).Elem(), &Fleet{})
	pulumi.RegisterOutputType(FleetOutput{})
}
