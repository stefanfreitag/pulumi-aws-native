// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package auditmanager

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// An entity that defines the scope of audit evidence collected by AWS Audit Manager.
func LookupAssessment(ctx *pulumi.Context, args *LookupAssessmentArgs, opts ...pulumi.InvokeOption) (*LookupAssessmentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAssessmentResult
	err := ctx.Invoke("aws-native:auditmanager:getAssessment", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupAssessmentArgs struct {
	AssessmentId string `pulumi:"assessmentId"`
}

type LookupAssessmentResult struct {
	Arn                          *string                       `pulumi:"arn"`
	AssessmentId                 *string                       `pulumi:"assessmentId"`
	AssessmentReportsDestination *AssessmentReportsDestination `pulumi:"assessmentReportsDestination"`
	CreationTime                 *float64                      `pulumi:"creationTime"`
	// The list of delegations.
	Delegations []AssessmentDelegation `pulumi:"delegations"`
	// The list of roles for the specified assessment.
	Roles  []AssessmentRole  `pulumi:"roles"`
	Scope  *AssessmentScope  `pulumi:"scope"`
	Status *AssessmentStatus `pulumi:"status"`
	// The tags associated with the assessment.
	Tags []AssessmentTag `pulumi:"tags"`
}

func LookupAssessmentOutput(ctx *pulumi.Context, args LookupAssessmentOutputArgs, opts ...pulumi.InvokeOption) LookupAssessmentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAssessmentResult, error) {
			args := v.(LookupAssessmentArgs)
			r, err := LookupAssessment(ctx, &args, opts...)
			var s LookupAssessmentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAssessmentResultOutput)
}

type LookupAssessmentOutputArgs struct {
	AssessmentId pulumi.StringInput `pulumi:"assessmentId"`
}

func (LookupAssessmentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAssessmentArgs)(nil)).Elem()
}

type LookupAssessmentResultOutput struct{ *pulumi.OutputState }

func (LookupAssessmentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAssessmentResult)(nil)).Elem()
}

func (o LookupAssessmentResultOutput) ToLookupAssessmentResultOutput() LookupAssessmentResultOutput {
	return o
}

func (o LookupAssessmentResultOutput) ToLookupAssessmentResultOutputWithContext(ctx context.Context) LookupAssessmentResultOutput {
	return o
}

func (o LookupAssessmentResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupAssessmentResult] {
	return pulumix.Output[LookupAssessmentResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupAssessmentResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssessmentResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupAssessmentResultOutput) AssessmentId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssessmentResult) *string { return v.AssessmentId }).(pulumi.StringPtrOutput)
}

func (o LookupAssessmentResultOutput) AssessmentReportsDestination() AssessmentReportsDestinationPtrOutput {
	return o.ApplyT(func(v LookupAssessmentResult) *AssessmentReportsDestination { return v.AssessmentReportsDestination }).(AssessmentReportsDestinationPtrOutput)
}

func (o LookupAssessmentResultOutput) CreationTime() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v LookupAssessmentResult) *float64 { return v.CreationTime }).(pulumi.Float64PtrOutput)
}

// The list of delegations.
func (o LookupAssessmentResultOutput) Delegations() AssessmentDelegationArrayOutput {
	return o.ApplyT(func(v LookupAssessmentResult) []AssessmentDelegation { return v.Delegations }).(AssessmentDelegationArrayOutput)
}

// The list of roles for the specified assessment.
func (o LookupAssessmentResultOutput) Roles() AssessmentRoleArrayOutput {
	return o.ApplyT(func(v LookupAssessmentResult) []AssessmentRole { return v.Roles }).(AssessmentRoleArrayOutput)
}

func (o LookupAssessmentResultOutput) Scope() AssessmentScopePtrOutput {
	return o.ApplyT(func(v LookupAssessmentResult) *AssessmentScope { return v.Scope }).(AssessmentScopePtrOutput)
}

func (o LookupAssessmentResultOutput) Status() AssessmentStatusPtrOutput {
	return o.ApplyT(func(v LookupAssessmentResult) *AssessmentStatus { return v.Status }).(AssessmentStatusPtrOutput)
}

// The tags associated with the assessment.
func (o LookupAssessmentResultOutput) Tags() AssessmentTagArrayOutput {
	return o.ApplyT(func(v LookupAssessmentResult) []AssessmentTag { return v.Tags }).(AssessmentTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAssessmentResultOutput{})
}
