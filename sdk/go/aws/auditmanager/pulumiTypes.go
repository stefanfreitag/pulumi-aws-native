// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package auditmanager

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

// The AWS account associated with the assessment.
type AssessmentAwsAccount struct {
	EmailAddress *string `pulumi:"emailAddress"`
	Id           *string `pulumi:"id"`
	Name         *string `pulumi:"name"`
}

// AssessmentAwsAccountInput is an input type that accepts AssessmentAwsAccountArgs and AssessmentAwsAccountOutput values.
// You can construct a concrete instance of `AssessmentAwsAccountInput` via:
//
//	AssessmentAwsAccountArgs{...}
type AssessmentAwsAccountInput interface {
	pulumi.Input

	ToAssessmentAwsAccountOutput() AssessmentAwsAccountOutput
	ToAssessmentAwsAccountOutputWithContext(context.Context) AssessmentAwsAccountOutput
}

// The AWS account associated with the assessment.
type AssessmentAwsAccountArgs struct {
	EmailAddress pulumi.StringPtrInput `pulumi:"emailAddress"`
	Id           pulumi.StringPtrInput `pulumi:"id"`
	Name         pulumi.StringPtrInput `pulumi:"name"`
}

func (AssessmentAwsAccountArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentAwsAccount)(nil)).Elem()
}

func (i AssessmentAwsAccountArgs) ToAssessmentAwsAccountOutput() AssessmentAwsAccountOutput {
	return i.ToAssessmentAwsAccountOutputWithContext(context.Background())
}

func (i AssessmentAwsAccountArgs) ToAssessmentAwsAccountOutputWithContext(ctx context.Context) AssessmentAwsAccountOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentAwsAccountOutput)
}

func (i AssessmentAwsAccountArgs) ToAssessmentAwsAccountPtrOutput() AssessmentAwsAccountPtrOutput {
	return i.ToAssessmentAwsAccountPtrOutputWithContext(context.Background())
}

func (i AssessmentAwsAccountArgs) ToAssessmentAwsAccountPtrOutputWithContext(ctx context.Context) AssessmentAwsAccountPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentAwsAccountOutput).ToAssessmentAwsAccountPtrOutputWithContext(ctx)
}

// AssessmentAwsAccountPtrInput is an input type that accepts AssessmentAwsAccountArgs, AssessmentAwsAccountPtr and AssessmentAwsAccountPtrOutput values.
// You can construct a concrete instance of `AssessmentAwsAccountPtrInput` via:
//
//	        AssessmentAwsAccountArgs{...}
//
//	or:
//
//	        nil
type AssessmentAwsAccountPtrInput interface {
	pulumi.Input

	ToAssessmentAwsAccountPtrOutput() AssessmentAwsAccountPtrOutput
	ToAssessmentAwsAccountPtrOutputWithContext(context.Context) AssessmentAwsAccountPtrOutput
}

type assessmentAwsAccountPtrType AssessmentAwsAccountArgs

func AssessmentAwsAccountPtr(v *AssessmentAwsAccountArgs) AssessmentAwsAccountPtrInput {
	return (*assessmentAwsAccountPtrType)(v)
}

func (*assessmentAwsAccountPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AssessmentAwsAccount)(nil)).Elem()
}

func (i *assessmentAwsAccountPtrType) ToAssessmentAwsAccountPtrOutput() AssessmentAwsAccountPtrOutput {
	return i.ToAssessmentAwsAccountPtrOutputWithContext(context.Background())
}

func (i *assessmentAwsAccountPtrType) ToAssessmentAwsAccountPtrOutputWithContext(ctx context.Context) AssessmentAwsAccountPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentAwsAccountPtrOutput)
}

// AssessmentAwsAccountArrayInput is an input type that accepts AssessmentAwsAccountArray and AssessmentAwsAccountArrayOutput values.
// You can construct a concrete instance of `AssessmentAwsAccountArrayInput` via:
//
//	AssessmentAwsAccountArray{ AssessmentAwsAccountArgs{...} }
type AssessmentAwsAccountArrayInput interface {
	pulumi.Input

	ToAssessmentAwsAccountArrayOutput() AssessmentAwsAccountArrayOutput
	ToAssessmentAwsAccountArrayOutputWithContext(context.Context) AssessmentAwsAccountArrayOutput
}

type AssessmentAwsAccountArray []AssessmentAwsAccountInput

func (AssessmentAwsAccountArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AssessmentAwsAccount)(nil)).Elem()
}

func (i AssessmentAwsAccountArray) ToAssessmentAwsAccountArrayOutput() AssessmentAwsAccountArrayOutput {
	return i.ToAssessmentAwsAccountArrayOutputWithContext(context.Background())
}

func (i AssessmentAwsAccountArray) ToAssessmentAwsAccountArrayOutputWithContext(ctx context.Context) AssessmentAwsAccountArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentAwsAccountArrayOutput)
}

