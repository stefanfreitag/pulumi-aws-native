// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package athena

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::Athena::DataCatalog
func LookupDataCatalog(ctx *pulumi.Context, args *LookupDataCatalogArgs, opts ...pulumi.InvokeOption) (*LookupDataCatalogResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDataCatalogResult
	err := ctx.Invoke("aws-native:athena:getDataCatalog", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDataCatalogArgs struct {
	// The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters.
	Name string `pulumi:"name"`
}

type LookupDataCatalogResult struct {
	// A description of the data catalog to be created.
	Description *string `pulumi:"description"`
	// Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type.
	Parameters map[string]string `pulumi:"parameters"`
	// A list of comma separated tags to add to the data catalog that is created.
	Tags []aws.Tag `pulumi:"tags"`
	// The type of data catalog to create: LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore.
	Type *DataCatalogType `pulumi:"type"`
}

func LookupDataCatalogOutput(ctx *pulumi.Context, args LookupDataCatalogOutputArgs, opts ...pulumi.InvokeOption) LookupDataCatalogResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDataCatalogResult, error) {
			args := v.(LookupDataCatalogArgs)
			r, err := LookupDataCatalog(ctx, &args, opts...)
			var s LookupDataCatalogResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDataCatalogResultOutput)
}

type LookupDataCatalogOutputArgs struct {
	// The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters.
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupDataCatalogOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataCatalogArgs)(nil)).Elem()
}

type LookupDataCatalogResultOutput struct{ *pulumi.OutputState }

func (LookupDataCatalogResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataCatalogResult)(nil)).Elem()
}

func (o LookupDataCatalogResultOutput) ToLookupDataCatalogResultOutput() LookupDataCatalogResultOutput {
	return o
}

func (o LookupDataCatalogResultOutput) ToLookupDataCatalogResultOutputWithContext(ctx context.Context) LookupDataCatalogResultOutput {
	return o
}

// A description of the data catalog to be created.
func (o LookupDataCatalogResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataCatalogResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type.
func (o LookupDataCatalogResultOutput) Parameters() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupDataCatalogResult) map[string]string { return v.Parameters }).(pulumi.StringMapOutput)
}

// A list of comma separated tags to add to the data catalog that is created.
func (o LookupDataCatalogResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupDataCatalogResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

// The type of data catalog to create: LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore.
func (o LookupDataCatalogResultOutput) Type() DataCatalogTypePtrOutput {
	return o.ApplyT(func(v LookupDataCatalogResult) *DataCatalogType { return v.Type }).(DataCatalogTypePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDataCatalogResultOutput{})
}
