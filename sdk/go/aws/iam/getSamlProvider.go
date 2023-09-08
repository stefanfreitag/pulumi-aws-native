// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::IAM::SAMLProvider
func LookupSamlProvider(ctx *pulumi.Context, args *LookupSamlProviderArgs, opts ...pulumi.InvokeOption) (*LookupSamlProviderResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSamlProviderResult
	err := ctx.Invoke("aws-native:iam:getSamlProvider", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSamlProviderArgs struct {
	// Amazon Resource Name (ARN) of the SAML provider
	Arn string `pulumi:"arn"`
}

type LookupSamlProviderResult struct {
	// Amazon Resource Name (ARN) of the SAML provider
	Arn                  *string           `pulumi:"arn"`
	SamlMetadataDocument *string           `pulumi:"samlMetadataDocument"`
	Tags                 []SamlProviderTag `pulumi:"tags"`
}

func LookupSamlProviderOutput(ctx *pulumi.Context, args LookupSamlProviderOutputArgs, opts ...pulumi.InvokeOption) LookupSamlProviderResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSamlProviderResult, error) {
			args := v.(LookupSamlProviderArgs)
			r, err := LookupSamlProvider(ctx, &args, opts...)
			var s LookupSamlProviderResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSamlProviderResultOutput)
}

type LookupSamlProviderOutputArgs struct {
	// Amazon Resource Name (ARN) of the SAML provider
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupSamlProviderOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSamlProviderArgs)(nil)).Elem()
}

type LookupSamlProviderResultOutput struct{ *pulumi.OutputState }

func (LookupSamlProviderResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSamlProviderResult)(nil)).Elem()
}

func (o LookupSamlProviderResultOutput) ToLookupSamlProviderResultOutput() LookupSamlProviderResultOutput {
	return o
}

func (o LookupSamlProviderResultOutput) ToLookupSamlProviderResultOutputWithContext(ctx context.Context) LookupSamlProviderResultOutput {
	return o
}

func (o LookupSamlProviderResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupSamlProviderResult] {
	return pulumix.Output[LookupSamlProviderResult]{
		OutputState: o.OutputState,
	}
}

// Amazon Resource Name (ARN) of the SAML provider
func (o LookupSamlProviderResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSamlProviderResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupSamlProviderResultOutput) SamlMetadataDocument() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSamlProviderResult) *string { return v.SamlMetadataDocument }).(pulumi.StringPtrOutput)
}

func (o LookupSamlProviderResultOutput) Tags() SamlProviderTagArrayOutput {
	return o.ApplyT(func(v LookupSamlProviderResult) []SamlProviderTag { return v.Tags }).(SamlProviderTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSamlProviderResultOutput{})
}
