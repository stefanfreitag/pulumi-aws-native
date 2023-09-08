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

// Resource Type definition for AWS::SageMaker::Project
func LookupProject(ctx *pulumi.Context, args *LookupProjectArgs, opts ...pulumi.InvokeOption) (*LookupProjectResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupProjectResult
	err := ctx.Invoke("aws-native:sagemaker:getProject", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupProjectArgs struct {
	ProjectArn string `pulumi:"projectArn"`
}

type LookupProjectResult struct {
	// The time at which the project was created.
	CreationTime *string `pulumi:"creationTime"`
	ProjectArn   *string `pulumi:"projectArn"`
	ProjectId    *string `pulumi:"projectId"`
	// The status of a project.
	ProjectStatus *ProjectStatus `pulumi:"projectStatus"`
	// Provisioned ServiceCatalog  Details
	ServiceCatalogProvisionedProductDetails *ServiceCatalogProvisionedProductDetailsProperties `pulumi:"serviceCatalogProvisionedProductDetails"`
}

func LookupProjectOutput(ctx *pulumi.Context, args LookupProjectOutputArgs, opts ...pulumi.InvokeOption) LookupProjectResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupProjectResult, error) {
			args := v.(LookupProjectArgs)
			r, err := LookupProject(ctx, &args, opts...)
			var s LookupProjectResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupProjectResultOutput)
}

type LookupProjectOutputArgs struct {
	ProjectArn pulumi.StringInput `pulumi:"projectArn"`
}

func (LookupProjectOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupProjectArgs)(nil)).Elem()
}

type LookupProjectResultOutput struct{ *pulumi.OutputState }

func (LookupProjectResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupProjectResult)(nil)).Elem()
}

func (o LookupProjectResultOutput) ToLookupProjectResultOutput() LookupProjectResultOutput {
	return o
}

func (o LookupProjectResultOutput) ToLookupProjectResultOutputWithContext(ctx context.Context) LookupProjectResultOutput {
	return o
}

func (o LookupProjectResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupProjectResult] {
	return pulumix.Output[LookupProjectResult]{
		OutputState: o.OutputState,
	}
}

// The time at which the project was created.
func (o LookupProjectResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProjectResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

func (o LookupProjectResultOutput) ProjectArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProjectResult) *string { return v.ProjectArn }).(pulumi.StringPtrOutput)
}

func (o LookupProjectResultOutput) ProjectId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProjectResult) *string { return v.ProjectId }).(pulumi.StringPtrOutput)
}

// The status of a project.
func (o LookupProjectResultOutput) ProjectStatus() ProjectStatusPtrOutput {
	return o.ApplyT(func(v LookupProjectResult) *ProjectStatus { return v.ProjectStatus }).(ProjectStatusPtrOutput)
}

// Provisioned ServiceCatalog  Details
func (o LookupProjectResultOutput) ServiceCatalogProvisionedProductDetails() ServiceCatalogProvisionedProductDetailsPropertiesPtrOutput {
	return o.ApplyT(func(v LookupProjectResult) *ServiceCatalogProvisionedProductDetailsProperties {
		return v.ServiceCatalogProvisionedProductDetails
	}).(ServiceCatalogProvisionedProductDetailsPropertiesPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupProjectResultOutput{})
}