// The AWS account associated with the assessment.
type AssessmentAwsAccountOutput struct{ *pulumi.OutputState }

func (AssessmentAwsAccountOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentAwsAccount)(nil)).Elem()
}

func (o AssessmentAwsAccountOutput) ToAssessmentAwsAccountOutput() AssessmentAwsAccountOutput {
	return o
}

func (o AssessmentAwsAccountOutput) ToAssessmentAwsAccountOutputWithContext(ctx context.Context) AssessmentAwsAccountOutput {
	return o
}

func (o AssessmentAwsAccountOutput) ToAssessmentAwsAccountPtrOutput() AssessmentAwsAccountPtrOutput {
	return o.ToAssessmentAwsAccountPtrOutputWithContext(context.Background())
}

func (o AssessmentAwsAccountOutput) ToAssessmentAwsAccountPtrOutputWithContext(ctx context.Context) AssessmentAwsAccountPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AssessmentAwsAccount) *AssessmentAwsAccount {
		return &v
	}).(AssessmentAwsAccountPtrOutput)
}

func (o AssessmentAwsAccountOutput) EmailAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentAwsAccount) *string { return v.EmailAddress }).(pulumi.StringPtrOutput)
}

func (o AssessmentAwsAccountOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentAwsAccount) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o AssessmentAwsAccountOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentAwsAccount) *string { return v.Name }).(pulumi.StringPtrOutput)
}

type AssessmentAwsAccountPtrOutput struct{ *pulumi.OutputState }

func (AssessmentAwsAccountPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AssessmentAwsAccount)(nil)).Elem()
}

func (o AssessmentAwsAccountPtrOutput) ToAssessmentAwsAccountPtrOutput() AssessmentAwsAccountPtrOutput {
	return o
}

func (o AssessmentAwsAccountPtrOutput) ToAssessmentAwsAccountPtrOutputWithContext(ctx context.Context) AssessmentAwsAccountPtrOutput {
	return o
}

func (o AssessmentAwsAccountPtrOutput) Elem() AssessmentAwsAccountOutput {
	return o.ApplyT(func(v *AssessmentAwsAccount) AssessmentAwsAccount {
		if v != nil {
			return *v
		}
		var ret AssessmentAwsAccount
		return ret
	}).(AssessmentAwsAccountOutput)
}

func (o AssessmentAwsAccountPtrOutput) EmailAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AssessmentAwsAccount) *string {
		if v == nil {
			return nil
		}
		return v.EmailAddress
	}).(pulumi.StringPtrOutput)
}

func (o AssessmentAwsAccountPtrOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AssessmentAwsAccount) *string {
		if v == nil {
			return nil
		}
		return v.Id
	}).(pulumi.StringPtrOutput)
}

func (o AssessmentAwsAccountPtrOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AssessmentAwsAccount) *string {
		if v == nil {
			return nil
		}
		return v.Name
	}).(pulumi.StringPtrOutput)
}

type AssessmentAwsAccountArrayOutput struct{ *pulumi.OutputState }

func (AssessmentAwsAccountArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AssessmentAwsAccount)(nil)).Elem()
}

func (o AssessmentAwsAccountArrayOutput) ToAssessmentAwsAccountArrayOutput() AssessmentAwsAccountArrayOutput {
	return o
}

func (o AssessmentAwsAccountArrayOutput) ToAssessmentAwsAccountArrayOutputWithContext(ctx context.Context) AssessmentAwsAccountArrayOutput {
	return o
}

func (o AssessmentAwsAccountArrayOutput) Index(i pulumi.IntInput) AssessmentAwsAccountOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AssessmentAwsAccount {
		return vs[0].([]AssessmentAwsAccount)[vs[1].(int)]
	}).(AssessmentAwsAccountOutput)
}

// An AWS service such as Amazon S3, AWS CloudTrail, and so on.
type AssessmentAwsService struct {
	ServiceName *string `pulumi:"serviceName"`
}

// AssessmentAwsServiceInput is an input type that accepts AssessmentAwsServiceArgs and AssessmentAwsServiceOutput values.
// You can construct a concrete instance of `AssessmentAwsServiceInput` via:
//
//	AssessmentAwsServiceArgs{...}
type AssessmentAwsServiceInput interface {
	pulumi.Input

	ToAssessmentAwsServiceOutput() AssessmentAwsServiceOutput
	ToAssessmentAwsServiceOutputWithContext(context.Context) AssessmentAwsServiceOutput
}

// An AWS service such as Amazon S3, AWS CloudTrail, and so on.
type AssessmentAwsServiceArgs struct {
	ServiceName pulumi.StringPtrInput `pulumi:"serviceName"`
}

func (AssessmentAwsServiceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentAwsService)(nil)).Elem()
}

