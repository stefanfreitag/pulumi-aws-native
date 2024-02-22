// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appintegrations

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppIntegrations::DataIntegration
func LookupDataIntegration(ctx *pulumi.Context, args *LookupDataIntegrationArgs, opts ...pulumi.InvokeOption) (*LookupDataIntegrationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDataIntegrationResult
	err := ctx.Invoke("aws-native:appintegrations:getDataIntegration", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDataIntegrationArgs struct {
	// The unique identifer of the data integration.
	Id string `pulumi:"id"`
}

type LookupDataIntegrationResult struct {
	// The Amazon Resource Name (ARN) of the data integration.
	DataIntegrationArn *string `pulumi:"dataIntegrationArn"`
	// The data integration description.
	Description *string `pulumi:"description"`
	// The configuration for what files should be pulled from the source.
	FileConfiguration *DataIntegrationFileConfiguration `pulumi:"fileConfiguration"`
	// The unique identifer of the data integration.
	Id *string `pulumi:"id"`
	// The name of the data integration.
	Name *string `pulumi:"name"`
	// The configuration for what data should be pulled from the source.
	ObjectConfiguration *DataIntegrationObjectConfiguration `pulumi:"objectConfiguration"`
	// The tags (keys and values) associated with the data integration.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupDataIntegrationOutput(ctx *pulumi.Context, args LookupDataIntegrationOutputArgs, opts ...pulumi.InvokeOption) LookupDataIntegrationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDataIntegrationResult, error) {
			args := v.(LookupDataIntegrationArgs)
			r, err := LookupDataIntegration(ctx, &args, opts...)
			var s LookupDataIntegrationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDataIntegrationResultOutput)
}

type LookupDataIntegrationOutputArgs struct {
	// The unique identifer of the data integration.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupDataIntegrationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataIntegrationArgs)(nil)).Elem()
}

type LookupDataIntegrationResultOutput struct{ *pulumi.OutputState }

func (LookupDataIntegrationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataIntegrationResult)(nil)).Elem()
}

func (o LookupDataIntegrationResultOutput) ToLookupDataIntegrationResultOutput() LookupDataIntegrationResultOutput {
	return o
}

func (o LookupDataIntegrationResultOutput) ToLookupDataIntegrationResultOutputWithContext(ctx context.Context) LookupDataIntegrationResultOutput {
	return o
}

// The Amazon Resource Name (ARN) of the data integration.
func (o LookupDataIntegrationResultOutput) DataIntegrationArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataIntegrationResult) *string { return v.DataIntegrationArn }).(pulumi.StringPtrOutput)
}

// The data integration description.
func (o LookupDataIntegrationResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataIntegrationResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The configuration for what files should be pulled from the source.
func (o LookupDataIntegrationResultOutput) FileConfiguration() DataIntegrationFileConfigurationPtrOutput {
	return o.ApplyT(func(v LookupDataIntegrationResult) *DataIntegrationFileConfiguration { return v.FileConfiguration }).(DataIntegrationFileConfigurationPtrOutput)
}

// The unique identifer of the data integration.
func (o LookupDataIntegrationResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataIntegrationResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The name of the data integration.
func (o LookupDataIntegrationResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataIntegrationResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The configuration for what data should be pulled from the source.
func (o LookupDataIntegrationResultOutput) ObjectConfiguration() DataIntegrationObjectConfigurationPtrOutput {
	return o.ApplyT(func(v LookupDataIntegrationResult) *DataIntegrationObjectConfiguration { return v.ObjectConfiguration }).(DataIntegrationObjectConfigurationPtrOutput)
}

// The tags (keys and values) associated with the data integration.
func (o LookupDataIntegrationResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupDataIntegrationResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDataIntegrationResultOutput{})
}
