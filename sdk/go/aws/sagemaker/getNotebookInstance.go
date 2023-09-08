// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::SageMaker::NotebookInstance
func LookupNotebookInstance(ctx *pulumi.Context, args *LookupNotebookInstanceArgs, opts ...pulumi.InvokeOption) (*LookupNotebookInstanceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupNotebookInstanceResult
	err := ctx.Invoke("aws-native:sagemaker:getNotebookInstance", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupNotebookInstanceArgs struct {
	Id string `pulumi:"id"`
}

type LookupNotebookInstanceResult struct {
	AcceleratorTypes                     []string                                              `pulumi:"acceleratorTypes"`
	AdditionalCodeRepositories           []string                                              `pulumi:"additionalCodeRepositories"`
	DefaultCodeRepository                *string                                               `pulumi:"defaultCodeRepository"`
	Id                                   *string                                               `pulumi:"id"`
	InstanceMetadataServiceConfiguration *NotebookInstanceInstanceMetadataServiceConfiguration `pulumi:"instanceMetadataServiceConfiguration"`
	InstanceType                         *string                                               `pulumi:"instanceType"`
	LifecycleConfigName                  *string                                               `pulumi:"lifecycleConfigName"`
	RoleArn                              *string                                               `pulumi:"roleArn"`
	RootAccess                           *string                                               `pulumi:"rootAccess"`
	Tags                                 []NotebookInstanceTag                                 `pulumi:"tags"`
	VolumeSizeInGb                       *int                                                  `pulumi:"volumeSizeInGb"`
}

func LookupNotebookInstanceOutput(ctx *pulumi.Context, args LookupNotebookInstanceOutputArgs, opts ...pulumi.InvokeOption) LookupNotebookInstanceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNotebookInstanceResult, error) {
			args := v.(LookupNotebookInstanceArgs)
			r, err := LookupNotebookInstance(ctx, &args, opts...)
			var s LookupNotebookInstanceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupNotebookInstanceResultOutput)
}

type LookupNotebookInstanceOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupNotebookInstanceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNotebookInstanceArgs)(nil)).Elem()
}

type LookupNotebookInstanceResultOutput struct{ *pulumi.OutputState }

func (LookupNotebookInstanceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNotebookInstanceResult)(nil)).Elem()
}

func (o LookupNotebookInstanceResultOutput) ToLookupNotebookInstanceResultOutput() LookupNotebookInstanceResultOutput {
	return o
}

func (o LookupNotebookInstanceResultOutput) ToLookupNotebookInstanceResultOutputWithContext(ctx context.Context) LookupNotebookInstanceResultOutput {
	return o
}

func (o LookupNotebookInstanceResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupNotebookInstanceResult] {
	return pulumix.Output[LookupNotebookInstanceResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupNotebookInstanceResultOutput) AcceleratorTypes() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) []string { return v.AcceleratorTypes }).(pulumi.StringArrayOutput)
}

func (o LookupNotebookInstanceResultOutput) AdditionalCodeRepositories() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) []string { return v.AdditionalCodeRepositories }).(pulumi.StringArrayOutput)
}

func (o LookupNotebookInstanceResultOutput) DefaultCodeRepository() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) *string { return v.DefaultCodeRepository }).(pulumi.StringPtrOutput)
}

func (o LookupNotebookInstanceResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupNotebookInstanceResultOutput) InstanceMetadataServiceConfiguration() NotebookInstanceInstanceMetadataServiceConfigurationPtrOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) *NotebookInstanceInstanceMetadataServiceConfiguration {
		return v.InstanceMetadataServiceConfiguration
	}).(NotebookInstanceInstanceMetadataServiceConfigurationPtrOutput)
}

func (o LookupNotebookInstanceResultOutput) InstanceType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) *string { return v.InstanceType }).(pulumi.StringPtrOutput)
}

func (o LookupNotebookInstanceResultOutput) LifecycleConfigName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) *string { return v.LifecycleConfigName }).(pulumi.StringPtrOutput)
}

func (o LookupNotebookInstanceResultOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) *string { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func (o LookupNotebookInstanceResultOutput) RootAccess() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) *string { return v.RootAccess }).(pulumi.StringPtrOutput)
}

func (o LookupNotebookInstanceResultOutput) Tags() NotebookInstanceTagArrayOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) []NotebookInstanceTag { return v.Tags }).(NotebookInstanceTagArrayOutput)
}

func (o LookupNotebookInstanceResultOutput) VolumeSizeInGb() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupNotebookInstanceResult) *int { return v.VolumeSizeInGb }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNotebookInstanceResultOutput{})
}
