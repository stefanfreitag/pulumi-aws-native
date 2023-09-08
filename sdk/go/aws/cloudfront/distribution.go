// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudfront

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::CloudFront::Distribution
type Distribution struct {
	pulumi.CustomResourceState

	DistributionConfig DistributionConfigOutput   `pulumi:"distributionConfig"`
	DomainName         pulumi.StringOutput        `pulumi:"domainName"`
	Tags               DistributionTagArrayOutput `pulumi:"tags"`
}

// NewDistribution registers a new resource with the given unique name, arguments, and options.
func NewDistribution(ctx *pulumi.Context,
	name string, args *DistributionArgs, opts ...pulumi.ResourceOption) (*Distribution, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DistributionConfig == nil {
		return nil, errors.New("invalid value for required argument 'DistributionConfig'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Distribution
	err := ctx.RegisterResource("aws-native:cloudfront:Distribution", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDistribution gets an existing Distribution resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDistribution(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DistributionState, opts ...pulumi.ResourceOption) (*Distribution, error) {
	var resource Distribution
	err := ctx.ReadResource("aws-native:cloudfront:Distribution", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Distribution resources.
type distributionState struct {
}

type DistributionState struct {
}

func (DistributionState) ElementType() reflect.Type {
	return reflect.TypeOf((*distributionState)(nil)).Elem()
}

type distributionArgs struct {
	DistributionConfig DistributionConfig `pulumi:"distributionConfig"`
	Tags               []DistributionTag  `pulumi:"tags"`
}

// The set of arguments for constructing a Distribution resource.
type DistributionArgs struct {
	DistributionConfig DistributionConfigInput
	Tags               DistributionTagArrayInput
}

func (DistributionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*distributionArgs)(nil)).Elem()
}

type DistributionInput interface {
	pulumi.Input

	ToDistributionOutput() DistributionOutput
	ToDistributionOutputWithContext(ctx context.Context) DistributionOutput
}

func (*Distribution) ElementType() reflect.Type {
	return reflect.TypeOf((**Distribution)(nil)).Elem()
}

func (i *Distribution) ToDistributionOutput() DistributionOutput {
	return i.ToDistributionOutputWithContext(context.Background())
}

func (i *Distribution) ToDistributionOutputWithContext(ctx context.Context) DistributionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DistributionOutput)
}

func (i *Distribution) ToOutput(ctx context.Context) pulumix.Output[*Distribution] {
	return pulumix.Output[*Distribution]{
		OutputState: i.ToDistributionOutputWithContext(ctx).OutputState,
	}
}

type DistributionOutput struct{ *pulumi.OutputState }

func (DistributionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Distribution)(nil)).Elem()
}

func (o DistributionOutput) ToDistributionOutput() DistributionOutput {
	return o
}

func (o DistributionOutput) ToDistributionOutputWithContext(ctx context.Context) DistributionOutput {
	return o
}

func (o DistributionOutput) ToOutput(ctx context.Context) pulumix.Output[*Distribution] {
	return pulumix.Output[*Distribution]{
		OutputState: o.OutputState,
	}
}

func (o DistributionOutput) DistributionConfig() DistributionConfigOutput {
	return o.ApplyT(func(v *Distribution) DistributionConfigOutput { return v.DistributionConfig }).(DistributionConfigOutput)
}

func (o DistributionOutput) DomainName() pulumi.StringOutput {
	return o.ApplyT(func(v *Distribution) pulumi.StringOutput { return v.DomainName }).(pulumi.StringOutput)
}

func (o DistributionOutput) Tags() DistributionTagArrayOutput {
	return o.ApplyT(func(v *Distribution) DistributionTagArrayOutput { return v.Tags }).(DistributionTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DistributionInput)(nil)).Elem(), &Distribution{})
	pulumi.RegisterOutputType(DistributionOutput{})
}
