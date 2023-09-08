// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The AWS::EC2::VerifiedAccessInstance resource creates an AWS EC2 Verified Access Instance.
type VerifiedAccessInstance struct {
	pulumi.CustomResourceState

	// Time this Verified Access Instance was created.
	CreationTime pulumi.StringOutput `pulumi:"creationTime"`
	// A description for the AWS Verified Access instance.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Time this Verified Access Instance was last updated.
	LastUpdatedTime pulumi.StringOutput `pulumi:"lastUpdatedTime"`
	// The configuration options for AWS Verified Access instances.
	LoggingConfigurations VerifiedAccessInstanceVerifiedAccessLogsPtrOutput `pulumi:"loggingConfigurations"`
	// An array of key-value pairs to apply to this resource.
	Tags VerifiedAccessInstanceTagArrayOutput `pulumi:"tags"`
	// The ID of the AWS Verified Access instance.
	VerifiedAccessInstanceId pulumi.StringOutput `pulumi:"verifiedAccessInstanceId"`
	// The IDs of the AWS Verified Access trust providers.
	VerifiedAccessTrustProviderIds pulumi.StringArrayOutput `pulumi:"verifiedAccessTrustProviderIds"`
	// AWS Verified Access trust providers.
	VerifiedAccessTrustProviders VerifiedAccessInstanceVerifiedAccessTrustProviderArrayOutput `pulumi:"verifiedAccessTrustProviders"`
}

// NewVerifiedAccessInstance registers a new resource with the given unique name, arguments, and options.
func NewVerifiedAccessInstance(ctx *pulumi.Context,
	name string, args *VerifiedAccessInstanceArgs, opts ...pulumi.ResourceOption) (*VerifiedAccessInstance, error) {
	if args == nil {
		args = &VerifiedAccessInstanceArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VerifiedAccessInstance
	err := ctx.RegisterResource("aws-native:ec2:VerifiedAccessInstance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVerifiedAccessInstance gets an existing VerifiedAccessInstance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVerifiedAccessInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VerifiedAccessInstanceState, opts ...pulumi.ResourceOption) (*VerifiedAccessInstance, error) {
	var resource VerifiedAccessInstance
	err := ctx.ReadResource("aws-native:ec2:VerifiedAccessInstance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VerifiedAccessInstance resources.
type verifiedAccessInstanceState struct {
}

type VerifiedAccessInstanceState struct {
}

func (VerifiedAccessInstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*verifiedAccessInstanceState)(nil)).Elem()
}

type verifiedAccessInstanceArgs struct {
	// A description for the AWS Verified Access instance.
	Description *string `pulumi:"description"`
	// The configuration options for AWS Verified Access instances.
	LoggingConfigurations *VerifiedAccessInstanceVerifiedAccessLogs `pulumi:"loggingConfigurations"`
	// An array of key-value pairs to apply to this resource.
	Tags []VerifiedAccessInstanceTag `pulumi:"tags"`
	// The IDs of the AWS Verified Access trust providers.
	VerifiedAccessTrustProviderIds []string `pulumi:"verifiedAccessTrustProviderIds"`
	// AWS Verified Access trust providers.
	VerifiedAccessTrustProviders []VerifiedAccessInstanceVerifiedAccessTrustProvider `pulumi:"verifiedAccessTrustProviders"`
}

// The set of arguments for constructing a VerifiedAccessInstance resource.
type VerifiedAccessInstanceArgs struct {
	// A description for the AWS Verified Access instance.
	Description pulumi.StringPtrInput
	// The configuration options for AWS Verified Access instances.
	LoggingConfigurations VerifiedAccessInstanceVerifiedAccessLogsPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags VerifiedAccessInstanceTagArrayInput
	// The IDs of the AWS Verified Access trust providers.
	VerifiedAccessTrustProviderIds pulumi.StringArrayInput
	// AWS Verified Access trust providers.
	VerifiedAccessTrustProviders VerifiedAccessInstanceVerifiedAccessTrustProviderArrayInput
}

func (VerifiedAccessInstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*verifiedAccessInstanceArgs)(nil)).Elem()
}

type VerifiedAccessInstanceInput interface {
	pulumi.Input

	ToVerifiedAccessInstanceOutput() VerifiedAccessInstanceOutput
	ToVerifiedAccessInstanceOutputWithContext(ctx context.Context) VerifiedAccessInstanceOutput
}

