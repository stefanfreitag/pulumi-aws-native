// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package connect

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Connect::Prompt
func LookupPrompt(ctx *pulumi.Context, args *LookupPromptArgs, opts ...pulumi.InvokeOption) (*LookupPromptResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPromptResult
	err := ctx.Invoke("aws-native:connect:getPrompt", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPromptArgs struct {
	// The Amazon Resource Name (ARN) for the prompt.
	PromptArn string `pulumi:"promptArn"`
}

type LookupPromptResult struct {
	// The description of the prompt.
	Description *string `pulumi:"description"`
	// The identifier of the Amazon Connect instance.
	InstanceArn *string `pulumi:"instanceArn"`
	// The name of the prompt.
	Name *string `pulumi:"name"`
	// The Amazon Resource Name (ARN) for the prompt.
	PromptArn *string `pulumi:"promptArn"`
	// An array of key-value pairs to apply to this resource.
	Tags []PromptTag `pulumi:"tags"`
}

func LookupPromptOutput(ctx *pulumi.Context, args LookupPromptOutputArgs, opts ...pulumi.InvokeOption) LookupPromptResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPromptResult, error) {
			args := v.(LookupPromptArgs)
			r, err := LookupPrompt(ctx, &args, opts...)
			var s LookupPromptResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPromptResultOutput)
}

type LookupPromptOutputArgs struct {
	// The Amazon Resource Name (ARN) for the prompt.
	PromptArn pulumi.StringInput `pulumi:"promptArn"`
}

func (LookupPromptOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPromptArgs)(nil)).Elem()
}

type LookupPromptResultOutput struct{ *pulumi.OutputState }

func (LookupPromptResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPromptResult)(nil)).Elem()
}

func (o LookupPromptResultOutput) ToLookupPromptResultOutput() LookupPromptResultOutput {
	return o
}

func (o LookupPromptResultOutput) ToLookupPromptResultOutputWithContext(ctx context.Context) LookupPromptResultOutput {
	return o
}

func (o LookupPromptResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupPromptResult] {
	return pulumix.Output[LookupPromptResult]{
		OutputState: o.OutputState,
	}
}

// The description of the prompt.
func (o LookupPromptResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPromptResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The identifier of the Amazon Connect instance.
func (o LookupPromptResultOutput) InstanceArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPromptResult) *string { return v.InstanceArn }).(pulumi.StringPtrOutput)
}

// The name of the prompt.
func (o LookupPromptResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPromptResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) for the prompt.
func (o LookupPromptResultOutput) PromptArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPromptResult) *string { return v.PromptArn }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupPromptResultOutput) Tags() PromptTagArrayOutput {
	return o.ApplyT(func(v LookupPromptResult) []PromptTag { return v.Tags }).(PromptTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPromptResultOutput{})
}
