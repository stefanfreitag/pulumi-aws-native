// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::RDS::GlobalCluster
func LookupGlobalCluster(ctx *pulumi.Context, args *LookupGlobalClusterArgs, opts ...pulumi.InvokeOption) (*LookupGlobalClusterResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupGlobalClusterResult
	err := ctx.Invoke("aws-native:rds:getGlobalCluster", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupGlobalClusterArgs struct {
	// The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.
	GlobalClusterIdentifier string `pulumi:"globalClusterIdentifier"`
}

type LookupGlobalClusterResult struct {
	// The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.
	DeletionProtection *bool `pulumi:"deletionProtection"`
	// The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
	EngineVersion *string `pulumi:"engineVersion"`
}

func LookupGlobalClusterOutput(ctx *pulumi.Context, args LookupGlobalClusterOutputArgs, opts ...pulumi.InvokeOption) LookupGlobalClusterResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupGlobalClusterResult, error) {
			args := v.(LookupGlobalClusterArgs)
			r, err := LookupGlobalCluster(ctx, &args, opts...)
			var s LookupGlobalClusterResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupGlobalClusterResultOutput)
}

type LookupGlobalClusterOutputArgs struct {
	// The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.
	GlobalClusterIdentifier pulumi.StringInput `pulumi:"globalClusterIdentifier"`
}

func (LookupGlobalClusterOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGlobalClusterArgs)(nil)).Elem()
}

type LookupGlobalClusterResultOutput struct{ *pulumi.OutputState }

func (LookupGlobalClusterResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGlobalClusterResult)(nil)).Elem()
}

func (o LookupGlobalClusterResultOutput) ToLookupGlobalClusterResultOutput() LookupGlobalClusterResultOutput {
	return o
}

func (o LookupGlobalClusterResultOutput) ToLookupGlobalClusterResultOutputWithContext(ctx context.Context) LookupGlobalClusterResultOutput {
	return o
}

func (o LookupGlobalClusterResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupGlobalClusterResult] {
	return pulumix.Output[LookupGlobalClusterResult]{
		OutputState: o.OutputState,
	}
}

// The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.
func (o LookupGlobalClusterResultOutput) DeletionProtection() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupGlobalClusterResult) *bool { return v.DeletionProtection }).(pulumi.BoolPtrOutput)
}

// The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
func (o LookupGlobalClusterResultOutput) EngineVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGlobalClusterResult) *string { return v.EngineVersion }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupGlobalClusterResultOutput{})
}
