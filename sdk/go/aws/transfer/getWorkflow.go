// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package transfer

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Transfer::Workflow
func LookupWorkflow(ctx *pulumi.Context, args *LookupWorkflowArgs, opts ...pulumi.InvokeOption) (*LookupWorkflowResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupWorkflowResult
	err := ctx.Invoke("aws-native:transfer:getWorkflow", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupWorkflowArgs struct {
	// A unique identifier for the workflow.
	WorkflowId string `pulumi:"workflowId"`
}

type LookupWorkflowResult struct {
	// Specifies the unique Amazon Resource Name (ARN) for the workflow.
	Arn *string `pulumi:"arn"`
	// Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.
	Tags []WorkflowTag `pulumi:"tags"`
	// A unique identifier for the workflow.
	WorkflowId *string `pulumi:"workflowId"`
}

func LookupWorkflowOutput(ctx *pulumi.Context, args LookupWorkflowOutputArgs, opts ...pulumi.InvokeOption) LookupWorkflowResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupWorkflowResult, error) {
			args := v.(LookupWorkflowArgs)
			r, err := LookupWorkflow(ctx, &args, opts...)
			var s LookupWorkflowResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupWorkflowResultOutput)
}

type LookupWorkflowOutputArgs struct {
	// A unique identifier for the workflow.
	WorkflowId pulumi.StringInput `pulumi:"workflowId"`
}

func (LookupWorkflowOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWorkflowArgs)(nil)).Elem()
}

type LookupWorkflowResultOutput struct{ *pulumi.OutputState }

func (LookupWorkflowResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWorkflowResult)(nil)).Elem()
}

func (o LookupWorkflowResultOutput) ToLookupWorkflowResultOutput() LookupWorkflowResultOutput {
	return o
}

func (o LookupWorkflowResultOutput) ToLookupWorkflowResultOutputWithContext(ctx context.Context) LookupWorkflowResultOutput {
	return o
}

func (o LookupWorkflowResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupWorkflowResult] {
	return pulumix.Output[LookupWorkflowResult]{
		OutputState: o.OutputState,
	}
}

// Specifies the unique Amazon Resource Name (ARN) for the workflow.
func (o LookupWorkflowResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWorkflowResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.
func (o LookupWorkflowResultOutput) Tags() WorkflowTagArrayOutput {
	return o.ApplyT(func(v LookupWorkflowResult) []WorkflowTag { return v.Tags }).(WorkflowTagArrayOutput)
}

// A unique identifier for the workflow.
func (o LookupWorkflowResultOutput) WorkflowId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWorkflowResult) *string { return v.WorkflowId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupWorkflowResultOutput{})
}
