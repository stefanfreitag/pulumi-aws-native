// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The “AWS::ApiGateway::ApiKey“ resource creates a unique key that you can distribute to clients who are executing API Gateway “Method“ resources that require an API key. To specify which API key clients must use, map the API key with the “RestApi“ and “Stage“ resources that include the methods that require a key.
func LookupApiKey(ctx *pulumi.Context, args *LookupApiKeyArgs, opts ...pulumi.InvokeOption) (*LookupApiKeyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupApiKeyResult
	err := ctx.Invoke("aws-native:apigateway:getApiKey", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupApiKeyArgs struct {
	// A Unique Key ID which identifies the API Key. Generated by the Create API and returned by the Read and List APIs
	ApiKeyId string `pulumi:"apiKeyId"`
}

type LookupApiKeyResult struct {
	// A Unique Key ID which identifies the API Key. Generated by the Create API and returned by the Read and List APIs
	ApiKeyId *string `pulumi:"apiKeyId"`
	// An MKT customer identifier, when integrating with the AWS SaaS Marketplace.
	CustomerId *string `pulumi:"customerId"`
	// The description of the ApiKey.
	Description *string `pulumi:"description"`
	// Specifies whether the ApiKey can be used by callers.
	Enabled *bool `pulumi:"enabled"`
	// DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.
	StageKeys []ApiKeyStageKey `pulumi:"stageKeys"`
	// The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with ``aws:``. The tag value can be up to 256 characters.
	Tags []ApiKeyTag `pulumi:"tags"`
}

func LookupApiKeyOutput(ctx *pulumi.Context, args LookupApiKeyOutputArgs, opts ...pulumi.InvokeOption) LookupApiKeyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupApiKeyResult, error) {
			args := v.(LookupApiKeyArgs)
			r, err := LookupApiKey(ctx, &args, opts...)
			var s LookupApiKeyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupApiKeyResultOutput)
}

type LookupApiKeyOutputArgs struct {
	// A Unique Key ID which identifies the API Key. Generated by the Create API and returned by the Read and List APIs
	ApiKeyId pulumi.StringInput `pulumi:"apiKeyId"`
}

func (LookupApiKeyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApiKeyArgs)(nil)).Elem()
}

type LookupApiKeyResultOutput struct{ *pulumi.OutputState }

func (LookupApiKeyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApiKeyResult)(nil)).Elem()
}

func (o LookupApiKeyResultOutput) ToLookupApiKeyResultOutput() LookupApiKeyResultOutput {
	return o
}

func (o LookupApiKeyResultOutput) ToLookupApiKeyResultOutputWithContext(ctx context.Context) LookupApiKeyResultOutput {
	return o
}

func (o LookupApiKeyResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupApiKeyResult] {
	return pulumix.Output[LookupApiKeyResult]{
		OutputState: o.OutputState,
	}
}

// A Unique Key ID which identifies the API Key. Generated by the Create API and returned by the Read and List APIs
func (o LookupApiKeyResultOutput) ApiKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApiKeyResult) *string { return v.ApiKeyId }).(pulumi.StringPtrOutput)
}

// An MKT customer identifier, when integrating with the AWS SaaS Marketplace.
func (o LookupApiKeyResultOutput) CustomerId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApiKeyResult) *string { return v.CustomerId }).(pulumi.StringPtrOutput)
}

// The description of the ApiKey.
func (o LookupApiKeyResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApiKeyResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Specifies whether the ApiKey can be used by callers.
func (o LookupApiKeyResultOutput) Enabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupApiKeyResult) *bool { return v.Enabled }).(pulumi.BoolPtrOutput)
}

// DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.
func (o LookupApiKeyResultOutput) StageKeys() ApiKeyStageKeyArrayOutput {
	return o.ApplyT(func(v LookupApiKeyResult) []ApiKeyStageKey { return v.StageKeys }).(ApiKeyStageKeyArrayOutput)
}

// The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with “aws:“. The tag value can be up to 256 characters.
func (o LookupApiKeyResultOutput) Tags() ApiKeyTagArrayOutput {
	return o.ApplyT(func(v LookupApiKeyResult) []ApiKeyTag { return v.Tags }).(ApiKeyTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupApiKeyResultOutput{})
}
