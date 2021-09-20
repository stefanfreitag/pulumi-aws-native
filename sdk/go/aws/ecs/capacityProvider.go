// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ecs

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ECS::CapacityProvider.
type CapacityProvider struct {
	pulumi.CustomResourceState

	AutoScalingGroupProvider CapacityProviderAutoScalingGroupProviderOutput `pulumi:"autoScalingGroupProvider"`
	Name                     pulumi.StringPtrOutput                         `pulumi:"name"`
	Tags                     CapacityProviderTagArrayOutput                 `pulumi:"tags"`
}

// NewCapacityProvider registers a new resource with the given unique name, arguments, and options.
func NewCapacityProvider(ctx *pulumi.Context,
	name string, args *CapacityProviderArgs, opts ...pulumi.ResourceOption) (*CapacityProvider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AutoScalingGroupProvider == nil {
		return nil, errors.New("invalid value for required argument 'AutoScalingGroupProvider'")
	}
	var resource CapacityProvider
	err := ctx.RegisterResource("aws-native:ecs:CapacityProvider", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCapacityProvider gets an existing CapacityProvider resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCapacityProvider(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CapacityProviderState, opts ...pulumi.ResourceOption) (*CapacityProvider, error) {
	var resource CapacityProvider
	err := ctx.ReadResource("aws-native:ecs:CapacityProvider", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CapacityProvider resources.
type capacityProviderState struct {
}

type CapacityProviderState struct {
}

func (CapacityProviderState) ElementType() reflect.Type {
	return reflect.TypeOf((*capacityProviderState)(nil)).Elem()
}

type capacityProviderArgs struct {
	AutoScalingGroupProvider CapacityProviderAutoScalingGroupProvider `pulumi:"autoScalingGroupProvider"`
	Name                     *string                                  `pulumi:"name"`
	Tags                     []CapacityProviderTag                    `pulumi:"tags"`
}

// The set of arguments for constructing a CapacityProvider resource.
type CapacityProviderArgs struct {
	AutoScalingGroupProvider CapacityProviderAutoScalingGroupProviderInput
	Name                     pulumi.StringPtrInput
	Tags                     CapacityProviderTagArrayInput
}

func (CapacityProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*capacityProviderArgs)(nil)).Elem()
}

type CapacityProviderInput interface {
	pulumi.Input

	ToCapacityProviderOutput() CapacityProviderOutput
	ToCapacityProviderOutputWithContext(ctx context.Context) CapacityProviderOutput
}

func (*CapacityProvider) ElementType() reflect.Type {
	return reflect.TypeOf((*CapacityProvider)(nil))
}

func (i *CapacityProvider) ToCapacityProviderOutput() CapacityProviderOutput {
	return i.ToCapacityProviderOutputWithContext(context.Background())
}

func (i *CapacityProvider) ToCapacityProviderOutputWithContext(ctx context.Context) CapacityProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CapacityProviderOutput)
}

type CapacityProviderOutput struct{ *pulumi.OutputState }

func (CapacityProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CapacityProvider)(nil))
}

func (o CapacityProviderOutput) ToCapacityProviderOutput() CapacityProviderOutput {
	return o
}

func (o CapacityProviderOutput) ToCapacityProviderOutputWithContext(ctx context.Context) CapacityProviderOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(CapacityProviderOutput{})
}
