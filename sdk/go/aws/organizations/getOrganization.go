// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package organizations

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::Organizations::Organization
func LookupOrganization(ctx *pulumi.Context, args *LookupOrganizationArgs, opts ...pulumi.InvokeOption) (*LookupOrganizationResult, error) {
	var rv LookupOrganizationResult
	err := ctx.Invoke("aws-native:organizations:getOrganization", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupOrganizationArgs struct {
	// The unique identifier (ID) of an organization.
	Id string `pulumi:"id"`
}

type LookupOrganizationResult struct {
	// The Amazon Resource Name (ARN) of an organization.
	Arn *string `pulumi:"arn"`
	// Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.
	FeatureSet *OrganizationFeatureSet `pulumi:"featureSet"`
	// The unique identifier (ID) of an organization.
	Id *string `pulumi:"id"`
	// The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.
	ManagementAccountArn *string `pulumi:"managementAccountArn"`
	// The email address that is associated with the AWS account that is designated as the management account for the organization.
	ManagementAccountEmail *string `pulumi:"managementAccountEmail"`
	// The unique identifier (ID) of the management account of an organization.
	ManagementAccountId *string `pulumi:"managementAccountId"`
	// The unique identifier (ID) for the root.
	RootId *string `pulumi:"rootId"`
}

func LookupOrganizationOutput(ctx *pulumi.Context, args LookupOrganizationOutputArgs, opts ...pulumi.InvokeOption) LookupOrganizationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupOrganizationResult, error) {
			args := v.(LookupOrganizationArgs)
			r, err := LookupOrganization(ctx, &args, opts...)
			var s LookupOrganizationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupOrganizationResultOutput)
}

type LookupOrganizationOutputArgs struct {
	// The unique identifier (ID) of an organization.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupOrganizationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOrganizationArgs)(nil)).Elem()
}

type LookupOrganizationResultOutput struct{ *pulumi.OutputState }

func (LookupOrganizationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOrganizationResult)(nil)).Elem()
}

func (o LookupOrganizationResultOutput) ToLookupOrganizationResultOutput() LookupOrganizationResultOutput {
	return o
}

func (o LookupOrganizationResultOutput) ToLookupOrganizationResultOutputWithContext(ctx context.Context) LookupOrganizationResultOutput {
	return o
}

// The Amazon Resource Name (ARN) of an organization.
func (o LookupOrganizationResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupOrganizationResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.
func (o LookupOrganizationResultOutput) FeatureSet() OrganizationFeatureSetPtrOutput {
	return o.ApplyT(func(v LookupOrganizationResult) *OrganizationFeatureSet { return v.FeatureSet }).(OrganizationFeatureSetPtrOutput)
}

// The unique identifier (ID) of an organization.
func (o LookupOrganizationResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupOrganizationResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.
func (o LookupOrganizationResultOutput) ManagementAccountArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupOrganizationResult) *string { return v.ManagementAccountArn }).(pulumi.StringPtrOutput)
}

// The email address that is associated with the AWS account that is designated as the management account for the organization.
func (o LookupOrganizationResultOutput) ManagementAccountEmail() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupOrganizationResult) *string { return v.ManagementAccountEmail }).(pulumi.StringPtrOutput)
}

// The unique identifier (ID) of the management account of an organization.
func (o LookupOrganizationResultOutput) ManagementAccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupOrganizationResult) *string { return v.ManagementAccountId }).(pulumi.StringPtrOutput)
}

// The unique identifier (ID) for the root.
func (o LookupOrganizationResultOutput) RootId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupOrganizationResult) *string { return v.RootId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupOrganizationResultOutput{})
}
