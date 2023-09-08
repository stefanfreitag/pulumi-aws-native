// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package pinpointemail

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::PinpointEmail::ConfigurationSet
func LookupConfigurationSet(ctx *pulumi.Context, args *LookupConfigurationSetArgs, opts ...pulumi.InvokeOption) (*LookupConfigurationSetResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupConfigurationSetResult
	err := ctx.Invoke("aws-native:pinpointemail:getConfigurationSet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupConfigurationSetArgs struct {
	Id string `pulumi:"id"`
}

type LookupConfigurationSetResult struct {
	DeliveryOptions   *ConfigurationSetDeliveryOptions   `pulumi:"deliveryOptions"`
	Id                *string                            `pulumi:"id"`
	ReputationOptions *ConfigurationSetReputationOptions `pulumi:"reputationOptions"`
	SendingOptions    *ConfigurationSetSendingOptions    `pulumi:"sendingOptions"`
	Tags              []ConfigurationSetTags             `pulumi:"tags"`
	TrackingOptions   *ConfigurationSetTrackingOptions   `pulumi:"trackingOptions"`
}

func LookupConfigurationSetOutput(ctx *pulumi.Context, args LookupConfigurationSetOutputArgs, opts ...pulumi.InvokeOption) LookupConfigurationSetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupConfigurationSetResult, error) {
			args := v.(LookupConfigurationSetArgs)
			r, err := LookupConfigurationSet(ctx, &args, opts...)
			var s LookupConfigurationSetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupConfigurationSetResultOutput)
}

type LookupConfigurationSetOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupConfigurationSetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupConfigurationSetArgs)(nil)).Elem()
}

type LookupConfigurationSetResultOutput struct{ *pulumi.OutputState }

func (LookupConfigurationSetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupConfigurationSetResult)(nil)).Elem()
}

func (o LookupConfigurationSetResultOutput) ToLookupConfigurationSetResultOutput() LookupConfigurationSetResultOutput {
	return o
}

func (o LookupConfigurationSetResultOutput) ToLookupConfigurationSetResultOutputWithContext(ctx context.Context) LookupConfigurationSetResultOutput {
	return o
}

func (o LookupConfigurationSetResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupConfigurationSetResult] {
	return pulumix.Output[LookupConfigurationSetResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupConfigurationSetResultOutput) DeliveryOptions() ConfigurationSetDeliveryOptionsPtrOutput {
	return o.ApplyT(func(v LookupConfigurationSetResult) *ConfigurationSetDeliveryOptions { return v.DeliveryOptions }).(ConfigurationSetDeliveryOptionsPtrOutput)
}

func (o LookupConfigurationSetResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupConfigurationSetResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupConfigurationSetResultOutput) ReputationOptions() ConfigurationSetReputationOptionsPtrOutput {
	return o.ApplyT(func(v LookupConfigurationSetResult) *ConfigurationSetReputationOptions { return v.ReputationOptions }).(ConfigurationSetReputationOptionsPtrOutput)
}

func (o LookupConfigurationSetResultOutput) SendingOptions() ConfigurationSetSendingOptionsPtrOutput {
	return o.ApplyT(func(v LookupConfigurationSetResult) *ConfigurationSetSendingOptions { return v.SendingOptions }).(ConfigurationSetSendingOptionsPtrOutput)
}

func (o LookupConfigurationSetResultOutput) Tags() ConfigurationSetTagsArrayOutput {
	return o.ApplyT(func(v LookupConfigurationSetResult) []ConfigurationSetTags { return v.Tags }).(ConfigurationSetTagsArrayOutput)
}

func (o LookupConfigurationSetResultOutput) TrackingOptions() ConfigurationSetTrackingOptionsPtrOutput {
	return o.ApplyT(func(v LookupConfigurationSetResult) *ConfigurationSetTrackingOptions { return v.TrackingOptions }).(ConfigurationSetTrackingOptionsPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupConfigurationSetResultOutput{})
}