func (*VerifiedAccessInstance) ElementType() reflect.Type {
	return reflect.TypeOf((**VerifiedAccessInstance)(nil)).Elem()
}

func (i *VerifiedAccessInstance) ToVerifiedAccessInstanceOutput() VerifiedAccessInstanceOutput {
	return i.ToVerifiedAccessInstanceOutputWithContext(context.Background())
}

func (i *VerifiedAccessInstance) ToVerifiedAccessInstanceOutputWithContext(ctx context.Context) VerifiedAccessInstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VerifiedAccessInstanceOutput)
}

func (i *VerifiedAccessInstance) ToOutput(ctx context.Context) pulumix.Output[*VerifiedAccessInstance] {
	return pulumix.Output[*VerifiedAccessInstance]{
		OutputState: i.ToVerifiedAccessInstanceOutputWithContext(ctx).OutputState,
	}
}

type VerifiedAccessInstanceOutput struct{ *pulumi.OutputState }

func (VerifiedAccessInstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VerifiedAccessInstance)(nil)).Elem()
}

func (o VerifiedAccessInstanceOutput) ToVerifiedAccessInstanceOutput() VerifiedAccessInstanceOutput {
	return o
}

func (o VerifiedAccessInstanceOutput) ToVerifiedAccessInstanceOutputWithContext(ctx context.Context) VerifiedAccessInstanceOutput {
	return o
}

func (o VerifiedAccessInstanceOutput) ToOutput(ctx context.Context) pulumix.Output[*VerifiedAccessInstance] {
	return pulumix.Output[*VerifiedAccessInstance]{
		OutputState: o.OutputState,
	}
}

// Time this Verified Access Instance was created.
func (o VerifiedAccessInstanceOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *VerifiedAccessInstance) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

// A description for the AWS Verified Access instance.
func (o VerifiedAccessInstanceOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VerifiedAccessInstance) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Time this Verified Access Instance was last updated.
func (o VerifiedAccessInstanceOutput) LastUpdatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *VerifiedAccessInstance) pulumi.StringOutput { return v.LastUpdatedTime }).(pulumi.StringOutput)
}

// The configuration options for AWS Verified Access instances.
func (o VerifiedAccessInstanceOutput) LoggingConfigurations() VerifiedAccessInstanceVerifiedAccessLogsPtrOutput {
	return o.ApplyT(func(v *VerifiedAccessInstance) VerifiedAccessInstanceVerifiedAccessLogsPtrOutput {
		return v.LoggingConfigurations
	}).(VerifiedAccessInstanceVerifiedAccessLogsPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o VerifiedAccessInstanceOutput) Tags() VerifiedAccessInstanceTagArrayOutput {
	return o.ApplyT(func(v *VerifiedAccessInstance) VerifiedAccessInstanceTagArrayOutput { return v.Tags }).(VerifiedAccessInstanceTagArrayOutput)
}

// The ID of the AWS Verified Access instance.
func (o VerifiedAccessInstanceOutput) VerifiedAccessInstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *VerifiedAccessInstance) pulumi.StringOutput { return v.VerifiedAccessInstanceId }).(pulumi.StringOutput)
}

// The IDs of the AWS Verified Access trust providers.
func (o VerifiedAccessInstanceOutput) VerifiedAccessTrustProviderIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *VerifiedAccessInstance) pulumi.StringArrayOutput { return v.VerifiedAccessTrustProviderIds }).(pulumi.StringArrayOutput)
}

// AWS Verified Access trust providers.
func (o VerifiedAccessInstanceOutput) VerifiedAccessTrustProviders() VerifiedAccessInstanceVerifiedAccessTrustProviderArrayOutput {
	return o.ApplyT(func(v *VerifiedAccessInstance) VerifiedAccessInstanceVerifiedAccessTrustProviderArrayOutput {
		return v.VerifiedAccessTrustProviders
	}).(VerifiedAccessInstanceVerifiedAccessTrustProviderArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VerifiedAccessInstanceInput)(nil)).Elem(), &VerifiedAccessInstance{})
	pulumi.RegisterOutputType(VerifiedAccessInstanceOutput{})
}
