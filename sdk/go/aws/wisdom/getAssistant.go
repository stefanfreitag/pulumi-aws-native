// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package wisdom

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::Wisdom::Assistant Resource Type
func LookupAssistant(ctx *pulumi.Context, args *LookupAssistantArgs, opts ...pulumi.InvokeOption) (*LookupAssistantResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAssistantResult
	err := ctx.Invoke("aws-native:wisdom:getAssistant", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupAssistantArgs struct {
	AssistantId string `pulumi:"assistantId"`
}

type LookupAssistantResult struct {
	AssistantArn *string `pulumi:"assistantArn"`
	AssistantId  *string `pulumi:"assistantId"`
}

func LookupAssistantOutput(ctx *pulumi.Context, args LookupAssistantOutputArgs, opts ...pulumi.InvokeOption) LookupAssistantResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAssistantResult, error) {
			args := v.(LookupAssistantArgs)
			r, err := LookupAssistant(ctx, &args, opts...)
			var s LookupAssistantResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAssistantResultOutput)
}

type LookupAssistantOutputArgs struct {
	AssistantId pulumi.StringInput `pulumi:"assistantId"`
}

func (LookupAssistantOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAssistantArgs)(nil)).Elem()
}

type LookupAssistantResultOutput struct{ *pulumi.OutputState }

func (LookupAssistantResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAssistantResult)(nil)).Elem()
}

func (o LookupAssistantResultOutput) ToLookupAssistantResultOutput() LookupAssistantResultOutput {
	return o
}

func (o LookupAssistantResultOutput) ToLookupAssistantResultOutputWithContext(ctx context.Context) LookupAssistantResultOutput {
	return o
}

func (o LookupAssistantResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupAssistantResult] {
	return pulumix.Output[LookupAssistantResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupAssistantResultOutput) AssistantArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssistantResult) *string { return v.AssistantArn }).(pulumi.StringPtrOutput)
}

func (o LookupAssistantResultOutput) AssistantId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssistantResult) *string { return v.AssistantId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAssistantResultOutput{})
}
