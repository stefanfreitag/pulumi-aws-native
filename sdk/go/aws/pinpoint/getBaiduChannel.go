// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Pinpoint::BaiduChannel
func LookupBaiduChannel(ctx *pulumi.Context, args *LookupBaiduChannelArgs, opts ...pulumi.InvokeOption) (*LookupBaiduChannelResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupBaiduChannelResult
	err := ctx.Invoke("aws-native:pinpoint:getBaiduChannel", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupBaiduChannelArgs struct {
	Id string `pulumi:"id"`
}

type LookupBaiduChannelResult struct {
	ApiKey    *string `pulumi:"apiKey"`
	Enabled   *bool   `pulumi:"enabled"`
	Id        *string `pulumi:"id"`
	SecretKey *string `pulumi:"secretKey"`
}

func LookupBaiduChannelOutput(ctx *pulumi.Context, args LookupBaiduChannelOutputArgs, opts ...pulumi.InvokeOption) LookupBaiduChannelResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupBaiduChannelResult, error) {
			args := v.(LookupBaiduChannelArgs)
			r, err := LookupBaiduChannel(ctx, &args, opts...)
			var s LookupBaiduChannelResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupBaiduChannelResultOutput)
}

type LookupBaiduChannelOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupBaiduChannelOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBaiduChannelArgs)(nil)).Elem()
}

type LookupBaiduChannelResultOutput struct{ *pulumi.OutputState }

func (LookupBaiduChannelResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBaiduChannelResult)(nil)).Elem()
}

func (o LookupBaiduChannelResultOutput) ToLookupBaiduChannelResultOutput() LookupBaiduChannelResultOutput {
	return o
}

func (o LookupBaiduChannelResultOutput) ToLookupBaiduChannelResultOutputWithContext(ctx context.Context) LookupBaiduChannelResultOutput {
	return o
}

func (o LookupBaiduChannelResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupBaiduChannelResult] {
	return pulumix.Output[LookupBaiduChannelResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupBaiduChannelResultOutput) ApiKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupBaiduChannelResult) *string { return v.ApiKey }).(pulumi.StringPtrOutput)
}

func (o LookupBaiduChannelResultOutput) Enabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupBaiduChannelResult) *bool { return v.Enabled }).(pulumi.BoolPtrOutput)
}

func (o LookupBaiduChannelResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupBaiduChannelResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupBaiduChannelResultOutput) SecretKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupBaiduChannelResult) *string { return v.SecretKey }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBaiduChannelResultOutput{})
}
