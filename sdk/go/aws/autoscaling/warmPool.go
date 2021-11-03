// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package autoscaling

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::AutoScaling::WarmPool.
type WarmPool struct {
	pulumi.CustomResourceState

	AutoScalingGroupName     pulumi.StringOutput    `pulumi:"autoScalingGroupName"`
	MaxGroupPreparedCapacity pulumi.IntPtrOutput    `pulumi:"maxGroupPreparedCapacity"`
	MinSize                  pulumi.IntPtrOutput    `pulumi:"minSize"`
	PoolState                pulumi.StringPtrOutput `pulumi:"poolState"`
}

// NewWarmPool registers a new resource with the given unique name, arguments, and options.
func NewWarmPool(ctx *pulumi.Context,
	name string, args *WarmPoolArgs, opts ...pulumi.ResourceOption) (*WarmPool, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AutoScalingGroupName == nil {
		return nil, errors.New("invalid value for required argument 'AutoScalingGroupName'")
	}
	var resource WarmPool
	err := ctx.RegisterResource("aws-native:autoscaling:WarmPool", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWarmPool gets an existing WarmPool resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWarmPool(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WarmPoolState, opts ...pulumi.ResourceOption) (*WarmPool, error) {
	var resource WarmPool
	err := ctx.ReadResource("aws-native:autoscaling:WarmPool", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WarmPool resources.
type warmPoolState struct {
}

type WarmPoolState struct {
}

func (WarmPoolState) ElementType() reflect.Type {
	return reflect.TypeOf((*warmPoolState)(nil)).Elem()
}

type warmPoolArgs struct {
	AutoScalingGroupName     string  `pulumi:"autoScalingGroupName"`
	MaxGroupPreparedCapacity *int    `pulumi:"maxGroupPreparedCapacity"`
	MinSize                  *int    `pulumi:"minSize"`
	PoolState                *string `pulumi:"poolState"`
}

// The set of arguments for constructing a WarmPool resource.
type WarmPoolArgs struct {
	AutoScalingGroupName     pulumi.StringInput
	MaxGroupPreparedCapacity pulumi.IntPtrInput
	MinSize                  pulumi.IntPtrInput
	PoolState                pulumi.StringPtrInput
}

func (WarmPoolArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*warmPoolArgs)(nil)).Elem()
}

type WarmPoolInput interface {
	pulumi.Input

	ToWarmPoolOutput() WarmPoolOutput
	ToWarmPoolOutputWithContext(ctx context.Context) WarmPoolOutput
}

func (*WarmPool) ElementType() reflect.Type {
	return reflect.TypeOf((*WarmPool)(nil))
}

func (i *WarmPool) ToWarmPoolOutput() WarmPoolOutput {
	return i.ToWarmPoolOutputWithContext(context.Background())
}

func (i *WarmPool) ToWarmPoolOutputWithContext(ctx context.Context) WarmPoolOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WarmPoolOutput)
}

type WarmPoolOutput struct{ *pulumi.OutputState }

func (WarmPoolOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*WarmPool)(nil))
}

func (o WarmPoolOutput) ToWarmPoolOutput() WarmPoolOutput {
	return o
}

func (o WarmPoolOutput) ToWarmPoolOutputWithContext(ctx context.Context) WarmPoolOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WarmPoolInput)(nil)).Elem(), &WarmPool{})
	pulumi.RegisterOutputType(WarmPoolOutput{})
}