func (i AssessmentAwsServiceArgs) ToAssessmentAwsServiceOutput() AssessmentAwsServiceOutput {
	return i.ToAssessmentAwsServiceOutputWithContext(context.Background())
}

func (i AssessmentAwsServiceArgs) ToAssessmentAwsServiceOutputWithContext(ctx context.Context) AssessmentAwsServiceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentAwsServiceOutput)
}

// AssessmentAwsServiceArrayInput is an input type that accepts AssessmentAwsServiceArray and AssessmentAwsServiceArrayOutput values.
// You can construct a concrete instance of `AssessmentAwsServiceArrayInput` via:
//
//	AssessmentAwsServiceArray{ AssessmentAwsServiceArgs{...} }
type AssessmentAwsServiceArrayInput interface {
	pulumi.Input

	ToAssessmentAwsServiceArrayOutput() AssessmentAwsServiceArrayOutput
	ToAssessmentAwsServiceArrayOutputWithContext(context.Context) AssessmentAwsServiceArrayOutput
}

type AssessmentAwsServiceArray []AssessmentAwsServiceInput

func (AssessmentAwsServiceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AssessmentAwsService)(nil)).Elem()
}

func (i AssessmentAwsServiceArray) ToAssessmentAwsServiceArrayOutput() AssessmentAwsServiceArrayOutput {
	return i.ToAssessmentAwsServiceArrayOutputWithContext(context.Background())
}

func (i AssessmentAwsServiceArray) ToAssessmentAwsServiceArrayOutputWithContext(ctx context.Context) AssessmentAwsServiceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentAwsServiceArrayOutput)
}

// An AWS service such as Amazon S3, AWS CloudTrail, and so on.
type AssessmentAwsServiceOutput struct{ *pulumi.OutputState }

func (AssessmentAwsServiceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentAwsService)(nil)).Elem()
}

func (o AssessmentAwsServiceOutput) ToAssessmentAwsServiceOutput() AssessmentAwsServiceOutput {
	return o
}

func (o AssessmentAwsServiceOutput) ToAssessmentAwsServiceOutputWithContext(ctx context.Context) AssessmentAwsServiceOutput {
	return o
}

func (o AssessmentAwsServiceOutput) ServiceName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentAwsService) *string { return v.ServiceName }).(pulumi.StringPtrOutput)
}

type AssessmentAwsServiceArrayOutput struct{ *pulumi.OutputState }

func (AssessmentAwsServiceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AssessmentAwsService)(nil)).Elem()
}

func (o AssessmentAwsServiceArrayOutput) ToAssessmentAwsServiceArrayOutput() AssessmentAwsServiceArrayOutput {
	return o
}

func (o AssessmentAwsServiceArrayOutput) ToAssessmentAwsServiceArrayOutputWithContext(ctx context.Context) AssessmentAwsServiceArrayOutput {
	return o
}

func (o AssessmentAwsServiceArrayOutput) Index(i pulumi.IntInput) AssessmentAwsServiceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AssessmentAwsService {
		return vs[0].([]AssessmentAwsService)[vs[1].(int)]
	}).(AssessmentAwsServiceOutput)
}

// The assignment of a control set to a delegate for review.
type AssessmentDelegation struct {
	AssessmentId   *string                     `pulumi:"assessmentId"`
	AssessmentName *string                     `pulumi:"assessmentName"`
	Comment        *string                     `pulumi:"comment"`
	ControlSetId   *string                     `pulumi:"controlSetId"`
	CreatedBy      *string                     `pulumi:"createdBy"`
	CreationTime   *float64                    `pulumi:"creationTime"`
	Id             *string                     `pulumi:"id"`
	LastUpdated    *float64                    `pulumi:"lastUpdated"`
	RoleArn        *string                     `pulumi:"roleArn"`
	RoleType       *AssessmentRoleType         `pulumi:"roleType"`
	Status         *AssessmentDelegationStatus `pulumi:"status"`
}

// AssessmentDelegationInput is an input type that accepts AssessmentDelegationArgs and AssessmentDelegationOutput values.
// You can construct a concrete instance of `AssessmentDelegationInput` via:
//
//	AssessmentDelegationArgs{...}
type AssessmentDelegationInput interface {
	pulumi.Input

	ToAssessmentDelegationOutput() AssessmentDelegationOutput
	ToAssessmentDelegationOutputWithContext(context.Context) AssessmentDelegationOutput
}

