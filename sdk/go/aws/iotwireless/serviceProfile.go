// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotwireless

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// An example resource schema demonstrating some basic constructs and validation rules.
type ServiceProfile struct {
	pulumi.CustomResourceState

	// Service profile Arn. Returned after successful create.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// LoRaWAN supports all LoRa specific attributes for service profile for CreateServiceProfile operation
	LoRaWan ServiceProfileLoRaWanServiceProfilePtrOutput `pulumi:"loRaWan"`
	// Name of service profile
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// A list of key-value pairs that contain metadata for the service profile.
	Tags ServiceProfileTagArrayOutput `pulumi:"tags"`
}

// NewServiceProfile registers a new resource with the given unique name, arguments, and options.
func NewServiceProfile(ctx *pulumi.Context,
	name string, args *ServiceProfileArgs, opts ...pulumi.ResourceOption) (*ServiceProfile, error) {
	if args == nil {
		args = &ServiceProfileArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ServiceProfile
	err := ctx.RegisterResource("aws-native:iotwireless:ServiceProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServiceProfile gets an existing ServiceProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServiceProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceProfileState, opts ...pulumi.ResourceOption) (*ServiceProfile, error) {
	var resource ServiceProfile
	err := ctx.ReadResource("aws-native:iotwireless:ServiceProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServiceProfile resources.
type serviceProfileState struct {
}

type ServiceProfileState struct {
}

func (ServiceProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceProfileState)(nil)).Elem()
}

type serviceProfileArgs struct {
	// LoRaWAN supports all LoRa specific attributes for service profile for CreateServiceProfile operation
	LoRaWan *ServiceProfileLoRaWanServiceProfile `pulumi:"loRaWan"`
	// Name of service profile
	Name *string `pulumi:"name"`
	// A list of key-value pairs that contain metadata for the service profile.
	Tags []ServiceProfileTag `pulumi:"tags"`
}

// The set of arguments for constructing a ServiceProfile resource.
type ServiceProfileArgs struct {
	// LoRaWAN supports all LoRa specific attributes for service profile for CreateServiceProfile operation
	LoRaWan ServiceProfileLoRaWanServiceProfilePtrInput
	// Name of service profile
	Name pulumi.StringPtrInput
	// A list of key-value pairs that contain metadata for the service profile.
	Tags ServiceProfileTagArrayInput
}

func (ServiceProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceProfileArgs)(nil)).Elem()
}

type ServiceProfileInput interface {
	pulumi.Input

	ToServiceProfileOutput() ServiceProfileOutput
	ToServiceProfileOutputWithContext(ctx context.Context) ServiceProfileOutput
}

func (*ServiceProfile) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceProfile)(nil)).Elem()
}

func (i *ServiceProfile) ToServiceProfileOutput() ServiceProfileOutput {
	return i.ToServiceProfileOutputWithContext(context.Background())
}

func (i *ServiceProfile) ToServiceProfileOutputWithContext(ctx context.Context) ServiceProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceProfileOutput)
}

func (i *ServiceProfile) ToOutput(ctx context.Context) pulumix.Output[*ServiceProfile] {
	return pulumix.Output[*ServiceProfile]{
		OutputState: i.ToServiceProfileOutputWithContext(ctx).OutputState,
	}
}

type ServiceProfileOutput struct{ *pulumi.OutputState }

func (ServiceProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceProfile)(nil)).Elem()
}

func (o ServiceProfileOutput) ToServiceProfileOutput() ServiceProfileOutput {
	return o
}

func (o ServiceProfileOutput) ToServiceProfileOutputWithContext(ctx context.Context) ServiceProfileOutput {
	return o
}

func (o ServiceProfileOutput) ToOutput(ctx context.Context) pulumix.Output[*ServiceProfile] {
	return pulumix.Output[*ServiceProfile]{
		OutputState: o.OutputState,
	}
}

// Service profile Arn. Returned after successful create.
func (o ServiceProfileOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceProfile) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// LoRaWAN supports all LoRa specific attributes for service profile for CreateServiceProfile operation
func (o ServiceProfileOutput) LoRaWan() ServiceProfileLoRaWanServiceProfilePtrOutput {
	return o.ApplyT(func(v *ServiceProfile) ServiceProfileLoRaWanServiceProfilePtrOutput { return v.LoRaWan }).(ServiceProfileLoRaWanServiceProfilePtrOutput)
}

// Name of service profile
func (o ServiceProfileOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ServiceProfile) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// A list of key-value pairs that contain metadata for the service profile.
func (o ServiceProfileOutput) Tags() ServiceProfileTagArrayOutput {
	return o.ApplyT(func(v *ServiceProfile) ServiceProfileTagArrayOutput { return v.Tags }).(ServiceProfileTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceProfileInput)(nil)).Elem(), &ServiceProfile{})
	pulumi.RegisterOutputType(ServiceProfileOutput{})
}
