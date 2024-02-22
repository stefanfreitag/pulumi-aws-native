// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SageMaker::ModelPackage
func LookupModelPackage(ctx *pulumi.Context, args *LookupModelPackageArgs, opts ...pulumi.InvokeOption) (*LookupModelPackageResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupModelPackageResult
	err := ctx.Invoke("aws-native:sagemaker:getModelPackage", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupModelPackageArgs struct {
	ModelPackageArn string `pulumi:"modelPackageArn"`
}

type LookupModelPackageResult struct {
	AdditionalInferenceSpecifications []ModelPackageAdditionalInferenceSpecificationDefinition `pulumi:"additionalInferenceSpecifications"`
	ApprovalDescription               *string                                                  `pulumi:"approvalDescription"`
	CertifyForMarketplace             *bool                                                    `pulumi:"certifyForMarketplace"`
	CreationTime                      *string                                                  `pulumi:"creationTime"`
	CustomerMetadataProperties        *ModelPackageCustomerMetadataProperties                  `pulumi:"customerMetadataProperties"`
	LastModifiedTime                  *string                                                  `pulumi:"lastModifiedTime"`
	ModelApprovalStatus               *ModelPackageModelApprovalStatus                         `pulumi:"modelApprovalStatus"`
	ModelPackageArn                   *string                                                  `pulumi:"modelPackageArn"`
	ModelPackageName                  *string                                                  `pulumi:"modelPackageName"`
	ModelPackageStatus                *ModelPackageStatus                                      `pulumi:"modelPackageStatus"`
	ModelPackageStatusDetails         *ModelPackageStatusDetails                               `pulumi:"modelPackageStatusDetails"`
	ModelPackageVersion               *int                                                     `pulumi:"modelPackageVersion"`
	SkipModelValidation               *ModelPackageSkipModelValidation                         `pulumi:"skipModelValidation"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupModelPackageOutput(ctx *pulumi.Context, args LookupModelPackageOutputArgs, opts ...pulumi.InvokeOption) LookupModelPackageResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupModelPackageResult, error) {
			args := v.(LookupModelPackageArgs)
			r, err := LookupModelPackage(ctx, &args, opts...)
			var s LookupModelPackageResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupModelPackageResultOutput)
}

type LookupModelPackageOutputArgs struct {
	ModelPackageArn pulumi.StringInput `pulumi:"modelPackageArn"`
}

func (LookupModelPackageOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupModelPackageArgs)(nil)).Elem()
}

type LookupModelPackageResultOutput struct{ *pulumi.OutputState }

func (LookupModelPackageResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupModelPackageResult)(nil)).Elem()
}

func (o LookupModelPackageResultOutput) ToLookupModelPackageResultOutput() LookupModelPackageResultOutput {
	return o
}

func (o LookupModelPackageResultOutput) ToLookupModelPackageResultOutputWithContext(ctx context.Context) LookupModelPackageResultOutput {
	return o
}

func (o LookupModelPackageResultOutput) AdditionalInferenceSpecifications() ModelPackageAdditionalInferenceSpecificationDefinitionArrayOutput {
	return o.ApplyT(func(v LookupModelPackageResult) []ModelPackageAdditionalInferenceSpecificationDefinition {
		return v.AdditionalInferenceSpecifications
	}).(ModelPackageAdditionalInferenceSpecificationDefinitionArrayOutput)
}

func (o LookupModelPackageResultOutput) ApprovalDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *string { return v.ApprovalDescription }).(pulumi.StringPtrOutput)
}

func (o LookupModelPackageResultOutput) CertifyForMarketplace() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *bool { return v.CertifyForMarketplace }).(pulumi.BoolPtrOutput)
}

func (o LookupModelPackageResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

func (o LookupModelPackageResultOutput) CustomerMetadataProperties() ModelPackageCustomerMetadataPropertiesPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *ModelPackageCustomerMetadataProperties {
		return v.CustomerMetadataProperties
	}).(ModelPackageCustomerMetadataPropertiesPtrOutput)
}

func (o LookupModelPackageResultOutput) LastModifiedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *string { return v.LastModifiedTime }).(pulumi.StringPtrOutput)
}

func (o LookupModelPackageResultOutput) ModelApprovalStatus() ModelPackageModelApprovalStatusPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *ModelPackageModelApprovalStatus { return v.ModelApprovalStatus }).(ModelPackageModelApprovalStatusPtrOutput)
}

func (o LookupModelPackageResultOutput) ModelPackageArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *string { return v.ModelPackageArn }).(pulumi.StringPtrOutput)
}

func (o LookupModelPackageResultOutput) ModelPackageName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *string { return v.ModelPackageName }).(pulumi.StringPtrOutput)
}

func (o LookupModelPackageResultOutput) ModelPackageStatus() ModelPackageStatusPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *ModelPackageStatus { return v.ModelPackageStatus }).(ModelPackageStatusPtrOutput)
}

func (o LookupModelPackageResultOutput) ModelPackageStatusDetails() ModelPackageStatusDetailsPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *ModelPackageStatusDetails { return v.ModelPackageStatusDetails }).(ModelPackageStatusDetailsPtrOutput)
}

func (o LookupModelPackageResultOutput) ModelPackageVersion() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *int { return v.ModelPackageVersion }).(pulumi.IntPtrOutput)
}

func (o LookupModelPackageResultOutput) SkipModelValidation() ModelPackageSkipModelValidationPtrOutput {
	return o.ApplyT(func(v LookupModelPackageResult) *ModelPackageSkipModelValidation { return v.SkipModelValidation }).(ModelPackageSkipModelValidationPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupModelPackageResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupModelPackageResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupModelPackageResultOutput{})
}
