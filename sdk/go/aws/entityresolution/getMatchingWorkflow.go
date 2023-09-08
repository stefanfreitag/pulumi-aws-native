// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package entityresolution

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// MatchingWorkflow defined in AWS Entity Resolution service
func LookupMatchingWorkflow(ctx *pulumi.Context, args *LookupMatchingWorkflowArgs, opts ...pulumi.InvokeOption) (*LookupMatchingWorkflowResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMatchingWorkflowResult
	err := ctx.Invoke("aws-native:entityresolution:getMatchingWorkflow", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupMatchingWorkflowArgs struct {
	// The name of the MatchingWorkflow
	WorkflowName string `pulumi:"workflowName"`
}

type LookupMatchingWorkflowResult struct {
	CreatedAt *string `pulumi:"createdAt"`
	// The description of the MatchingWorkflow
	Description          *string                               `pulumi:"description"`
	InputSourceConfig    []MatchingWorkflowInputSource         `pulumi:"inputSourceConfig"`
	OutputSourceConfig   []MatchingWorkflowOutputSource        `pulumi:"outputSourceConfig"`
	ResolutionTechniques *MatchingWorkflowResolutionTechniques `pulumi:"resolutionTechniques"`
	RoleArn              *string                               `pulumi:"roleArn"`
	Tags                 []MatchingWorkflowTag                 `pulumi:"tags"`
	UpdatedAt            *string                               `pulumi:"updatedAt"`
	WorkflowArn          *string                               `pulumi:"workflowArn"`
}

func LookupMatchingWorkflowOutput(ctx *pulumi.Context, args LookupMatchingWorkflowOutputArgs, opts ...pulumi.InvokeOption) LookupMatchingWorkflowResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMatchingWorkflowResult, error) {
			args := v.(LookupMatchingWorkflowArgs)
			r, err := LookupMatchingWorkflow(ctx, &args, opts...)
			var s LookupMatchingWorkflowResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupMatchingWorkflowResultOutput)
}

type LookupMatchingWorkflowOutputArgs struct {
	// The name of the MatchingWorkflow
	WorkflowName pulumi.StringInput `pulumi:"workflowName"`
}

func (LookupMatchingWorkflowOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMatchingWorkflowArgs)(nil)).Elem()
}

type LookupMatchingWorkflowResultOutput struct{ *pulumi.OutputState }

func (LookupMatchingWorkflowResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMatchingWorkflowResult)(nil)).Elem()
}

func (o LookupMatchingWorkflowResultOutput) ToLookupMatchingWorkflowResultOutput() LookupMatchingWorkflowResultOutput {
	return o
}

func (o LookupMatchingWorkflowResultOutput) ToLookupMatchingWorkflowResultOutputWithContext(ctx context.Context) LookupMatchingWorkflowResultOutput {
	return o
}

func (o LookupMatchingWorkflowResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupMatchingWorkflowResult] {
	return pulumix.Output[LookupMatchingWorkflowResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupMatchingWorkflowResultOutput) CreatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMatchingWorkflowResult) *string { return v.CreatedAt }).(pulumi.StringPtrOutput)
}

// The description of the MatchingWorkflow
func (o LookupMatchingWorkflowResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMatchingWorkflowResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupMatchingWorkflowResultOutput) InputSourceConfig() MatchingWorkflowInputSourceArrayOutput {
	return o.ApplyT(func(v LookupMatchingWorkflowResult) []MatchingWorkflowInputSource { return v.InputSourceConfig }).(MatchingWorkflowInputSourceArrayOutput)
}

func (o LookupMatchingWorkflowResultOutput) OutputSourceConfig() MatchingWorkflowOutputSourceArrayOutput {
	return o.ApplyT(func(v LookupMatchingWorkflowResult) []MatchingWorkflowOutputSource { return v.OutputSourceConfig }).(MatchingWorkflowOutputSourceArrayOutput)
}

func (o LookupMatchingWorkflowResultOutput) ResolutionTechniques() MatchingWorkflowResolutionTechniquesPtrOutput {
	return o.ApplyT(func(v LookupMatchingWorkflowResult) *MatchingWorkflowResolutionTechniques {
		return v.ResolutionTechniques
	}).(MatchingWorkflowResolutionTechniquesPtrOutput)
}

func (o LookupMatchingWorkflowResultOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMatchingWorkflowResult) *string { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func (o LookupMatchingWorkflowResultOutput) Tags() MatchingWorkflowTagArrayOutput {
	return o.ApplyT(func(v LookupMatchingWorkflowResult) []MatchingWorkflowTag { return v.Tags }).(MatchingWorkflowTagArrayOutput)
}

func (o LookupMatchingWorkflowResultOutput) UpdatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMatchingWorkflowResult) *string { return v.UpdatedAt }).(pulumi.StringPtrOutput)
}

func (o LookupMatchingWorkflowResultOutput) WorkflowArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMatchingWorkflowResult) *string { return v.WorkflowArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMatchingWorkflowResultOutput{})
}
