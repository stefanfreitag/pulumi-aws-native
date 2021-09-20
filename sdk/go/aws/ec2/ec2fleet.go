// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::EC2Fleet
type EC2Fleet struct {
	pulumi.CustomResourceState

	Context                          pulumi.StringPtrOutput                              `pulumi:"context"`
	ExcessCapacityTerminationPolicy  EC2FleetExcessCapacityTerminationPolicyPtrOutput    `pulumi:"excessCapacityTerminationPolicy"`
	FleetId                          pulumi.StringOutput                                 `pulumi:"fleetId"`
	LaunchTemplateConfigs            EC2FleetFleetLaunchTemplateConfigRequestArrayOutput `pulumi:"launchTemplateConfigs"`
	OnDemandOptions                  EC2FleetOnDemandOptionsRequestPtrOutput             `pulumi:"onDemandOptions"`
	ReplaceUnhealthyInstances        pulumi.BoolPtrOutput                                `pulumi:"replaceUnhealthyInstances"`
	SpotOptions                      EC2FleetSpotOptionsRequestPtrOutput                 `pulumi:"spotOptions"`
	TagSpecifications                EC2FleetTagSpecificationArrayOutput                 `pulumi:"tagSpecifications"`
	TargetCapacitySpecification      EC2FleetTargetCapacitySpecificationRequestOutput    `pulumi:"targetCapacitySpecification"`
	TerminateInstancesWithExpiration pulumi.BoolPtrOutput                                `pulumi:"terminateInstancesWithExpiration"`
	Type                             EC2FleetTypePtrOutput                               `pulumi:"type"`
	ValidFrom                        pulumi.StringPtrOutput                              `pulumi:"validFrom"`
	ValidUntil                       pulumi.StringPtrOutput                              `pulumi:"validUntil"`
}

// NewEC2Fleet registers a new resource with the given unique name, arguments, and options.
func NewEC2Fleet(ctx *pulumi.Context,
	name string, args *EC2FleetArgs, opts ...pulumi.ResourceOption) (*EC2Fleet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.LaunchTemplateConfigs == nil {
		return nil, errors.New("invalid value for required argument 'LaunchTemplateConfigs'")
	}
	if args.TargetCapacitySpecification == nil {
		return nil, errors.New("invalid value for required argument 'TargetCapacitySpecification'")
	}
	var resource EC2Fleet
	err := ctx.RegisterResource("aws-native:ec2:EC2Fleet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEC2Fleet gets an existing EC2Fleet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEC2Fleet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EC2FleetState, opts ...pulumi.ResourceOption) (*EC2Fleet, error) {
	var resource EC2Fleet
	err := ctx.ReadResource("aws-native:ec2:EC2Fleet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EC2Fleet resources.
type ec2fleetState struct {
}

type EC2FleetState struct {
}

func (EC2FleetState) ElementType() reflect.Type {
	return reflect.TypeOf((*ec2fleetState)(nil)).Elem()
}

type ec2fleetArgs struct {
	Context                          *string                                    `pulumi:"context"`
	ExcessCapacityTerminationPolicy  *EC2FleetExcessCapacityTerminationPolicy   `pulumi:"excessCapacityTerminationPolicy"`
	LaunchTemplateConfigs            []EC2FleetFleetLaunchTemplateConfigRequest `pulumi:"launchTemplateConfigs"`
	OnDemandOptions                  *EC2FleetOnDemandOptionsRequest            `pulumi:"onDemandOptions"`
	ReplaceUnhealthyInstances        *bool                                      `pulumi:"replaceUnhealthyInstances"`
	SpotOptions                      *EC2FleetSpotOptionsRequest                `pulumi:"spotOptions"`
	TagSpecifications                []EC2FleetTagSpecification                 `pulumi:"tagSpecifications"`
	TargetCapacitySpecification      EC2FleetTargetCapacitySpecificationRequest `pulumi:"targetCapacitySpecification"`
	TerminateInstancesWithExpiration *bool                                      `pulumi:"terminateInstancesWithExpiration"`
	Type                             *EC2FleetType                              `pulumi:"type"`
	ValidFrom                        *string                                    `pulumi:"validFrom"`
	ValidUntil                       *string                                    `pulumi:"validUntil"`
}

// The set of arguments for constructing a EC2Fleet resource.
type EC2FleetArgs struct {
	Context                          pulumi.StringPtrInput
	ExcessCapacityTerminationPolicy  EC2FleetExcessCapacityTerminationPolicyPtrInput
	LaunchTemplateConfigs            EC2FleetFleetLaunchTemplateConfigRequestArrayInput
	OnDemandOptions                  EC2FleetOnDemandOptionsRequestPtrInput
	ReplaceUnhealthyInstances        pulumi.BoolPtrInput
	SpotOptions                      EC2FleetSpotOptionsRequestPtrInput
	TagSpecifications                EC2FleetTagSpecificationArrayInput
	TargetCapacitySpecification      EC2FleetTargetCapacitySpecificationRequestInput
	TerminateInstancesWithExpiration pulumi.BoolPtrInput
	Type                             EC2FleetTypePtrInput
	ValidFrom                        pulumi.StringPtrInput
	ValidUntil                       pulumi.StringPtrInput
}

func (EC2FleetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ec2fleetArgs)(nil)).Elem()
}

type EC2FleetInput interface {
	pulumi.Input

	ToEC2FleetOutput() EC2FleetOutput
	ToEC2FleetOutputWithContext(ctx context.Context) EC2FleetOutput
}

func (*EC2Fleet) ElementType() reflect.Type {
	return reflect.TypeOf((*EC2Fleet)(nil))
}

func (i *EC2Fleet) ToEC2FleetOutput() EC2FleetOutput {
	return i.ToEC2FleetOutputWithContext(context.Background())
}

func (i *EC2Fleet) ToEC2FleetOutputWithContext(ctx context.Context) EC2FleetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EC2FleetOutput)
}

type EC2FleetOutput struct{ *pulumi.OutputState }

func (EC2FleetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EC2Fleet)(nil))
}

func (o EC2FleetOutput) ToEC2FleetOutput() EC2FleetOutput {
	return o
}

func (o EC2FleetOutput) ToEC2FleetOutputWithContext(ctx context.Context) EC2FleetOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(EC2FleetOutput{})
}
