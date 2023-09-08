// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package route53resolver

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfig.
type ResolverQueryLoggingConfig struct {
	pulumi.CustomResourceState

	// Arn
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Count
	AssociationCount pulumi.IntOutput `pulumi:"associationCount"`
	// Rfc3339TimeString
	CreationTime pulumi.StringOutput `pulumi:"creationTime"`
	// The id of the creator request.
	CreatorRequestId pulumi.StringOutput `pulumi:"creatorRequestId"`
	// destination arn
	DestinationArn pulumi.StringPtrOutput `pulumi:"destinationArn"`
	// ResolverQueryLogConfigName
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// AccountId
	OwnerId pulumi.StringOutput `pulumi:"ownerId"`
	// ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
	ShareStatus ResolverQueryLoggingConfigShareStatusOutput `pulumi:"shareStatus"`
	// ResolverQueryLogConfigStatus, possible values are CREATING, CREATED, DELETED AND FAILED.
	Status ResolverQueryLoggingConfigStatusOutput `pulumi:"status"`
}

// NewResolverQueryLoggingConfig registers a new resource with the given unique name, arguments, and options.
func NewResolverQueryLoggingConfig(ctx *pulumi.Context,
	name string, args *ResolverQueryLoggingConfigArgs, opts ...pulumi.ResourceOption) (*ResolverQueryLoggingConfig, error) {
	if args == nil {
		args = &ResolverQueryLoggingConfigArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"destinationArn",
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ResolverQueryLoggingConfig
	err := ctx.RegisterResource("aws-native:route53resolver:ResolverQueryLoggingConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResolverQueryLoggingConfig gets an existing ResolverQueryLoggingConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResolverQueryLoggingConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResolverQueryLoggingConfigState, opts ...pulumi.ResourceOption) (*ResolverQueryLoggingConfig, error) {
	var resource ResolverQueryLoggingConfig
	err := ctx.ReadResource("aws-native:route53resolver:ResolverQueryLoggingConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResolverQueryLoggingConfig resources.
type resolverQueryLoggingConfigState struct {
}

type ResolverQueryLoggingConfigState struct {
}

func (ResolverQueryLoggingConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*resolverQueryLoggingConfigState)(nil)).Elem()
}

type resolverQueryLoggingConfigArgs struct {
	// destination arn
	DestinationArn *string `pulumi:"destinationArn"`
	// ResolverQueryLogConfigName
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a ResolverQueryLoggingConfig resource.
type ResolverQueryLoggingConfigArgs struct {
	// destination arn
	DestinationArn pulumi.StringPtrInput
	// ResolverQueryLogConfigName
	Name pulumi.StringPtrInput
}

func (ResolverQueryLoggingConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resolverQueryLoggingConfigArgs)(nil)).Elem()
}

type ResolverQueryLoggingConfigInput interface {
	pulumi.Input

	ToResolverQueryLoggingConfigOutput() ResolverQueryLoggingConfigOutput
	ToResolverQueryLoggingConfigOutputWithContext(ctx context.Context) ResolverQueryLoggingConfigOutput
}

func (*ResolverQueryLoggingConfig) ElementType() reflect.Type {
	return reflect.TypeOf((**ResolverQueryLoggingConfig)(nil)).Elem()
}

func (i *ResolverQueryLoggingConfig) ToResolverQueryLoggingConfigOutput() ResolverQueryLoggingConfigOutput {
	return i.ToResolverQueryLoggingConfigOutputWithContext(context.Background())
}

func (i *ResolverQueryLoggingConfig) ToResolverQueryLoggingConfigOutputWithContext(ctx context.Context) ResolverQueryLoggingConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResolverQueryLoggingConfigOutput)
}

func (i *ResolverQueryLoggingConfig) ToOutput(ctx context.Context) pulumix.Output[*ResolverQueryLoggingConfig] {
	return pulumix.Output[*ResolverQueryLoggingConfig]{
		OutputState: i.ToResolverQueryLoggingConfigOutputWithContext(ctx).OutputState,
	}
}

type ResolverQueryLoggingConfigOutput struct{ *pulumi.OutputState }

func (ResolverQueryLoggingConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ResolverQueryLoggingConfig)(nil)).Elem()
}

func (o ResolverQueryLoggingConfigOutput) ToResolverQueryLoggingConfigOutput() ResolverQueryLoggingConfigOutput {
	return o
}

func (o ResolverQueryLoggingConfigOutput) ToResolverQueryLoggingConfigOutputWithContext(ctx context.Context) ResolverQueryLoggingConfigOutput {
	return o
}

func (o ResolverQueryLoggingConfigOutput) ToOutput(ctx context.Context) pulumix.Output[*ResolverQueryLoggingConfig] {
	return pulumix.Output[*ResolverQueryLoggingConfig]{
		OutputState: o.OutputState,
	}
}

// Arn
func (o ResolverQueryLoggingConfigOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *ResolverQueryLoggingConfig) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Count
func (o ResolverQueryLoggingConfigOutput) AssociationCount() pulumi.IntOutput {
	return o.ApplyT(func(v *ResolverQueryLoggingConfig) pulumi.IntOutput { return v.AssociationCount }).(pulumi.IntOutput)
}

// Rfc3339TimeString
func (o ResolverQueryLoggingConfigOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *ResolverQueryLoggingConfig) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

// The id of the creator request.
func (o ResolverQueryLoggingConfigOutput) CreatorRequestId() pulumi.StringOutput {
	return o.ApplyT(func(v *ResolverQueryLoggingConfig) pulumi.StringOutput { return v.CreatorRequestId }).(pulumi.StringOutput)
}

// destination arn
func (o ResolverQueryLoggingConfigOutput) DestinationArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ResolverQueryLoggingConfig) pulumi.StringPtrOutput { return v.DestinationArn }).(pulumi.StringPtrOutput)
}

// ResolverQueryLogConfigName
func (o ResolverQueryLoggingConfigOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ResolverQueryLoggingConfig) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// AccountId
func (o ResolverQueryLoggingConfigOutput) OwnerId() pulumi.StringOutput {
	return o.ApplyT(func(v *ResolverQueryLoggingConfig) pulumi.StringOutput { return v.OwnerId }).(pulumi.StringOutput)
}

// ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
func (o ResolverQueryLoggingConfigOutput) ShareStatus() ResolverQueryLoggingConfigShareStatusOutput {
	return o.ApplyT(func(v *ResolverQueryLoggingConfig) ResolverQueryLoggingConfigShareStatusOutput { return v.ShareStatus }).(ResolverQueryLoggingConfigShareStatusOutput)
}

// ResolverQueryLogConfigStatus, possible values are CREATING, CREATED, DELETED AND FAILED.
func (o ResolverQueryLoggingConfigOutput) Status() ResolverQueryLoggingConfigStatusOutput {
	return o.ApplyT(func(v *ResolverQueryLoggingConfig) ResolverQueryLoggingConfigStatusOutput { return v.Status }).(ResolverQueryLoggingConfigStatusOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ResolverQueryLoggingConfigInput)(nil)).Elem(), &ResolverQueryLoggingConfig{})
	pulumi.RegisterOutputType(ResolverQueryLoggingConfigOutput{})
}
