// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package resiliencehub

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type Definition for Resiliency Policy.
type ResiliencyPolicy struct {
	pulumi.CustomResourceState

	// Data Location Constraint of the Policy.
	DataLocationConstraint ResiliencyPolicyDataLocationConstraintPtrOutput `pulumi:"dataLocationConstraint"`
	Policy                 ResiliencyPolicyPolicyMapOutput                 `pulumi:"policy"`
	// Amazon Resource Name (ARN) of the Resiliency Policy.
	PolicyArn pulumi.StringOutput `pulumi:"policyArn"`
	// Description of Resiliency Policy.
	PolicyDescription pulumi.StringPtrOutput `pulumi:"policyDescription"`
	// Name of Resiliency Policy.
	PolicyName pulumi.StringOutput             `pulumi:"policyName"`
	Tags       ResiliencyPolicyTagMapPtrOutput `pulumi:"tags"`
	// Resiliency Policy Tier.
	Tier ResiliencyPolicyTierOutput `pulumi:"tier"`
}

// NewResiliencyPolicy registers a new resource with the given unique name, arguments, and options.
func NewResiliencyPolicy(ctx *pulumi.Context,
	name string, args *ResiliencyPolicyArgs, opts ...pulumi.ResourceOption) (*ResiliencyPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Policy == nil {
		return nil, errors.New("invalid value for required argument 'Policy'")
	}
	if args.PolicyName == nil {
		return nil, errors.New("invalid value for required argument 'PolicyName'")
	}
	if args.Tier == nil {
		return nil, errors.New("invalid value for required argument 'Tier'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ResiliencyPolicy
	err := ctx.RegisterResource("aws-native:resiliencehub:ResiliencyPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResiliencyPolicy gets an existing ResiliencyPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResiliencyPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResiliencyPolicyState, opts ...pulumi.ResourceOption) (*ResiliencyPolicy, error) {
	var resource ResiliencyPolicy
	err := ctx.ReadResource("aws-native:resiliencehub:ResiliencyPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResiliencyPolicy resources.
type resiliencyPolicyState struct {
}

type ResiliencyPolicyState struct {
}

func (ResiliencyPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*resiliencyPolicyState)(nil)).Elem()
}

type resiliencyPolicyArgs struct {
	// Data Location Constraint of the Policy.
	DataLocationConstraint *ResiliencyPolicyDataLocationConstraint `pulumi:"dataLocationConstraint"`
	Policy                 ResiliencyPolicyPolicyMap               `pulumi:"policy"`
	// Description of Resiliency Policy.
	PolicyDescription *string `pulumi:"policyDescription"`
	// Name of Resiliency Policy.
	PolicyName string                  `pulumi:"policyName"`
	Tags       *ResiliencyPolicyTagMap `pulumi:"tags"`
	// Resiliency Policy Tier.
	Tier ResiliencyPolicyTier `pulumi:"tier"`
}

// The set of arguments for constructing a ResiliencyPolicy resource.
type ResiliencyPolicyArgs struct {
	// Data Location Constraint of the Policy.
	DataLocationConstraint ResiliencyPolicyDataLocationConstraintPtrInput
	Policy                 ResiliencyPolicyPolicyMapInput
	// Description of Resiliency Policy.
	PolicyDescription pulumi.StringPtrInput
	// Name of Resiliency Policy.
	PolicyName pulumi.StringInput
	Tags       ResiliencyPolicyTagMapPtrInput
	// Resiliency Policy Tier.
	Tier ResiliencyPolicyTierInput
}

func (ResiliencyPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resiliencyPolicyArgs)(nil)).Elem()
}

type ResiliencyPolicyInput interface {
	pulumi.Input

	ToResiliencyPolicyOutput() ResiliencyPolicyOutput
	ToResiliencyPolicyOutputWithContext(ctx context.Context) ResiliencyPolicyOutput
}

func (*ResiliencyPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**ResiliencyPolicy)(nil)).Elem()
}

func (i *ResiliencyPolicy) ToResiliencyPolicyOutput() ResiliencyPolicyOutput {
	return i.ToResiliencyPolicyOutputWithContext(context.Background())
}

func (i *ResiliencyPolicy) ToResiliencyPolicyOutputWithContext(ctx context.Context) ResiliencyPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResiliencyPolicyOutput)
}

func (i *ResiliencyPolicy) ToOutput(ctx context.Context) pulumix.Output[*ResiliencyPolicy] {
	return pulumix.Output[*ResiliencyPolicy]{
		OutputState: i.ToResiliencyPolicyOutputWithContext(ctx).OutputState,
	}
}

type ResiliencyPolicyOutput struct{ *pulumi.OutputState }

func (ResiliencyPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ResiliencyPolicy)(nil)).Elem()
}

func (o ResiliencyPolicyOutput) ToResiliencyPolicyOutput() ResiliencyPolicyOutput {
	return o
}

func (o ResiliencyPolicyOutput) ToResiliencyPolicyOutputWithContext(ctx context.Context) ResiliencyPolicyOutput {
	return o
}

func (o ResiliencyPolicyOutput) ToOutput(ctx context.Context) pulumix.Output[*ResiliencyPolicy] {
	return pulumix.Output[*ResiliencyPolicy]{
		OutputState: o.OutputState,
	}
}

// Data Location Constraint of the Policy.
func (o ResiliencyPolicyOutput) DataLocationConstraint() ResiliencyPolicyDataLocationConstraintPtrOutput {
	return o.ApplyT(func(v *ResiliencyPolicy) ResiliencyPolicyDataLocationConstraintPtrOutput {
		return v.DataLocationConstraint
	}).(ResiliencyPolicyDataLocationConstraintPtrOutput)
}

func (o ResiliencyPolicyOutput) Policy() ResiliencyPolicyPolicyMapOutput {
	return o.ApplyT(func(v *ResiliencyPolicy) ResiliencyPolicyPolicyMapOutput { return v.Policy }).(ResiliencyPolicyPolicyMapOutput)
}

// Amazon Resource Name (ARN) of the Resiliency Policy.
func (o ResiliencyPolicyOutput) PolicyArn() pulumi.StringOutput {
	return o.ApplyT(func(v *ResiliencyPolicy) pulumi.StringOutput { return v.PolicyArn }).(pulumi.StringOutput)
}

// Description of Resiliency Policy.
func (o ResiliencyPolicyOutput) PolicyDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ResiliencyPolicy) pulumi.StringPtrOutput { return v.PolicyDescription }).(pulumi.StringPtrOutput)
}

// Name of Resiliency Policy.
func (o ResiliencyPolicyOutput) PolicyName() pulumi.StringOutput {
	return o.ApplyT(func(v *ResiliencyPolicy) pulumi.StringOutput { return v.PolicyName }).(pulumi.StringOutput)
}

func (o ResiliencyPolicyOutput) Tags() ResiliencyPolicyTagMapPtrOutput {
	return o.ApplyT(func(v *ResiliencyPolicy) ResiliencyPolicyTagMapPtrOutput { return v.Tags }).(ResiliencyPolicyTagMapPtrOutput)
}

// Resiliency Policy Tier.
func (o ResiliencyPolicyOutput) Tier() ResiliencyPolicyTierOutput {
	return o.ApplyT(func(v *ResiliencyPolicy) ResiliencyPolicyTierOutput { return v.Tier }).(ResiliencyPolicyTierOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ResiliencyPolicyInput)(nil)).Elem(), &ResiliencyPolicy{})
	pulumi.RegisterOutputType(ResiliencyPolicyOutput{})
}
