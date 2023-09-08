// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package personalize

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::Personalize::Schema.
func LookupSchema(ctx *pulumi.Context, args *LookupSchemaArgs, opts ...pulumi.InvokeOption) (*LookupSchemaResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSchemaResult
	err := ctx.Invoke("aws-native:personalize:getSchema", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSchemaArgs struct {
	// Arn for the schema.
	SchemaArn string `pulumi:"schemaArn"`
}

type LookupSchemaResult struct {
	// Arn for the schema.
	SchemaArn *string `pulumi:"schemaArn"`
}

func LookupSchemaOutput(ctx *pulumi.Context, args LookupSchemaOutputArgs, opts ...pulumi.InvokeOption) LookupSchemaResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSchemaResult, error) {
			args := v.(LookupSchemaArgs)
			r, err := LookupSchema(ctx, &args, opts...)
			var s LookupSchemaResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSchemaResultOutput)
}

type LookupSchemaOutputArgs struct {
	// Arn for the schema.
	SchemaArn pulumi.StringInput `pulumi:"schemaArn"`
}

func (LookupSchemaOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSchemaArgs)(nil)).Elem()
}

type LookupSchemaResultOutput struct{ *pulumi.OutputState }

func (LookupSchemaResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSchemaResult)(nil)).Elem()
}

func (o LookupSchemaResultOutput) ToLookupSchemaResultOutput() LookupSchemaResultOutput {
	return o
}

func (o LookupSchemaResultOutput) ToLookupSchemaResultOutputWithContext(ctx context.Context) LookupSchemaResultOutput {
	return o
}

func (o LookupSchemaResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupSchemaResult] {
	return pulumix.Output[LookupSchemaResult]{
		OutputState: o.OutputState,
	}
}

// Arn for the schema.
func (o LookupSchemaResultOutput) SchemaArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSchemaResult) *string { return v.SchemaArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSchemaResultOutput{})
}