// The assignment of a control set to a delegate for review.
type AssessmentDelegationArgs struct {
	AssessmentId   pulumi.StringPtrInput              `pulumi:"assessmentId"`
	AssessmentName pulumi.StringPtrInput              `pulumi:"assessmentName"`
	Comment        pulumi.StringPtrInput              `pulumi:"comment"`
	ControlSetId   pulumi.StringPtrInput              `pulumi:"controlSetId"`
	CreatedBy      pulumi.StringPtrInput              `pulumi:"createdBy"`
	CreationTime   pulumi.Float64PtrInput             `pulumi:"creationTime"`
	Id             pulumi.StringPtrInput              `pulumi:"id"`
	LastUpdated    pulumi.Float64PtrInput             `pulumi:"lastUpdated"`
	RoleArn        pulumi.StringPtrInput              `pulumi:"roleArn"`
	RoleType       AssessmentRoleTypePtrInput         `pulumi:"roleType"`
	Status         AssessmentDelegationStatusPtrInput `pulumi:"status"`
}

func (AssessmentDelegationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentDelegation)(nil)).Elem()
}

func (i AssessmentDelegationArgs) ToAssessmentDelegationOutput() AssessmentDelegationOutput {
	return i.ToAssessmentDelegationOutputWithContext(context.Background())
}

func (i AssessmentDelegationArgs) ToAssessmentDelegationOutputWithContext(ctx context.Context) AssessmentDelegationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentDelegationOutput)
}

// AssessmentDelegationArrayInput is an input type that accepts AssessmentDelegationArray and AssessmentDelegationArrayOutput values.
// You can construct a concrete instance of `AssessmentDelegationArrayInput` via:
//
//	AssessmentDelegationArray{ AssessmentDelegationArgs{...} }
type AssessmentDelegationArrayInput interface {
	pulumi.Input

	ToAssessmentDelegationArrayOutput() AssessmentDelegationArrayOutput
	ToAssessmentDelegationArrayOutputWithContext(context.Context) AssessmentDelegationArrayOutput
}

type AssessmentDelegationArray []AssessmentDelegationInput

func (AssessmentDelegationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AssessmentDelegation)(nil)).Elem()
}

func (i AssessmentDelegationArray) ToAssessmentDelegationArrayOutput() AssessmentDelegationArrayOutput {
	return i.ToAssessmentDelegationArrayOutputWithContext(context.Background())
}

func (i AssessmentDelegationArray) ToAssessmentDelegationArrayOutputWithContext(ctx context.Context) AssessmentDelegationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentDelegationArrayOutput)
}

// The assignment of a control set to a delegate for review.
type AssessmentDelegationOutput struct{ *pulumi.OutputState }

func (AssessmentDelegationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentDelegation)(nil)).Elem()
}

func (o AssessmentDelegationOutput) ToAssessmentDelegationOutput() AssessmentDelegationOutput {
	return o
}

func (o AssessmentDelegationOutput) ToAssessmentDelegationOutputWithContext(ctx context.Context) AssessmentDelegationOutput {
	return o
}

func (o AssessmentDelegationOutput) AssessmentId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *string { return v.AssessmentId }).(pulumi.StringPtrOutput)
}

func (o AssessmentDelegationOutput) AssessmentName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *string { return v.AssessmentName }).(pulumi.StringPtrOutput)
}

func (o AssessmentDelegationOutput) Comment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *string { return v.Comment }).(pulumi.StringPtrOutput)
}

func (o AssessmentDelegationOutput) ControlSetId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *string { return v.ControlSetId }).(pulumi.StringPtrOutput)
}

func (o AssessmentDelegationOutput) CreatedBy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *string { return v.CreatedBy }).(pulumi.StringPtrOutput)
}

func (o AssessmentDelegationOutput) CreationTime() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *float64 { return v.CreationTime }).(pulumi.Float64PtrOutput)
}

func (o AssessmentDelegationOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o AssessmentDelegationOutput) LastUpdated() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *float64 { return v.LastUpdated }).(pulumi.Float64PtrOutput)
}

func (o AssessmentDelegationOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *string { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func (o AssessmentDelegationOutput) RoleType() AssessmentRoleTypePtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *AssessmentRoleType { return v.RoleType }).(AssessmentRoleTypePtrOutput)
}

func (o AssessmentDelegationOutput) Status() AssessmentDelegationStatusPtrOutput {
	return o.ApplyT(func(v AssessmentDelegation) *AssessmentDelegationStatus { return v.Status }).(AssessmentDelegationStatusPtrOutput)
}

type AssessmentDelegationArrayOutput struct{ *pulumi.OutputState }

func (AssessmentDelegationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AssessmentDelegation)(nil)).Elem()
}

func (o AssessmentDelegationArrayOutput) ToAssessmentDelegationArrayOutput() AssessmentDelegationArrayOutput {
	return o
}

func (o AssessmentDelegationArrayOutput) ToAssessmentDelegationArrayOutputWithContext(ctx context.Context) AssessmentDelegationArrayOutput {
	return o
}

func (o AssessmentDelegationArrayOutput) Index(i pulumi.IntInput) AssessmentDelegationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AssessmentDelegation {
		return vs[0].([]AssessmentDelegation)[vs[1].(int)]
	}).(AssessmentDelegationOutput)
}

