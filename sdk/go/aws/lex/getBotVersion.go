// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lex

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.
func LookupBotVersion(ctx *pulumi.Context, args *LookupBotVersionArgs, opts ...pulumi.InvokeOption) (*LookupBotVersionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupBotVersionResult
	err := ctx.Invoke("aws-native:lex:getBotVersion", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupBotVersionArgs struct {
	BotId      string `pulumi:"botId"`
	BotVersion string `pulumi:"botVersion"`
}

type LookupBotVersionResult struct {
	BotVersion  *string `pulumi:"botVersion"`
	Description *string `pulumi:"description"`
}

func LookupBotVersionOutput(ctx *pulumi.Context, args LookupBotVersionOutputArgs, opts ...pulumi.InvokeOption) LookupBotVersionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupBotVersionResult, error) {
			args := v.(LookupBotVersionArgs)
			r, err := LookupBotVersion(ctx, &args, opts...)
			var s LookupBotVersionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupBotVersionResultOutput)
}

type LookupBotVersionOutputArgs struct {
	BotId      pulumi.StringInput `pulumi:"botId"`
	BotVersion pulumi.StringInput `pulumi:"botVersion"`
}

func (LookupBotVersionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBotVersionArgs)(nil)).Elem()
}

type LookupBotVersionResultOutput struct{ *pulumi.OutputState }

func (LookupBotVersionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBotVersionResult)(nil)).Elem()
}

func (o LookupBotVersionResultOutput) ToLookupBotVersionResultOutput() LookupBotVersionResultOutput {
	return o
}

func (o LookupBotVersionResultOutput) ToLookupBotVersionResultOutputWithContext(ctx context.Context) LookupBotVersionResultOutput {
	return o
}

func (o LookupBotVersionResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupBotVersionResult] {
	return pulumix.Output[LookupBotVersionResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupBotVersionResultOutput) BotVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupBotVersionResult) *string { return v.BotVersion }).(pulumi.StringPtrOutput)
}

func (o LookupBotVersionResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupBotVersionResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBotVersionResultOutput{})
}
