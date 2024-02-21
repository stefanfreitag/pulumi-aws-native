// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ssm

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::SSM::Association resource associates an SSM document in AWS Systems Manager with EC2 instances that contain a configuration agent to process the document.
func LookupAssociation(ctx *pulumi.Context, args *LookupAssociationArgs, opts ...pulumi.InvokeOption) (*LookupAssociationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAssociationResult
	err := ctx.Invoke("aws-native:ssm:getAssociation", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupAssociationArgs struct {
	// Unique identifier of the association.
	AssociationId string `pulumi:"associationId"`
}

type LookupAssociationResult struct {
	ApplyOnlyAtCronInterval *bool `pulumi:"applyOnlyAtCronInterval"`
	// Unique identifier of the association.
	AssociationId *string `pulumi:"associationId"`
	// The name of the association.
	AssociationName               *string                        `pulumi:"associationName"`
	AutomationTargetParameterName *string                        `pulumi:"automationTargetParameterName"`
	CalendarNames                 []string                       `pulumi:"calendarNames"`
	ComplianceSeverity            *AssociationComplianceSeverity `pulumi:"complianceSeverity"`
	// The version of the SSM document to associate with the target.
	DocumentVersion *string `pulumi:"documentVersion"`
	// The ID of the instance that the SSM document is associated with.
	InstanceId     *string `pulumi:"instanceId"`
	MaxConcurrency *string `pulumi:"maxConcurrency"`
	MaxErrors      *string `pulumi:"maxErrors"`
	// The name of the SSM document.
	Name           *string                                       `pulumi:"name"`
	OutputLocation *AssociationInstanceAssociationOutputLocation `pulumi:"outputLocation"`
	// Parameter values that the SSM document uses at runtime.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSM::Association` for more information about the expected schema for this property.
	Parameters interface{} `pulumi:"parameters"`
	// A Cron or Rate expression that specifies when the association is applied to the target.
	ScheduleExpression *string                    `pulumi:"scheduleExpression"`
	ScheduleOffset     *int                       `pulumi:"scheduleOffset"`
	SyncCompliance     *AssociationSyncCompliance `pulumi:"syncCompliance"`
	// The targets that the SSM document sends commands to.
	Targets []AssociationTarget `pulumi:"targets"`
}

func LookupAssociationOutput(ctx *pulumi.Context, args LookupAssociationOutputArgs, opts ...pulumi.InvokeOption) LookupAssociationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAssociationResult, error) {
			args := v.(LookupAssociationArgs)
			r, err := LookupAssociation(ctx, &args, opts...)
			var s LookupAssociationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAssociationResultOutput)
}

type LookupAssociationOutputArgs struct {
	// Unique identifier of the association.
	AssociationId pulumi.StringInput `pulumi:"associationId"`
}

func (LookupAssociationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAssociationArgs)(nil)).Elem()
}

type LookupAssociationResultOutput struct{ *pulumi.OutputState }

func (LookupAssociationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAssociationResult)(nil)).Elem()
}

func (o LookupAssociationResultOutput) ToLookupAssociationResultOutput() LookupAssociationResultOutput {
	return o
}

func (o LookupAssociationResultOutput) ToLookupAssociationResultOutputWithContext(ctx context.Context) LookupAssociationResultOutput {
	return o
}

func (o LookupAssociationResultOutput) ApplyOnlyAtCronInterval() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *bool { return v.ApplyOnlyAtCronInterval }).(pulumi.BoolPtrOutput)
}

// Unique identifier of the association.
func (o LookupAssociationResultOutput) AssociationId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *string { return v.AssociationId }).(pulumi.StringPtrOutput)
}

// The name of the association.
func (o LookupAssociationResultOutput) AssociationName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *string { return v.AssociationName }).(pulumi.StringPtrOutput)
}

func (o LookupAssociationResultOutput) AutomationTargetParameterName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *string { return v.AutomationTargetParameterName }).(pulumi.StringPtrOutput)
}

func (o LookupAssociationResultOutput) CalendarNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupAssociationResult) []string { return v.CalendarNames }).(pulumi.StringArrayOutput)
}

func (o LookupAssociationResultOutput) ComplianceSeverity() AssociationComplianceSeverityPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *AssociationComplianceSeverity { return v.ComplianceSeverity }).(AssociationComplianceSeverityPtrOutput)
}

// The version of the SSM document to associate with the target.
func (o LookupAssociationResultOutput) DocumentVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *string { return v.DocumentVersion }).(pulumi.StringPtrOutput)
}

// The ID of the instance that the SSM document is associated with.
func (o LookupAssociationResultOutput) InstanceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *string { return v.InstanceId }).(pulumi.StringPtrOutput)
}

func (o LookupAssociationResultOutput) MaxConcurrency() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *string { return v.MaxConcurrency }).(pulumi.StringPtrOutput)
}

func (o LookupAssociationResultOutput) MaxErrors() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *string { return v.MaxErrors }).(pulumi.StringPtrOutput)
}

// The name of the SSM document.
func (o LookupAssociationResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupAssociationResultOutput) OutputLocation() AssociationInstanceAssociationOutputLocationPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *AssociationInstanceAssociationOutputLocation { return v.OutputLocation }).(AssociationInstanceAssociationOutputLocationPtrOutput)
}

// Parameter values that the SSM document uses at runtime.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSM::Association` for more information about the expected schema for this property.
func (o LookupAssociationResultOutput) Parameters() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupAssociationResult) interface{} { return v.Parameters }).(pulumi.AnyOutput)
}

// A Cron or Rate expression that specifies when the association is applied to the target.
func (o LookupAssociationResultOutput) ScheduleExpression() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *string { return v.ScheduleExpression }).(pulumi.StringPtrOutput)
}

func (o LookupAssociationResultOutput) ScheduleOffset() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *int { return v.ScheduleOffset }).(pulumi.IntPtrOutput)
}

func (o LookupAssociationResultOutput) SyncCompliance() AssociationSyncCompliancePtrOutput {
	return o.ApplyT(func(v LookupAssociationResult) *AssociationSyncCompliance { return v.SyncCompliance }).(AssociationSyncCompliancePtrOutput)
}

// The targets that the SSM document sends commands to.
func (o LookupAssociationResultOutput) Targets() AssociationTargetArrayOutput {
	return o.ApplyT(func(v LookupAssociationResult) []AssociationTarget { return v.Targets }).(AssociationTargetArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAssociationResultOutput{})
}