// The destination in which evidence reports are stored for the specified assessment.
type AssessmentReportsDestination struct {
	Destination     *string                          `pulumi:"destination"`
	DestinationType *AssessmentReportDestinationType `pulumi:"destinationType"`
}

// AssessmentReportsDestinationInput is an input type that accepts AssessmentReportsDestinationArgs and AssessmentReportsDestinationOutput values.
// You can construct a concrete instance of `AssessmentReportsDestinationInput` via:
//
//	AssessmentReportsDestinationArgs{...}
type AssessmentReportsDestinationInput interface {
	pulumi.Input

	ToAssessmentReportsDestinationOutput() AssessmentReportsDestinationOutput
	ToAssessmentReportsDestinationOutputWithContext(context.Context) AssessmentReportsDestinationOutput
}

// The destination in which evidence reports are stored for the specified assessment.
type AssessmentReportsDestinationArgs struct {
	Destination     pulumi.StringPtrInput                   `pulumi:"destination"`
	DestinationType AssessmentReportDestinationTypePtrInput `pulumi:"destinationType"`
}

func (AssessmentReportsDestinationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentReportsDestination)(nil)).Elem()
}

func (i AssessmentReportsDestinationArgs) ToAssessmentReportsDestinationOutput() AssessmentReportsDestinationOutput {
	return i.ToAssessmentReportsDestinationOutputWithContext(context.Background())
}

func (i AssessmentReportsDestinationArgs) ToAssessmentReportsDestinationOutputWithContext(ctx context.Context) AssessmentReportsDestinationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentReportsDestinationOutput)
}

func (i AssessmentReportsDestinationArgs) ToAssessmentReportsDestinationPtrOutput() AssessmentReportsDestinationPtrOutput {
	return i.ToAssessmentReportsDestinationPtrOutputWithContext(context.Background())
}

func (i AssessmentReportsDestinationArgs) ToAssessmentReportsDestinationPtrOutputWithContext(ctx context.Context) AssessmentReportsDestinationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentReportsDestinationOutput).ToAssessmentReportsDestinationPtrOutputWithContext(ctx)
}

// AssessmentReportsDestinationPtrInput is an input type that accepts AssessmentReportsDestinationArgs, AssessmentReportsDestinationPtr and AssessmentReportsDestinationPtrOutput values.
// You can construct a concrete instance of `AssessmentReportsDestinationPtrInput` via:
//
//	        AssessmentReportsDestinationArgs{...}
//
//	or:
//
//	        nil
type AssessmentReportsDestinationPtrInput interface {
	pulumi.Input

	ToAssessmentReportsDestinationPtrOutput() AssessmentReportsDestinationPtrOutput
	ToAssessmentReportsDestinationPtrOutputWithContext(context.Context) AssessmentReportsDestinationPtrOutput
}

type assessmentReportsDestinationPtrType AssessmentReportsDestinationArgs

func AssessmentReportsDestinationPtr(v *AssessmentReportsDestinationArgs) AssessmentReportsDestinationPtrInput {
	return (*assessmentReportsDestinationPtrType)(v)
}

func (*assessmentReportsDestinationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AssessmentReportsDestination)(nil)).Elem()
}

func (i *assessmentReportsDestinationPtrType) ToAssessmentReportsDestinationPtrOutput() AssessmentReportsDestinationPtrOutput {
	return i.ToAssessmentReportsDestinationPtrOutputWithContext(context.Background())
}

func (i *assessmentReportsDestinationPtrType) ToAssessmentReportsDestinationPtrOutputWithContext(ctx context.Context) AssessmentReportsDestinationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentReportsDestinationPtrOutput)
}

// The destination in which evidence reports are stored for the specified assessment.
type AssessmentReportsDestinationOutput struct{ *pulumi.OutputState }

func (AssessmentReportsDestinationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentReportsDestination)(nil)).Elem()
}

func (o AssessmentReportsDestinationOutput) ToAssessmentReportsDestinationOutput() AssessmentReportsDestinationOutput {
	return o
}

func (o AssessmentReportsDestinationOutput) ToAssessmentReportsDestinationOutputWithContext(ctx context.Context) AssessmentReportsDestinationOutput {
	return o
}

func (o AssessmentReportsDestinationOutput) ToAssessmentReportsDestinationPtrOutput() AssessmentReportsDestinationPtrOutput {
	return o.ToAssessmentReportsDestinationPtrOutputWithContext(context.Background())
}

func (o AssessmentReportsDestinationOutput) ToAssessmentReportsDestinationPtrOutputWithContext(ctx context.Context) AssessmentReportsDestinationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AssessmentReportsDestination) *AssessmentReportsDestination {
		return &v
	}).(AssessmentReportsDestinationPtrOutput)
}

