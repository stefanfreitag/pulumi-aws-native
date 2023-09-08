// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Glue::SecurityConfiguration
func LookupSecurityConfiguration(ctx *pulumi.Context, args *LookupSecurityConfigurationArgs, opts ...pulumi.InvokeOption) (*LookupSecurityConfigurationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSecurityConfigurationResult
	err := ctx.Invoke("aws-native:glue:getSecurityConfiguration", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSecurityConfigurationArgs struct {
	Id string `pulumi:"id"`
}

type LookupSecurityConfigurationResult struct {
	EncryptionConfiguration *SecurityConfigurationEncryptionConfiguration `pulumi:"encryptionConfiguration"`
	Id                      *string                                       `pulumi:"id"`
}

func LookupSecurityConfigurationOutput(ctx *pulumi.Context, args LookupSecurityConfigurationOutputArgs, opts ...pulumi.InvokeOption) LookupSecurityConfigurationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSecurityConfigurationResult, error) {
			args := v.(LookupSecurityConfigurationArgs)
			r, err := LookupSecurityConfiguration(ctx, &args, opts...)
			var s LookupSecurityConfigurationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSecurityConfigurationResultOutput)
}

type LookupSecurityConfigurationOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupSecurityConfigurationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSecurityConfigurationArgs)(nil)).Elem()
}

type LookupSecurityConfigurationResultOutput struct{ *pulumi.OutputState }

func (LookupSecurityConfigurationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSecurityConfigurationResult)(nil)).Elem()
}

func (o LookupSecurityConfigurationResultOutput) ToLookupSecurityConfigurationResultOutput() LookupSecurityConfigurationResultOutput {
	return o
}

func (o LookupSecurityConfigurationResultOutput) ToLookupSecurityConfigurationResultOutputWithContext(ctx context.Context) LookupSecurityConfigurationResultOutput {
	return o
}

func (o LookupSecurityConfigurationResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupSecurityConfigurationResult] {
	return pulumix.Output[LookupSecurityConfigurationResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupSecurityConfigurationResultOutput) EncryptionConfiguration() SecurityConfigurationEncryptionConfigurationPtrOutput {
	return o.ApplyT(func(v LookupSecurityConfigurationResult) *SecurityConfigurationEncryptionConfiguration {
		return v.EncryptionConfiguration
	}).(SecurityConfigurationEncryptionConfigurationPtrOutput)
}

func (o LookupSecurityConfigurationResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSecurityConfigurationResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSecurityConfigurationResultOutput{})
}
