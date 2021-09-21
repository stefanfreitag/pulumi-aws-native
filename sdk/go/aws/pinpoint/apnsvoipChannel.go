// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Pinpoint::APNSVoipChannel
//
// Deprecated: APNSVoipChannel is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type APNSVoipChannel struct {
	pulumi.CustomResourceState

	ApplicationId               pulumi.StringOutput    `pulumi:"applicationId"`
	BundleId                    pulumi.StringPtrOutput `pulumi:"bundleId"`
	Certificate                 pulumi.StringPtrOutput `pulumi:"certificate"`
	DefaultAuthenticationMethod pulumi.StringPtrOutput `pulumi:"defaultAuthenticationMethod"`
	Enabled                     pulumi.BoolPtrOutput   `pulumi:"enabled"`
	PrivateKey                  pulumi.StringPtrOutput `pulumi:"privateKey"`
	TeamId                      pulumi.StringPtrOutput `pulumi:"teamId"`
	TokenKey                    pulumi.StringPtrOutput `pulumi:"tokenKey"`
	TokenKeyId                  pulumi.StringPtrOutput `pulumi:"tokenKeyId"`
}

// NewAPNSVoipChannel registers a new resource with the given unique name, arguments, and options.
func NewAPNSVoipChannel(ctx *pulumi.Context,
	name string, args *APNSVoipChannelArgs, opts ...pulumi.ResourceOption) (*APNSVoipChannel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApplicationId == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationId'")
	}
	var resource APNSVoipChannel
	err := ctx.RegisterResource("aws-native:pinpoint:APNSVoipChannel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAPNSVoipChannel gets an existing APNSVoipChannel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAPNSVoipChannel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *APNSVoipChannelState, opts ...pulumi.ResourceOption) (*APNSVoipChannel, error) {
	var resource APNSVoipChannel
	err := ctx.ReadResource("aws-native:pinpoint:APNSVoipChannel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering APNSVoipChannel resources.
type apnsvoipChannelState struct {
}

type APNSVoipChannelState struct {
}

func (APNSVoipChannelState) ElementType() reflect.Type {
	return reflect.TypeOf((*apnsvoipChannelState)(nil)).Elem()
}

type apnsvoipChannelArgs struct {
	ApplicationId               string  `pulumi:"applicationId"`
	BundleId                    *string `pulumi:"bundleId"`
	Certificate                 *string `pulumi:"certificate"`
	DefaultAuthenticationMethod *string `pulumi:"defaultAuthenticationMethod"`
	Enabled                     *bool   `pulumi:"enabled"`
	PrivateKey                  *string `pulumi:"privateKey"`
	TeamId                      *string `pulumi:"teamId"`
	TokenKey                    *string `pulumi:"tokenKey"`
	TokenKeyId                  *string `pulumi:"tokenKeyId"`
}

// The set of arguments for constructing a APNSVoipChannel resource.
type APNSVoipChannelArgs struct {
	ApplicationId               pulumi.StringInput
	BundleId                    pulumi.StringPtrInput
	Certificate                 pulumi.StringPtrInput
	DefaultAuthenticationMethod pulumi.StringPtrInput
	Enabled                     pulumi.BoolPtrInput
	PrivateKey                  pulumi.StringPtrInput
	TeamId                      pulumi.StringPtrInput
	TokenKey                    pulumi.StringPtrInput
	TokenKeyId                  pulumi.StringPtrInput
}

func (APNSVoipChannelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*apnsvoipChannelArgs)(nil)).Elem()
}

type APNSVoipChannelInput interface {
	pulumi.Input

	ToAPNSVoipChannelOutput() APNSVoipChannelOutput
	ToAPNSVoipChannelOutputWithContext(ctx context.Context) APNSVoipChannelOutput
}

func (*APNSVoipChannel) ElementType() reflect.Type {
	return reflect.TypeOf((*APNSVoipChannel)(nil))
}

func (i *APNSVoipChannel) ToAPNSVoipChannelOutput() APNSVoipChannelOutput {
	return i.ToAPNSVoipChannelOutputWithContext(context.Background())
}

func (i *APNSVoipChannel) ToAPNSVoipChannelOutputWithContext(ctx context.Context) APNSVoipChannelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(APNSVoipChannelOutput)
}

type APNSVoipChannelOutput struct{ *pulumi.OutputState }

func (APNSVoipChannelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*APNSVoipChannel)(nil))
}

func (o APNSVoipChannelOutput) ToAPNSVoipChannelOutput() APNSVoipChannelOutput {
	return o
}

func (o APNSVoipChannelOutput) ToAPNSVoipChannelOutputWithContext(ctx context.Context) APNSVoipChannelOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(APNSVoipChannelOutput{})
}