func (o AssessmentReportsDestinationOutput) Destination() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentReportsDestination) *string { return v.Destination }).(pulumi.StringPtrOutput)
}

func (o AssessmentReportsDestinationOutput) DestinationType() AssessmentReportDestinationTypePtrOutput {
	return o.ApplyT(func(v AssessmentReportsDestination) *AssessmentReportDestinationType { return v.DestinationType }).(AssessmentReportDestinationTypePtrOutput)
}

type AssessmentReportsDestinationPtrOutput struct{ *pulumi.OutputState }

func (AssessmentReportsDestinationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AssessmentReportsDestination)(nil)).Elem()
}

func (o AssessmentReportsDestinationPtrOutput) ToAssessmentReportsDestinationPtrOutput() AssessmentReportsDestinationPtrOutput {
	return o
}

func (o AssessmentReportsDestinationPtrOutput) ToAssessmentReportsDestinationPtrOutputWithContext(ctx context.Context) AssessmentReportsDestinationPtrOutput {
	return o
}

func (o AssessmentReportsDestinationPtrOutput) Elem() AssessmentReportsDestinationOutput {
	return o.ApplyT(func(v *AssessmentReportsDestination) AssessmentReportsDestination {
		if v != nil {
			return *v
		}
		var ret AssessmentReportsDestination
		return ret
	}).(AssessmentReportsDestinationOutput)
}

func (o AssessmentReportsDestinationPtrOutput) Destination() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AssessmentReportsDestination) *string {
		if v == nil {
			return nil
		}
		return v.Destination
	}).(pulumi.StringPtrOutput)
}

func (o AssessmentReportsDestinationPtrOutput) DestinationType() AssessmentReportDestinationTypePtrOutput {
	return o.ApplyT(func(v *AssessmentReportsDestination) *AssessmentReportDestinationType {
		if v == nil {
			return nil
		}
		return v.DestinationType
	}).(AssessmentReportDestinationTypePtrOutput)
}

// The wrapper that contains AWS Audit Manager role information, such as the role type and IAM ARN.
type AssessmentRole struct {
	RoleArn  *string             `pulumi:"roleArn"`
	RoleType *AssessmentRoleType `pulumi:"roleType"`
}

// AssessmentRoleInput is an input type that accepts AssessmentRoleArgs and AssessmentRoleOutput values.
// You can construct a concrete instance of `AssessmentRoleInput` via:
//
//	AssessmentRoleArgs{...}
type AssessmentRoleInput interface {
	pulumi.Input

	ToAssessmentRoleOutput() AssessmentRoleOutput
	ToAssessmentRoleOutputWithContext(context.Context) AssessmentRoleOutput
}

// The wrapper that contains AWS Audit Manager role information, such as the role type and IAM ARN.
type AssessmentRoleArgs struct {
	RoleArn  pulumi.StringPtrInput      `pulumi:"roleArn"`
	RoleType AssessmentRoleTypePtrInput `pulumi:"roleType"`
}

func (AssessmentRoleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentRole)(nil)).Elem()
}

func (i AssessmentRoleArgs) ToAssessmentRoleOutput() AssessmentRoleOutput {
	return i.ToAssessmentRoleOutputWithContext(context.Background())
}

func (i AssessmentRoleArgs) ToAssessmentRoleOutputWithContext(ctx context.Context) AssessmentRoleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentRoleOutput)
}

// AssessmentRoleArrayInput is an input type that accepts AssessmentRoleArray and AssessmentRoleArrayOutput values.
// You can construct a concrete instance of `AssessmentRoleArrayInput` via:
//
//	AssessmentRoleArray{ AssessmentRoleArgs{...} }
type AssessmentRoleArrayInput interface {
	pulumi.Input

	ToAssessmentRoleArrayOutput() AssessmentRoleArrayOutput
	ToAssessmentRoleArrayOutputWithContext(context.Context) AssessmentRoleArrayOutput
}

type AssessmentRoleArray []AssessmentRoleInput

func (AssessmentRoleArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AssessmentRole)(nil)).Elem()
}

func (i AssessmentRoleArray) ToAssessmentRoleArrayOutput() AssessmentRoleArrayOutput {
	return i.ToAssessmentRoleArrayOutputWithContext(context.Background())
}

func (i AssessmentRoleArray) ToAssessmentRoleArrayOutputWithContext(ctx context.Context) AssessmentRoleArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentRoleArrayOutput)
}

// The wrapper that contains AWS Audit Manager role information, such as the role type and IAM ARN.
type AssessmentRoleOutput struct{ *pulumi.OutputState }

func (AssessmentRoleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentRole)(nil)).Elem()
}

func (o AssessmentRoleOutput) ToAssessmentRoleOutput() AssessmentRoleOutput {
	return o
}

