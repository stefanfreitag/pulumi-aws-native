// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cassandra

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::Cassandra::Table
func LookupTable(ctx *pulumi.Context, args *LookupTableArgs, opts ...pulumi.InvokeOption) (*LookupTableResult, error) {
	var rv LookupTableResult
	err := ctx.Invoke("aws-native:cassandra:getTable", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTableArgs struct {
	// Name for Cassandra keyspace
	KeyspaceName string `pulumi:"keyspaceName"`
	// Name for Cassandra table
	TableName string `pulumi:"tableName"`
}

type LookupTableResult struct {
	BillingMode *TableBillingMode `pulumi:"billingMode"`
	// Default TTL (Time To Live) in seconds, where zero is disabled. If the value is greater than zero, TTL is enabled for the entire table and an expiration timestamp is added to each column.
	DefaultTimeToLive       *int                          `pulumi:"defaultTimeToLive"`
	EncryptionSpecification *TableEncryptionSpecification `pulumi:"encryptionSpecification"`
	// Indicates whether point in time recovery is enabled (true) or disabled (false) on the table
	PointInTimeRecoveryEnabled *bool `pulumi:"pointInTimeRecoveryEnabled"`
	// Non-key columns of the table
	RegularColumns []TableColumn `pulumi:"regularColumns"`
	// An array of key-value pairs to apply to this resource
	Tags []TableTag `pulumi:"tags"`
}

func LookupTableOutput(ctx *pulumi.Context, args LookupTableOutputArgs, opts ...pulumi.InvokeOption) LookupTableResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTableResult, error) {
			args := v.(LookupTableArgs)
			r, err := LookupTable(ctx, &args, opts...)
			var s LookupTableResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTableResultOutput)
}

type LookupTableOutputArgs struct {
	// Name for Cassandra keyspace
	KeyspaceName pulumi.StringInput `pulumi:"keyspaceName"`
	// Name for Cassandra table
	TableName pulumi.StringInput `pulumi:"tableName"`
}

func (LookupTableOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTableArgs)(nil)).Elem()
}

type LookupTableResultOutput struct{ *pulumi.OutputState }

func (LookupTableResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTableResult)(nil)).Elem()
}

func (o LookupTableResultOutput) ToLookupTableResultOutput() LookupTableResultOutput {
	return o
}

func (o LookupTableResultOutput) ToLookupTableResultOutputWithContext(ctx context.Context) LookupTableResultOutput {
	return o
}

func (o LookupTableResultOutput) BillingMode() TableBillingModePtrOutput {
	return o.ApplyT(func(v LookupTableResult) *TableBillingMode { return v.BillingMode }).(TableBillingModePtrOutput)
}

// Default TTL (Time To Live) in seconds, where zero is disabled. If the value is greater than zero, TTL is enabled for the entire table and an expiration timestamp is added to each column.
func (o LookupTableResultOutput) DefaultTimeToLive() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *int { return v.DefaultTimeToLive }).(pulumi.IntPtrOutput)
}

func (o LookupTableResultOutput) EncryptionSpecification() TableEncryptionSpecificationPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *TableEncryptionSpecification { return v.EncryptionSpecification }).(TableEncryptionSpecificationPtrOutput)
}

// Indicates whether point in time recovery is enabled (true) or disabled (false) on the table
func (o LookupTableResultOutput) PointInTimeRecoveryEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *bool { return v.PointInTimeRecoveryEnabled }).(pulumi.BoolPtrOutput)
}

// Non-key columns of the table
func (o LookupTableResultOutput) RegularColumns() TableColumnArrayOutput {
	return o.ApplyT(func(v LookupTableResult) []TableColumn { return v.RegularColumns }).(TableColumnArrayOutput)
}

// An array of key-value pairs to apply to this resource
func (o LookupTableResultOutput) Tags() TableTagArrayOutput {
	return o.ApplyT(func(v LookupTableResult) []TableTag { return v.Tags }).(TableTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTableResultOutput{})
}
