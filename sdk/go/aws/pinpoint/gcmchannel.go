// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Pinpoint::GCMChannel
//
// Deprecated: GCMChannel is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type GCMChannel struct {
	pulumi.CustomResourceState

	ApiKey        pulumi.StringOutput  `pulumi:"apiKey"`
	ApplicationId pulumi.StringOutput  `pulumi:"applicationId"`
	Enabled       pulumi.BoolPtrOutput `pulumi:"enabled"`
}

// NewGCMChannel registers a new resource with the given unique name, arguments, and options.
func NewGCMChannel(ctx *pulumi.Context,
	name string, args *GCMChannelArgs, opts ...pulumi.ResourceOption) (*GCMChannel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApiKey == nil {
		return nil, errors.New("invalid value for required argument 'ApiKey'")
	}
	if args.ApplicationId == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationId'")
	}
	var resource GCMChannel
	err := ctx.RegisterResource("aws-native:pinpoint:GCMChannel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGCMChannel gets an existing GCMChannel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGCMChannel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GCMChannelState, opts ...pulumi.ResourceOption) (*GCMChannel, error) {
	var resource GCMChannel
	err := ctx.ReadResource("aws-native:pinpoint:GCMChannel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GCMChannel resources.
type gcmchannelState struct {
}

type GCMChannelState struct {
}

func (GCMChannelState) ElementType() reflect.Type {
	return reflect.TypeOf((*gcmchannelState)(nil)).Elem()
}

type gcmchannelArgs struct {
	ApiKey        string `pulumi:"apiKey"`
	ApplicationId string `pulumi:"applicationId"`
	Enabled       *bool  `pulumi:"enabled"`
}

// The set of arguments for constructing a GCMChannel resource.
type GCMChannelArgs struct {
	ApiKey        pulumi.StringInput
	ApplicationId pulumi.StringInput
	Enabled       pulumi.BoolPtrInput
}

func (GCMChannelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*gcmchannelArgs)(nil)).Elem()
}

type GCMChannelInput interface {
	pulumi.Input

	ToGCMChannelOutput() GCMChannelOutput
	ToGCMChannelOutputWithContext(ctx context.Context) GCMChannelOutput
}

func (*GCMChannel) ElementType() reflect.Type {
	return reflect.TypeOf((*GCMChannel)(nil))
}

func (i *GCMChannel) ToGCMChannelOutput() GCMChannelOutput {
	return i.ToGCMChannelOutputWithContext(context.Background())
}

func (i *GCMChannel) ToGCMChannelOutputWithContext(ctx context.Context) GCMChannelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GCMChannelOutput)
}

type GCMChannelOutput struct{ *pulumi.OutputState }

func (GCMChannelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GCMChannel)(nil))
}

func (o GCMChannelOutput) ToGCMChannelOutput() GCMChannelOutput {
	return o
}

func (o GCMChannelOutput) ToGCMChannelOutputWithContext(ctx context.Context) GCMChannelOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(GCMChannelOutput{})
}
