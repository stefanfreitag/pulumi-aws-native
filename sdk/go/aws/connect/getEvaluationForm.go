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

// Resource Type definition for AWS::Connect::EvaluationForm
func LookupEvaluationForm(ctx *pulumi.Context, args *LookupEvaluationFormArgs, opts ...pulumi.InvokeOption) (*LookupEvaluationFormResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupEvaluationFormResult
	err := ctx.Invoke("aws-native:connect:getEvaluationForm", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupEvaluationFormArgs struct {
	// The Amazon Resource Name (ARN) for the evaluation form.
	EvaluationFormArn string `pulumi:"evaluationFormArn"`
}

type LookupEvaluationFormResult struct {
	// The description of the evaluation form.
	Description *string `pulumi:"description"`
	// The Amazon Resource Name (ARN) for the evaluation form.
	EvaluationFormArn *string `pulumi:"evaluationFormArn"`
	// The Amazon Resource Name (ARN) of the instance.
	InstanceArn *string `pulumi:"instanceArn"`
	// The list of evaluation form items.
	Items []EvaluationFormBaseItem `pulumi:"items"`
	// The scoring strategy.
	ScoringStrategy *EvaluationFormScoringStrategy `pulumi:"scoringStrategy"`
	// The status of the evaluation form.
	Status *EvaluationFormStatus `pulumi:"status"`
	// One or more tags.
	Tags []EvaluationFormTag `pulumi:"tags"`
	// The title of the evaluation form.
	Title *string `pulumi:"title"`
}

func LookupEvaluationFormOutput(ctx *pulumi.Context, args LookupEvaluationFormOutputArgs, opts ...pulumi.InvokeOption) LookupEvaluationFormResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupEvaluationFormResult, error) {
			args := v.(LookupEvaluationFormArgs)
			r, err := LookupEvaluationForm(ctx, &args, opts...)
			var s LookupEvaluationFormResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupEvaluationFormResultOutput)
}

type LookupEvaluationFormOutputArgs struct {
	// The Amazon Resource Name (ARN) for the evaluation form.
	EvaluationFormArn pulumi.StringInput `pulumi:"evaluationFormArn"`
}

func (LookupEvaluationFormOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEvaluationFormArgs)(nil)).Elem()
}

type LookupEvaluationFormResultOutput struct{ *pulumi.OutputState }

func (LookupEvaluationFormResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEvaluationFormResult)(nil)).Elem()
}

func (o LookupEvaluationFormResultOutput) ToLookupEvaluationFormResultOutput() LookupEvaluationFormResultOutput {
	return o
}

func (o LookupEvaluationFormResultOutput) ToLookupEvaluationFormResultOutputWithContext(ctx context.Context) LookupEvaluationFormResultOutput {
	return o
}

func (o LookupEvaluationFormResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupEvaluationFormResult] {
	return pulumix.Output[LookupEvaluationFormResult]{
		OutputState: o.OutputState,
	}
}

// The description of the evaluation form.
func (o LookupEvaluationFormResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEvaluationFormResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) for the evaluation form.
func (o LookupEvaluationFormResultOutput) EvaluationFormArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEvaluationFormResult) *string { return v.EvaluationFormArn }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of the instance.
func (o LookupEvaluationFormResultOutput) InstanceArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEvaluationFormResult) *string { return v.InstanceArn }).(pulumi.StringPtrOutput)
}

// The list of evaluation form items.
func (o LookupEvaluationFormResultOutput) Items() EvaluationFormBaseItemArrayOutput {
	return o.ApplyT(func(v LookupEvaluationFormResult) []EvaluationFormBaseItem { return v.Items }).(EvaluationFormBaseItemArrayOutput)
}

// The scoring strategy.
func (o LookupEvaluationFormResultOutput) ScoringStrategy() EvaluationFormScoringStrategyPtrOutput {
	return o.ApplyT(func(v LookupEvaluationFormResult) *EvaluationFormScoringStrategy { return v.ScoringStrategy }).(EvaluationFormScoringStrategyPtrOutput)
}

// The status of the evaluation form.
func (o LookupEvaluationFormResultOutput) Status() EvaluationFormStatusPtrOutput {
	return o.ApplyT(func(v LookupEvaluationFormResult) *EvaluationFormStatus { return v.Status }).(EvaluationFormStatusPtrOutput)
}

// One or more tags.
func (o LookupEvaluationFormResultOutput) Tags() EvaluationFormTagArrayOutput {
	return o.ApplyT(func(v LookupEvaluationFormResult) []EvaluationFormTag { return v.Tags }).(EvaluationFormTagArrayOutput)
}

// The title of the evaluation form.
func (o LookupEvaluationFormResultOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEvaluationFormResult) *string { return v.Title }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupEvaluationFormResultOutput{})
}