func (o AssessmentRoleOutput) ToAssessmentRoleOutputWithContext(ctx context.Context) AssessmentRoleOutput {
	return o
}

func (o AssessmentRoleOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AssessmentRole) *string { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func (o AssessmentRoleOutput) RoleType() AssessmentRoleTypePtrOutput {
	return o.ApplyT(func(v AssessmentRole) *AssessmentRoleType { return v.RoleType }).(AssessmentRoleTypePtrOutput)
}

type AssessmentRoleArrayOutput struct{ *pulumi.OutputState }

func (AssessmentRoleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AssessmentRole)(nil)).Elem()
}

func (o AssessmentRoleArrayOutput) ToAssessmentRoleArrayOutput() AssessmentRoleArrayOutput {
	return o
}

func (o AssessmentRoleArrayOutput) ToAssessmentRoleArrayOutputWithContext(ctx context.Context) AssessmentRoleArrayOutput {
	return o
}

func (o AssessmentRoleArrayOutput) Index(i pulumi.IntInput) AssessmentRoleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AssessmentRole {
		return vs[0].([]AssessmentRole)[vs[1].(int)]
	}).(AssessmentRoleOutput)
}

// The wrapper that contains the AWS accounts and AWS services in scope for the assessment.
type AssessmentScope struct {
	// The AWS accounts included in scope.
	AwsAccounts []AssessmentAwsAccount `pulumi:"awsAccounts"`
	// The AWS services included in scope.
	AwsServices []AssessmentAwsService `pulumi:"awsServices"`
}

// AssessmentScopeInput is an input type that accepts AssessmentScopeArgs and AssessmentScopeOutput values.
// You can construct a concrete instance of `AssessmentScopeInput` via:
//
//	AssessmentScopeArgs{...}
type AssessmentScopeInput interface {
	pulumi.Input

	ToAssessmentScopeOutput() AssessmentScopeOutput
	ToAssessmentScopeOutputWithContext(context.Context) AssessmentScopeOutput
}

// The wrapper that contains the AWS accounts and AWS services in scope for the assessment.
type AssessmentScopeArgs struct {
	// The AWS accounts included in scope.
	AwsAccounts AssessmentAwsAccountArrayInput `pulumi:"awsAccounts"`
	// The AWS services included in scope.
	AwsServices AssessmentAwsServiceArrayInput `pulumi:"awsServices"`
}

func (AssessmentScopeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentScope)(nil)).Elem()
}

func (i AssessmentScopeArgs) ToAssessmentScopeOutput() AssessmentScopeOutput {
	return i.ToAssessmentScopeOutputWithContext(context.Background())
}

func (i AssessmentScopeArgs) ToAssessmentScopeOutputWithContext(ctx context.Context) AssessmentScopeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentScopeOutput)
}

func (i AssessmentScopeArgs) ToAssessmentScopePtrOutput() AssessmentScopePtrOutput {
	return i.ToAssessmentScopePtrOutputWithContext(context.Background())
}

func (i AssessmentScopeArgs) ToAssessmentScopePtrOutputWithContext(ctx context.Context) AssessmentScopePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentScopeOutput).ToAssessmentScopePtrOutputWithContext(ctx)
}

// AssessmentScopePtrInput is an input type that accepts AssessmentScopeArgs, AssessmentScopePtr and AssessmentScopePtrOutput values.
// You can construct a concrete instance of `AssessmentScopePtrInput` via:
//
//	        AssessmentScopeArgs{...}
//
//	or:
//
//	        nil
type AssessmentScopePtrInput interface {
	pulumi.Input

	ToAssessmentScopePtrOutput() AssessmentScopePtrOutput
	ToAssessmentScopePtrOutputWithContext(context.Context) AssessmentScopePtrOutput
}

type assessmentScopePtrType AssessmentScopeArgs

func AssessmentScopePtr(v *AssessmentScopeArgs) AssessmentScopePtrInput {
	return (*assessmentScopePtrType)(v)
}

func (*assessmentScopePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AssessmentScope)(nil)).Elem()
}

func (i *assessmentScopePtrType) ToAssessmentScopePtrOutput() AssessmentScopePtrOutput {
	return i.ToAssessmentScopePtrOutputWithContext(context.Background())
}

func (i *assessmentScopePtrType) ToAssessmentScopePtrOutputWithContext(ctx context.Context) AssessmentScopePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssessmentScopePtrOutput)
}

// The wrapper that contains the AWS accounts and AWS services in scope for the assessment.
type AssessmentScopeOutput struct{ *pulumi.OutputState }

func (AssessmentScopeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssessmentScope)(nil)).Elem()
}

func (o AssessmentScopeOutput) ToAssessmentScopeOutput() AssessmentScopeOutput {
	return o
}

func (o AssessmentScopeOutput) ToAssessmentScopeOutputWithContext(ctx context.Context) AssessmentScopeOutput {
	return o
}

