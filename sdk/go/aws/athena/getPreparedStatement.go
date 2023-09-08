// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package athena

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::Athena::PreparedStatement
func LookupPreparedStatement(ctx *pulumi.Context, args *LookupPreparedStatementArgs, opts ...pulumi.InvokeOption) (*LookupPreparedStatementResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPreparedStatementResult
	err := ctx.Invoke("aws-native:athena:getPreparedStatement", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPreparedStatementArgs struct {
	// The name of the prepared statement.
	StatementName string `pulumi:"statementName"`
	// The name of the workgroup to which the prepared statement belongs.
	WorkGroup string `pulumi:"workGroup"`
}

type LookupPreparedStatementResult struct {
	// The description of the prepared statement.
	Description *string `pulumi:"description"`
	// The query string for the prepared statement.
	QueryStatement *string `pulumi:"queryStatement"`
}

func LookupPreparedStatementOutput(ctx *pulumi.Context, args LookupPreparedStatementOutputArgs, opts ...pulumi.InvokeOption) LookupPreparedStatementResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPreparedStatementResult, error) {
			args := v.(LookupPreparedStatementArgs)
			r, err := LookupPreparedStatement(ctx, &args, opts...)
			var s LookupPreparedStatementResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPreparedStatementResultOutput)
}

type LookupPreparedStatementOutputArgs struct {
	// The name of the prepared statement.
	StatementName pulumi.StringInput `pulumi:"statementName"`
	// The name of the workgroup to which the prepared statement belongs.
	WorkGroup pulumi.StringInput `pulumi:"workGroup"`
}

func (LookupPreparedStatementOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPreparedStatementArgs)(nil)).Elem()
}

type LookupPreparedStatementResultOutput struct{ *pulumi.OutputState }

func (LookupPreparedStatementResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPreparedStatementResult)(nil)).Elem()
}

func (o LookupPreparedStatementResultOutput) ToLookupPreparedStatementResultOutput() LookupPreparedStatementResultOutput {
	return o
}

func (o LookupPreparedStatementResultOutput) ToLookupPreparedStatementResultOutputWithContext(ctx context.Context) LookupPreparedStatementResultOutput {
	return o
}

func (o LookupPreparedStatementResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupPreparedStatementResult] {
	return pulumix.Output[LookupPreparedStatementResult]{
		OutputState: o.OutputState,
	}
}

// The description of the prepared statement.
func (o LookupPreparedStatementResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPreparedStatementResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The query string for the prepared statement.
func (o LookupPreparedStatementResultOutput) QueryStatement() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPreparedStatementResult) *string { return v.QueryStatement }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPreparedStatementResultOutput{})
}
