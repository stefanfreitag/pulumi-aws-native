// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::DataSync::LocationAzureBlob.
func LookupLocationAzureBlob(ctx *pulumi.Context, args *LookupLocationAzureBlobArgs, opts ...pulumi.InvokeOption) (*LookupLocationAzureBlobResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLocationAzureBlobResult
	err := ctx.Invoke("aws-native:datasync:getLocationAzureBlob", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLocationAzureBlobArgs struct {
	// The Amazon Resource Name (ARN) of the Azure Blob Location that is created.
	LocationArn string `pulumi:"locationArn"`
}

type LookupLocationAzureBlobResult struct {
	// The Amazon Resource Names (ARNs) of agents to use for an Azure Blob Location.
	AgentArns []string `pulumi:"agentArns"`
	// Specifies an access tier for the objects you're transferring into your Azure Blob Storage container.
	AzureAccessTier *LocationAzureBlobAzureAccessTier `pulumi:"azureAccessTier"`
	// The specific authentication type that you want DataSync to use to access your Azure Blob Container.
	AzureBlobAuthenticationType *LocationAzureBlobAzureBlobAuthenticationType `pulumi:"azureBlobAuthenticationType"`
	// Specifies a blob type for the objects you're transferring into your Azure Blob Storage container.
	AzureBlobType *LocationAzureBlobAzureBlobType `pulumi:"azureBlobType"`
	// The Amazon Resource Name (ARN) of the Azure Blob Location that is created.
	LocationArn *string `pulumi:"locationArn"`
	// The URL of the Azure Blob Location that was described.
	LocationUri *string `pulumi:"locationUri"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupLocationAzureBlobOutput(ctx *pulumi.Context, args LookupLocationAzureBlobOutputArgs, opts ...pulumi.InvokeOption) LookupLocationAzureBlobResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLocationAzureBlobResult, error) {
			args := v.(LookupLocationAzureBlobArgs)
			r, err := LookupLocationAzureBlob(ctx, &args, opts...)
			var s LookupLocationAzureBlobResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLocationAzureBlobResultOutput)
}

type LookupLocationAzureBlobOutputArgs struct {
	// The Amazon Resource Name (ARN) of the Azure Blob Location that is created.
	LocationArn pulumi.StringInput `pulumi:"locationArn"`
}

func (LookupLocationAzureBlobOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLocationAzureBlobArgs)(nil)).Elem()
}

type LookupLocationAzureBlobResultOutput struct{ *pulumi.OutputState }

func (LookupLocationAzureBlobResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLocationAzureBlobResult)(nil)).Elem()
}

func (o LookupLocationAzureBlobResultOutput) ToLookupLocationAzureBlobResultOutput() LookupLocationAzureBlobResultOutput {
	return o
}

func (o LookupLocationAzureBlobResultOutput) ToLookupLocationAzureBlobResultOutputWithContext(ctx context.Context) LookupLocationAzureBlobResultOutput {
	return o
}

// The Amazon Resource Names (ARNs) of agents to use for an Azure Blob Location.
func (o LookupLocationAzureBlobResultOutput) AgentArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupLocationAzureBlobResult) []string { return v.AgentArns }).(pulumi.StringArrayOutput)
}

// Specifies an access tier for the objects you're transferring into your Azure Blob Storage container.
func (o LookupLocationAzureBlobResultOutput) AzureAccessTier() LocationAzureBlobAzureAccessTierPtrOutput {
	return o.ApplyT(func(v LookupLocationAzureBlobResult) *LocationAzureBlobAzureAccessTier { return v.AzureAccessTier }).(LocationAzureBlobAzureAccessTierPtrOutput)
}

// The specific authentication type that you want DataSync to use to access your Azure Blob Container.
func (o LookupLocationAzureBlobResultOutput) AzureBlobAuthenticationType() LocationAzureBlobAzureBlobAuthenticationTypePtrOutput {
	return o.ApplyT(func(v LookupLocationAzureBlobResult) *LocationAzureBlobAzureBlobAuthenticationType {
		return v.AzureBlobAuthenticationType
	}).(LocationAzureBlobAzureBlobAuthenticationTypePtrOutput)
}

// Specifies a blob type for the objects you're transferring into your Azure Blob Storage container.
func (o LookupLocationAzureBlobResultOutput) AzureBlobType() LocationAzureBlobAzureBlobTypePtrOutput {
	return o.ApplyT(func(v LookupLocationAzureBlobResult) *LocationAzureBlobAzureBlobType { return v.AzureBlobType }).(LocationAzureBlobAzureBlobTypePtrOutput)
}

// The Amazon Resource Name (ARN) of the Azure Blob Location that is created.
func (o LookupLocationAzureBlobResultOutput) LocationArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationAzureBlobResult) *string { return v.LocationArn }).(pulumi.StringPtrOutput)
}

// The URL of the Azure Blob Location that was described.
func (o LookupLocationAzureBlobResultOutput) LocationUri() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationAzureBlobResult) *string { return v.LocationUri }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupLocationAzureBlobResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupLocationAzureBlobResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLocationAzureBlobResultOutput{})
}
