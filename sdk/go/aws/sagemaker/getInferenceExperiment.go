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

// Resource Type definition for AWS::SageMaker::InferenceExperiment
func LookupInferenceExperiment(ctx *pulumi.Context, args *LookupInferenceExperimentArgs, opts ...pulumi.InvokeOption) (*LookupInferenceExperimentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupInferenceExperimentResult
	err := ctx.Invoke("aws-native:sagemaker:getInferenceExperiment", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupInferenceExperimentArgs struct {
	// The name for the inference experiment.
	Name string `pulumi:"name"`
}

type LookupInferenceExperimentResult struct {
	// The Amazon Resource Name (ARN) of the inference experiment.
	Arn *string `pulumi:"arn"`
	// The timestamp at which you created the inference experiment.
	CreationTime      *string                               `pulumi:"creationTime"`
	DataStorageConfig *InferenceExperimentDataStorageConfig `pulumi:"dataStorageConfig"`
	// The description of the inference experiment.
	Description *string `pulumi:"description"`
	// The desired state of the experiment after starting or stopping operation.
	DesiredState     *InferenceExperimentDesiredState     `pulumi:"desiredState"`
	EndpointMetadata *InferenceExperimentEndpointMetadata `pulumi:"endpointMetadata"`
	// The timestamp at which you last modified the inference experiment.
	LastModifiedTime *string `pulumi:"lastModifiedTime"`
	// An array of ModelVariantConfig objects. Each ModelVariantConfig object in the array describes the infrastructure configuration for the corresponding variant.
	ModelVariants    []InferenceExperimentModelVariantConfig `pulumi:"modelVariants"`
	Schedule         *InferenceExperimentSchedule            `pulumi:"schedule"`
	ShadowModeConfig *InferenceExperimentShadowModeConfig    `pulumi:"shadowModeConfig"`
	// The status of the inference experiment.
	Status *InferenceExperimentStatus `pulumi:"status"`
	// The error message or client-specified reason from the StopInferenceExperiment API, that explains the status of the inference experiment.
	StatusReason *string `pulumi:"statusReason"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupInferenceExperimentOutput(ctx *pulumi.Context, args LookupInferenceExperimentOutputArgs, opts ...pulumi.InvokeOption) LookupInferenceExperimentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupInferenceExperimentResult, error) {
			args := v.(LookupInferenceExperimentArgs)
			r, err := LookupInferenceExperiment(ctx, &args, opts...)
			var s LookupInferenceExperimentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupInferenceExperimentResultOutput)
}

type LookupInferenceExperimentOutputArgs struct {
	// The name for the inference experiment.
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupInferenceExperimentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInferenceExperimentArgs)(nil)).Elem()
}

type LookupInferenceExperimentResultOutput struct{ *pulumi.OutputState }

func (LookupInferenceExperimentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInferenceExperimentResult)(nil)).Elem()
}

func (o LookupInferenceExperimentResultOutput) ToLookupInferenceExperimentResultOutput() LookupInferenceExperimentResultOutput {
	return o
}

func (o LookupInferenceExperimentResultOutput) ToLookupInferenceExperimentResultOutputWithContext(ctx context.Context) LookupInferenceExperimentResultOutput {
	return o
}

// The Amazon Resource Name (ARN) of the inference experiment.
func (o LookupInferenceExperimentResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// The timestamp at which you created the inference experiment.
func (o LookupInferenceExperimentResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

func (o LookupInferenceExperimentResultOutput) DataStorageConfig() InferenceExperimentDataStorageConfigPtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *InferenceExperimentDataStorageConfig {
		return v.DataStorageConfig
	}).(InferenceExperimentDataStorageConfigPtrOutput)
}

// The description of the inference experiment.
func (o LookupInferenceExperimentResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The desired state of the experiment after starting or stopping operation.
func (o LookupInferenceExperimentResultOutput) DesiredState() InferenceExperimentDesiredStatePtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *InferenceExperimentDesiredState { return v.DesiredState }).(InferenceExperimentDesiredStatePtrOutput)
}

func (o LookupInferenceExperimentResultOutput) EndpointMetadata() InferenceExperimentEndpointMetadataPtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *InferenceExperimentEndpointMetadata {
		return v.EndpointMetadata
	}).(InferenceExperimentEndpointMetadataPtrOutput)
}

// The timestamp at which you last modified the inference experiment.
func (o LookupInferenceExperimentResultOutput) LastModifiedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *string { return v.LastModifiedTime }).(pulumi.StringPtrOutput)
}

// An array of ModelVariantConfig objects. Each ModelVariantConfig object in the array describes the infrastructure configuration for the corresponding variant.
func (o LookupInferenceExperimentResultOutput) ModelVariants() InferenceExperimentModelVariantConfigArrayOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) []InferenceExperimentModelVariantConfig {
		return v.ModelVariants
	}).(InferenceExperimentModelVariantConfigArrayOutput)
}

func (o LookupInferenceExperimentResultOutput) Schedule() InferenceExperimentSchedulePtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *InferenceExperimentSchedule { return v.Schedule }).(InferenceExperimentSchedulePtrOutput)
}

func (o LookupInferenceExperimentResultOutput) ShadowModeConfig() InferenceExperimentShadowModeConfigPtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *InferenceExperimentShadowModeConfig {
		return v.ShadowModeConfig
	}).(InferenceExperimentShadowModeConfigPtrOutput)
}

// The status of the inference experiment.
func (o LookupInferenceExperimentResultOutput) Status() InferenceExperimentStatusPtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *InferenceExperimentStatus { return v.Status }).(InferenceExperimentStatusPtrOutput)
}

// The error message or client-specified reason from the StopInferenceExperiment API, that explains the status of the inference experiment.
func (o LookupInferenceExperimentResultOutput) StatusReason() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) *string { return v.StatusReason }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupInferenceExperimentResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupInferenceExperimentResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupInferenceExperimentResultOutput{})
}
