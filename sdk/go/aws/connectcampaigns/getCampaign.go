// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package connectcampaigns

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::ConnectCampaigns::Campaign Resource Type
func LookupCampaign(ctx *pulumi.Context, args *LookupCampaignArgs, opts ...pulumi.InvokeOption) (*LookupCampaignResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCampaignResult
	err := ctx.Invoke("aws-native:connectcampaigns:getCampaign", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCampaignArgs struct {
	// Amazon Connect Campaign Arn
	Arn string `pulumi:"arn"`
}

type LookupCampaignResult struct {
	// Amazon Connect Campaign Arn
	Arn          *string               `pulumi:"arn"`
	DialerConfig *CampaignDialerConfig `pulumi:"dialerConfig"`
	// Amazon Connect Campaign Name
	Name               *string                     `pulumi:"name"`
	OutboundCallConfig *CampaignOutboundCallConfig `pulumi:"outboundCallConfig"`
	// One or more tags.
	Tags []CampaignTag `pulumi:"tags"`
}

func LookupCampaignOutput(ctx *pulumi.Context, args LookupCampaignOutputArgs, opts ...pulumi.InvokeOption) LookupCampaignResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCampaignResult, error) {
			args := v.(LookupCampaignArgs)
			r, err := LookupCampaign(ctx, &args, opts...)
			var s LookupCampaignResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCampaignResultOutput)
}

type LookupCampaignOutputArgs struct {
	// Amazon Connect Campaign Arn
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupCampaignOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCampaignArgs)(nil)).Elem()
}

type LookupCampaignResultOutput struct{ *pulumi.OutputState }

func (LookupCampaignResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCampaignResult)(nil)).Elem()
}

func (o LookupCampaignResultOutput) ToLookupCampaignResultOutput() LookupCampaignResultOutput {
	return o
}

func (o LookupCampaignResultOutput) ToLookupCampaignResultOutputWithContext(ctx context.Context) LookupCampaignResultOutput {
	return o
}

func (o LookupCampaignResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupCampaignResult] {
	return pulumix.Output[LookupCampaignResult]{
		OutputState: o.OutputState,
	}
}

// Amazon Connect Campaign Arn
func (o LookupCampaignResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCampaignResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupCampaignResultOutput) DialerConfig() CampaignDialerConfigPtrOutput {
	return o.ApplyT(func(v LookupCampaignResult) *CampaignDialerConfig { return v.DialerConfig }).(CampaignDialerConfigPtrOutput)
}

// Amazon Connect Campaign Name
func (o LookupCampaignResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCampaignResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupCampaignResultOutput) OutboundCallConfig() CampaignOutboundCallConfigPtrOutput {
	return o.ApplyT(func(v LookupCampaignResult) *CampaignOutboundCallConfig { return v.OutboundCallConfig }).(CampaignOutboundCallConfigPtrOutput)
}

// One or more tags.
func (o LookupCampaignResultOutput) Tags() CampaignTagArrayOutput {
	return o.ApplyT(func(v LookupCampaignResult) []CampaignTag { return v.Tags }).(CampaignTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCampaignResultOutput{})
}