func (o AssessmentScopeOutput) ToAssessmentScopePtrOutput() AssessmentScopePtrOutput {
	return o.ToAssessmentScopePtrOutputWithContext(context.Background())
}

func (o AssessmentScopeOutput) ToAssessmentScopePtrOutputWithContext(ctx context.Context) AssessmentScopePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AssessmentScope) *AssessmentScope {
		return &v
	}).(AssessmentScopePtrOutput)
}

// The AWS accounts included in scope.
func (o AssessmentScopeOutput) AwsAccounts() AssessmentAwsAccountArrayOutput {
	return o.ApplyT(func(v AssessmentScope) []AssessmentAwsAccount { return v.AwsAccounts }).(AssessmentAwsAccountArrayOutput)
}

// The AWS services included in scope.
func (o AssessmentScopeOutput) AwsServices() AssessmentAwsServiceArrayOutput {
	return o.ApplyT(func(v AssessmentScope) []AssessmentAwsService { return v.AwsServices }).(AssessmentAwsServiceArrayOutput)
}

type AssessmentScopePtrOutput struct{ *pulumi.OutputState }

func (AssessmentScopePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AssessmentScope)(nil)).Elem()
}

func (o AssessmentScopePtrOutput) ToAssessmentScopePtrOutput() AssessmentScopePtrOutput {
	return o
}

func (o AssessmentScopePtrOutput) ToAssessmentScopePtrOutputWithContext(ctx context.Context) AssessmentScopePtrOutput {
	return o
}

func (o AssessmentScopePtrOutput) Elem() AssessmentScopeOutput {
	return o.ApplyT(func(v *AssessmentScope) AssessmentScope {
		if v != nil {
			return *v
		}
		var ret AssessmentScope
		return ret
	}).(AssessmentScopeOutput)
}

// The AWS accounts included in scope.
func (o AssessmentScopePtrOutput) AwsAccounts() AssessmentAwsAccountArrayOutput {
	return o.ApplyT(func(v *AssessmentScope) []AssessmentAwsAccount {
		if v == nil {
			return nil
		}
		return v.AwsAccounts
	}).(AssessmentAwsAccountArrayOutput)
}

// The AWS services included in scope.
func (o AssessmentScopePtrOutput) AwsServices() AssessmentAwsServiceArrayOutput {
	return o.ApplyT(func(v *AssessmentScope) []AssessmentAwsService {
		if v == nil {
			return nil
		}
		return v.AwsServices
	}).(AssessmentAwsServiceArrayOutput)
}

// A key-value pair to associate with a resource.
type AssessmentTag struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key string `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value string `pulumi:"value"`
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentAwsAccountInput)(nil)).Elem(), AssessmentAwsAccountArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentAwsAccountPtrInput)(nil)).Elem(), AssessmentAwsAccountArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentAwsAccountArrayInput)(nil)).Elem(), AssessmentAwsAccountArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentAwsServiceInput)(nil)).Elem(), AssessmentAwsServiceArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentAwsServiceArrayInput)(nil)).Elem(), AssessmentAwsServiceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentDelegationInput)(nil)).Elem(), AssessmentDelegationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentDelegationArrayInput)(nil)).Elem(), AssessmentDelegationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentReportsDestinationInput)(nil)).Elem(), AssessmentReportsDestinationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentReportsDestinationPtrInput)(nil)).Elem(), AssessmentReportsDestinationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentRoleInput)(nil)).Elem(), AssessmentRoleArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentRoleArrayInput)(nil)).Elem(), AssessmentRoleArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentScopeInput)(nil)).Elem(), AssessmentScopeArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AssessmentScopePtrInput)(nil)).Elem(), AssessmentScopeArgs{})
	pulumi.RegisterOutputType(AssessmentAwsAccountOutput{})
	pulumi.RegisterOutputType(AssessmentAwsAccountPtrOutput{})
	pulumi.RegisterOutputType(AssessmentAwsAccountArrayOutput{})
	pulumi.RegisterOutputType(AssessmentAwsServiceOutput{})
	pulumi.RegisterOutputType(AssessmentAwsServiceArrayOutput{})
	pulumi.RegisterOutputType(AssessmentDelegationOutput{})
	pulumi.RegisterOutputType(AssessmentDelegationArrayOutput{})
	pulumi.RegisterOutputType(AssessmentReportsDestinationOutput{})
	pulumi.RegisterOutputType(AssessmentReportsDestinationPtrOutput{})
	pulumi.RegisterOutputType(AssessmentRoleOutput{})
	pulumi.RegisterOutputType(AssessmentRoleArrayOutput{})
	pulumi.RegisterOutputType(AssessmentScopeOutput{})
	pulumi.RegisterOutputType(AssessmentScopePtrOutput{})
}
