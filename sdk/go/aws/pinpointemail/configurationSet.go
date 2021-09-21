// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpointemail

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::PinpointEmail::ConfigurationSet
//
// Deprecated: ConfigurationSet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ConfigurationSet struct {
	pulumi.CustomResourceState

	DeliveryOptions   ConfigurationSetDeliveryOptionsPtrOutput   `pulumi:"deliveryOptions"`
	Name              pulumi.StringOutput                        `pulumi:"name"`
	ReputationOptions ConfigurationSetReputationOptionsPtrOutput `pulumi:"reputationOptions"`
	SendingOptions    ConfigurationSetSendingOptionsPtrOutput    `pulumi:"sendingOptions"`
	Tags              ConfigurationSetTagsArrayOutput            `pulumi:"tags"`
	TrackingOptions   ConfigurationSetTrackingOptionsPtrOutput   `pulumi:"trackingOptions"`
}

// NewConfigurationSet registers a new resource with the given unique name, arguments, and options.
func NewConfigurationSet(ctx *pulumi.Context,
	name string, args *ConfigurationSetArgs, opts ...pulumi.ResourceOption) (*ConfigurationSet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource ConfigurationSet
	err := ctx.RegisterResource("aws-native:pinpointemail:ConfigurationSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfigurationSet gets an existing ConfigurationSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfigurationSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigurationSetState, opts ...pulumi.ResourceOption) (*ConfigurationSet, error) {
	var resource ConfigurationSet
	err := ctx.ReadResource("aws-native:pinpointemail:ConfigurationSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConfigurationSet resources.
type configurationSetState struct {
}

type ConfigurationSetState struct {
}

func (ConfigurationSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationSetState)(nil)).Elem()
}

type configurationSetArgs struct {
	DeliveryOptions   *ConfigurationSetDeliveryOptions   `pulumi:"deliveryOptions"`
	Name              string                             `pulumi:"name"`
	ReputationOptions *ConfigurationSetReputationOptions `pulumi:"reputationOptions"`
	SendingOptions    *ConfigurationSetSendingOptions    `pulumi:"sendingOptions"`
	Tags              []ConfigurationSetTags             `pulumi:"tags"`
	TrackingOptions   *ConfigurationSetTrackingOptions   `pulumi:"trackingOptions"`
}

// The set of arguments for constructing a ConfigurationSet resource.
type ConfigurationSetArgs struct {
	DeliveryOptions   ConfigurationSetDeliveryOptionsPtrInput
	Name              pulumi.StringInput
	ReputationOptions ConfigurationSetReputationOptionsPtrInput
	SendingOptions    ConfigurationSetSendingOptionsPtrInput
	Tags              ConfigurationSetTagsArrayInput
	TrackingOptions   ConfigurationSetTrackingOptionsPtrInput
}

func (ConfigurationSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationSetArgs)(nil)).Elem()
}

type ConfigurationSetInput interface {
	pulumi.Input

	ToConfigurationSetOutput() ConfigurationSetOutput
	ToConfigurationSetOutputWithContext(ctx context.Context) ConfigurationSetOutput
}

func (*ConfigurationSet) ElementType() reflect.Type {
	return reflect.TypeOf((*ConfigurationSet)(nil))
}

func (i *ConfigurationSet) ToConfigurationSetOutput() ConfigurationSetOutput {
	return i.ToConfigurationSetOutputWithContext(context.Background())
}

func (i *ConfigurationSet) ToConfigurationSetOutputWithContext(ctx context.Context) ConfigurationSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigurationSetOutput)
}

type ConfigurationSetOutput struct{ *pulumi.OutputState }

func (ConfigurationSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConfigurationSet)(nil))
}

func (o ConfigurationSetOutput) ToConfigurationSetOutput() ConfigurationSetOutput {
	return o
}

func (o ConfigurationSetOutput) ToConfigurationSetOutputWithContext(ctx context.Context) ConfigurationSetOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ConfigurationSetOutput{})
}
