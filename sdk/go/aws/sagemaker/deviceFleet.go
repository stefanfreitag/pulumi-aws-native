// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::SageMaker::DeviceFleet
type DeviceFleet struct {
	pulumi.CustomResourceState

	// Description for the edge device fleet
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The name of the edge device fleet
	DeviceFleetName pulumi.StringOutput `pulumi:"deviceFleetName"`
	// S3 bucket and an ecryption key id (if available) to store outputs for the fleet
	OutputConfig DeviceFleetEdgeOutputConfigOutput `pulumi:"outputConfig"`
	// Role associated with the device fleet
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// Associate tags with the resource
	Tags DeviceFleetTagArrayOutput `pulumi:"tags"`
}

// NewDeviceFleet registers a new resource with the given unique name, arguments, and options.
func NewDeviceFleet(ctx *pulumi.Context,
	name string, args *DeviceFleetArgs, opts ...pulumi.ResourceOption) (*DeviceFleet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.OutputConfig == nil {
		return nil, errors.New("invalid value for required argument 'OutputConfig'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"deviceFleetName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DeviceFleet
	err := ctx.RegisterResource("aws-native:sagemaker:DeviceFleet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeviceFleet gets an existing DeviceFleet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeviceFleet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeviceFleetState, opts ...pulumi.ResourceOption) (*DeviceFleet, error) {
	var resource DeviceFleet
	err := ctx.ReadResource("aws-native:sagemaker:DeviceFleet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DeviceFleet resources.
type deviceFleetState struct {
}

type DeviceFleetState struct {
}

func (DeviceFleetState) ElementType() reflect.Type {
	return reflect.TypeOf((*deviceFleetState)(nil)).Elem()
}

type deviceFleetArgs struct {
	// Description for the edge device fleet
	Description *string `pulumi:"description"`
	// The name of the edge device fleet
	DeviceFleetName *string `pulumi:"deviceFleetName"`
	// S3 bucket and an ecryption key id (if available) to store outputs for the fleet
	OutputConfig DeviceFleetEdgeOutputConfig `pulumi:"outputConfig"`
	// Role associated with the device fleet
	RoleArn string `pulumi:"roleArn"`
	// Associate tags with the resource
	Tags []DeviceFleetTag `pulumi:"tags"`
}

// The set of arguments for constructing a DeviceFleet resource.
type DeviceFleetArgs struct {
	// Description for the edge device fleet
	Description pulumi.StringPtrInput
	// The name of the edge device fleet
	DeviceFleetName pulumi.StringPtrInput
	// S3 bucket and an ecryption key id (if available) to store outputs for the fleet
	OutputConfig DeviceFleetEdgeOutputConfigInput
	// Role associated with the device fleet
	RoleArn pulumi.StringInput
	// Associate tags with the resource
	Tags DeviceFleetTagArrayInput
}

func (DeviceFleetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deviceFleetArgs)(nil)).Elem()
}

type DeviceFleetInput interface {
	pulumi.Input

	ToDeviceFleetOutput() DeviceFleetOutput
	ToDeviceFleetOutputWithContext(ctx context.Context) DeviceFleetOutput
}

func (*DeviceFleet) ElementType() reflect.Type {
	return reflect.TypeOf((**DeviceFleet)(nil)).Elem()
}

func (i *DeviceFleet) ToDeviceFleetOutput() DeviceFleetOutput {
	return i.ToDeviceFleetOutputWithContext(context.Background())
}

func (i *DeviceFleet) ToDeviceFleetOutputWithContext(ctx context.Context) DeviceFleetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeviceFleetOutput)
}

func (i *DeviceFleet) ToOutput(ctx context.Context) pulumix.Output[*DeviceFleet] {
	return pulumix.Output[*DeviceFleet]{
		OutputState: i.ToDeviceFleetOutputWithContext(ctx).OutputState,
	}
}

type DeviceFleetOutput struct{ *pulumi.OutputState }

func (DeviceFleetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DeviceFleet)(nil)).Elem()
}

func (o DeviceFleetOutput) ToDeviceFleetOutput() DeviceFleetOutput {
	return o
}

func (o DeviceFleetOutput) ToDeviceFleetOutputWithContext(ctx context.Context) DeviceFleetOutput {
	return o
}

func (o DeviceFleetOutput) ToOutput(ctx context.Context) pulumix.Output[*DeviceFleet] {
	return pulumix.Output[*DeviceFleet]{
		OutputState: o.OutputState,
	}
}

// Description for the edge device fleet
func (o DeviceFleetOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeviceFleet) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The name of the edge device fleet
func (o DeviceFleetOutput) DeviceFleetName() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceFleet) pulumi.StringOutput { return v.DeviceFleetName }).(pulumi.StringOutput)
}

// S3 bucket and an ecryption key id (if available) to store outputs for the fleet
func (o DeviceFleetOutput) OutputConfig() DeviceFleetEdgeOutputConfigOutput {
	return o.ApplyT(func(v *DeviceFleet) DeviceFleetEdgeOutputConfigOutput { return v.OutputConfig }).(DeviceFleetEdgeOutputConfigOutput)
}

// Role associated with the device fleet
func (o DeviceFleetOutput) RoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceFleet) pulumi.StringOutput { return v.RoleArn }).(pulumi.StringOutput)
}

// Associate tags with the resource
func (o DeviceFleetOutput) Tags() DeviceFleetTagArrayOutput {
	return o.ApplyT(func(v *DeviceFleet) DeviceFleetTagArrayOutput { return v.Tags }).(DeviceFleetTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DeviceFleetInput)(nil)).Elem(), &DeviceFleet{})
	pulumi.RegisterOutputType(DeviceFleetOutput{})
}
