// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicediscovery

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ServiceDiscovery::PrivateDnsNamespace
func LookupPrivateDnsNamespace(ctx *pulumi.Context, args *LookupPrivateDnsNamespaceArgs, opts ...pulumi.InvokeOption) (*LookupPrivateDnsNamespaceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPrivateDnsNamespaceResult
	err := ctx.Invoke("aws-native:servicediscovery:getPrivateDnsNamespace", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPrivateDnsNamespaceArgs struct {
	Id string `pulumi:"id"`
}

type LookupPrivateDnsNamespaceResult struct {
	Arn          *string                        `pulumi:"arn"`
	Description  *string                        `pulumi:"description"`
	HostedZoneId *string                        `pulumi:"hostedZoneId"`
	Id           *string                        `pulumi:"id"`
	Properties   *PrivateDnsNamespaceProperties `pulumi:"properties"`
	Tags         []aws.Tag                      `pulumi:"tags"`
}

func LookupPrivateDnsNamespaceOutput(ctx *pulumi.Context, args LookupPrivateDnsNamespaceOutputArgs, opts ...pulumi.InvokeOption) LookupPrivateDnsNamespaceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPrivateDnsNamespaceResult, error) {
			args := v.(LookupPrivateDnsNamespaceArgs)
			r, err := LookupPrivateDnsNamespace(ctx, &args, opts...)
			var s LookupPrivateDnsNamespaceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPrivateDnsNamespaceResultOutput)
}

type LookupPrivateDnsNamespaceOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupPrivateDnsNamespaceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPrivateDnsNamespaceArgs)(nil)).Elem()
}

type LookupPrivateDnsNamespaceResultOutput struct{ *pulumi.OutputState }

func (LookupPrivateDnsNamespaceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPrivateDnsNamespaceResult)(nil)).Elem()
}

func (o LookupPrivateDnsNamespaceResultOutput) ToLookupPrivateDnsNamespaceResultOutput() LookupPrivateDnsNamespaceResultOutput {
	return o
}

func (o LookupPrivateDnsNamespaceResultOutput) ToLookupPrivateDnsNamespaceResultOutputWithContext(ctx context.Context) LookupPrivateDnsNamespaceResultOutput {
	return o
}

func (o LookupPrivateDnsNamespaceResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPrivateDnsNamespaceResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupPrivateDnsNamespaceResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPrivateDnsNamespaceResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupPrivateDnsNamespaceResultOutput) HostedZoneId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPrivateDnsNamespaceResult) *string { return v.HostedZoneId }).(pulumi.StringPtrOutput)
}

func (o LookupPrivateDnsNamespaceResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPrivateDnsNamespaceResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupPrivateDnsNamespaceResultOutput) Properties() PrivateDnsNamespacePropertiesPtrOutput {
	return o.ApplyT(func(v LookupPrivateDnsNamespaceResult) *PrivateDnsNamespaceProperties { return v.Properties }).(PrivateDnsNamespacePropertiesPtrOutput)
}

func (o LookupPrivateDnsNamespaceResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupPrivateDnsNamespaceResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPrivateDnsNamespaceResultOutput{})
}
