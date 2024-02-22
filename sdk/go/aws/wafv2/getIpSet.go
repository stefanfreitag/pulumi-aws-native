// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package wafv2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Contains a list of IP addresses. This can be either IPV4 or IPV6. The list will be mutually
func LookupIpSet(ctx *pulumi.Context, args *LookupIpSetArgs, opts ...pulumi.InvokeOption) (*LookupIpSetResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupIpSetResult
	err := ctx.Invoke("aws-native:wafv2:getIpSet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupIpSetArgs struct {
	Id    string     `pulumi:"id"`
	Name  string     `pulumi:"name"`
	Scope IpSetScope `pulumi:"scope"`
}

type LookupIpSetResult struct {
	// List of IPAddresses.
	Addresses        []string               `pulumi:"addresses"`
	Arn              *string                `pulumi:"arn"`
	Description      *string                `pulumi:"description"`
	Id               *string                `pulumi:"id"`
	IpAddressVersion *IpSetIpAddressVersion `pulumi:"ipAddressVersion"`
	Tags             []aws.Tag              `pulumi:"tags"`
}

func LookupIpSetOutput(ctx *pulumi.Context, args LookupIpSetOutputArgs, opts ...pulumi.InvokeOption) LookupIpSetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupIpSetResult, error) {
			args := v.(LookupIpSetArgs)
			r, err := LookupIpSet(ctx, &args, opts...)
			var s LookupIpSetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupIpSetResultOutput)
}

type LookupIpSetOutputArgs struct {
	Id    pulumi.StringInput `pulumi:"id"`
	Name  pulumi.StringInput `pulumi:"name"`
	Scope IpSetScopeInput    `pulumi:"scope"`
}

func (LookupIpSetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpSetArgs)(nil)).Elem()
}

type LookupIpSetResultOutput struct{ *pulumi.OutputState }

func (LookupIpSetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpSetResult)(nil)).Elem()
}

func (o LookupIpSetResultOutput) ToLookupIpSetResultOutput() LookupIpSetResultOutput {
	return o
}

func (o LookupIpSetResultOutput) ToLookupIpSetResultOutputWithContext(ctx context.Context) LookupIpSetResultOutput {
	return o
}

// List of IPAddresses.
func (o LookupIpSetResultOutput) Addresses() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupIpSetResult) []string { return v.Addresses }).(pulumi.StringArrayOutput)
}

func (o LookupIpSetResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpSetResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupIpSetResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpSetResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupIpSetResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpSetResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupIpSetResultOutput) IpAddressVersion() IpSetIpAddressVersionPtrOutput {
	return o.ApplyT(func(v LookupIpSetResult) *IpSetIpAddressVersion { return v.IpAddressVersion }).(IpSetIpAddressVersionPtrOutput)
}

func (o LookupIpSetResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupIpSetResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupIpSetResultOutput{})
}
