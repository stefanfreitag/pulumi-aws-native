// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mediapackagev2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::MediaPackageV2::ChannelPolicy Resource Type
type ChannelPolicy struct {
	pulumi.CustomResourceState

	ChannelGroupName pulumi.StringPtrOutput `pulumi:"channelGroupName"`
	ChannelName      pulumi.StringPtrOutput `pulumi:"channelName"`
	Policy           pulumi.AnyOutput       `pulumi:"policy"`
}

// NewChannelPolicy registers a new resource with the given unique name, arguments, and options.
func NewChannelPolicy(ctx *pulumi.Context,
	name string, args *ChannelPolicyArgs, opts ...pulumi.ResourceOption) (*ChannelPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Policy == nil {
		return nil, errors.New("invalid value for required argument 'Policy'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"channelGroupName",
		"channelName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ChannelPolicy
	err := ctx.RegisterResource("aws-native:mediapackagev2:ChannelPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetChannelPolicy gets an existing ChannelPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetChannelPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ChannelPolicyState, opts ...pulumi.ResourceOption) (*ChannelPolicy, error) {
	var resource ChannelPolicy
	err := ctx.ReadResource("aws-native:mediapackagev2:ChannelPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ChannelPolicy resources.
type channelPolicyState struct {
}

type ChannelPolicyState struct {
}

func (ChannelPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*channelPolicyState)(nil)).Elem()
}

type channelPolicyArgs struct {
	ChannelGroupName *string     `pulumi:"channelGroupName"`
	ChannelName      *string     `pulumi:"channelName"`
	Policy           interface{} `pulumi:"policy"`
}

// The set of arguments for constructing a ChannelPolicy resource.
type ChannelPolicyArgs struct {
	ChannelGroupName pulumi.StringPtrInput
	ChannelName      pulumi.StringPtrInput
	Policy           pulumi.Input
}

func (ChannelPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*channelPolicyArgs)(nil)).Elem()
}

type ChannelPolicyInput interface {
	pulumi.Input

	ToChannelPolicyOutput() ChannelPolicyOutput
	ToChannelPolicyOutputWithContext(ctx context.Context) ChannelPolicyOutput
}

func (*ChannelPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**ChannelPolicy)(nil)).Elem()
}

func (i *ChannelPolicy) ToChannelPolicyOutput() ChannelPolicyOutput {
	return i.ToChannelPolicyOutputWithContext(context.Background())
}

func (i *ChannelPolicy) ToChannelPolicyOutputWithContext(ctx context.Context) ChannelPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ChannelPolicyOutput)
}

func (i *ChannelPolicy) ToOutput(ctx context.Context) pulumix.Output[*ChannelPolicy] {
	return pulumix.Output[*ChannelPolicy]{
		OutputState: i.ToChannelPolicyOutputWithContext(ctx).OutputState,
	}
}

type ChannelPolicyOutput struct{ *pulumi.OutputState }

func (ChannelPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ChannelPolicy)(nil)).Elem()
}

func (o ChannelPolicyOutput) ToChannelPolicyOutput() ChannelPolicyOutput {
	return o
}

func (o ChannelPolicyOutput) ToChannelPolicyOutputWithContext(ctx context.Context) ChannelPolicyOutput {
	return o
}

func (o ChannelPolicyOutput) ToOutput(ctx context.Context) pulumix.Output[*ChannelPolicy] {
	return pulumix.Output[*ChannelPolicy]{
		OutputState: o.OutputState,
	}
}

func (o ChannelPolicyOutput) ChannelGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ChannelPolicy) pulumi.StringPtrOutput { return v.ChannelGroupName }).(pulumi.StringPtrOutput)
}

func (o ChannelPolicyOutput) ChannelName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ChannelPolicy) pulumi.StringPtrOutput { return v.ChannelName }).(pulumi.StringPtrOutput)
}

func (o ChannelPolicyOutput) Policy() pulumi.AnyOutput {
	return o.ApplyT(func(v *ChannelPolicy) pulumi.AnyOutput { return v.Policy }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ChannelPolicyInput)(nil)).Elem(), &ChannelPolicy{})
	pulumi.RegisterOutputType(ChannelPolicyOutput{})
}
