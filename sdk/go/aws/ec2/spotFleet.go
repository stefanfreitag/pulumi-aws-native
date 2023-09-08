// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::EC2::SpotFleet
type SpotFleet struct {
	pulumi.CustomResourceState

	SpotFleetRequestConfigData SpotFleetRequestConfigDataOutput `pulumi:"spotFleetRequestConfigData"`
}

// NewSpotFleet registers a new resource with the given unique name, arguments, and options.
func NewSpotFleet(ctx *pulumi.Context,
	name string, args *SpotFleetArgs, opts ...pulumi.ResourceOption) (*SpotFleet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SpotFleetRequestConfigData == nil {
		return nil, errors.New("invalid value for required argument 'SpotFleetRequestConfigData'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"spotFleetRequestConfigData.allocationStrategy",
		"spotFleetRequestConfigData.iamFleetRole",
		"spotFleetRequestConfigData.instanceInterruptionBehavior",
		"spotFleetRequestConfigData.instancePoolsToUseCount",
		"spotFleetRequestConfigData.launchSpecifications[*]",
		"spotFleetRequestConfigData.launchTemplateConfigs[*]",
		"spotFleetRequestConfigData.loadBalancersConfig",
		"spotFleetRequestConfigData.onDemandAllocationStrategy",
		"spotFleetRequestConfigData.onDemandMaxTotalPrice",
		"spotFleetRequestConfigData.onDemandTargetCapacity",
		"spotFleetRequestConfigData.replaceUnhealthyInstances",
		"spotFleetRequestConfigData.spotMaintenanceStrategies",
		"spotFleetRequestConfigData.spotMaxTotalPrice",
		"spotFleetRequestConfigData.spotPrice",
		"spotFleetRequestConfigData.tagSpecifications[*]",
		"spotFleetRequestConfigData.terminateInstancesWithExpiration",
		"spotFleetRequestConfigData.type",
		"spotFleetRequestConfigData.validFrom",
		"spotFleetRequestConfigData.validUntil",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SpotFleet
	err := ctx.RegisterResource("aws-native:ec2:SpotFleet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSpotFleet gets an existing SpotFleet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSpotFleet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SpotFleetState, opts ...pulumi.ResourceOption) (*SpotFleet, error) {
	var resource SpotFleet
	err := ctx.ReadResource("aws-native:ec2:SpotFleet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SpotFleet resources.
type spotFleetState struct {
}

type SpotFleetState struct {
}

func (SpotFleetState) ElementType() reflect.Type {
	return reflect.TypeOf((*spotFleetState)(nil)).Elem()
}

type spotFleetArgs struct {
	SpotFleetRequestConfigData SpotFleetRequestConfigData `pulumi:"spotFleetRequestConfigData"`
}

// The set of arguments for constructing a SpotFleet resource.
type SpotFleetArgs struct {
	SpotFleetRequestConfigData SpotFleetRequestConfigDataInput
}

func (SpotFleetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*spotFleetArgs)(nil)).Elem()
}

type SpotFleetInput interface {
	pulumi.Input

	ToSpotFleetOutput() SpotFleetOutput
	ToSpotFleetOutputWithContext(ctx context.Context) SpotFleetOutput
}

func (*SpotFleet) ElementType() reflect.Type {
	return reflect.TypeOf((**SpotFleet)(nil)).Elem()
}

func (i *SpotFleet) ToSpotFleetOutput() SpotFleetOutput {
	return i.ToSpotFleetOutputWithContext(context.Background())
}

func (i *SpotFleet) ToSpotFleetOutputWithContext(ctx context.Context) SpotFleetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SpotFleetOutput)
}

func (i *SpotFleet) ToOutput(ctx context.Context) pulumix.Output[*SpotFleet] {
	return pulumix.Output[*SpotFleet]{
		OutputState: i.ToSpotFleetOutputWithContext(ctx).OutputState,
	}
}

type SpotFleetOutput struct{ *pulumi.OutputState }

func (SpotFleetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SpotFleet)(nil)).Elem()
}

func (o SpotFleetOutput) ToSpotFleetOutput() SpotFleetOutput {
	return o
}

func (o SpotFleetOutput) ToSpotFleetOutputWithContext(ctx context.Context) SpotFleetOutput {
	return o
}

func (o SpotFleetOutput) ToOutput(ctx context.Context) pulumix.Output[*SpotFleet] {
	return pulumix.Output[*SpotFleet]{
		OutputState: o.OutputState,
	}
}

func (o SpotFleetOutput) SpotFleetRequestConfigData() SpotFleetRequestConfigDataOutput {
	return o.ApplyT(func(v *SpotFleet) SpotFleetRequestConfigDataOutput { return v.SpotFleetRequestConfigData }).(SpotFleetRequestConfigDataOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SpotFleetInput)(nil)).Elem(), &SpotFleet{})
	pulumi.RegisterOutputType(SpotFleetOutput{})
}
